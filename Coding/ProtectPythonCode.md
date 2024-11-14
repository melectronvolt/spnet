# Protect Python Code 🛡️

# ℹ Introduction
Python scripts can be protected in order to avoid stealing intellectual property, algorithms or anything else you want to hide from the final user. As using an interpreter (usually `CPython`), your code is translated from human readable language (python) in python bytecodes (stored in `__pycache__`) by the computer of the user; with some modifications of `CPython` source code, you could extract all the code (even if it's obfuscated) without difficulties. The solution provided here does work only with `Windows`. But you could use `Wine` on Linux to run the binaries. 

```{image} ../_static/_medias/it/python/protect/Structure_Protection.png
:width: 700px
:align: center
:class: vspace
```

```{admonition} How to dump code object to disk ?
Compile Python from the source. Modify the `_PyEval_EvalFrameDefault` function such that it dumps the code object to disk.
```


In this note, I propose a strong way of protecting your python scripts. Python Script will be obfuscated by a tool named **`PyArmor`** which relies on an external unknown not open-source library. The essential algorithms/functions will be translated in C++ by **`Cython`** which will provide a Dynamic Link Library which will be protected by **`Enigma Protector`** and called by our Python script. All the program will be packed with **`PyInstaller`**.
# 🔧 Requirements
- [Enigma Protector](https://enigmaprotector.com/en/order.html) - 200 €
In order to compile, you need to move two files in your project from the sdk/VC path of *Enigma Protector*. 
File 1 : `enigma_ide.h`
File 2 : `enigma_ide64.lib`

In `enigma_ide.h`, just insert the following line.
```cpp
#include <windows.h>
```

- [PyArmor](https://pyarmor.readthedocs.io) - 100 €
```bash
pip install pyarmor
pyarmor register pyarmor-regfile-1.zip
pyarmor -v
```
```bash
Pyarmor 8.1.9 (pro), 00XXXX, XXXXXXXX

License Type    : pyarmor-pro
License No.     : pyarmor-vax-00XXXX
License To      : XXXXXXXX (Rémi MEVAERE)

BCC Mode        : Yes
RFT Mode        : Yes

Notes
* Internet connection is required to verify Pyarmor license
```
- [Cython](https://cython.readthedocs.io/en/latest/) with [MSVC](https://visualstudio.microsoft.com/downloads/)
```bash
pip install cython
```
- [PyInstaller](https://pyinstaller.org/)
```bash
pip install pyinstaller
```
- [UPX](https://upx.github.io/)
```bash
choco install upx
```
## ⚙️Process


```{image} ../_static/_medias/it/python/protect/mermaid-diagram-2024-11-14-143155.svg
:width: 700px
:align: center
:class: vspace
```


# 🔨 Building protected `extension.pyd`
## 🏎️ Cython testing

```{admonition} About Cython
Cython is a programming language that aims to be a superset of the Python programming language, designed to give C-like performance with code that is written mostly in Python with optional additional C-inspired syntax. Cython is a compiled language that is typically used to generate CPython extension modules.
```


Cython could generate with your Python code a **c++ file** which could be compiled in a dynamic link library (DLL) which could be directly called by your python code.

The first file is the python file script you want to convert in C. Please note the extension **.pyx**.
File : `fib.pyx`

```python
# cython: language_level=3
def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()
```

Now we need to create the `setup.py`, which is a python Makefile (for more information
see [Source Files and Compilation](https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html)
File : `setup.py`

```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fib.pyx"),
)
```

Run the following command :

```bash
python setup.py build_ext --inplace
```

It converts it in `c` and compile with `msvc` in `fib.cp311-win_amd64.pyd`



```{image} ../_static/_medias/it/python/protect/shareware1.png
:width: 700px
:align: center
:class: vspace
```

**DLL Export Viewer** tells us this is a valid DLL

```python
import fib

fib.fib(50000000)  # will give the expected result
```
## 🔮 Enigma Protector
The goal is to protect your python app, and especially here  with Enigma Protector your extension in `.pyd`. In order to do this, you will need :

- some of your most important code into a `.pyx file` which will be converted in `c++`, this code will be protected ;
- protect the DLL produced by cython with enigma protector ;
- Use it !

```{important}
C compiled files are faster than python cause they don't deal with python object structure. C files are also faster when they deal with loops, and cause they don't deal with the GIL, cython gives you the opportunity to use all your CPU cores.
```

```{warning}
Be careful, GIL exists to avoid some complex problem with memory access to shared variables and handle correctly garbage collector.
```


### ⚒ Tuning before compilation
Here we are working with a `c++` file. It doesn't change a lot except in `setup.py`.
File : `setup.py`

```python
from setuptools import setup, Extension  
from Cython.Distutils import build_ext

setup(
    name='Test app',
    ext_modules=[
        Extension('test_it',
                  sources=['script_test.pyx'],
                  extra_link_args=['/MAP'],
                  libraries=["enigma_ide64"],
                  language="c++")
    ],
    cmdclass={'build_ext': build_ext}
)
```

### 👓 API Studying
I will not copy all the [manual](https://enigmaprotector.com/en/help.html) in this article, if you want more informations about the API please read the manual.

A ==Marker== is a set of bytes placed into the source code and helping Enigma Protector find the code inside markers for processing. A marker consists of two parts: begin marker and end marker.
```cpp
// Markers API
__declspec(dllimport) void __stdcall EP_Marker(const char*);
```

==EP_RegHardware== function serves for retrieving unique user PC information. The function does not have parameters. If the function succeeds, the return value is a pointer to the null-terminated ANSI string. If the function fails, the return value is 0.
```cpp
// Registration API
__declspec(dllimport) char* __stdcall EP_RegHardwareID(); 
__declspec(dllimport) wchar_t* __stdcall EP_RegHardwareIDW();
```

==EP_RegKeyStatus== EP_RegKeyStatus returns the error status of registration information after the key verification routine. It should be called after any function that verifies registration information, for example, after [EP_RegCheckKey](https://enigmaprotector.com/en/help/manual/228dccf2db5df2e70cce7c6eef76f790) or [EP_RegLoadAndCheckKey](https://enigmaprotector.com/en/help/manual/6e2da73e9435938a6435821a0493d3d7).
```cpp
__declspec(dllimport) int __stdcall EP_RegKeyStatus();
```

==EP_RegCheckAndSaveKeyW== function serves for verifying and saving the registration information. It has the same functionality as [EP_RegCheckAndSaveKey](https://enigmaprotector.com/en/help/manual/5b6524b0b5ceafe4cc77dfb43530dfda), but is used for processing Unicode (wide) strings data. Please note, to use this function you should enable UNICODE Registration Scheme at [REGISTRATION FEATURES - Common panel](https://enigmaprotector.com/en/help/manual/c6986f6340cdc24bb53c8eeba016050f).
```cpp
__declspec(dllimport) BOOL __stdcall EP_RegCheckAndSaveKeyW( const wchar_t* Name, const wchar_t* Key );
```

==EP_RegDeleteKey== function serves for deleting the existing registration information.
```cpp
__declspec(dllimport) BOOL __stdcall EP_RegDeleteKey();
```

==EP_ProtectedString== function returns protected strings. See also [Protection Features - Protected Strings](https://enigmaprotector.com/en/help/manual/4d1c32e6e3747944d4012cb6c54e818c).
```cpp
__declspec(dllimport) int __stdcall EP_ProtectedStringByID( int ID, const char* Str, int Len);  
__declspec(dllimport) int __stdcall EP_ProtectedStringByKey( const char* Key, const char* Str, int Len);
```

#### 🎇 Using Widestring Char (Unicode) in Cython - **wchar_t***

Because the API exposes two kinds of function. One `AnsiString` and one `WideString`, please consider the following code to work with ==WideString==.

```python
# Imports and declaration to work fromWideChar
from cpython.ref cimport PyObject
from libc.stddef cimport wchar_t

cdef extern from "Python.h":
    PyObject * PyUnicode_FromWideChar(wchar_t *w, Py_ssize_t size)
    
# import functions
cdef extern from "enigma_ide.h":
    void EP_Marker(char* Name)
    char* EP_RegHardwareID()
    wchar_t * EP_RegHardwareIDW()   

cdef PyObject * pystr = PyUnicode_FromWideChar(EP_RegHardwareIDW(), -1)
wide_str_hid = str(<object> pystr)
print('WideChar :', wide_str_hid)
```
```python
> WideChar : 02EF34-F57F02
```
#### 🗜️RISC Markers Virtualization
File : `script_test.pyx`
```python
# distutils: language = c++
# cython: language_level=3
# import functions
cdef extern from "enigma_ide.h":
    void EP_Marker(char* Name)

# Declare a trivial function
def sum_it(number1, number2):
    return number1 + number2

# Protect this with RISC virtualization
EP_Marker("vm_risc_begin")
a = 4
b = 7
c = a + b
print('Virtualized :', c)
EP_Marker("vm_risc_end")

# Classic python code
print("Give me the sum :", sum_it(1, 2))
input("End, press key")
```
Convert and build with `msvc`
```bash
python setup.py build_ext --inplace
```


```{image} ../_static/_medias/it/python/protect/shareware3.png
:width: 700px
:align: center
:class: vspace
```


The protected module and his functions are callable like any other module in python. So in our program we will load this `extension.pyd` like any other package/module.

**Exemple** : importing `test_it` will run the module init code.
```python
import test_it
```


```{image} ../_static/_medias/it/python/protect/shareware4.png
:width: 400px
:align: center
:class: vspace
```


#### 🗜️Choose function to Virtualize
- Need `extra_link_args=['/MAP']` in `setup.py`
- Virtual Machine → Functions Selecting → Add Functions


```{image} ../_static/_medias/it/python/protect/Pastedimage20230504141234.png
:width: 700px
:align: center
:class: vspace
```


In order for a function to be visible in **Enigma Protector**, it’s important to mark the function `public`
```python
cpdef public int ma_fonction_A(int number1, int number2):
    print("Welcome in function A")
    cdef int number3
    number3 = int(input("Give me a number :"))
    return number1 + number2 + number3
```
### 🔏 Registration feature
#### 🖲️Get Hardware ID
```python
# distutils: language = c++
# cython: language_level=3

import cython
from cpython.ref cimport PyObject
from libc.stddef cimport wchar_t

cdef extern from "Python.h":
    PyObject * PyUnicode_FromWideChar(wchar_t *w, Py_ssize_t size)
    wchar_t * PyUnicode_AsWideCharString(object, Py_ssize_t *)

cdef extern from "enigma_ide.h":
    char * EP_RegHardwareID()
    wchar_t * EP_RegHardwareIDW()

# ANSI
ansi_str_hid = str(EP_RegHardwareID(), 'cp1252')
print('EP_RegHardwareID :', ansi_str_hid)

# WIDE
cdef PyObject * pystr
pystr = PyUnicode_FromWideChar(EP_RegHardwareIDW(), -1)
wide_str_hid = str(<object> pystr)
print('EP_RegHardwareWide :', wide_str_hid)
```
#### 🔓Register software

First you need to generate a key, please note that in this article I will use WideChar (Unicode in configuration). It's more complex than ANSI, if you understand with Unicode, it will be straightforward for ANSI.

```{image} ../_static/_medias/it/python/protect/shareware6.png
:width: 700px
:align: center
:class: vspace
```

```python
# distutils: language = c++
# cython: language_level=3

import cython
from cpython.ref cimport PyObject
from libc.stddef cimport wchar_t
from libcpp cimport bool

cdef extern from "Python.h":
    PyObject * PyUnicode_FromWideChar(wchar_t *w, Py_ssize_t size)
    wchar_t * PyUnicode_AsWideCharString(object, Py_ssize_t *)
    
cdef extern from "enigma_ide.h":
    bool EP_RegCheckAndSaveKeyW(wchar_t * Name, wchar_t * Key)

reg_name = input("Name :")
reg_key = input("Key :")

cdef wchar_t *reg_name_wchar
cdef wchar_t *reg_key_wchar
cdef Py_ssize_t length

reg_name = u"Test-WrongUSER"
reg_key = u"CKML369-XGSH5DW-RVG2ANU-W4FG4K4-J2RQYHM-32SD3LD-XJPKSYB-S5RPPPE-SEURZXQ"

reg_name_wchar = PyUnicode_AsWideCharString(reg_name, &length)
reg_key_wchar = PyUnicode_AsWideCharString(reg_key, &length)

print("Registration to : ", reg_name)
if EP_RegCheckAndSaveKeyW(reg_name_wchar, reg_key_wchar):
	print("Registration OK, please restart APP")
	quit()
else:
	print("Registration ERROR")
```

##### 🪟Registration dialog
If you want to use the registration dialog just use the dedicated API
```python
cdef extern from "enigma_ide.h":
    void EP_RegShowDialog()

if not registered:
    EP_RegShowDialog()
```
#### 🪄 Registration status
```cpp
# distutils: language = c++
# cython: language_level=3

import cython
from cpython.ref cimport PyObject
from libc.stddef cimport wchar_t

cdef extern from "enigma_ide.h":
    int EP_RegKeyStatus()
    
if EP_RegKeyStatus() == 1:
	print("You are registered")
else:
	print("You are NOT registered")
```
#### 🔐Locking function from registration
```python
# distutils: language = c++
# cython: language_level=3

import cython

cdef extern from "enigma_ide.h":
    void EP_Marker(char * Name)

cdef public int ma_fonction_B(int number1, int number2):
    cdef int number3
    
	# If the user is registered and the key allow block 6
    EP_Marker("reg_crypt_begin6")
    print("Welcome to the registered and crypted part 6")
    number3 = int(input("Give me a number :"))
    EP_Marker("reg_crypt_end6")
    
    # If the user is not registered or doesn't allow block 6
    EP_Marker("unreg_crypt_begin6")
    print("Welcome to the unregistered part 6")
    number3 = 8
    EP_Marker("unreg_crypt_end6")
    return number1 - number2 - number3
```
#### ❌ Delete registration
```python
# distutils: language = c++
# cython: language_level=3

import cython
from libcpp cimport bool

cdef extern from "enigma_ide.h":
    bool EP_RegDeleteKey()
    
if EP_RegDeleteKey() == 1:
	print("Deletion of registration OK")
```
### 🗃️ File virtualization
It's possible to hide some files inside the executable. You will access to these files directly from your script.

```{image} ../_static/_medias/it/python/protect/shareware5.png
:width: 700px
:align: center
:class: vspace
```

**Add** a file `virtual_file.txt` with some text

You could read the file with python easily :
```python
with open('virtual_file.txt') as f:
    lines = f.readlines()

print("------- virtual_file.txt -------")
print(lines)
print("--------------------------------")
```
### 🧵 Protected strings
You can add some sensible protected strings in your code. We will see in this section how to retrieve them :

```{image} ../_static/_medias/it/python/protect/shareware7.png
:width: 700px
:align: center
:class: vspace
```

**Add** some strings in Enigma Protector
#### 🧶 Ansistring
##### ID
```python
import cython
from libc.stdlib cimport malloc, free
from cpython.bytes cimport PyBytes_FromStringAndSize

cdef extern from "enigma_ide.h":
    int EP_ProtectedStringByID(int ID, char * Buffer, int Len)
    
cdef char * buf_string_2  
buf_size_2 = EP_ProtectedStringByID(2, b'', 0)  
print("Size of the string #2: ", buf_size_2)  
buf_string_2 = <char *> malloc((buf_size_2) * sizeof(char))  
if EP_ProtectedStringByID(2, buf_string_2, buf_size_2) != 0:  

    py_bytes = PyBytes_FromStringAndSize(<char *> buf_string_2, buf_size_2)  
    ansi_string = py_bytes.decode('windows-1252')  
    print('AnsiString :', ansi_string)  
else:  
    print("Error can't extract #2")  
  
free(buf_string_2)
```
##### Key
```python
import cython
from libc.stdlib cimport malloc, free

cdef extern from "enigma_ide.h":
    int EP_ProtectedStringByKey(char * Key, char * Left, int Len)
    
cdef char * buf_string_2

buf_size = EP_ProtectedStringByKey("tckQpD9z", b'', 0)
print("Size of the string #1: ", buf_size)
buf_string_2 = <char *> malloc((buf_size + 1) * sizeof(char))
if EP_ProtectedStringByKey("tckQpD9z", buf_string_2, buf_size) != 0:
	buf_string_2[buf_size] = b'\0'
	print(str(buf_string_2, 'cp1252'))
else:
	print("Error can't extract #1")
free(buf_string_2)
```
#### 🪢 Widestring
```python
import cython

from cpython.ref cimport PyObject
from libc.stddef cimport wchar_t
from libc.stdlib cimport malloc, free
from cpython.bytes cimport PyBytes_FromStringAndSize

cdef extern from "enigma_ide.h":
    int EP_ProtectedStringByID(int ID, char * Buffer, int Len)

buf_size = EP_ProtectedStringByID(1, b'', 0)  
print("Size of the string #1: ", buf_size)  
  
cdef wchar_t * buf_string  
if buf_size > 0:  
    buf_string = <wchar_t *> malloc(buf_size)  
    if not buf_string:  
        raise MemoryError("Failed to allocate memory")  
    EP_ProtectedStringByID(1, <char *> buf_string, buf_size)  
  
    py_bytes = PyBytes_FromStringAndSize(<char *>buf_string, buf_size)  
    wide_string = py_bytes.decode('utf-16')  
    print('WideString :', wide_string)  
free(buf_string)
```
#### 💾 Binary
```python
import cython

from cpython.ref cimport PyObject
from libc.stdlib cimport malloc, free

cdef extern from "enigma_ide.h":
    int EP_ProtectedStringByKey(char * Key, char * Left, int Len)

cdef char * buf_string_2

buf_size = EP_ProtectedStringByID(3, b'', 0)
print("Size of the string #3: ", buf_size)

buf_string_2 = <char *> malloc((buf_size + 1) * sizeof(char))

if EP_ProtectedStringByID(3, buf_string_2, buf_size) != 0:
	print(str(buf_string_2))
else:
	print("Error can't extract #3")
free(buf_string_2)
```
### ✒️Signing `extension.pyd`
**Advantage for signing code :**
- Validates code integrity
- Issuing company reputation and authenticity
- Safe and secure user experience
- Seamless integration with multiple platforms

- On my side, I have a certificate issue from [Sectigo](https://sectigo.com/ssl-certificates-tls/code-signing)
```bash
signtool sign /fd SHA256 /n "Rémi MEVAERE" /t http://timestamp.digicert.com .\cython_protect.cp311-win_amd64.pyd
```

```{image} ../_static/_medias/it/python/protect/Pastedimage20230505143923.png
:width: 400px
:align: center
:class: vspace
```

# 🛡Building protected my_script.py
## ♾️Informations
- Current features of ==PyArmor 8+==
  
|                 OS |  Windows   | Apple  | Linux |       |            |         |       |       |
| ------------------:|:----------:|:------:|:-----:|:-----:|:----------:|:-------:| ----- |:-----:|
|               Arch | x86/x86_64 | x86_64 | arm64 | arm64 | x86/x86_64 | aarch64 | armv7 | armv6 |
| Themida Protection |     Y      |   No   |  No   |  No   |     No     |   No    | No    |  No   |
|           RFT Mode |     Y      |   Y    |   Y   |   Y   |     Y      |    Y    | Y     |  No   |
|           BCC Mode |     Y      |   Y    |   Y   |   Y   |     Y      |    Y    | Futur |  No   |
|             Others |     Y      |   Y    |   Y   |   Y   |     Y      |    Y    | Y     |  No   |
|          pyarmor-7 |     Y      |   Y    |   Y   |   Y   |     Y      |    Y    | Y     |   Y   |

- PyArmor only work with the interpreter (version) used by your script. So be sure that the final user are using the same interpreter. One way is to packed python with `PyInstaller`.
## 📄 Our script
The program we want to protect is composed of two scripts. If we want to use and load our `extension.pyd` just load like any other module.

File : `main.py`
```python
from fibonacci import fibonacci

print("Welcome to the test program")
nbr = input("Please enter an integer : ")
if None != (fib_list := fibonacci(nbr)):
    print("Sequence of Fibonacci : ")
    print(fib_list)
input("Press key to stop")
```

File : `fibonacci.py`
```python
def fibonacci(n):
    try:
        nbr = int(n)
        if nbr <= 0:
            raise ValueError

        FibArray = [0, 1]

        for i in range(nbr - 2):
            FibArray.append(FibArray[-1] + FibArray[-2])

        return FibArray

    except:
        print("Incorrect input")
        return None
```
## 📜 Obfuscating one script
First we want to protect the script `fibonacci.py` to see what’s happening.
```bash
pyarmor gen fibonacci.py
```

```{image} ../_static/_medias/it/python/protect/Pastedimage20230504150348.png
:width: 700px
:align: center
:class: vspace
```

The obfuscated `fibonacci.py` is :
```python
from pyarmor_runtime_005107 import __pyarmor__  
__pyarmor__(__name__, __file__, b'PY005107\x00\x03\x0b\x00\xa7\r\r\n\x80\x00\x01\x00\x08\x00\x00\x00\x04\x00\x
... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... 
"\xcf\x8d)mO\xfa\xe7\x04\xc8\xfeZ\xf6K\xf6,F\x14k\xbd\x07\x1e\xf5\x12\xf97=!\xb0`'")
```
And `pyarmor_runtime.pyd` is integrated in the `dist` folder. Let’s see what contains `pyarmor_runtime.pyd`, it's an executable from PyArmor. Not open-source.

```{image} ../_static/_medias/it/python/protect/Pastedimage20230504150725.png
:width: 700px
:align: center
:class: vspace
```

The program `main.py` works as expected :
```python
(pyarmor-cython-py3.11) D:\JetBrainsProjects\PyCharm\PyArmor_Cython\dist>python main.py
Welcome to the test program
Please enter an integer : 55
Sequence of Fibonacci :
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832
040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272]
Press key to stop
```
The key needed to read/decrypt/deobfuscate `fibonacci.py` is directly included in the PyArmor_Runtimes package.
### 📜 Obfuscating multiple script
```bash
pyarmor gen main.py fibonacci.py
```
The program `main.py` will works as expected.
### 🥽 Protecting features
Activate the mode you desire.
```bash
--obf-module <0,1> # enable all module 1
--obf-code <0,1,2> # Obfuscation mode (best is 2)
--enable <jit,rft,bcc,themida>
--enable-jit # Use JIT to process some sensitive data to improve security
--enable-rft # renaming function/class in the scripts
--enable-bcc # converting Python functions to C functions
--enable-themida # Use Themida to protect runtime package
--mix-str # Mix the string constant in scripts
--assert-call # Assert function is obfuscated
--assert-import # Assert module is obfuscated
--period N # Check Runtime Key periodically.
```
## 🗝️Excluding Key and binding to user
In most cases, it’s better to not include the `key` into runtimes, but provide it and personnalized it for each user. **PyArmor** gives us some nice options.

### ‼️ Excluding Key
#### Change the name of the licence file
```bash
pyarmor cfg outer_keyname="my_licence.key"
```
#### Don’t include the key
```bash
pyarmor gen main.py fibonacci.py --outer
```
And expected behavior :
```python
> (venv) D:\JetBrainsProjects\PyCharm\PyArmorV2\dist>python main.py
> 	Traceback (most recent call last):
> 	 File "D:\JetBrainsProjects\PyCharm\PyArmorV2\dist\main.py", line 2, in <module>
> 	   from pyarmor_runtime_005107 import __pyarmor__
> 	 File "D:\JetBrainsProjects\PyCharm\PyArmorV2\dist\pyarmor_runtime_005107\__init__.py", line 2, in <module>
> 	   from .pyarmor_runtime import __pyarmor__
> 	RuntimeError: missing license key to run the script (1:10251)
```
### 🔑 Generate Key
#### Syntax
```python
pyarmor gen key <options>
# Options
# -O PATH, --output PATH
# -e DATE, --expired DATE
# --period N
# -b DEV, --bind-device DEV
# --bind-data, store data
```

Bind device
```bash
$ pyarmor gen key -b 128.16.4.10 # IP
$ pyarmor gen key -b 52:38:6a:f2:c2:ff # MAC ADDRESS
$ pyarmor gen key -b HXS2000CN2A # SERIAL NUMBER OF DISK
$ pyarmor gen key -e 30 # 30 Days / Check NTP SERVER
$ pyarmor gen key -e .2022-12-31 # Date / Don't Check NTP SERVER (see .)
$ pyarmor gen key --period 1 # check every 1hour
$ pyarmor gen key --period 3600s # check every 1hour
$ pyarmor gen key --period 60m # check every 1hour
$ pyarmor gen key --period 1h # check every 1hour
$ pyarmor gen key --bind-data "Licensed to Rémi"
```

Generating a key
```python
pyarmor gen key -e 30 --bind-data "Licensed to Rémi"
```
#### 🔎 Get data from the key
##### get hdinfo
```python
__pyarmor__(0, None, b'hdinfo', 1) # serial n°first harddisk
__pyarmor__(1, None, b'hdinfo', 1) # mac address first card
__pyarmor__(2, None, b'hdinfo', 1) # ipv4 first card
__pyarmor__(0, "/dev/vda2", b'hdinfo', 1)
__pyarmor__(1, "eth2", b'hdinfo', 1)
__pyarmor__(0, "/0", b'hdinfo', 1) # First disk
__pyarmor__(0, "/1", b'hdinfo', 1) # Second disk
__pyarmor__(1, "*", b'hdinfo', 1) # get all network
```
##### get keyinfo
```python
print('bind data is', __pyarmor__(0, None, b'keyinfo', 1))
print('expired epoch is' __pyarmor__(1, None, b'keyinfo', 1))
```
##### Example
```python
print('this is __pyarmor__', __pyarmor__) # crash if no runtimes
print(__pyarmor__(0, None, b'hdinfo', 1))  
print('bind data is', __pyarmor__(0, None, b'keyinfo', 1))  
print('expired epoch is', __pyarmor__(1, None, b'keyinfo', 1))  
print("Welcome to the test program")
```
give
```python
>(venv) D:\JetBrainsProjects\PyCharm\PyArmorV2\dist>python main.py
>	this is __pyarmor__ <built-in function __pyarmor__>
>	WD-WCC7K7LPJLSE
>	bind data is b'Licensed to R\xc3\xa9mi'
>	expired epoch is 1685944028

```
##### Test if protected `__assert_armored__`
Parameters:
- **arg** (_object_) – arg is a module or callable object
Returns:
- return `arg` self if `arg` is obfuscated, otherwise, raise protection error.
```python
m = __import__('abc')
__assert_armored__(m)

def hello(msg):
    print(msg)

__assert_armored__(hello)
hello('abc')
```
# 📦Packaging with PyInstaller
PyArmor need absolutely to use the same version used when protecting the script. The easiest way to distribute the app will be to packed the interpreter, the app, the extension. Please see below how to proceed :
## 🩹 Generating and patching spec file
+ First we need to specify a different folder for our obfuscated files (cause `dist` will be used by pyinstaller)
```bash
pyarmor gen -O obfdist main.py fibonacci.py --outer
```
- Next we need to move the runtime package to the current path to ask pyinstaller to include it
```bash
mv obfdist/pyarmor_runtime_000000 ./
```
- Generate the spec file for **PyInstaller**
```bash
pyi-makespec --hidden-import pyarmor_runtime_000000 main.py fibonacci.py
```
- Patching `foo.spec` by inserting extra code after `a = Analysis`
```python
a = Analysis(
    ...
)

# Patched by PyArmor
_src = r'/path/to/src'
_obf = r'/path/to/src/obfdist'

_count = 0
for i in range(len(a.scripts)):
    if a.scripts[i][1].startswith(_src):
        x = a.scripts[i][1].replace(_src, _obf)
        if os.path.exists(x):
            a.scripts[i] = a.scripts[i][0], x, a.scripts[i][2]
            _count += 1
if _count == 0:
    raise RuntimeError('No obfuscated script found')

for i in range(len(a.pure)):
    if a.pure[i][1].startswith(_src):
        x = a.pure[i][1].replace(_src, _obf)
        if os.path.exists(x):
            if hasattr(a.pure, '_code_cache'):
                with open(x) as f:
                    a.pure._code_cache[a.pure[i][0]] = compile(f.read(), a.pure[i][1], 'exec')
            a.pure[i] = a.pure[i][0], x, a.pure[i][2]
# Patch end.
```
- Generate the final bundle
```bash
pyinstaller main.spec
```
## 🗺️ Add icon
In the spec file
```bash
exe = EXE(  
...
icon='my_icon.ico'  
)
```
## ℹ️ Adding version info
In the spec file
```bash
exe = EXE(  
...
version='VersionInfo.rc',  
icon='my_icon.ico'  
)
```
With `VersionInfo.rc`:
```bash
VSVersionInfo(  
ffi=FixedFileInfo(  
filevers=(1, 2, 3, 4),  
OS=0x40004,  
fileType=0x1,  
),  
kids=[  
StringFileInfo(  
[  
StringTable(  
u'040904B0',  
[StringStruct(u'CompanyName', u'Company Name'),  
StringStruct(u'FileDescription', u'Description'),  
StringStruct(u'InternalName', u'Internal Name !!'),  
StringStruct(u'LegalCopyright', u'Copyright (c) yep'),  
StringStruct(u'OriginalFilename', u'main.exe'),  
StringStruct(u'ProductName', u'ProductName'),  
StringStruct(u'ProductVersion', u'1.2.3 (2312321)')])  
]),  
VarFileInfo([VarStruct(u'Translation', [0x0409 , 0x04B0 ])])  
]  
)
```
- Generate the final bundle
```bash
pyinstaller main.spec
```
```{image} ../_static/_medias/it/python/protect/Pastedimage20230506080946.png
:width: 400px
:align: center
:class: vspace
```

```{image} ../_static/_medias/it/python/protect/Pastedimage20230506081000.png
:width: 400px
:align: center
:class: vspace
```

## ✒️ Signing the Package
```bash
signtool sign /fd SHA256 /n "Rémi MEVAERE" /t http://timestamp.digicert.com .\main.exe
```

```{image} ../_static/_medias/it/python/protect/Pastedimage20230506081105.png
:width: 700px
:align: center
:class: vspace
```

- Move the licence file `my_licence.key`
# 🌐Conclusion
- We’ve seen how to protect our python program or some sensitive parts that we don't want to share ;
- Each time, we have to trust an external program (not open-source) ;
- Even if it seems strong, with time, method and courage it is possible to **crack** your program, if the CPU can run the code, the cracker can see it !
- Better solution would be to provide the software as a service (I hate that), more updates and a good service ;
- It’s not suitable for programs that need maximum resources cause using virtual machine /obfuscation / protection add extra steps to CPU and more memory ;
- This article is a good example of how interface **C++ Libraries** with Python. 

```{hint}
- Rémi MEVAERE for sciences-physiques.net the 3 July 2024
- PyArmor 8.5.10, Enigma Protector X64 7.60, Python 3.12, PyInstaller 6.8
```
