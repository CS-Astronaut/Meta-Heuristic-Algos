# Particle Swarm Optimization (PSO) – Benchmarking Results

This project implements **Particle Swarm Optimization (PSO)** and evaluates its performance on 5 standard benchmark functions (2D).
All experiments were performed with the following parameters:

* **Population size (swarm):** 50
* **Cognitive coefficient (c1):** 1.42
* **Social coefficient (c2):** 1.42
* **Inertia weight (w):** 0.74
* **Stopping condition:** 40,000 function evaluations (800 iterations × 50 particles)
* **Independent runs:** 20

---

## Benchmark Functions

| Function       | Properties                                                           | Global Minimum                            |
| -------------- | -------------------------------------------------------------------- | ----------------------------------------- |
| **Ackley N.2** | 2-dimensional, non-separable, unimodal, convex, differentiable       | $f(0,0) = -200$                           |
| **Beale**      | 2-dimensional, continuous, multimodal, non-convex                    | $f(3,0.5) = 0$                            |
| **Brent**      | 2-dimensional, non-separable, unimodal, convex, differentiable       | $f(-10,-10) \approx 1.38 \times 10^{-87}$ |
| **Drop-Wave**  | 2-dimensional, continuous, unimodal, non-convex                      | $f(0,0) = -1$                             |
| **Ackley N.3** | 2-dimensional, non-separable, multimodal, non-convex, differentiable | $f(0,0) \approx -186.41$                  |

---

## Results Summary (20 runs)

| Function   | Mean Best   | Std Dev | Best Observed | Known Optimum | Best Solution (x) |
| ---------- | ----------- | ------- | ------------- | ------------- | ----------------- |
| Ackley N.2 | -200.000000 | 0.0     | -200.0        | -200.0        | \[0.0, -0.0]      |
| Beale      | 0.000000    | 0.0     | 0.0           | 0.0           | \[3.0, 0.5]       |
| Brent      | 0.000000    | 0.0     | 1.38e-87      | 1.38e-87      | \[-10.0, -10.0]   |
| Drop-Wave  | -1.000000   | 0.0     | -1.0          | -1.0          | \[-0.0, 0.0]      |
| Ackley N.3 | -186.411213 | 0.0     | -186.411      | ≈ -186.411    | \[0.0, -0.006773] |

---

## Notes

* The algorithm consistently converged to the true global minima across all 20 runs.
* Unlike GA (which showed small variance across runs), PSO in this configuration achieved **perfect reproducibility** on these benchmark functions.
* CSV with summary results: `pso_benchmark_results_summary.csv`
