import numpy as np, pandas as pd
from math import exp, cos, sin, sqrt
from IPython.display import display

def ackley_n2_vec(X):
    # X shape (...,2)
    r = np.sqrt(X[...,0]**2 + X[...,1]**2)
    return -200.0 * np.exp(-0.2 * r)

def ackley_n3_vec(X):
    r = np.sqrt(X[...,0]**2 + X[...,1]**2)
    return -200.0 * np.exp(-0.2 * r) + 5.0 * np.exp(np.cos(3*X[...,0]) + np.sin(3*X[...,1]))

def beale_vec(X):
    X0 = X[...,0]; Y = X[...,1]
    return (1.5 - X0 + X0*Y)**2 + (2.25 - X0 + X0*(Y**2))**2 + (2.625 - X0 + X0*(Y**3))**2

def brent_vec(X):
    X0 = X[...,0]; Y = X[...,1]
    return (X0 + 10.0)**2 + (Y + 10.0)**2 + np.exp(-X0**2 - Y**2)

def drop_wave_vec(X):
    X0 = X[...,0]; Y = X[...,1]
    r = np.sqrt(X0**2 + Y**2)
    numerator = 1.0 + np.cos(12.0 * r)
    denominator = 0.5 * (X0**2 + Y**2) + 2.0
    return - numerator / denominator

funcs_vec = [
    ("Ackley N.2", ackley_n2_vec, np.array([-32.0, -32.0]), np.array([32.0, 32.0]), -200.0),
    ("Beale", beale_vec, np.array([-4.5, -4.5]), np.array([4.5, 4.5]), 0.0),
    ("Brent", brent_vec, np.array([-20.0, -20.0]), np.array([0.0, 0.0]), np.exp(-200.0)),
    ("Drop-Wave", drop_wave_vec, np.array([-5.2, -5.2]), np.array([5.2, 5.2]), -1.0),
    ("Ackley N.3", ackley_n3_vec, np.array([-32.0, -32.0]), np.array([32.0, 32.0]), None),
]

CROSSOVER_PROB = 0.75
MUTATION_PROB = 0.01
POP_SIZE = 50
MAX_EVALS = 40000
TOURNAMENT_SIZE = 3
N_RUNS = 20

rng_global = np.random.default_rng()

def run_ga_vectorized(func_vec, lower, upper, seed=None):
    rng = np.random.default_rng(seed)
    dim = len(lower)
    # init pop
    pop = rng.uniform(lower, upper, size=(POP_SIZE, dim))
    fitnesses = func_vec(pop)
    evals = POP_SIZE
    best_idx = int(np.argmin(fitnesses))
    best_val = float(fitnesses[best_idx])
    best_x = pop[best_idx].copy()
    # main loop
    while evals < MAX_EVALS:
        # selection: for each of POP_SIZE parents, conduct tournament of size k
        # produce parents indices arrays p1_idx and p2_idx (length POP_SIZE)
        # vectorized tournament: sample k indices for each parent
        cand_idxs = rng.integers(0, POP_SIZE, size=(POP_SIZE, TOURNAMENT_SIZE))
        # find best among candidates per row
        cand_fits = fitnesses[cand_idxs]  # shape (POP_SIZE, TOURNAMENT_SIZE)
        best_cand_pos = np.argmin(cand_fits, axis=1)
        p1_idx = cand_idxs[np.arange(POP_SIZE), best_cand_pos]
        # repeat for p2
        cand_idxs2 = rng.integers(0, POP_SIZE, size=(POP_SIZE, TOURNAMENT_SIZE))
        cand_fits2 = fitnesses[cand_idxs2]
        best_cand_pos2 = np.argmin(cand_fits2, axis=1)
        p2_idx = cand_idxs2[np.arange(POP_SIZE), best_cand_pos2]
        p1 = pop[p1_idx]
        p2 = pop[p2_idx]
        # crossover
        do_xover = rng.random(size=POP_SIZE) < CROSSOVER_PROB
        alphas = rng.random(size=(POP_SIZE, dim))
        children = np.where(do_xover[:,None], alphas * p1 + (1 - alphas) * p2, p1.copy())
        # mutation (per gene)
        mut_mask = rng.random(size=(POP_SIZE, dim)) < MUTATION_PROB
        if mut_mask.any():
            widths = upper - lower
            sigmas = 0.1 * widths
            noise = rng.normal(0, 1, size=(POP_SIZE, dim)) * sigmas
            children = np.where(mut_mask, children + noise, children)
        # clip to bounds
        children = np.clip(children, lower, upper)
        # evaluate children in batch
        child_fits = func_vec(children)
        evals += POP_SIZE
        # update best
        min_idx = int(np.argmin(child_fits))
        if child_fits[min_idx] < best_val:
            best_val = float(child_fits[min_idx])
            best_x = children[min_idx].copy()
        # replace population with children
        pop = children
        fitnesses = child_fits
    return best_val, best_x

# run experiments
summary_rows = []
all_results = []
print("Starting vectorized GA runs...")
for name, fvec, lower, upper, known in funcs_vec:
    best_vals = np.empty(N_RUNS)
    best_xs = []
    for i in range(N_RUNS):
        seed = rng_global.integers(1_000_000_000)
        bv, bx = run_ga_vectorized(fvec, lower, upper, seed=seed)
        best_vals[i] = bv
        best_xs.append(bx)
    meanv = float(np.mean(best_vals))
    stdv = float(np.std(best_vals, ddof=1))
    idx_best = int(np.argmin(best_vals))
    summary_rows.append({
        "function": name,
        "mean_best": round(meanv,6),
        "std_best": round(stdv,6),
        "best_observed_val": float(best_vals[idx_best]),
        "best_observed_x": np.round(best_xs[idx_best],6).tolist(),
        "known_min": known
    })
    all_results.append({"function": name, "best_vals": best_vals, "best_xs": best_xs})
    print(f"{name}: mean={meanv:.6g}, std={stdv:.6g}, best={best_vals.min():.6g}")

df = pd.DataFrame(summary_rows)
display(df)
# per-run table
rows = []
for r in all_results:
    row = {"function": r["function"]}
    for i,val in enumerate(r["best_vals"], start=1):
        row[f"run_{i}"] = float(np.round(val,8))
    rows.append(row)
df_runs = pd.DataFrame(rows)
display(df_runs)

# Save summary CSV
csv_path = "/mnt/data/ga_benchmark_results_summary_vectorized.csv"
df.to_csv(csv_path, index=False)
print("Saved summary CSV to:", csv_path)
