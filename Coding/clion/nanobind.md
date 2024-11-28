# Nanobind 🔗

```{image} ../../_static/_medias/coding/clion/nanobind.png
:width: 300px
:align: center
:class: vspace
```

## Description
- **Origine** 🌱
    **nanobind** est une bibliothèque de liaison compacte conçue pour exposer des types C++ à Python et vice-versa. Elle évoque des outils tels que Boost.Python et pybind11 grâce à une syntaxe presque identique.
- **Efficacité Supérieure** 🚀
     L'un des principaux avantages de nanobind est son efficacité par rapport à d'autres outils. Les liaisons se compilent plus rapidement, produisent des binaires plus petits et offrent de meilleures performances en temps d'exécution.
- **Performance Comparée** 📊
    Des benchmarks montrent que nanobind offre un temps de compilation jusqu'à ~4× plus rapide, des binaires jusqu'à ~5× plus petits, et des surcoûts en temps d'exécution jusqu'à ~10× plus bas par rapport à pybind11. De plus, nanobind surpasse Cython sur d'importants critères, avec une réduction de la taille des binaires de 3-12×, une réduction du temps de compilation de 1.6-4×, et une performance en temps d'exécution similaire.
- **Simplicité et Familiarité** 🎯
    Bien que nanobind soit distinct dans ses performances, il utilise une syntaxe presque identique à celle de bibliothèques populaires comme pybind11, rendant la transition ou l'apprentissage plus simple pour les développeurs familiers avec ces outils.
- **Interopérabilité** 🔄
	À l'instar d'autres bibliothèques de liaison, nanobind permet une conversion transparente entre de nombreux types C++ et Python, facilitant ainsi l'intégration de codes et bibliothèques entre les deux langages.
- **Modernité** 🌟
    Compte tenu de ses performances et de sa comparaison avec des outils modernes, que nanobind soit également basé sur des caractéristiques modernes du C++.
- **Open Source** 📜
	Comme de nombreux outils puissants, nanobind est un logiciel open source (BSD). Cela signifie qu'il est non seulement libre d'utilisation, mais aussi que sa communauté est active et contribue constamment à son amélioration.
- **Utilisation courante** 🛠️
	Bien que nanobind puisse être relativement nouveau ou moins connu que d'autres outils, ses performances supérieures le rendent attrayant pour le développement d'extensions Python en C++, notamment lorsque la vitesse de compilation, la taille des binaires ou la performance en temps d'exécution sont des critères essentiels.

En somme, nanobind offre une solution efficace et performante pour créer des liaisons entre Python et C++. Avec ses avantages en matière de compilation, de taille binaire et de temps d'exécution, c'est un choix solide pour les développeurs cherchant une alternative haute performance à d'autres bibliothèques de liaison. 🌉🚀🖥️🐍

## Installation simple
```bash
# Si vous n'avez pas initialisé git pour votre projet
git init
# Téléchargement du module
git submodule add https://github.com/wjakob/nanobind ext/nanobind
git submodule update --init --recursive
```
## CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.26)  
project(my_ext)  
  
set(CMAKE_CXX_STANDARD 23)  
  
find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)  
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)  
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")  
endif()  
  
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ext/nanobind)  
nanobind_add_module(my_ext main.cpp)
```
## Main.cpp
```cpp
#include <nanobind/nanobind.h>  

int add(int a, int b) { return a + b; }  
  
NB_MODULE(my_ext, m) {  
    m.def("add", &add);  
}
```
## Utilisation en Python
```python
Python 3.11.1 (main, Dec 23 2022, 09:28:24) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

import my_ext

my_ext.add(1, 2)
3
```