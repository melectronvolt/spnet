# Results 🥇

## Information ℹ️
- CPU : 13th Gen Intel(R) Core(TM) i7-13700K   3.40 GHz
- RAM : 64,0 GB
- Windows 11 23H2
- Ubuntu 13.10 on Virtual Machine, VirtualBox 7.0.12, host Windows, 32 GB, 16 processors
## Performance 🚩
### 🪟 Windows

| Language / Framework                              | Execution Time (s) | Slower than C++ |
| ------------------------------------------------- | :----------------: | :-------------: |
| C++ MSVC x64 v19.38.33133 / Linker v14.38.33133.0 |  1.0028 ± 0.0007   |      1.0x       |
| DotnetCore v8.0.100                               |  1.0029 ± 0.0006   |      1.0x       |
| Cython v3.0.7                                     |  1.0045 ± 0.0005   |      1.0x       |
| Cython Full v3.0.7                                |  1.0047 ± 0.0005   |      1.0x       |
| ASM - MASM x64 v14.38.33133.0                     |  1.3251 ± 0.0002   |      1.3x       |
| ASM - NASM x64 v2.16.01                           |  1.3258 ± 0.0002   |      1.3x       |
| Javascript - nodeJS v21.5.0                       |    2.74 ± 0.06     |      2.7x       |
| TypeScript - compiled v21.5.0                     |    3.20 ± 0.03     |      3.2x       |
| TypeScript ts-node v5.3.3                         |    3.20 ± 0.03     |      3.2x       |
| PyPy v7.3.14 with MSC v.1929 with python v3.10.13 |   7.734 ± 0.009    |      7.7x       |
| Firefox v122.0b4                                  |   9.775 ± 0.006    |      9.8x       |
| TypeScript compiled Firefox v122.0b4              |    9.87 ± 0.03     |      9.9x       |
| Python 3.12.1                                     |    27.09 ± 0.02    |      27.1x      |

```python
import matplotlib.pyplot as plt  
import numpy as np  
  
languages = [  
    "ASM - MASM x64 v14.38.33133.0", "ASM - NASM x64 v2.16.01",  
    "C++ MSVC x64 v19.38.33133 / Linker v14.38.33133.0", "DotnetCore v8.0.100",  
    "Cython v3.0.7", "Cython Full v3.0.7",  
    "Javascript - nodeJS v21.5.0", "TypeScript - compiled v21.5.0",  
    "TypeScript ts-node v5.3.3", "PyPy v7.3.14 with MSC v.1929 with python v3.10.13",  
    "Firefox v122.0b4", "TypeScript compiled Firefox v122.0b4",  
    "Python 3.12.1"  
]  
execution_times = [  
    1.3251, 1.3258 ,  
    1.0028, 1.0029,  
    1.0045, 1.0047,  
    2.74, 3.20,  
    3.20, 7.734,  
    9.775, 9.87,  
    27.09  
]  
  
# Create a logarithmic scale for color mapping  
log_scale = np.log10(execution_times)  
log_min, log_max = np.min(log_scale), np.max(log_scale)  
colors = plt.cm.jet((log_scale - log_min) / (log_max - log_min))  
  
# Creating the histogram with adjusted colors  
fig, ax = plt.subplots(figsize=(18, 8))  # Increased width for better visibility  
bars = ax.barh(languages, execution_times, color=colors)  
plt.xlabel('Execution Time (s)')  
plt.ylabel('Language / Framework')  
plt.title('Execution Time Comparison for Windows 11 23H2')  
  
# Create a colorbar with a logarithmic scale  
sm = plt.cm.ScalarMappable(cmap='jet', norm=plt.Normalize(vmin=min(execution_times), vmax=max(execution_times)))  
cbar = plt.colorbar(sm, ax=ax)  
cbar.set_label('Execution Time (s)')  
  
plt.tight_layout()  
plt.show()
```

```{image} ../../_static/_medias/it/fibo/result1.png
:width: 700px
:align: center
:class: vspace
```

### 🐧 Linux
| Language / Framework                            | Execution Time (s) | Slower than C++ |
| ----------------------------------------------- | :----------------: | :-------------: |
| Cython v3.0.7                                   |  1.0151 ± 0.0008   |      1.0x       |
| Cython Full v3.0.7                              |  1.0162 ± 0.0007   |      1.0x       |
| Dotnet Core v8.0.100                            |   1.0181 ± 0.001   |      1.0x       |
| C++ gcc version v13.2.0                         |   1.0185 ± 0.003   |      1.0x       |
| NASM x64 DLL v2.16.01                           |  1.3356 ± 0.0001   |      1.3x       |
| Javascript - nodeJS v21.5.0                     |    2.59 ± 0.02     |      2.6x       |
| TypeScript ts-node v5.3.3                       |    3.21 ± 0.03     |      3.2x       |
| TypeScript - compiled v21.5.0                   |    3.22 ± 0.03     |      3.2x       |
| PyPy 7.3.14 with GCC 10.2.1 with Python 3.10.13 |   3.450 ± 0.009    |      3.5x       |
| Firefox v119                                    |   4.725 ± 0.004    |      4.7x       |
| TypeScript compiled Firefox v119                |   7.004 ± 0.004    |      7.0x       |
| Python 3.12.1                                   |    19.18 ± 0.03    |      19.2x      |

```{image} ../../_static/_medias/it/fibo/result2.png
:width: 700px
:align: center
:class: vspace
```

## Development and Debug Time 🧑‍💻

| Language / Framework                              | Dev/debug time (min) | Line of codes | Copilot | Debug |
| ------------------------------------------------- |:--------------------:|:-------------:|:-------:|:-----:|
| PyPy v7.3.14 with MSC v.1929 with python v3.10.13 |          30          |      72       |   ✅    |  🟢   |
| Python 3.12.1                                     |          30          |      72       |   ✅    |  🟢   |
| Cython v3.0.7                                     |          45          |      75       |   ✅    |  🟢   |
| Cython Full v3.0.7                                |          60          |      114      |   ✅    |  🟢   |
| C++ MSVC x64 v19.38.33133 / Linker v14.38.33133.0 |         120          |      63       |   ✅    |  🟢   |
| DotnetCore v8.0.100                               |         120          |      84       |   ✅    |  🟢   |
| Javascript - nodeJS v21.5.0                       |         140          |      125      |   ✅    |  🟡   |
| TypeScript - compiled v21.5.0                     |         140          |      131      |   ✅    |  🟡   |
| TypeScript ts-node v5.3.3                         |         140          |      131      |   ✅    |  🟡   |
| Firefox v122.0b4                                  |         140          |      125      |   ✅    |  🟡   |
| TypeScript compiled Firefox v122.0b4              |         140          |      131      |   ✅    |  🟡   |
| ASM - MASM x64 v14.38.33133.0                     |         660          |      255      |   ❌    |  🔴   |
| ASM - NASM x64 v2.16.01                           |         660          |      254      |   ❌    |  🔴   |

```{image} ../../_static/_medias/it/fibo/result3.png
:width: 700px
:align: center
:class: vspace
```

## Size of executable 📦

| Language / Framework                              | Size (kB)  | 
| ------------------------------------------------- |:----------:|
| ASM - MASM x64 v14.38.33133.0                     |   3.072    |
| ASM - NASM x64 v2.16.01                           |   3.072    |
| C++ MSVC x64 v19.38.33133 / Linker v14.38.33133.0 |   11.264   |
| Javascript - nodeJS v21.5.0                       |  8431.893  |
| TypeScript - compiled v21.5.0                     |  8431.893  |
| TypeScript ts-node v5.3.3                         |  8431.893  |
| Cython v3.0.7                                     | 20971.520  |
| Cython Full v3.0.7                                | 20971.520  |
| Python 3.12.1                                     | 20971.520  |
| PyPy v7.3.14 with MSC v.1929 with python v3.10.13 | 111995.055 |
| DotnetCore v8.0.100                               | 104857.600 |
| Firefox v122.0b4                                  | 235061.671 |
| TypeScript compiled Firefox v122.0b4              | 235061.671 |

```{image} ../../_static/_medias/it/fibo/result4.png
:width: 700px
:align: center
:class: vspace
```