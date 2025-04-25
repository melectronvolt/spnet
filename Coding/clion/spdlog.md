# spdlog 📃

```{image} ../../_static/_medias/coding/clion/spdlog.png
:width: 300px
:align: center
:class: vspace
```

## Description
- **Origine** 🌱
    **spdlog** est une bibliothèque de journalisation rapide, extensible et header-only pour C++. Elle est conçue pour offrir à la fois une grande performance et une utilisation très simple.
- **Performance** 🚀
    Un des atouts majeurs de spdlog est sa rapidité. Il est conçu pour être l'un des plus rapides, sinon le plus rapide, des frameworks de journalisation en C++.
- **Header-only** 📃:
    Bien qu'il existe une version compilée, spdlog est principalement une bibliothèque "header-only", ce qui facilite son intégration dans des projets sans avoir besoin de compiler des binaires séparés.
- **Syntaxe Intuitive** 🎯
    spdlog offre une syntaxe similaire à celle de la fonction printf ou à la syntaxe de flux de C++, rendant son utilisation familière pour de nombreux développeurs.
- **Formatage Flexible** 
    La bibliothèque utilise le formatage basé sur `{}` qui est très similaire à Python. Cela permet d'ajouter facilement des variables dans les messages de journalisation.
- **Multithreading** 
    spdlog est thread-safe. Vous pouvez donc l'utiliser sans souci dans des applications multithreadées.
- **Niveaux de Journalisation** 📊
    Comme la plupart des frameworks de journalisation, spdlog offre plusieurs niveaux de journalisation tels que info, warn, error, debug, etc., permettant ainsi de filtrer et de classer les messages selon leur importance.
- **Rotation et Troncature des Fichiers** 🔄
    spdlog gère automatiquement la rotation et la troncature des fichiers de log, évitant ainsi que les fichiers ne deviennent trop volumineux.
- **Sinks** 🚰
    "Sinks" (sorties) sont des endroits où vos logs sont dirigés. spdlog offre une variété de "sinks", permettant d'écrire des logs dans des fichiers, sur la console, vers des sorties réseau et plus encore.
- **Extensibilité** 🔌:
	Si les fonctionnalités standard ne suffisent pas, spdlog est extensible, permettant aux développeurs d'ajouter leurs propres "sinks" ou formateurs.
- **Open Source** 📜
	spdlog est un projet open source, ce qui signifie que la communauté peut contribuer à son développement, l'utiliser librement et le modifier selon ses besoins.

En résumé, spdlog est une bibliothèque de journalisation C++ moderne, rapide et flexible. Grâce à sa simplicité d'utilisation, sa performance et sa capacité d'extension, elle est largement adoptée dans de nombreux projets C++ à travers le monde. 🌍📖🖥️

## Windows
### Compilation
```powershell
# Définir les chemins et les variables pour le téléchargement et l'installation de la bibliothèque
$BASE_PATH = "D:\Coding\Frameworks"
$NAME_LIBRARY = "spdlog"
$LIBRARY_VERSION = "1.15.1"
$DOWNLOAD_URL = "https://github.com/gabime/spdlog/archive/refs/tags/v${LIBRARY_VERSION}.zip"

# compiler le chemin de base pour la bibliothèque
$BASE_LIBRARY_PATH = Join-Path -Path $BASE_PATH -ChildPath "$NAME_LIBRARY"

# compiler le chemin vers la version spécifique de la bibliothèque
$VERSION_LIBRARY_PATH = Join-Path -Path $BASE_LIBRARY_PATH -ChildPath "$LIBRARY_VERSION"

# Définir le nom du répertoire extrait et le nom de l'archive
$EXTRACTED_DIR_NAME = "spdlog-${LIBRARY_VERSION}"
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

# Fonction pour compiler et installer la bibliothèque
function BuildAndInstallLibrary($build_directory, $config, $sharedLibs) {
    $directory = Join-Path -Path $VERSION_LIBRARY_PATH -ChildPath $build_directory
    # Créer un répertoire pour la construction
    New-Item -ItemType Directory -Path $directory -Force
    Set-Location -Path $directory


    $cmakeArgs = @(
        "..",
        "-DCMAKE_INSTALL_PREFIX=${VERSION_LIBRARY_PATH}",
        "-DCMAKE_BUILD_TYPE=$config",
        "-DBUILD_SHARED_LIBS=$sharedLibs"
        "-DCMAKE_CXX_FLAGS=/utf-8"  # Force Unicode support in MSVC
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
  
# 🔧 Force MSVC to use UTF-8 encoding
add_compile_options("/utf-8")  
  
# Nomme le projet "spdlog_testing".  
project(spdlog_testing)  
  
# Fixe la version du standard C++ utilisée à C++23.  
set(CMAKE_CXX_STANDARD 23)  
  
# Définit le chemin de base pour spdlog.  
set(spdlog_BASE_PATH "D:/Coding/Frameworks/spdlog/1.15.1")  
  
# Indique si spdlog est utilisé en tant que DLL (bibliothèque dynamique) ou non.  
SET(USE_DYNAMIC_spdlog OFF)  
  
if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
 if (USE_DYNAMIC_spdlog)  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_debug_dll")  
    else()  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_debug")  
    endif()  
else ()  
 if (USE_DYNAMIC_spdlog)  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_release_dll")  
    else()  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_release")  
    endif()  
endif ()  
  
  
# Affiche le type de build (Debug, Release, etc.).  
MESSAGE("Type: ${CMAKE_BUILD_TYPE}")  
  
# Si spdlog est utilisé comme une DLL.  
if (USE_DYNAMIC_spdlog)  
    MESSAGE("Link: Dynamic (DLL)")  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        set(spdlog_DLL_PATH "${spdlog_BASE_PATH}/build_debug/Debug")  
    else ()  
        set(spdlog_DLL_PATH "${spdlog_BASE_PATH}/build_release/Release")  
    endif ()  
  
    # Définit le répertoire de destination pour les DLLs.  
    set(DLL_DEST_DIR ${CMAKE_BINARY_DIR})  
    MESSAGE("Copy the DLLs to the executable directory : ${DLL_DEST_DIR}")  
  
    # Récupère tous les fichiers DLL du chemin spécifié.  
    file(GLOB spdlog_DLLS "${spdlog_DLL_PATH}/*.dll")  
    # Boucle pour copier chaque DLL dans le répertoire d'exécution.  
    foreach (DLL ${spdlog_DLLS})  
        get_filename_component(DLL_NAME ${DLL} NAME)  
        MESSAGE("DLL : ${DLL_NAME}")  
        configure_file("${spdlog_DLL_PATH}/${DLL_NAME}" "${DLL_DEST_DIR}/${DLL_NAME}" COPYONLY)  
    endforeach ()  
else ()  
    MESSAGE("Link: Static")  
endif ()  
  
# Ajoute le chemin de base de spdlog à CMAKE_PREFIX_PATH pour faciliter la recherche de paquets.  
list(APPEND CMAKE_PREFIX_PATH "${spdlog_BASE_PATH_find}")  
  
# Ajoute le répertoire d'en-tête de spdlog aux répertoires d'inclusion du projet.  
include_directories("${spdlog_BASE_PATH}/include")  
  
# Recherche le paquet spdlog version 3 et indique qu'il est obligatoire.  
find_package(spdlog REQUIRED)  
  
# Ajoute un exécutable nommé "spdlog_testing" avec "main.cpp" comme source.  
add_executable(spdlog_testing main.cpp)  
  
if (USE_DYNAMIC_spdlog)  
    target_link_libraries(spdlog_testing PRIVATE spdlog::spdlog)  
else ()  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        target_link_libraries(spdlog_testing PRIVATE  
                "${spdlog_BASE_PATH}/build_debug/Debug/spdlogd.lib")  
    else ()  
        target_link_libraries(spdlog_testing PRIVATE  
                "${spdlog_BASE_PATH}/build_release/Release/spdlog.lib")  
    endif ()  
endif ()
```
## Linux
### Installation
```bash
#!/bin/bash
# -------------------------------------------------------------------------------
# Installation automatisée de spdlog 1.15.2 sur Debian / Ubuntu
# -------------------------------------------------------------------------------

# 1. Mise à jour du système et installation des dépendances indispensables
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential cmake ninja-build unzip wget

# 2. Définition des variables liées à spdlog 1.15.2
ROOT_PATH="/opt/spdlog"                       # Répertoire racine pour toutes les versions
LIBRARY_VERSION="1.15.2"                      # Version x.y.z de spdlog
ARCHIVE_NAME="v${LIBRARY_VERSION}.zip"        # Nom du fichier ZIP téléchargé
EXTRACTED_DIR_NAME="spdlog-${LIBRARY_VERSION}"# Dossier généré après extraction
DOWNLOAD_URL="https://github.com/gabime/spdlog/archive/refs/tags/${ARCHIVE_NAME}"
INSTALL_PREFIX="${ROOT_PATH}/${LIBRARY_VERSION}" # Chemin d’installation isolé

# 3. Création (ou vérification) du répertoire racine puis déplacement
sudo mkdir -p "${ROOT_PATH}"
cd "${ROOT_PATH}" || { echo "Erreur : impossible d’accéder à ${ROOT_PATH}" >&2; exit 1; }

# 4. Téléchargement de l’archive spdlog
wget "${DOWNLOAD_URL}"

# 5. Nettoyage d’une éventuelle installation précédente de la même version
sudo rm -rf "${LIBRARY_VERSION}"

# 6. Extraction de l’archive ZIP
unzip "${ARCHIVE_NAME}"

# 7. Renommage du dossier extrait pour refléter directement la version
mv "${EXTRACTED_DIR_NAME}" "${LIBRARY_VERSION}"

# 8. Suppression de l’archive afin d’économiser de l’espace
rm "${ARCHIVE_NAME}"

# 9. Passage dans le dossier source de spdlog
cd "${LIBRARY_VERSION}" || { echo "Erreur : impossible d’accéder à ${LIBRARY_VERSION}" >&2; exit 1; }

# 10. Options CMake communes
CMAKE_BASE_OPTIONS="-DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX} -DSPDLOG_BUILD_TESTS=OFF"

# 11. Compilation — quatre variantes
#     • Debug   statique
#     • Release statique
#     • Debug   partagée
#     • Release partagée

## 11-a : Debug statique
mkdir build_debug && cd build_debug
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Debug   -DBUILD_SHARED_LIBS=OFF
cmake --build . --config Debug
cmake --install . --config Debug
cd ..

## 11-b : Release statique
mkdir build_release && cd build_release
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF
cmake --build . --config Release
cmake --install . --config Release
cd ..

## 11-c : Debug partagée
mkdir build_debug_so && cd build_debug_so
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Debug   -DBUILD_SHARED_LIBS=ON
cmake --build . --config Debug
cmake --install . --config Debug
cd ..

## 11-d : Release partagée
mkdir build_release_so && cd build_release_so
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON
cmake --build . --config Release
cmake --install . --config Release
cd ..

# -------------------------------------------------------------------------------
# Fin de l’installation de spdlog 1.15.2
#     • Bibliothèques statiques et partagées installées sous : ${INSTALL_PREFIX}
# -------------------------------------------------------------------------------

```
### CMakeLists.txt
```cmake
# Spécifie la version minimale requise de CMake pour exécuter ce script.  
cmake_minimum_required(VERSION 3.26)  
  
# Nomme le projet "spdlog_testing".  
project(spdlog_testing)  
  
# Fixe la version du standard C++ utilisée à C++23.  
set(CMAKE_CXX_STANDARD 23)  
  
# Définit le chemin de base pour spdlog.  
set(spdlog_BASE_PATH "/opt/spdlog/1.15.1")  
  
# Indique si spdlog est utilisé en tant que SO (bibliothèque dynamique) ou non.  
SET(USE_DYNAMIC_spdlog ON)  
  
if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
 if (USE_DYNAMIC_spdlog)  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_debug_so")  
    else()  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_debug")  
    endif()  
else ()  
 if (USE_DYNAMIC_spdlog)  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_release_so")  
    else()  
    set(spdlog_BASE_PATH_find "${spdlog_BASE_PATH}/build_release")  
    endif()  
endif ()  
  
  
# Affiche le type de build (Debug, Release, etc.).  
MESSAGE("Type: ${CMAKE_BUILD_TYPE}")  
  
# Si spdlog est utilisé comme une SO.  
if (USE_DYNAMIC_spdlog)  
    MESSAGE("Link: Dynamic (SO)")  
     # Définit le répertoire de destination pour les SOs.  
    set(SO_DEST_DIR ${CMAKE_BINARY_DIR})  
    MESSAGE("Copy the SOs to the executable directory : ${SO_DEST_DIR}")  
    MESSAGE("Copy the SOs from the directory : ${spdlog_BASE_PATH_find}")  
    # Récupère tous les fichiers SO du chemin spécifié.  
    file(GLOB spdlog_SOS "${spdlog_BASE_PATH_find}/*.so")  
    # Boucle pour copier chaque SO dans le répertoire d'exécution.  
    foreach (SO ${spdlog_SOS})  
        get_filename_component(SO_NAME ${SO} NAME)  
        MESSAGE("SO : ${SO_NAME}")  
        configure_file("${spdlog_BASE_PATH_find}/${SO_NAME}" "${SO_DEST_DIR}/${SO_NAME}" COPYONLY)  
    endforeach ()  
else ()  
    MESSAGE("Link: Static")  
endif ()  
  
# Ajoute le chemin de base de spdlog à CMAKE_PREFIX_PATH pour faciliter la recherche de paquets.  
list(APPEND CMAKE_PREFIX_PATH "${spdlog_BASE_PATH_find}")  
  
# Ajoute le répertoire d'en-tête de spdlog aux répertoires d'inclusion du projet.  
include_directories("${spdlog_BASE_PATH}/include")  
  
# Recherche le paquet spdlog version 3 et indique qu'il est obligatoire.  
find_package(spdlog REQUIRED)  
  
# Ajoute un exécutable nommé "spdlog_testing" avec "main.cpp" comme source.  
add_executable(spdlog_testing main.cpp)  
  
if (USE_DYNAMIC_spdlog)  
    target_link_libraries(spdlog_testing PRIVATE spdlog::spdlog)  
else ()  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        target_link_libraries(spdlog_testing PRIVATE  
                "${spdlog_BASE_PATH}/build_debug/libspdlogd.a")  
    else ()  
        target_link_libraries(spdlog_testing PRIVATE  
                "${spdlog_BASE_PATH}/build_release/libspdlog.a")  
    endif ()  
endif ()
```
## Test
```cpp
#include <iostream>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_color_sinks.h>

int main() {
    // Créer un logger console coloré
    auto console = spdlog::stdout_color_mt("console");
    
    // Définir le niveau de journalisation en info. Cela signifie que tous les journaux inférieurs à "info" ne seront pas affichés.
    spdlog::set_level(spdlog::level::info);

    // Définir un gestionnaire d'erreurs personnalisé
    spdlog::set_error_handler([](const std::string &msg) {
        std::cerr << "Erreur spdlog: " << msg << std::endl;
    });

    console->info("Bienvenue dans spdlog !");
    console->warn("Un warning");
    console->error("Ceci est une erreur!");

    return 0;
}

```