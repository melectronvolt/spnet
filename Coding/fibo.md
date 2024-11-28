# ⏱️ Fibonacci Project 

## The project
This project involves translating algorithm in different programming languages to perform certain tasks, such as generating Fibonacci sequence items, detecting prime numbers, and computing the golden ratio. Disclaimer, this project was done fast, it was for pedagogical purpose and it’s not a good example of state of the art coding.

### Project Overview
This project involves creating and comparing algorithms in different programming languages for scientific computing tasks. The main objectives are to:
- Generate the first `n` items of the Fibonacci sequence.
- Detect prime numbers up to a user-defined limit.
- Compute the golden ratio and calculate its error against $\frac{1+\sqrt{5}}{2}$.
#### Cross-Platform Compatibility
- The program should be compatible with both **Linux** 🐧 and **Windows** 🪟 operating systems.
#### Packaging and Language Requirements

- Compile into **DLL** for Windows and **SO** for Linux.
- Callable via **Python**, with Python handling time tracking.
- Implementations in various languages:
  - **Assembly**: MASM x64 for DLL and NASM for DLL/SO (no SIMD AVX2 instructions).
  - **C++**: Using MSVC x64 and GCC compilers with `-O3` or `/Ox` optimizations.
  - **C#**: Using .NET Core 8 for DLL.
  - **Python**: Version 3.12.1, it’s forbidden in our example to use extra library in C like numpy or panda.
  - PyPy 7.3.14
  - **JavaScript/TypeScript**: Node.js (version 21.5.0) and in Firefox.
#### Performance Metrics
- **Time to Code**: Measure the development and debugging time in each language using JetBrains IDEs and GitHub Copilot.
- **Execution Time**: Record the time for single and multiple executions, including computing the uncertainty.

$$ u(\Delta T) = \frac{\sigma_{n-1}}{\sqrt{n}}$$

$$\sigma_{n-1} = \sqrt{ \frac{1}{n-1} \sum_{i=1}^{n} (\Delta t_i - \mu)^2 }$$

$$ \mu = \sum^n_{i=1} \frac{\Delta t_i}{n}$$

#### Optimization Constraints
- Focus on straightforward algorithms without excessive optimization.
## Goal
This structured approach allows for an in-depth comparison of different programming languages and environments in handling typical scientific computing tasks.
## Return

```cpp
enum fbReturn {
    OK,      // 0
    TMT,     // Too much terms
    TB,      // Too big
    PRM_ERR, // Parameters error
};
```

## Signature

```cpp
extern "C" fbReturn FibonacciInterop(
	unsigned long long fbStart,
	unsigned char maxTerms, // Number of terms to compute (2 byte)
	unsigned long long maxFibo,  // Max number of terms (2 byte)
    unsigned long long maxFactor, // Max Factorization number (4 bytes)
    unsigned char nbrOfLoops, // number of loops of the algorithms (1 byte Max)
    unsigned long long* arTerms, // pointer to an array of `maxTerms` * 50 unsigned Long Long integer (quad word) to store the Fibonacci Term (flatten multidim)
    bool* arPrimes, // pointer to an array of `maxTerms` * 50  Boolean (1 bit), true if it's prime and false if it's not (flatten multidim)
    double* arErrors, // pointer of `maxTerms` array of double precision float to store the error of the gold number
    double& fldGoldNumber, // pointer to a double precision float to store final value of gold number
}
```

```{toctree}
:maxdepth: 1

Fibo/0-algo
Fibo/1-python
Fibo/2-cpp
Fibo/3-asm
Fibo/4-dotnet
Fibo/5-js
Fibo/6-results
Fibo/7-conclusion
```