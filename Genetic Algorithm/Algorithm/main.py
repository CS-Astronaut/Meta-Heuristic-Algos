import numpy as np
import pandas as pd
from benchfunc import funcs_vec
import time
from IPython.display import display

# GA parameters
CROSSOVER_PROB = 0.75
MUTATION_PROB = 0.02
POP_SIZE = 60
MAX_EVALS = 20000
TOURNAMENT_SIZE = 3
N_RUNS = 10

rng_global = np.random.default_rng()

def run_ga_vectorized(func, lower, upper, seed=None):
    rng = np.random.default_rng(seed)
    dim = int(lower.shape[0])
    pop = rng.uniform(lower, upper, size=(POP_SIZE, dim))
    # some functions expect 1-D input; ensure func handles batch arrays
    fitness = func(pop)
    evals = POP_SIZE
    best_idx = int(np.argmin(fitness))
    best_val = float(fitness[best_idx])
    best_x = pop[best_idx].copy()
    
    while evals < MAX_EVALS:
        # tournament selection to produce parents
        cand = rng.integers(0, POP_SIZE, size=(POP_SIZE, TOURNAMENT_SIZE))
        cand_f = fitness[cand]
        winners = cand[np.arange(POP_SIZE), np.argmin(cand_f, axis=1)]
        p1 = pop[winners]
        
        cand2 = rng.integers(0, POP_SIZE, size=(POP_SIZE, TOURNAMENT_SIZE))
        cand_f2 = fitness[cand2]
        winners2 = cand2[np.arange(POP_SIZE), np.argmin(cand_f2, axis=1)]
        p2 = pop[winners2]
        
        # crossover (blend)
        do_x = rng.random(size=POP_SIZE) < CROSSOVER_PROB
        alpha = rng.random(size=(POP_SIZE, dim))
        children = np.where(do_x[:,None], alpha*p1 + (1-alpha)*p2, p1.copy())
        
        # mutation gaussian
        mut_mask = rng.random(size=(POP_SIZE, dim)) < MUTATION_PROB
        if mut_mask.any():
            sigma = 0.1 * (upper - lower)
            noise = rng.normal(0,1,size=(POP_SIZE, dim)) * sigma
            children = np.where(mut_mask, children + noise, children)
        
        children = np.clip(children, lower, upper)
        child_f = func(children)
        evals += POP_SIZE
        
        # update best
        idx = int(np.argmin(child_f))
        if child_f[idx] < best_val:
            best_val = float(child_f[idx])
            best_x = children[idx].copy()
        
        pop = children
        fitness = child_f
    
    return best_val, best_x

# run experiments
summary_rows = []
all_results = []
print("Starting vectorized GA runs...")

for name, func, low, high, known in funcs_vec:
    best_vals = np.empty(N_RUNS)
    best_xs = []
    
    for i in range(N_RUNS):
        seed = rng_global.integers(1_000_000_000)
        try:
            bv, bx = run_ga_vectorized(func, low, high, seed=seed)
        except Exception as e:
            print(f"  Skipping run due to error evaluating {name}: {e}")
            bv, bx = np.nan, None
        best_vals[i] = bv
        best_xs.append(bx)
    
    # Handle case where all runs failed
    valid_vals = best_vals[~np.isnan(best_vals)]
    if len(valid_vals) > 0:
        meanv = float(np.nanmean(best_vals))
        stdv = float(np.nanstd(best_vals, ddof=1)) if len(valid_vals) > 1 else 0.0
        idx_best = int(np.nanargmin(best_vals))
        best_observed_val = float(best_vals[idx_best])
        best_observed_x = np.round(best_xs[idx_best], 6).tolist() if best_xs[idx_best] is not None else None
    else:
        meanv = np.nan
        stdv = np.nan
        best_observed_val = np.nan
        best_observed_x = None
    
    summary_rows.append({
        "function": name,
        "mean_best": round(meanv, 6) if not np.isnan(meanv) else np.nan,
        "std_best": round(stdv, 6) if not np.isnan(stdv) else np.nan,
        "best_observed_val": best_observed_val,
        "best_observed_x": best_observed_x,
        "known_min": known
    })
    
    all_results.append({"function": name, "best_vals": best_vals, "best_xs": best_xs})
    
    if len(valid_vals) > 0:
        print(f"{name}: mean={meanv:.6g}, std={stdv:.6g}, best={np.nanmin(best_vals):.6g}")
    else:
        print(f"{name}: All runs failed - no valid results")

df = pd.DataFrame(summary_rows)
display(df)

# per-run table
rows = []
for r in all_results:
    row = {"function": r["function"]}
    for i, val in enumerate(r["best_vals"], start=1):
        if not np.isnan(val):
            row[f"run_{i}"] = float(np.round(val, 8))
        else:
            row[f"run_{i}"] = np.nan
    rows.append(row)

df_runs = pd.DataFrame(rows)
display(df_runs)

# Save summary CSV
csv_path = "ga_benchmark_results_summary_vectorized.csv"
df.to_csv(csv_path, index=False)
print("Saved summary CSV to:", csv_path)
