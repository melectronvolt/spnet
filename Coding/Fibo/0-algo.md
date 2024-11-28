# The Algorithm 🗺️

## FlowChart

```{image} ../../_static/_medias/it/fibo/algo1.svg
:width: 700px
:align: center
:class: vspace
```

## Compute Golden Constant

$$ \frac{1+\sqrt{5}}{2}$$

## Check parameters

```{image} ../../_static/_medias/it/fibo/algo2.svg
:width: 700px
:align: center
:class: vspace
```



```{attention}
- The maximum term is 93, which is $12,200,160,415,121,876,738$; the 94th term exceeds 64 bits.
- Risk of overflow if it’s exceed 64 bits. $2^{64} -1 = 18,446,744,073,709,551,615.$
```


# Improvements for searching prime numbers
- If you want to optimize it, you can consider the following tips: 
	- Avoid testing even numbers.  
	- Stop testing when the divisor is greater than the square root of the number.  
	  
- You can also explore more efficient algorithms such as:  
	- The sieve of Eratosthenes tables.  
	- The Miller-Rabin algorithm, although it is not the purpose of this test.