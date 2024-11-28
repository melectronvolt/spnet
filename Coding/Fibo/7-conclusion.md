# Conclusion 🏁

The conclusions are based on the following results. Clearly, it's a personal opinion shaped by my education and experiences. I quickly started coding at 10 with BASIC (on DOS), then moved on to learn Visual Basic 6, and after that, I developed a long-lasting affection for Delphi from Borland and Embarcadero. Subsequently, I pursued studies in physics and chemistry at university. Following that, I learned Python, C++, and most recently, ASM, purely for enjoyment.

## C# and Dotnet framework 📦
### 👍 Advantages
- Cross-platform: code can easily be ported to Linux with no changes required
- Great optimization: comparable in speed to `C++`
- Not verbose: language syntax is clear and straightforward
- Simplified parallel computing
- Abundant scientific functions included in .NET Core, eliminating the need to reinvent the wheel
- Built-in garbage collector
- Nice debugger, profiler…
### 👎 Disadvantages
- Requires installation of the .NET Core runtime
- Limited memory control
- Controlled by Microsoft; the product roadmap is unpredictable and subject to frequent changes. In my opinion, it's more suitable for developers rather than scientists.
- Steep learning curve
- Size of the runtime + “binaries”
- Limited support for GPU computing (perhaps through libraries like ILGPU?)
- Not ideal for prototyping due to strong typing
### ✅ Suitable Use Cases
- When integrating with the entire .NET ecosystem without needing to switch to other platforms
- For developers aiming to quickly build cross-platform desktop applications
### ❌ Less Suitable Use Cases
- In the field of scientific computing
- For machine learning applications
## JavaScript 🌐
### 👍 Advantages
- Good performance compared to Python
- Compatible with all web browsers
- Numerous visualization libraries and frameworks
- Enables full-stack development with Node.js
- Easy to learn and use
- Suitable for rapid prototyping due to its dynamic typing
- Debugging is okay
### 👎 Disadvantages
- While generally faster than interpreted languages like Python, JavaScript's performance lags behind that of compiled languages.
- Limited precision in floating-point numbers due to IEEE 754 double precision, which can cause problems in scientific computations.
- Challenges with memory management
- Size of the runtime + script
- Scarcity of scientific libraries when compared to other languages
- Managing asynchrony can be complex for beginners, and it may not be intuitive for scientists.
- Overwhelming number of frameworks that are constantly being released 
### ✅ Ideal Use Cases
- Excellent for creating web interfaces (front only)
### ❌ Less Ideal Use Cases
- Not the best choice for desktop applications, memory hungry
- Not recommended for applications where performance is a critical concern
- The scientific field, due to the lack of specialized libraries and precision issues
- Machine learning applications, which often require more specialized tools and libraries
## ASM 🧮
### 👍 Advantages
- Encourages knowledge of computer architecture, which is beneficial for learning
- Results in a small program footprint
- Presents a healthy challenge to developers
- No abstraction layers: interaction with hardware is direct and explicit
- Opportunities for hardware-specific optimization
- Seamless interaction with C and C++ (a significant plus)
### 👎 Disadvantages
- Inherently high complexity
- Optimization is hard (my c++ program is faster)
- Debugging can be difficult and tedious
- Not inherently portable; requires adaptation for different platforms (different hardware, operating systems)
- Lengthy development time
- Lack of scientific libraries available
- Highly prone to errors due to the low-level nature of the language (totally unsafe)
- Often involves reinventing the wheel for many common functionalities
### ✅ Ideal Use Cases
- Suitable for embedded device development
- When high-performance is critical for specific sections of code that need to be directly integrated with C/C++ binaries
### ❌ Less Ideal Use Cases
- Not practical for developing a modern application
- Prototyping in assembly language (ASM) is highly impractical
- Ill-suited for applications requiring user interaction
## C++ 🧩
### 👍 Advantages
- Great performance
- Good portability
- Mature ecosystem with a lot of scientific library
- You handle memory
- Template Metaprogramming and Multi-Paradigm Language
- Could use CUDA to GPU calculation
- Small size
### 👎 Disadvantages
- A bit complex if you want to create complex code
- Not very intuitive, but simpler than JavaScript for me
- A bit verbose
- More Error Prone with Memory Management by user
- A bit unsafe
### ✅ Ideal Use Cases
- High performance app (executable and libraries)
- Small size of the executable
- Small portions of code to speed up section in Python
- Embedded device development
- Big desktop app
### ❌ Less Ideal Use Cases (for me)
- Prototyping
- WebApp
## Python 🐍
### 👍 Advantages
- Extremely user-friendly
- Rapid prototyping capabilities
- Effortless direct conversion to native code with `Cython`
- A wealth of high-quality libraries (e.g., NumPy, Pandas, PyTorch)
- Straightforward integration with C and C++, offering extensive compatibility
- Strong community support
- Cross-platform compatibility
- Simplified data visualization
- Ease of performing GPU calculations
- Performance boost with PyPy without extra work

### 👎 Disadvantages
- Generally slower performance, with computationally intensive tasks often handled by packages written in C/C++
- The Global Interpreter Lock (GIL) can be a bottleneck; however, it can be circumvented using `Cython` or interfacing with C/C++
- Really slow (for loop) without native packages
- Higher memory consumption compared to some other languages
- Indentation-based syntax may be unfamiliar to those new to Python
- Not tailored for mobile computing
- Larger footprint due to the combined size of Python, scripts, and virtual environments
- Managing dependencies can be complicated when distributing applications

### ✅ Ideal Use Cases
- Quick and efficient prototyping
- Research in the scientific field, especially when utilizing extensions in C/C++ and Cython
- Machine Learning projects, particularly with frameworks that have CUDA integration like PyTorch
- Backend development for web applications
- Creating small graphical user interface (GUI) applications

### ❌ Less Ideal Use Cases
- Building standalone heavyweight desktop applications