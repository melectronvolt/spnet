# Boost 🚈

```{image} ../../_static/_medias/coding/clion/boostlogo.png
:width: 300px
:align: center
:class: vspace
```

## Description
**Boost C++ Libraries**, ou simplement **Boost**, est une collection de bibliothèques logicielles destinée à augmenter la fonctionnalité et la productivité du langage C++.

- **Origine** 🌱
	Boost est né d'une initiative communautaire visant à fournir des solutions de haute qualité qui complètent la bibliothèque standard C++ (STL). Il est largement reconnu et respecté dans la communauté de développement C++.
- **Contenu** 📚
	Boost comprend un large éventail de bibliothèques qui couvrent différentes fonctionnalités, allant de structures de données, algorithmes, utilitaires, à des bibliothèques pour la programmation concurrente, réseau, test unitaire, et bien plus.
- **Portabilité** 💼
	Une des grandes forces de Boost est sa portabilité. Les bibliothèques sont conçues pour fonctionner sur une grande variété de systèmes et de compilateurs.
- **Qualité** ⭐
	Les bibliothèques Boost sont généralement considérées comme de très haute qualité. Beaucoup d'entre elles sont le fruit d'un travail collaboratif et ont été soumises à des revues rigoureuses par la communauté.
- **Influence sur le C++ Standard** 🔄:
	De nombreuses fonctionnalités et bibliothèques initialement introduites dans Boost ont été intégrées ultérieurement dans la norme C++ officielle. C'est une preuve de la qualité et de l'utilité de Boost dans l'évolution du langage C++.
- **Licence** 📜
	Boost est distribué sous la Boost Software License, qui est une licence libre et open-source. Cela signifie que vous pouvez l'utiliser dans vos projets personnels et commerciaux sans restriction.
- **Utilisation** 🛠
	Pour utiliser Boost, vous devez le télécharger et le configurer pour votre environnement de développement. Certaines bibliothèques nécessitent une étape de compilation, tandis que d'autres sont entièrement basées sur des en-têtes (header-only) et ne nécessitent pas de compilation séparée.

En conclusion, Boost C++ Libraries est une ressource précieuse pour tout développeur C++ cherchant à élargir ses capacités, à gagner du temps grâce à des solutions éprouvées, ou à se familiariser avec des fonctionnalités qui pourraient éventuellement être adoptées dans le standard C++ à l'avenir. 🚀👩‍💻👨‍💻
## Windows
### Installation

> [!WARNING] ICU
> Sous Windows je ne comprends pas pourquoi boost n’arrive pas à trouver les bibliothèques ICU récupérer depuis VCPKG. Bref il va falloir le compiler à la main 💪🏻.

⚠️ : Ouvrir `Developer PowerShell for VS 2022` pour la compilation de ICU ce sera indispensable


> [!WARNING] X64 Compilation
> On my side (Win11 / VS 2022), I’m forced to launch the x64 cmd line environment and execute the script with this kind of command line

```bash
powershell.exe -File "C:\Scripts\BackupScript.ps1" -noexit
```

```powershell
$BASE_PATH = "F:\Frameworks"

$NAME_LIBRARY = "Boost"
$LIBRARY_VERSION = "1.86.0"
$LIBRARY_VERSION_NAME = "1_86_0"
$LIBRARY_NAME_SUB_BOOST = "boost_1_86_0"
$ARCHIVE_NAME_BOOST = "boost_${LIBRARY_VERSION_NAME}"
$DOWNLOAD_BOOST_URL = "https://boostorg.jfrog.io/artifactory/main/release/${LIBRARY_VERSION}/source/${ARCHIVE_NAME_BOOST}.zip"

$NAME_LIBRARY_VCPKG = "vcpkg"
$DIRECTORY_VCPKG_BASE = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY_VCPKG
$DIRECTORY_VCPKG_INSTALLED = Join-Path -Path $DIRECTORY_VCPKG_BASE -ChildPath "installed\x64-windows"
$DIRECTORY_VCPKG_INSTALLED_INCLUDE = Join-Path -Path $DIRECTORY_VCPKG_INSTALLED -ChildPath "include"
$DIRECTORY_VCPKG_INSTALLED_LIB = Join-Path -Path $DIRECTORY_VCPKG_INSTALLED -ChildPath "lib"

$NAME_LIBRARY_ICU = "ICU"
$LIBRARY_VERSION_ICU = "release-75-1"
$LIBRARY_NAME_ICU4C = "icu4c-75_1"
$DOWNLOAD_ICU_URL = "https://github.com/unicode-org/icu/releases/download/${LIBRARY_VERSION_ICU}/${LIBRARY_NAME_ICU4C}-src.zip"
$ARCHIVE_NAME_ICU = "${LIBRARY_VERSION_ICU}.zip"

$BASE_PATH_BOOST = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY
$BASE_PATH_ICU = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY_ICU
$BASE_PATH_VCPKG = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY_VCPKG


Set-Location -Path $BASE_PATH

##############################
#            VCPKG
##############################

if (Test-Path $DIRECTORY_VCPKG_BASE) {
    Remove-Item -Path $DIRECTORY_VCPKG_BASE -Recurse -Force
}

git clone https://github.com/microsoft/vcpkg.git
Set-Location -Path $BASE_PATH_VCPKG 

# Run the bootstrap script
.\bootstrap-vcpkg.bat

# Install the required libraries
.\vcpkg install zlib bzip2 liblzma zstd libiconv

##############################
#            ICU
##############################

New-Item -ItemType Directory -Path $BASE_PATH_ICU -Force
Set-Location -Path $BASE_PATH_ICU

$ZIP_PATH = Join-Path -Path $BASE_PATH_ICU -ChildPath $ARCHIVE_NAME_ICU

if (Test-Path $ZIP_PATH) {
    Remove-Item -Path $ZIP_PATH
}

if (Test-Path "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}") {
    Remove-Item -Path "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" -Recurse -Force
}

if (Test-Path "${BASE_PATH_ICU}\icu") {
    Remove-Item -Path "${BASE_PATH_ICU}\icu" -Recurse -Force
}

Invoke-WebRequest -Uri $DOWNLOAD_ICU_URL -OutFile $ZIP_PATH

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($ZIP_PATH, $BASE_PATH_ICU)

Rename-Item -Path "$BASE_PATH_ICU\icu" -NewName "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}"

$INSTALL_PATH_ICU = Join-Path -Path "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" -ChildPath "\source\allinone"

Set-Location -Path $INSTALL_PATH_ICU
msbuild allinone.sln /p:Configuration=Debug /p:Platform=x64
msbuild allinone.sln /p:Configuration=Release /p:Platform=x64

##############################
#            BOOST
##############################

New-Item -ItemType Directory -Path $BASE_PATH_BOOST -Force
Set-Location -Path $BASE_PATH_BOOST

$ZIP_PATH = Join-Path -Path $BASE_PATH_BOOST -ChildPath "${ARCHIVE_NAME_BOOST}.zip"

if (Test-Path $ZIP_PATH) {
    Remove-Item -Path $ZIP_PATH
}

if (Test-Path "$BASE_PATH_BOOST\${LIBRARY_VERSION}") {
    Remove-Item -Path "$BASE_PATH_BOOST\${LIBRARY_VERSION}" -Recurse -Force
}

Invoke-WebRequest -Uri $DOWNLOAD_BOOST_URL -OutFile $ZIP_PATH

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($ZIP_PATH, $BASE_PATH_BOOST)

if (Test-Path $ZIP_PATH) {
    Remove-Item -Path $ZIP_PATH
}

Rename-Item -Path "$BASE_PATH_BOOST\${LIBRARY_NAME_SUB_BOOST}" -NewName "${BASE_PATH_BOOST}\${LIBRARY_VERSION}"
Set-Location -Path "$BASE_PATH_BOOST\${LIBRARY_VERSION}"

.\bootstrap.bat

.\b2.exe address-model=64 variant=debug link=static,shared "-sZLIB_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZLIB_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sBZIP2_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sBZIP2_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sLZMA_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sLZMA_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sZSTD_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZSTD_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sICU_PATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" "-sICU_INCLUDE=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\include" "-sICU_LIBPATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\lib64" "-sICONV_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sICONV_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sICONV_PATH=${DIRECTORY_VCPKG_INSTALLED}"

.\b2.exe address-model=64 variant=release link=static,shared "-sZLIB_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZLIB_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sBZIP2_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sBZIP2_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sLZMA_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sLZMA_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sZSTD_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZSTD_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sICU_PATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" "-sICU_INCLUDE=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\include" "-sICU_LIBPATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\lib64" "-sICONV_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sICONV_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" "-sICONV_PATH=${DIRECTORY_VCPKG_INSTALLED}"
```

```{image} ../../_static/_medias/coding/clion/boostcmd.png
:width: 400px
:align: center
:class: vspace
```

### b2 info
Pour construire Boost avec les paramètres donnés, vous pouvez utiliser la commande suivante :
```bash
b2 variant=debug,release link=static,shared threading=multi address-model=64 toolset=msvc-14.3 --build-type=complete --layout=versioned stage
```
Explication des paramètres :
- `variant=debug,release` : Construire à la fois les versions de débogage et de production.
- `link=static,shared` : Générer à la fois des bibliothèques statiques (`.lib`) et des bibliothèques dynamiques (`.dll`).
- `threading=multi` : Activer le multi-threading.
- `address-model=64` : Cibler l'architecture x64.
- `toolset=msvc-14.3` : Utiliser le compilateur Visual C++ 14.3. Vous devrez peut-être ajuster cela en fonction de la version de Visual Studio que vous utilisez.
- `--build-type=complete` : Construire toutes les variantes de bibliothèques.
- `--layout=versioned` : Générer des bibliothèques avec une disposition versionnée. Cette option ajoutera un suffixe aux noms des bibliothèques avec la version de Boost, le nom du compilateur et d'autres options.
- `stage` : Cela indique à `b2` de placer les bibliothèques construites dans le répertoire `stage`.

Vous pouvez remplacer `msvc-14.3` par la version du compilateur de votre choix. Vous pouvez également remplacer `stage` par `install` et ajouter `--prefix=chemin/vers/installation` si vous souhaitez installer Boost dans un répertoire spécifique au lieu de simplement mettre en scène les bibliothèques.
### Using Boost
```cmake
cmake_minimum_required(VERSION 3.26)  
project(Boost_testing)  
  
set(BOOST_ROOT "F:\\Frameworks\\boost\\1.86.0")  
  
set(Boost_USE_STATIC_LIBS ON)  
  
find_package(Boost REQUIRED COMPONENTS filesystem)  
  
include_directories(${Boost_INCLUDE_DIRS})  
link_directories(${Boost_LIBRARY_DIR_DEBUG})  
  
set(CMAKE_CXX_STANDARD 20)  
add_executable(Boost_testing main.cpp)
target_link_libraries(Boost_testing PRIVATE Boost::filesystem)
```
## Linux
### Installation
Installing Boost on Linux is really easier, just install the correct dev packages and compile boost.
```bash
#!/bin/bash

sudo apt update && sudo apt upgrade -y && sudo apt install -y build-essential g++ autotools-dev libicu-dev libbz2-dev liblzma-dev zlib1g-dev libiconv-hook-dev libpython3-dev libexpat1-dev libzstd-dev

ROOT_PATH="/home/remi/Frameworks"
LIBRARY_NAME="Boost"
LIBRARY_VERSION="1.86.0"
LIBRARY_VERSION_NAME="1_86_0"
DOWNLOAD_URL="https://boostorg.jfrog.io/artifactory/main/release/${LIBRARY_VERSION}/source/boost_${LIBRARY_VERSION_NAME}.tar.gz"
ARCHIVE_NAME="boost_${LIBRARY_VERSION_NAME}.tar.gz"
EXTRACTED_DIR_NAME="boost_${LIBRARY_VERSION_NAME}"

cd $ROOT_PATH
mkdir -p $LIBRARY_NAME
cd $LIBRARY_NAME

wget $DOWNLOAD_URL
tar -xvf $ARCHIVE_NAME
mv $EXTRACTED_DIR_NAME $LIBRARY_VERSION
rm $ARCHIVE_NAME
cd $LIBRARY_VERSION

./bootstrap.sh

./b2 address-model=64 variant=debug link=static,shared
./b2 address-model=64 variant=release link=static,shared
```
### Using Boost
```cmake
cmake_minimum_required(VERSION 3.26)  
project(Boost_testing)  
  
set(BOOST_ROOT "/home/remi/Frameworks/Boost/1.86.0")  
  
set(Boost_USE_STATIC_LIBS ON)
  
find_package(Boost REQUIRED COMPONENTS filesystem)  
  
include_directories(${Boost_INCLUDE_DIRS})  
link_directories(${Boost_LIBRARY_DIR_DEBUG})  
  
set(CMAKE_CXX_STANDARD 20)  
add_executable(Boost_testing main.cpp)
target_link_libraries(Boost_testing PRIVATE Boost::filesystem)
```
## Exemple de programme
```cpp
#include <iostream>  
#include <boost/filesystem.hpp>  
  
int main() {  
    boost::filesystem::path current_directory = boost::filesystem::current_path();  
  
    std::cout << "Listing contents of: " << current_directory.string() << std::endl;  
  
    for (const auto& entry : boost::filesystem::directory_iterator(current_directory)) {  
        std::cout << entry.path().string() << std::endl;  
    }  
    return 0;  
}
```