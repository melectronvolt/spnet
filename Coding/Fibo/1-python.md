# Python 📇

## Benchmark parameters

This page describe the framework to compute the results and print them. And above all handle the call of the libraries.

### Benchmark parameters `benchParameters.py`
```python
class parameters:  
    fiboMaxTerms: int = 74  # 74 is the maximum number of terms that can be calculated, it must fit in int64  
    numberRun: int = 40  # Number of times the test is performed  
    fiboStart: int = 1  # The first term of the fibonacci sequence  
    fiboMaxValue: int = 1304969544928657  # The maximum value of the fibonacci sequence, it must fit in int64  
    fiboMaxFactor: int = 4000000  # The maximum value of the factorization  
    fiboNbrOfLoops: int = 7  # The number of times the test is performed  
    showResult: bool = False  # Hide the result of the test
```
### Compute the value and print the value `printResults.py`
```python
from typing import List  
from benchParameters import parameters
```
#### Compute
```python
def mean(lst: List[float]) -> float:
    """Calculate the mean.

       :param lst: List[float]
          The list of values.
       :type lst: list of float

       :return: float
          The mean.
    """
    return sum(lst) / len(lst)


def standard_deviation(lst: List[float]) -> float:
    """Calculate the standard deviation.

       :param lst: List[float]
          The list of values.
       :type lst: list of float

       :return: float
          The standard deviation.
    """
    # Calculate the variance (average of squared differences from the mean)
    variance = sum((x - mean(lst)) ** 2 for x in lst) / len(lst)
    # Standard deviation is the square root of the variance
    std_dev = variance ** 0.5
    return std_dev

def standard_uncertainty(lst: List[float]) -> float:
    """Calculate the standard uncertainty.
       :param lst: List[float]
          The list of values.
       :type lst: list of float

       :return: float
          The standard uncertainty or -1 if failure.
    """
    if (len(lst) > 1):
        variance_correct = sum((x - mean(lst)) ** 2 for x in lst) / (len(lst) - 1)
        std_dev_correct = variance_correct ** 0.5
        se = std_dev_correct / len(lst) ** 0.5
        return se
    else:
        return -1
```
#### Print the value
```python
def printResults(arPrimes, arTerms, goldenNbr, maxTerms, listTimeCount, nameTest):
    """Print the results of the test, exploit value from the arrays.

   :param arPrimes: array of bool
      If it is True it is a prime number.
   :type arPrimes: list of bool
   :param arTerms: array of int64 items (max)
      Each term of the fibonacci sequence is stored in this array.
      For each 50 items, the first is the current term, the 49 others are the factors.
   :type arTerms: list of int64 items (max)
   :param goldenNbr: float
      The golden number, not calculated by the division, but directly with (1 + sqrt(5)) / 2.
   :type goldenNbr: float
   :param maxTerms: unsigned char
      The maximum number of terms that can be calculated, it must fit in int64.
   :type maxTerms: unsigned char
   :param listTimeCount: array of float
      The time taken for the test.
   :type listTimeCount: list of float
   :param nameTest: str
      The name of the test.
   :type nameTest: str

   :return: None
      This function does not return anything. It prints the results.

   :notes:
      This function prints the results of a test, including the prime numbers,
      terms, the golden number, the maximum number of terms, the time taken,
      and the name of the test.
    """
    if parameters.showResult:
        for i in range(0, maxTerms):
            ligne = ''
            baseIndex = i * 50
            if arTerms[baseIndex]:
                if arPrimes[baseIndex]:
                    ligne += f"{i + 1} - [{arTerms[baseIndex]}] : "
                else:
                    ligne += f"{i + 1} - {arTerms[baseIndex]} : "
                addValue = False
                for position in range(1, 50):
                    index = baseIndex + position
                    if arTerms[index]:
                        if arPrimes[index]:
                            ligne += f"[{arTerms[index]}] x "
                        else:
                            ligne += f"{arTerms[index]} x "
                        addValue = True
                if addValue:
                    ligne = ligne[:- 3]
                else:
                    ligne += "Factor not found"
            if ligne:
                print(ligne)
    print("--------------------------------------------------")
    print(nameTest)
    print("Golden Number : ", goldenNbr)
    print("Mean execution time(s) : " + str(mean(listTimeCount)))
    print("Standard Deviation (s) : " + str(standard_deviation(listTimeCount)))
    print("Standard Uncertainty (s) : " + str(standard_uncertainty(listTimeCount)))
```
### Execute test `main.py`
#### Import
```python
import time  
from printResults import printResults  
from benchParameters import parameters  
from typing import List
from array import array  
import ctypes  
import os  
current_directory = os.getcwd()
```
#### Conduct Test
```python
def execute_loop(nameTest: str, functionToTest) -> None:
    """Execute a test loop for a given function and print the results.

   This function performs a test loop for a specified function and prints the results.
   It runs the function `parameters.numberRun` times, measuring the time taken for each run.
   After the loop, it calculates and prints the results, including prime numbers,
   terms, the golden number, and the time taken.

   :param nameTest: str
      The name of the test.
   :type nameTest: str
   :param functionToTest: callable
      The function to be tested. It should have the signature `() -> Tuple`.
   :type functionToTest: callable

   :return: None
      This function does not return anything but prints the test results."""

    # List of time taken for the test to calculate the mean and the standard deviation
    listTimeCount: List[float] = []

    for _ in range(parameters.numberRun):
        start_time: float = time.time()  # Start the timer
        fbRet, arTerms, arPrimes, arError, goldenNbr = functionToTest()
        end_time: float = time.time()  # End the timer
        listTimeCount.append(end_time - start_time)  # Add the time taken in the list

    printResults(arPrimes, arTerms, goldenNbr, parameters.fiboMaxTerms, listTimeCount, nameTest)
```
#### Windows load DLL for C++ / ASM
```python
# Load the DLL  
lib = ctypes.CDLL(  
    os.path.join(current_directory, 'InteropFibonacciWinCPP.dll'))  # Update with the correct path to your DLL  
# Set the argument types for the fibonacci_interop function  
lib.fibonacci_interop_cpp.argtypes = [  
    ctypes.c_ulonglong, ctypes.c_ubyte, ctypes.c_longlong, ctypes.c_ulonglong, ctypes.c_ubyte,  
    ctypes.POINTER(ctypes.c_ulonglong), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_double),  
    ctypes.POINTER(ctypes.c_double)  
]  
# Set the return type for the fibonacci_interop function  
lib.fibonacci_interop_cpp.restype = ctypes.c_int
```

```python
arTerms = (ctypes.c_ulonglong * (parameters.fiboMaxTerms * 50))()  # Adjust size as needed  
arPrimes = (ctypes.c_bool * (parameters.fiboMaxTerms * 50))()  # Adjust size as needed  
arError = (ctypes.c_double * parameters.fiboMaxTerms)()  # Adjust size as needed  
goldenNbr = ctypes.c_double()  
  
result = lib.fibonacci_interop_cpp(parameters.fiboStart, parameters.fiboMaxTerms, parameters.fiboMaxValue,  
                                   parameters.fiboMaxFactor, parameters.fiboNbrOfLoops, arTerms, arPrimes, arError,  
                                   ctypes.byref(goldenNbr))  
return result, arTerms, arPrimes, arError, goldenNbr.value
```

#### Windows load DLL for Dotnet
##### Import
```python
from pythonnet import load  
load("coreclr")  
import clr  # Import CLR from Python.NET  
clr.AddReference('System')  
clr.AddReference(os.path.join(current_directory, 'DllFibonacci.dll'))  
from DllFibonacci import MyFiboClass  
from System import Array  
from System import UInt64, Boolean, Single, Double  
from System.Runtime.InteropServices import GCHandle, GCHandleType
```
##### Test
```python
def execute_dotnet():  
    arTerms = Array[UInt64](range(parameters.fiboMaxTerms * 50))  
    arPrimes = Array[Boolean]([False] * (parameters.fiboMaxTerms * 50))  
    arError = Array[Double]([0.0] * parameters.fiboMaxTerms)  
  
    # Call the method  
    # Initialize the out parameter as a reference    goldenNbr = Array[Double]([0.0])  
  
    fibonacciResult = MyFiboClass.fibonacci_interop_cs(parameters.fiboStart, parameters.fiboMaxTerms,  
                                                       parameters.fiboMaxValue, parameters.fiboMaxFactor,  
                                                       parameters.fiboNbrOfLoops, arTerms,  
                                                       arPrimes, arError)  
  
    result = fibonacciResult.Result  
    return result, arTerms, arPrimes, arError, fibonacciResult.GoldenNumber
```
#### Linux load SO for C++ / ASM
```python
lib = ctypes.CDLL(
    os.path.join(current_directory, 'libInteropFibonacciWinCPP.so'))  # Update with the correct path to your DLL
# Set the argument types for the fibonacci_interop function
lib.fibonacci_interop_cpp.argtypes = [
    ctypes.c_ulonglong, ctypes.c_ubyte, ctypes.c_longlong, ctypes.c_ulonglong, ctypes.c_ubyte,
    ctypes.POINTER(ctypes.c_ulonglong), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
# Set the return type for the fibonacci_interop function
lib.fibonacci_interop_cpp.restype = ctypes.c_int
```
#### Python
```python
from module_python import fibonacci_interop_python  
```
#### Cython
```python
from fiboCython import fibonacci_interop_cython  
from fiboCythonFull import fibonacci_interop_cython_full  

def execute_cython():  
    """Execute the test in Cython."""  
    arTerms = array('Q', [0] * parameters.fiboMaxTerms * 50)  # 'Q' for unsigned long long  
    arPrimes = array('b', [0] * parameters.fiboMaxTerms * 50)  # 'b' for signed char  
    arError = array('d', [0] * parameters.fiboMaxTerms)  # 'f' for double  
  
    fbRet, goldenNbr = fibonacci_interop_cython(parameters.fiboStart, parameters.fiboMaxTerms, parameters.fiboMaxValue,  
                                                parameters.fiboMaxFactor, parameters.fiboNbrOfLoops, arTerms, arPrimes,  
                                                arError)  
    return fbRet, arTerms, arPrimes, arError, goldenNbr
```

## Python calculation 🧮
Here is the translation of the algorithm for Python, Cython is included

### Import and declaration
```python
from enum import Enum  
from math import sqrt  
from typing import List, Tuple

class fbReturn(Enum):  
    OK = 0  
    TMT = 1  
    TB = 2  
    PRM_ERR = 3
```

### `isPrime()`
```python
    def isPrime(numberPrime: int) -> bool:
        """Check if the number is a prime number.

       :param numberPrime: int
          The number to be tested.
       :type numberPrime: int

       :return: bool
          True if the number is a prime number, False otherwise.

       :notes:
          This algorithm is a brute-force, non-optimized version. The goal is not to optimize it.

          If you want to optimize it, you can consider the following tips:
          - Avoid testing even numbers.
          - Stop testing when the divisor is greater than the square root of the number.

          You can also explore more efficient algorithms such as:
          - The sieve of Eratosthenes tables.
          - The Miller-Rabin algorithm, although it is not the purpose of this test.
        """

        # MaxSearch to don't test all the numbers
        maxSearch: int = numberPrime if numberPrime < maxFactor else maxFactor

        for i in range(2, maxSearch):
            # It's not a prime number if it is divisible by another number (except 1 and itself)
            # The module operator (%) returns the remainder of the division
            if (numberPrime % i) == 0:
                return False
        return True
```
#### Cython
```cython
cdef char isPrime(unsigned long long numberPrime, unsigned long long maxFactor):
    cdef unsigned long long i
    cdef unsigned long long maxSearch = numberPrime if numberPrime < maxFactor else maxFactor
    for i in range(2, maxSearch):
        if numberPrime % i == 0:
            return 0 
    return 1  
```
### `factorization()`
```python
    def factorization(baseIndex: int) -> None:
        """Factorize the number and fill the array after the baseIndex with the factors.

               :param baseIndex: int
                  The base index of the array, which is a multiple of 50.
               :type baseIndex: int

               :return: None
                  This function does not return anything. It fills the arrays.

               :notes:
                  The maximum number of factors is 49.

                  The algorithm used here is not optimized; it's just a straightforward implementation.
        """
        position: int = 0  # The offset in the array after baseIndex
        result = arTerms[baseIndex]  # The number to be factorized
        testNbr = 2  # The number to be tested (1 is not tested, it is useless)

        while result != 1:  # While the number is not factorized
            if (result % testNbr) == 0:  # If the number is divisible by the test number
                position += 1  # We increment the offset in the array
                arTerms[baseIndex + position] = testNbr  # We add the factor in the array
                arPrimes[baseIndex + position] = isPrime(
                    testNbr)  # We check if the factor is a prime number and we add it in the array
                result /= testNbr  # We divide the number by the factor
                if position == 49:  # If the offset is 49, leave the loop, it was the last factor that could be entered in the array
                    break
                continue
            testNbr += 1  # We test the next number
            if testNbr > maxFactor:  # If the test number is greater than the maximum factor, leave the loop
                break
```
#### Cython
```cython
cdef void factorization(unsigned long long* arTerms, char* arPrimes, int baseIndex, unsigned long long maxFactor):  
    cdef int position = 0  
    cdef unsigned long long result = arTerms[baseIndex]  
    cdef unsigned long long testNbr = 2  
  
    while result != 1:  
        if result % testNbr == 0:  
            position += 1  
            arTerms[baseIndex + position] = testNbr  
            arPrimes[baseIndex + position] = isPrime(testNbr, maxFactor)  
            result /= testNbr  
            if position == 49:  
                break  
            continue        testNbr += 1  
        if testNbr > maxFactor:  
            break
```

### Called Function
```python
def fibonacci_interop_python(fbStart: int, maxTerms: int, maxFibo: int, maxFactor: int, nbrOfLoops: int) \
        -> Tuple[fbReturn, List, List, List, float]:
    """ Calculate Fibonacci sequence values and related information.
       :param fbStart: int
          The two first terms of the Fibonacci sequence.
       :type fbStart: int
       :param maxTerms: int
          The maximum number of terms that can be calculated; it must fit in int64.
       :type maxTerms: int
       :param maxFibo: int
          The maximum value of the Fibonacci sequence; it must fit in int64.
       :type maxFibo: int
       :param maxFactor: int
          The maximum value of the factorization.
       :type maxFactor: int
       :param nbrOfLoops: int
          The number of times the test is performed.
       :type nbrOfLoops: int

       :return: Tuple[int, List, List, List, float]
          A tuple with the following components:
          - 0 (int): fbReturn.OK if the test is OK
          - 1 (List[int]): arTerms, a list of integer values (empty by default)
          - 2 (List[bool]): arPrimes, a list of boolean values (empty by default)
          - 3 (List[float]): arError, a list of float values (empty by default)
          - 4 (float): goldenConst, the golden constant

          Possible return values:
          - fbReturn.OK: Test is OK
          - fbReturn.TMT: maxTerms is too high
          - fbReturn.TB: maxFibo is too high
          - fbReturn.PRM_ERR: One of the parameters is not correct
    """
    arTerms: List[int] = []
    arPrimes: List[bool] = []
    arError: List[float] = []
        if (fbStart < 1) or (maxFibo < 1) or (maxTerms < 3) or (maxFactor < 2) or (nbrOfLoops < 1):
        return fbReturn.PRM_ERR, None, None, None, None

    if maxTerms > 93:
        return fbReturn.TMT, None, None, None, None

    if maxFibo > 18446744073709551615:
        return fbReturn.TB, None, None, None, None

    # Compute the golden number
    goldenConst: float = (1 + sqrt(5)) / 2

    # Loop for benchmarks
    for _ in range(nbrOfLoops):

        # Fill the lists with 0, or false
        arTerms = [0] * maxTerms * 50
        arTerms[0] = fbStart
        arTerms[50] = fbStart
        arPrimes = [0] * maxTerms * 50
        arError = [0] * maxTerms

        # Factorize the first two terms
        factorization(0)
        factorization(50)

        for currentTerm in range(2, maxTerms):  # Loop for the fibonacci sequence
            baseIndex = currentTerm * 50  # The base index of the array which is a multiple of 50
            nextValue = arTerms[baseIndex - 50] + arTerms[
                baseIndex - 2 * 50]  # The next value of the fibonacci sequence

            if nextValue > maxFibo:  # If the next value is greater than the maximum value, leave the loop
                return fbReturn.OK, arTerms, arPrimes, arError, goldenConst

            arTerms[baseIndex] = nextValue  # We add the next value in the array
            arPrimes[baseIndex] = isPrime(
                arTerms[baseIndex])  # We check if the next value is a prime number and we add it in the array
            arError[currentTerm] = abs(
                goldenConst - (arTerms[baseIndex] / arTerms[baseIndex - 50]))  # We calculate the error
            factorization(baseIndex)  # We factorize this value

    return fbReturn.OK, arTerms, arPrimes, arError, goldenConst
```

#### Cython
```cython
cdef fbReturn fibonacci_interop_c(unsigned long long fbStart, unsigned char maxTerms, unsigned long long maxFibo, unsigned long long maxFactor, unsigned char nbrOfLoops,unsigned long long* arTerms, char* arPrimes, double* arError, double* goldenNbr):
    cdef int  baseIndex
    cdef int currentTerm
    cdef unsigned long long nextValue

    goldenNbr[0] = (1 + sqrt(5)) / 2

    if fbStart < 1 or maxFibo < 1 or maxTerms < 3 or maxFactor < 2 or nbrOfLoops < 1:
        return fbReturn.PRM_ERR

    if maxTerms > 93:
        return fbReturn.TMT

    if maxFibo > 18446744073709551615 or maxFactor > 18446744073709551615:
        return fbReturn.TB

    for _ in range(nbrOfLoops):
        arTerms[0] = fbStart
        arTerms[50] = fbStart
        factorization(arTerms, arPrimes, 0, maxFactor)
        factorization(arTerms, arPrimes, 50, maxFactor)

        for currentTerm in range(2, maxTerms):
            baseIndex = currentTerm * 50
            nextValue = arTerms[baseIndex - 50] + arTerms[
                baseIndex - 2 * 50]  # The next value of the fibonacci sequence

            if nextValue > maxFibo:  # If the next value is greater than the maximum value, leave the loop
                return fbReturn.OK

            arTerms[baseIndex] = nextValue
            arPrimes[baseIndex] = isPrime(arTerms[baseIndex], maxFactor)
            arError[currentTerm] = abs(goldenNbr[0] - (arTerms[baseIndex] / arTerms[baseIndex - 50]))
            factorization(arTerms, arPrimes, baseIndex, maxFactor)

    return fbReturn.OK

cpdef tuple fibonacci_interop_cython(unsigned long long fbStart, unsigned char maxTerms, unsigned long long maxFibo, unsigned long long maxFactor, unsigned char nbrOfLoops,array arTermsArray, array arPrimesArray, array arErrorArray):
    cdef unsigned long long[:] arTerms = arTermsArray
    cdef char[:] arPrimes = arPrimesArray
    cdef double[:] arError = arErrorArray
    cdef double goldenNbr

    # Call the C function
    result = fibonacci_interop_c(fbStart, maxTerms, maxFibo, maxFactor, nbrOfLoops,
                                         &arTerms[0], &arPrimes[0], &arError[0], &goldenNbr)

    # Return the result and golden number
    return result, goldenNbr
```

#### Cython full

```cython
cpdef void fibonacci_interop_cython_full(unsigned long long fbStart, unsigned char maxTerms, unsigned long long maxFibo, unsigned long long maxFactor,  
                                 unsigned char nbrOfLoops, unsigned char nbrOfRuns):  
    cdef unsigned long long * arTerms  
    cdef char * arPrimes  
    cdef double * arError  
    cdef double * timeArray  
    cdef double goldenNbr  
    cdef int array_size  
    
    # Dynamically allocate memory  
    array_size = maxTerms * 50  
    arTerms = <unsigned long long *> malloc(array_size * sizeof(unsigned long long))  
    arPrimes = <char *> malloc(array_size * sizeof(char))  
    arError = <double *> malloc(maxTerms * sizeof(double))  
    timeArray = <double *> malloc(nbrOfRuns * sizeof(double))  
  
    # Check if memory allocation was successful but we don't care  
    if not arTerms or not arPrimes or not arError or not timeArray:  
        # Handle memory allocation failure  
        if arTerms: free(arTerms)  
        if arPrimes: free(arPrimes)  
        if arError: free(arError)  
        if timeArray: free(timeArray)  
        raise MemoryError("Failed to allocate memory")  

	''' ---------------
	   SOME STUFF
	 ---------------'''
  
    # Free memory  
    free(arTerms)  
    free(arPrimes)  
    free(arError)  
    free(timeArray)
```