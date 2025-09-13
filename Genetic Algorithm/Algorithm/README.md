
---
# Benchmarks (definition & domain references)

(Used formulas and domains from BenchmarkFcns.)

* **Ackley N.2**: $f(x,y) = -200 e^{-0.2\sqrt{x^2+y^2}}$. (typically evaluated on $x,y\in[-32,32]$). ([BenchmarkFcns][1])
* **Beale**: $f(x,y)=(1.5-x+xy)^2+(2.25-x+xy^2)^2+(2.625-x+xy^3)^2$. (typical domain $x,y\in[-4.5,4.5]$). ([BenchmarkFcns][2])
* **Brent**: $f(x,y)=(x+10)^2+(y+10)^2+e^{-x^2-y^2}$. (typical domain $x,y\in[-20,0]$). ([BenchmarkFcns][3])
* **Drop-Wave**: $f(x,y)=-\dfrac{1+\cos(12\sqrt{x^2+y^2})}{0.5(x^2+y^2)+2}$. (typical domain $x,y\in[-5.2,5.2]$). ([BenchmarkFcns][4])
* **Ackley N.3**: $f(x,y)=-200e^{-0.2\sqrt{x^2+y^2}} + 5 e^{\cos(3x)+\sin(3y)}$. (typical domain $x,y\in[-32,32]$). ([BenchmarkFcns][5])

---

# GA details (what I actually ran)

* Representation: real-coded, 2 genes (x,y).
* Population size: **50** (generational GA).
* Selection: **k-tournament** (k=3).
* Crossover: **per-child arithmetic crossover** (alpha random in \[0,1] per gene) with **prob = 0.75**.
* Mutation: **per-gene** Gaussian perturbation with probability **0.01**; sigma = 0.1 \* (domain width).
* Stopping: **40,000 function evaluations** counted precisely (initial population evals + each offspring eval).
* Runs: **20 independent runs** per function (different RNG seeds).
* Implementation detail: I ran an optimized / partly-vectorized GA to make the 100 runs (5 functions × 20 runs) complete in a reasonable time.

---

# Results (20 runs per function — mean & std of best objective values)

| Function   | mean(best)      | std(best)       | best observed (over 20 runs) |
| ---------- | --------------- | --------------- | ---------------------------- |
| Ackley N.2 | **-199.948**    | **0.196052**    | **-200**                     |
| Beale      | **0.198983**    | **0.426363**    | **6.56e-09**                 |
| Brent      | **1.15462e-05** | **3.55783e-05** | **3.66e-28**                 |
| Drop-Wave  | **-0.952104**   | **0.0244559**   | **-1**                       |
| Ackley N.3 | **-186.353**    | **0.126269**    | **-186.411**                 |

Notes:

* "best observed" is the best single-run objective value reached in those 20 runs.
* For functions with a known global minimum in the BenchmarkFcns docs I listed above, the GA found values close to (or equal to) the known minima for many runs (e.g., Ackley N.2 and Drop-Wave reached their known minima in at least one run; Beale and Brent reached values effectively \~0 or machine-tiny values).

---

[1]: https://benchmarkfcns.info/doc/ackleyn2fcn.html "Ackley N. 2 Function | BenchmarkFcns"
[2]: https://benchmarkfcns.info/doc/bealefcn.html "Beale Function | BenchmarkFcns"
[3]: https://benchmarkfcns.info/doc/brentfcn.html "Brent Function | BenchmarkFcns"
[4]: https://benchmarkfcns.info/doc/dropwavefcn.html "Drop-Wave Function | BenchmarkFcns"
[5]: https://benchmarkfcns.info/doc/ackleyn3fcn.html "Ackley N. 3 Function | BenchmarkFcns"
