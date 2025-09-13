import numpy as np
import pandas as pd
from benchfunc import funcs_vec
from IPython.display import display

# ----------------------------
# PSO Parameters
# ----------------------------
POP_SIZE = 50
MAX_EVALS = 40000
MAX_ITERS = MAX_EVALS // POP_SIZE  # 800 iterations
C1 = 1.42
C2 = 1.42
W = 0.74
N_RUNS = 20

rng_global = np.random.default_rng()

# ----------------------------
# PSO Algorithm
# ----------------------------
def run_pso(func_vec, lower, upper, seed=None):
    rng = np.random.default_rng(seed)
    dim = int(lower.shape[0])  # Handle numpy array shape

    # init positions and velocities
    pos = rng.uniform(lower, upper, size=(POP_SIZE, dim))
    vel = rng.uniform(-abs(upper-lower), abs(upper-lower), size=(POP_SIZE, dim)) * 0.1

    # evaluate initial fitness
    fitnesses = func_vec(pos)
    evals = POP_SIZE

    # personal bests
    pbest_pos = pos.copy()
    pbest_val = fitnesses.copy()

    # global best
    g_idx = int(np.argmin(pbest_val))
    gbest_pos = pbest_pos[g_idx].copy()
    gbest_val = float(pbest_val[g_idx])

    # iterations
    for it in range(MAX_ITERS):
        # velocity update
        r1 = rng.random(size=(POP_SIZE, dim))
        r2 = rng.random(size=(POP_SIZE, dim))
        vel = (W*vel 
               + C1*r1*(pbest_pos - pos) 
               + C2*r2*(gbest_pos - pos))

        # position update
        pos = pos + vel
        pos = np.clip(pos, lower, upper)

        # evaluate
        fitnesses = func_vec(pos)
        evals += POP_SIZE

        # update personal best
        better_mask = fitnesses < pbest_val
        pbest_pos[better_mask] = pos[better_mask]
        pbest_val[better_mask] = fitnesses[better_mask]

        # update global best
        min_idx = int(np.argmin(pbest_val))
        if pbest_val[min_idx] < gbest_val:
            gbest_val = float(pbest_val[min_idx])
            gbest_pos = pbest_pos[min_idx].copy()

        if evals >= MAX_EVALS:
            break

    return gbest_val, gbest_pos

# ----------------------------
# Run Experiments
# ----------------------------
summary_rows = []
all_results = []
print("Starting PSO runs...")

for name, fvec, lower, upper, known in funcs_vec:
    best_vals = np.empty(N_RUNS)
    best_xs = []
    
    for i in range(N_RUNS):
        seed = rng_global.integers(1_000_000_000)
        try:
            bv, bx = run_pso(fvec, lower, upper, seed=seed)
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

# Per-run results
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
csv_path = "pso_benchmark_results_summary.csv"
df.to_csv(csv_path, index=False)
print("Saved summary CSV to:", csv_path)
