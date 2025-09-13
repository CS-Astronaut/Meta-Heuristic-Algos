import numpy as np, pandas as pd
from math import exp, cos, sin, sqrt
from IPython.display import display

# ----------------------------
# Benchmark functions (vectorized)
# ----------------------------
def ackley_n2_vec(X):
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

# ----------------------------
# PSO Parameters
# ----------------------------
POP_SIZE = 50
MAX_EVALS = 40000
MAX_ITERS = MAX_EVALS // POP_SIZE  # 800 iterations
C1 = 1.42
C2 = 1.42
W  = 0.74
N_RUNS = 20

rng_global = np.random.default_rng()

# ----------------------------
# PSO Algorithm
# ----------------------------
def run_pso(func_vec, lower, upper, seed=None):
    rng = np.random.default_rng(seed)
    dim = len(lower)

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
        bv, bx = run_pso(fvec, lower, upper, seed=seed)
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

# Per-run results
rows = []
for r in all_results:
    row = {"function": r["function"]}
    for i,val in enumerate(r["best_vals"], start=1):
        row[f"run_{i}"] = float(np.round(val,8))
    rows.append(row)
df_runs = pd.DataFrame(rows)
display(df_runs)

# Save summary CSV
csv_path = "pso_benchmark_results_summary.csv"
df.to_csv(csv_path, index=False)
print("Saved summary CSV to:", csv_path)

