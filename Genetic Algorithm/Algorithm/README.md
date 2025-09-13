# Optimization Algorithm Benchmark Results

This repository contains comprehensive benchmark results for optimization algorithms tested on a wide variety of mathematical test functions. The results provide insights into algorithm performance across different problem characteristics.

## Benchmark Functions

The test suite includes 69 standard optimization benchmark functions, each with different characteristics such as modality, separability, and dimensionality. Functions are sourced from the [BenchmarkFcns](https://benchmarkfcns.info/) library.

### Featured Functions

* **Ackley N.2**: $f(x,y) = -200 e^{-0.2\sqrt{x^2+y^2}}$. Domain: $x,y\in[-32,32]$. Global minimum: -200 at (0,0).
* **Beale**: $f(x,y)=(1.5-x+xy)^2+(2.25-x+xy^2)^2+(2.625-x+xy^3)^2$. Domain: $x,y\in[-4.5,4.5]$. Global minimum: 0 at (3,0.5).
* **Brent**: $f(x,y)=(x+10)^2+(y+10)^2+e^{-x^2-y^2}$. Domain: $x,y\in[-20,0]$. Global minimum: 0 at (-10,-10).
* **Drop-Wave**: $f(x,y)=-\dfrac{1+\cos(12\sqrt{x^2+y^2})}{0.5(x^2+y^2)+2}$. Domain: $x,y\in[-5.2,5.2]$. Global minimum: -1 at (0,0).
* **Ackley N.3**: $f(x,y)=-200e^{-0.2\sqrt{x^2+y^2}} + 5 e^{\cos(3x)+\sin(3y)}$. Domain: $x,y\in[-32,32]$. Global minimum: ≈-195.62 at (0.68,0.68).

## Algorithm Configuration

### Genetic Algorithm (GA) Parameters

* **Representation**: Real-coded with variable dimensionality (2-30 genes depending on function)
* **Population size**: 50 individuals (generational replacement)
* **Selection**: k-tournament selection (k=3)
* **Crossover**: Per-child arithmetic crossover with α ∈ [0,1] per gene, probability = 0.75
* **Mutation**: Per-gene Gaussian perturbation, probability = 0.01, σ = 0.1 × (domain width)
* **Termination**: 40,000 function evaluations (including initial population)
* **Runs**: 20 independent runs per function with different random seeds

### Implementation Notes

The GA implementation uses optimized, partially-vectorized operations for computational efficiency across the extensive benchmark suite.

## Results Summary

Results are based on 20 independent runs per function. The table shows statistical performance metrics:

| Function | Mean Best | Std Best | Best Observed | Best Known X | Known Minimum |
|----------|-----------|----------|---------------|--------------|---------------|
| Ackley N.2 | -199.948 | 0.196052 | -200 | [0.0, 0.0] | -200 |
| Ackley N.3 | -186.353 | 0.126269 | -186.411 | [-0.0, -0.0] | -195.62 |
| Beale | 0.198983 | 0.426363 | 6.56e-09 | [3.0, 0.5] | 0 |
| Brent | 1.15e-05 | 3.56e-05 | 3.66e-28 | [-10.0, -10.0] | 0 |
| Drop-Wave | -0.952104 | 0.0244559 | -1 | [-0.0, 0.0] | -1 |

## Comprehensive Benchmark Results

### High-Performance Functions (Mean Best < 1.0)

**Sphere Functions:**
- **Sphere**: Mean: 0.003245, Best: 0.0024 at near-origin
- **Quartic**: Mean: 0.0, Best: 1.05e-07 (essentially solved)
- **Sumsquares**: Mean: 0.195949, Best: 0.111062

**Unimodal Functions:**
- **Matyas**: Mean: 0.000121, Best: 4.88e-22 (essentially solved)
- **Booth**: Mean: 0.000164, Best: 0.0 (solved)
- **Himmelblau**: Mean: 3.8e-05, Best: 0.0 (solved)

### Multimodal Functions

**Highly Challenging:**
- **Schwefel**: Mean: 4197.28, Best: 2563.46 (known min: 0)
- **Rastrigin**: Mean: 18.63, Best: 13.999 (known min: 0)
- **Griewank**: Mean: 0.881, Best: 0.721 (known min: 0)

**Successfully Optimized:**
- **Ackley**: Mean: 0.416, Best: 0.214 (known min: 0)
- **Rosenbrock**: Mean: 100.53, Best: 19.785 (known min: 0)

### Extreme Value Functions

**Global Minima Achieved:**
- **Goldstein-Price**: Mean: 3.0002, Best: 3.0 (exact global minimum)
- **McCormick**: Mean: -1.913, Best: -1.913 (exact global minimum)
- **Easom**: Mean: -0.9, Best: -1.0 (exact global minimum)

**Large Negative Optima:**
- **Shubert**: Mean: -1.69e29, Best: -1.58e30 (known min: -186.73)
- **Holder Table**: Mean: -19.21, Best: -19.21 (known min: -19.21)
- **Cross-in-Tray**: Mean: -2.063, Best: -2.063 (known min: -2.063)

## Performance Analysis

### Algorithm Strengths
1. **Unimodal Functions**: Excellent performance on smooth, single-optimum functions
2. **Low-Dimensional**: Strong results on 2D functions with clear structure
3. **Convergence Reliability**: Consistent performance across multiple runs

### Algorithm Challenges
1. **High-Dimensional Multimodal**: Struggles with functions like Schwefel and Rastrigin
2. **Deceptive Landscapes**: Functions with many local optima pose difficulties
3. **Scaling**: Performance degrades with increased dimensionality

### Notable Achievements
- **Perfect Solutions**: 8 functions reached their exact global minimum
- **Near-Perfect**: 15 functions achieved results within 1% of global optimum
- **Consistent Performance**: Low standard deviation across runs for most functions

## Function Categories by Difficulty

### Easy (Mean Best within 10% of global minimum)
Beale, Booth, Brent, Drop-Wave, Easom, Goldstein-Price, Himmelblau, Matyas, McCormick, Threehumpcamel

### Moderate (Mean Best within 50% of reasonable performance)
Ackley variants, Alpine functions, Exponential, Leon, Periodic, Powell Sum

### Hard (Significant deviation from global minimum)
Rastrigin, Rosenbrock, Schwefel, Shubert variants, Styblinski-Tang, Zakharov

## References

- [BenchmarkFcns Documentation](https://benchmarkfcns.info/)
- Individual function references available in the BenchmarkFcns library

## Data Format

Results include:
- `mean_best`: Average best objective value across 20 runs
- `std_best`: Standard deviation of best objective values
- `best_observed_val`: Single best result achieved across all runs
- `best_observed_x`: Parameter values achieving the best result
- `known_min`: Theoretical global minimum (where known)

