# C++ 💫

Just the translation from python, really easy
## CMakeLists.txt
### Windows
```cmake
cmake_minimum_required(VERSION 3.27)  
project(InteropFibonacciWinCPP)  
  
set(CMAKE_CXX_STANDARD 17)  
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /O2 /arch:AVX2")  
  
add_library(InteropFibonacciWinCPP SHARED library.cpp)
```
### Linux
```cmake
cmake_minimum_required(VERSION 3.27)
project(InteropFibonacciWinCPP)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -march=native")

add_library(InteropFibonacciWinCPP SHARED library.cpp)
```
## Prologue
```cpp
#include <cmath>  
#include <string>  
  
enum class fbReturn {  
    OK, TMT, TB, PRM_ERR  
};
```
## Prime number ?
```cpp
bool isPrime(unsigned long long numberPrime, unsigned long long maxFactor) {  
    int maxSearch = (numberPrime < maxFactor) ? numberPrime : maxFactor;  
    for (unsigned long long i = 2; i < maxSearch; ++i) {  
        if (numberPrime % i == 0)  
            return false;  
    }    return true;  
}
```
## Do Factorization
```cpp
void factorization(unsigned long long* arTerms, bool* arPrimes, int baseIndex, unsigned long long maxFactor) {  
    int position = 0;  
    unsigned long long result = arTerms[baseIndex];  
    unsigned long long testNbr = 2;  
  
    while (result != 1) {  
        if (result % testNbr == 0) {  
            position += 1;  
            arTerms[baseIndex + position] = testNbr;  
            arPrimes[baseIndex + position] = isPrime(testNbr, maxFactor);  
            result /= testNbr;  
            if (position == 49)  
                break;  
            continue;  
        }        testNbr += 1;  
        if (testNbr > maxFactor)  
            break;  
    }}
```
## The test
```cpp
extern "C" __declspec(dllexport) fbReturn fibonacci_interop_cpp(unsigned long long fbStart, unsigned char maxTerms, unsigned long long maxFibo, unsigned long long maxFactor, unsigned char nbrOfLoops,  
                           unsigned long long* arTerms, bool* arPrimes, double* arError, double& goldenNbr) {  
  
    if (fbStart < 1 || maxFibo < 1 || maxTerms < 3 || maxFactor < 2 || nbrOfLoops < 1)  
        return fbReturn::PRM_ERR;  
  
    if (maxTerms > 93)  
        return fbReturn::TMT;  
  
    if (maxFibo > 18446744073709551615)  
        return fbReturn::TB;  
    if (maxFactor > 18446744073709551615)  
        return fbReturn::TB;  
  
    goldenNbr = (1 + sqrt(5)) / 2;  
    unsigned long long nextValue;  
  
    for (int loop = 0; loop < nbrOfLoops; ++loop) {  
        std::fill_n(arTerms, maxTerms * 50, 0);  
        arTerms[0] = arTerms[50] = fbStart;  
        std::fill_n(arPrimes, maxTerms * 50, false);  
        std::fill_n(arError, maxTerms, 0.0);  
  
        factorization(arTerms, arPrimes, 0, maxFactor);  
        factorization(arTerms, arPrimes, 50, maxFactor);  
  
        for (int currentTerm = 2; currentTerm < maxTerms; ++currentTerm) {  
            int baseIndex = currentTerm * 50;  
            nextValue = arTerms[baseIndex - 50] + arTerms[baseIndex - 100];  
  
            if (nextValue > maxFibo)  
                return fbReturn::OK;  
  
            arTerms[baseIndex] = nextValue;  
            arPrimes[baseIndex] = isPrime(arTerms[baseIndex], maxFactor);  
            arError[currentTerm] = abs(goldenNbr - (arTerms[baseIndex]) / arTerms[baseIndex - 50]);  
            factorization(arTerms, arPrimes, baseIndex, maxFactor);  
        }    }  
    return fbReturn::OK;  
}
```