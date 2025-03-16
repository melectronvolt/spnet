# Catch2 🫳🏼

```{image} ../../_static/_medias/coding/clion/catch2logo.png
:width: 300px
:align: center
:class: vspace
```
## Description
- **Origine** 🌱
    Catch2 est la suite de Catch (l'acronyme pour "C++ Automated Test Cases in Headers"). Il a été conçu pour offrir une simplicité d'utilisation tout en évitant les complications des étapes de compilation principales.
- **De "Header-only" à une bibliothèque traditionnelle** 🔄
    Bien que les versions précédentes de Catch étaient "header-only", la version 3 apporte des changements significatifs. Le plus notable est que Catch2 n'est plus une bibliothèque en un seul en-tête. À partir de la v3, Catch2 se comporte comme une bibliothèque traditionnelle, avec plusieurs en-têtes et une implémentation compilée séparément.
- **Simplicité** 🎯
    Malgré ce changement majeur, la philosophie principale de Catch2 reste la même : offrir un moyen simple et naturel d'écrire des tests sans sacrifier la fonctionnalité.
- **Sections et BDD** 🧪
    Catch2 introduit le concept de "sections", permettant de diviser un test en plusieurs étapes ou scénarios. Il supporte également une syntaxe inspirée de BDD (Behavior-Driven Development) avec des mots-clés tels que `Given`, `When`, et `Then`, améliorant la lisibilité des tests.
- **Reporting riche** 📊
    Catch2 fournit des rapports détaillés et configurables, et supporte plusieurs formats de sortie pour s'intégrer facilement à d'autres outils ou systèmes CI/CD.
- **Compatibilité** 🔄
    Bien qu'il ait évolué, Catch2 reste compatible avec les dernières normes C++ et fonctionne avec de nombreux compilateurs, le rendant idéal pour les projets modernes.
- **Extensions** 🔌
    Le framework peut être étendu grâce à divers reporters, listeners et même avec des frameworks de mocking pour s'adapter aux besoins spécifiques du projet.
- **Communauté** 🧑‍🤝‍🧑
    La popularité et l'évolution de Catch2 ont conduit à une communauté active, contribuant régulièrement à son développement et fournissant un soutien aux utilisateurs.

En synthèse, Catch2, avec ses mises à jour dans la v3, demeure un framework de test robuste pour C++, combinant simplicité et flexibilité. Il s'adapte aux besoins changeants des développeurs, tout en fournissant un outil de test efficace et fiable. 🛠️🧠🔬

## Windows : Installation 
### Mon script
- Des répertoires différents pour les versions debug/release
- La possibilité du choix d’utiliser ensuite les DLL ou les versions statiques
```powershell
# Définir les chemins et les variables pour le téléchargement et l'installation de la bibliothèque
$BASE_PATH = "D:\Coding\Frameworks"
$NAME_LIBRARY = "Catch2"
$LIBRARY_VERSION = "3.8.0"
$DOWNLOAD_URL = "https://github.com/catchorg/Catch2/archive/refs/tags/v${LIBRARY_VERSION}.zip"

# compiler le chemin de base pour la bibliothèque
$BASE_LIBRARY_PATH = Join-Path -Path $BASE_PATH -ChildPath "$NAME_LIBRARY"

# compiler le chemin vers la version spécifique de la bibliothèque
$VERSION_LIBRARY_PATH = Join-Path -Path $BASE_LIBRARY_PATH -ChildPath "$LIBRARY_VERSION"

# Définir le nom du répertoire extrait et le nom de l'archive
$EXTRACTED_DIR_NAME = "Catch2-${LIBRARY_VERSION}"
$ARCHIVE_NAME = "v${LIBRARY_VERSION}.zip"
$INSTALLATION_DIR = "${BASE_PATH}\${NAME_LIBRARY}\${LIBRARY_VERSION}"

# compiler le chemin complet vers l'archive ZIP
$ZIP_PATH = Join-Path -Path $BASE_LIBRARY_PATH -ChildPath $ARCHIVE_NAME

New-Item -ItemType Directory -Path $BASE_LIBRARY_PATH -Force
Set-Location -Path $BASE_LIBRARY_PATH

# Télécharger l'archive ZIP depuis l'URL spécifiée
Invoke-WebRequest -Uri $DOWNLOAD_URL -OutFile $ZIP_PATH

# Ajouter la capacité de décompresser des fichiers ZIP
Add-Type -AssemblyName System.IO.Compression.FileSystem
# Extraire l'archive ZIP au chemin de la bibliothèque
[System.IO.Compression.ZipFile]::ExtractToDirectory($ZIP_PATH, $BASE_LIBRARY_PATH)

# Renommer le répertoire extrait pour qu'il corresponde à la version de la bibliothèque
$OLD_DIR = Join-Path -Path $BASE_LIBRARY_PATH -ChildPath $EXTRACTED_DIR_NAME
Rename-Item -Path $OLD_DIR -NewName ($LIBRARY_VERSION)

# Supprimer l'archive ZIP une fois qu'elle n'est plus nécessaire
Remove-Item -Path $ZIP_PATH

Set-Location -Path $VERSION_LIBRARY_PATH

# Fonction pour compiler et installer la bibliothèque
function BuildAndInstallLibrary($build_directory, $config, $sharedLibs) {
    $directory = Join-Path -Path $VERSION_LIBRARY_PATH -ChildPath $build_directory
    # Créer un répertoire pour la construction
    New-Item -ItemType Directory -Path $directory -Force
    Set-Location -Path $directory

    $cmakeArgs = @(
        "..",
        "-DBUILD_TESTING=OFF",
        "-DCMAKE_INSTALL_PREFIX=${VERSION_LIBRARY_PATH}",
        "-DCMAKE_BUILD_TYPE=$config",
        "-DBUILD_SHARED_LIBS=$sharedLibs"
    )
    
    # Run cmake with the arguments
    & cmake $cmakeArgs
    & cmake --build . --config $config
    & cmake --install . --config $config
}

# Utilisation de la fonction pour compiler et installer la bibliothèque dans différentes configurations
BuildAndInstallLibrary "build_debug" "Debug" "OFF"
BuildAndInstallLibrary "build_release" "Release" "OFF"
BuildAndInstallLibrary "build_debug_dll" "Debug" "ON"
BuildAndInstallLibrary "build_release_dll" "Release" "ON"
```
### CMakeLists.txt
```cmake
# Spécifie la version minimale requise de CMake pour exécuter ce script.
cmake_minimum_required(VERSION 3.26)

# Nomme le projet "Catch2_testing".
project(Catch2_testing)

# Fixe la version du standard C++ utilisée à C++23.
set(CMAKE_CXX_STANDARD 23)

# Définit le chemin de base pour Catch2.
set(CATCH2_BASE_PATH "D:/Coding/Frameworks/Catch2/3.8.0")

# Indique si Catch2 est utilisé en tant que DLL (bibliothèque dynamique) ou non.
SET(USE_DYNAMIC_CATCH2 ON)

# Affiche le type de build (Debug, Release, etc.).
MESSAGE("Type: ${CMAKE_BUILD_TYPE}")

# Si Catch2 est utilisé comme une DLL.
if (USE_DYNAMIC_CATCH2)
    MESSAGE("Link: Dynamic (DLL)")
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")
        set(CATCH2_DLL_PATH "${CATCH2_BASE_PATH}/build_debug_dll/src/Debug")
    else ()
        set(CATCH2_DLL_PATH "${CATCH2_BASE_PATH}/build_release_dll/src/Release")
    endif ()

    # Définit le répertoire de destination pour les DLLs.
    set(DLL_DEST_DIR ${CMAKE_BINARY_DIR})
    MESSAGE("Copy the DLLs to the executable directory : ${DLL_DEST_DIR}")

    # Récupère tous les fichiers DLL du chemin spécifié.
    file(GLOB CATCH2_DLLS "${CATCH2_DLL_PATH}/*.dll")
    # Boucle pour copier chaque DLL dans le répertoire d'exécution.
    foreach (DLL ${CATCH2_DLLS})
        get_filename_component(DLL_NAME ${DLL} NAME)
        MESSAGE("DLL : ${DLL_NAME}")
        configure_file("${CATCH2_DLL_PATH}/${DLL_NAME}" "${DLL_DEST_DIR}/${DLL_NAME}" COPYONLY)
    endforeach ()
else ()
    MESSAGE("Link: Static")
endif ()

# Ajoute le chemin de base de Catch2 à CMAKE_PREFIX_PATH pour faciliter la recherche de paquets.
list(APPEND CMAKE_PREFIX_PATH ${CATCH2_BASE_PATH})

# Ajoute le répertoire d'en-tête de Catch2 aux répertoires d'inclusion du projet.
include_directories("${CATCH2_BASE_PATH}/include")

# Recherche le paquet Catch2 version 3 et indique qu'il est obligatoire.
find_package(Catch2 3 REQUIRED)

# Ajoute un exécutable nommé "Catch2_testing" avec "main.cpp" comme source.
add_executable(Catch2_testing main.cpp)

if (USE_DYNAMIC_CATCH2)
    target_link_libraries(Catch2_testing PRIVATE Catch2::Catch2WithMain)
else ()
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")
        target_link_libraries(Catch2_testing PRIVATE
		        "${CATCH2_BASE_PATH}/build_debug/src/Debug/Catch2Maind.lib"
                "${CATCH2_BASE_PATH}/build_debug/src/Debug/Catch2d.lib")
    else ()
        target_link_libraries(Catch2_testing PRIVATE
			    "${CATCH2_BASE_PATH}/build_release/src/Release/Catch2Main.lib"
                "${CATCH2_BASE_PATH}/build_release/src/Release/Catch2.lib")
    endif ()
endif ()
```
## Linux : Installation
### Mon Script

```bash
#!/bin/bash

# Define common paths and variables
ROOT_PATH="/home/remi/Frameworks"
LIBRARY_NAME="Catch2"
LIBRARY_VERSION="3.8.0"
DOWNLOAD_URL="https://github.com/catchorg/Catch2/archive/refs/tags/v${LIBRARY_VERSION}.tar.gz"
EXTRACTED_DIR_NAME="Catch2-${LIBRARY_VERSION}"
ARCHIVE_NAME="v${LIBRARY_VERSION}.tar.gz"
INSTALLATION_DIR="${ROOT_PATH}/${LIBRARY_NAME}/${LIBRARY_VERSION}"

# Navigate to the root path and set up directories
cd $ROOT_PATH
mkdir -p $LIBRARY_NAME
cd $LIBRARY_NAME

# Download and extract the library
wget $DOWNLOAD_URL
tar -xzvf $ARCHIVE_NAME
mv $EXTRACTED_DIR_NAME $LIBRARY_VERSION
rm $ARCHIVE_NAME
cd $LIBRARY_VERSION

# Define common cmake options
CMAKE_OPTIONS="-DBUILD_TESTING=OFF -DCMAKE_INSTALL_PREFIX=$INSTALLATION_DIR"

# Build and install functions
build_and_install() {
    local build_dir=$1
    local build_type=$2
    local shared_libs=$3
	mkdir $build_dir
    cd $build_dir
    cmake .. $CMAKE_OPTIONS -DCMAKE_BUILD_TYPE=$build_type -DBUILD_SHARED_LIBS=$shared_libs
    cmake --build . --config $build_type
    cmake --install . --config $build_type
    cd ..
}

# Invoke the build functions
build_and_install "build_debug" "Debug" "OFF"
build_and_install "build_release" "Release" "OFF"
build_and_install "build_debug_so" "Debug" "ON"
build_and_install "build_release_so" "Release" "ON"
```
### CMakeLists.txt
```cmake
# Spécifie la version minimale requise de CMake pour exécuter ce script.  
cmake_minimum_required(VERSION 3.26)  
  
# Nomme le projet "Catch2_testing".  
project(Catch2_testing)  
  
# Fixe la version du standard C++ utilisée à C++23.  
set(CMAKE_CXX_STANDARD 23)  
  
# Définit le chemin de base pour Catch2.  
set(CATCH2_BASE_PATH "/opt/catch2/3.8.0")  
  
# Indique si Catch2 est utilisé en tant que DLL (bibliothèque dynamique) ou non.  
SET(USE_DYNAMIC_CATCH2 OFF)  
  
# Affiche le type de build (Debug, Release, etc.).  
MESSAGE("Type: ${CMAKE_BUILD_TYPE}")  
  
# Si Catch2 est utilisé comme une DLL.  
if (USE_DYNAMIC_CATCH2)  
    MESSAGE("Link: Dynamic (SO)")  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        set(CATCH2_DLL_PATH "${CATCH2_BASE_PATH}/build_debug_so/src")  
    else ()  
        set(CATCH2_DLL_PATH "${CATCH2_BASE_PATH}/build_release_so/src")  
    endif ()  
  
    # Définit le répertoire de destination pour les DLLs.  
    set(DLL_DEST_DIR ${CMAKE_BINARY_DIR})  
    MESSAGE("Copy the SO files to the executable directory : ${DLL_DEST_DIR}")  
    MESSAGE("${CATCH2_DLL_PATH}/*.so")  
  
  
    # Récupère tous les fichiers DLL du chemin spécifié.  
    file(GLOB CATCH2_DLLS "${CATCH2_DLL_PATH}/*.so")  
    # Boucle pour copier chaque DLL dans le répertoire d'exécution.  
    foreach (DLL ${CATCH2_DLLS})  
        get_filename_component(DLL_NAME ${DLL} NAME)  
        MESSAGE("SO File : ${DLL_NAME}")  
        configure_file("${CATCH2_DLL_PATH}/${DLL_NAME}" "${DLL_DEST_DIR}/${DLL_NAME}" COPYONLY)  
    endforeach ()  
else ()  
    MESSAGE("Link: Static")  
endif ()  
  
# Ajoute le chemin de base de Catch2 à CMAKE_PREFIX_PATH pour faciliter la recherche de paquets.  
list(APPEND CMAKE_PREFIX_PATH ${CATCH2_BASE_PATH})  
  
# Ajoute le répertoire d'en-tête de Catch2 aux répertoires d'inclusion du projet.  
include_directories("${CATCH2_BASE_PATH}/include")  
  
# Recherche le paquet Catch2 version 3 et indique qu'il est obligatoire.  
find_package(Catch2 3 REQUIRED)  
  
# Ajoute un exécutable nommé "Catch2_testing" avec "main.cpp" comme source.  
add_executable(Catch2_testing main.cpp)  
  
if (USE_DYNAMIC_CATCH2)  
    target_link_libraries(Catch2_testing PRIVATE Catch2::Catch2WithMain)  
else ()  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        target_link_libraries(Catch2_testing PRIVATE  
                "${CATCH2_BASE_PATH}/build_debug/src/libCatch2Maind.a"  
                "${CATCH2_BASE_PATH}/build_debug/src/libCatch2d.a")  
    else ()  
        target_link_libraries(Catch2_testing PRIVATE  
                "${CATCH2_BASE_PATH}/build_release/src/libCatch2Main.a"  
                "${CATCH2_BASE_PATH}/build_release/src/libCatch2.a")  
    endif ()  
endif ()
```
## Programme test
```cpp
#include <catch2/catch_test_macros.hpp>  
  
unsigned int Factorial( unsigned int number ) {  
    return number <= 1 ? number : Factorial(number-1)*number;  
}  
  
TEST_CASE( "Factorials are computed", "[factorial]" ) {  
    REQUIRE( Factorial(1) == 1 );  
    REQUIRE( Factorial(2) == 2 );  
    REQUIRE( Factorial(3) == 6 );  
    REQUIRE( Factorial(10) == 3628800 );  
}  
  
TEST_CASE( "vectors can be sized and resized", "[vector]" ) {  
  
    std::vector<int> v( 5 );  
  
    REQUIRE( v.size() == 5 );  
    REQUIRE( v.capacity() >= 5 );  
  
    SECTION( "resizing bigger changes size and capacity" ) {  
        v.resize( 10 );  
  
        REQUIRE( v.size() == 10 );  
        REQUIRE( v.capacity() >= 10 );  
    }    SECTION( "resizing smaller changes size but not capacity" ) {  
        v.resize( 0 );  
  
        REQUIRE( v.size() == 0 );  
        REQUIRE( v.capacity() >= 5 );  
    }    SECTION( "reserving bigger changes capacity but not size" ) {  
        v.reserve( 10 );  
  
        REQUIRE( v.size() == 5 );  
        REQUIRE( v.capacity() >= 10 );  
    }    SECTION( "reserving smaller does not change size or capacity" ) {  
        v.reserve( 0 );  
  
        REQUIRE( v.size() == 5 );  
        REQUIRE( v.capacity() >= 5 );  
    }}
```