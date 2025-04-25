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
# Définition du chemin de base pour les frameworks
$BASE_PATH = "D:\Coding\Frameworks"

# Configuration pour la bibliothèque Boost
$NAME_LIBRARY = "Boost"
$LIBRARY_VERSION = "1.87.0"
$LIBRARY_VERSION_NAME = "1_87"
$LIBRARY_NAME_SUB_BOOST = "boost_1_87_0"
$ARCHIVE_NAME_BOOST = "boost_${LIBRARY_VERSION_NAME}"
$DOWNLOAD_BOOST_URL = "https://archives.boost.io/release/${LIBRARY_VERSION}/source/${LIBRARY_NAME_SUB_BOOST}.zip"

# Configuration pour vcpkg et définition des chemins d'installation des dépendances
$NAME_LIBRARY_VCPKG = "vcpkg"
$DIRECTORY_VCPKG_BASE = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY_VCPKG
$DIRECTORY_VCPKG_INSTALLED = Join-Path -Path $DIRECTORY_VCPKG_BASE -ChildPath "installed\x64-windows"
$DIRECTORY_VCPKG_INSTALLED_INCLUDE = Join-Path -Path $DIRECTORY_VCPKG_INSTALLED -ChildPath "include"
$DIRECTORY_VCPKG_INSTALLED_LIB = Join-Path -Path $DIRECTORY_VCPKG_INSTALLED -ChildPath "lib"

# Configuration pour la bibliothèque ICU
$NAME_LIBRARY_ICU = "ICU"
$LIBRARY_VERSION_ICU = "release-74-2"
$LIBRARY_NAME_ICU4C = "icu4c-74_2"
$DOWNLOAD_ICU_URL = "https://github.com/unicode-org/icu/releases/download/${LIBRARY_VERSION_ICU}/${LIBRARY_NAME_ICU4C}-src.zip"
$ARCHIVE_NAME_ICU = "${LIBRARY_VERSION_ICU}.zip"

# Définition des chemins pour Boost, ICU et vcpkg
$BASE_PATH_BOOST = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY
$BASE_PATH_ICU = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY_ICU
$BASE_PATH_VCPKG = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY_VCPKG

# Positionnement dans le répertoire de base
Set-Location -Path $BASE_PATH

##################################
#            VCPKG
##################################

# Suppression du répertoire vcpkg s'il existe pour un démarrage propre
if (Test-Path $DIRECTORY_VCPKG_BASE) {
    Remove-Item -Path $DIRECTORY_VCPKG_BASE -Recurse -Force
}

# Clonage du dépôt vcpkg depuis GitHub
git clone https://github.com/microsoft/vcpkg.git

# Passage dans le répertoire cloné de vcpkg
Set-Location -Path $BASE_PATH_VCPKG 

# Exécution du script de bootstrap pour initialiser vcpkg
.\bootstrap-vcpkg.bat

# Installation des bibliothèques requises via vcpkg (zlib, bzip2, liblzma, zstd, libiconv)
.\vcpkg install zlib bzip2 liblzma zstd libiconv

##################################
#            ICU
##################################

# Création du répertoire pour ICU et positionnement à l'intérieur
New-Item -ItemType Directory -Path $BASE_PATH_ICU -Force
Set-Location -Path $BASE_PATH_ICU

# Définition du chemin complet de l'archive ICU à télécharger
$ZIP_PATH = Join-Path -Path $BASE_PATH_ICU -ChildPath $ARCHIVE_NAME_ICU

# Suppression de l'archive ICU si elle existe déjà
if (Test-Path $ZIP_PATH) {
    Remove-Item -Path $ZIP_PATH
}

# Suppression d'anciens dossiers ICU (si existants) pour éviter les conflits
if (Test-Path "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}") {
    Remove-Item -Path "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" -Recurse -Force
}

if (Test-Path "${BASE_PATH_ICU}\icu") {
    Remove-Item -Path "${BASE_PATH_ICU}\icu" -Recurse -Force
}

# Téléchargement de l'archive ICU depuis GitHub
Invoke-WebRequest -Uri $DOWNLOAD_ICU_URL -OutFile $ZIP_PATH

# Chargement de l'assembly .NET pour la manipulation de fichiers ZIP
Add-Type -AssemblyName System.IO.Compression.FileSystem

# Extraction de l'archive ZIP dans le répertoire ICU
[System.IO.Compression.ZipFile]::ExtractToDirectory($ZIP_PATH, $BASE_PATH_ICU)

# Renommage du dossier extrait pour qu'il corresponde à la version spécifiée d'ICU
Rename-Item -Path "$BASE_PATH_ICU\icu" -NewName "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}"

# Définition du chemin d'installation pour la construction d'ICU (dossier "allinone")
$INSTALL_PATH_ICU = Join-Path -Path "${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" -ChildPath "\source\allinone"

# Passage dans le répertoire de construction d'ICU
Set-Location -Path $INSTALL_PATH_ICU

# Compilation d'ICU en mode Debug puis en mode Release avec MSBuild pour la plateforme x64
msbuild allinone.sln /p:Configuration=Debug /p:Platform=x64
msbuild allinone.sln /p:Configuration=Release /p:Platform=x64

##################################
#            BOOST
##################################

# Création du répertoire pour Boost et positionnement à l'intérieur
New-Item -ItemType Directory -Path $BASE_PATH_BOOST -Force
Set-Location -Path $BASE_PATH_BOOST

# Définition du chemin complet de l'archive Boost à télécharger
$ZIP_PATH = Join-Path -Path $BASE_PATH_BOOST -ChildPath "${ARCHIVE_NAME_BOOST}.zip"

# Suppression de l'archive Boost si elle existe déjà
if (Test-Path $ZIP_PATH) {
    Remove-Item -Path $ZIP_PATH
}

# Suppression d'un ancien dossier Boost (si existant) pour éviter les conflits
if (Test-Path "$BASE_PATH_BOOST\${LIBRARY_VERSION}") {
    Remove-Item -Path "$BASE_PATH_BOOST\${LIBRARY_VERSION}" -Recurse -Force
}

# Téléchargement de l'archive Boost depuis le serveur officiel
Invoke-WebRequest -Uri $DOWNLOAD_BOOST_URL -OutFile $ZIP_PATH

# Extraction de l'archive ZIP de Boost dans le répertoire Boost
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($ZIP_PATH, $BASE_PATH_BOOST)

# Suppression de l'archive ZIP après extraction
if (Test-Path $ZIP_PATH) {
    Remove-Item -Path $ZIP_PATH
}

# Renommage du dossier extrait pour correspondre à la version spécifiée de Boost
Rename-Item -Path "$BASE_PATH_BOOST\${LIBRARY_NAME_SUB_BOOST}" -NewName "${BASE_PATH_BOOST}\${LIBRARY_VERSION}"

# Passage dans le répertoire Boost correspondant à la version spécifiée
Set-Location -Path "$BASE_PATH_BOOST\${LIBRARY_VERSION}"

# Exécution du script de bootstrap de Boost pour initialiser la compilation
.\bootstrap.bat

# Compilation de Boost en mode Debug (64 bits, liens statiques et dynamiques) en passant les chemins d'inclusion et des librairies
.\b2.exe address-model=64 variant=debug link=static,shared `
    "-sZLIB_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZLIB_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sBZIP2_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sBZIP2_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sLZMA_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sLZMA_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sZSTD_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZSTD_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sICU_PATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" "-sICU_INCLUDE=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\include" `
    "-sICU_LIBPATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\lib64" `
    "-sICONV_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sICONV_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sICONV_PATH=${DIRECTORY_VCPKG_INSTALLED}"

# Compilation de Boost en mode Release (64 bits, liens statiques et dynamiques) en passant les mêmes paramètres de configuration
.\b2.exe address-model=64 variant=release link=static,shared `
    "-sZLIB_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZLIB_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sBZIP2_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sBZIP2_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sLZMA_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sLZMA_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sZSTD_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sZSTD_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sICU_PATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}" "-sICU_INCLUDE=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\include" `
    "-sICU_LIBPATH=${BASE_PATH_ICU}\${LIBRARY_VERSION_ICU}\lib64" `
    "-sICONV_INCLUDE=${DIRECTORY_VCPKG_INSTALLED_INCLUDE}" "-sICONV_LIBPATH=${DIRECTORY_VCPKG_INSTALLED_LIB}" `
    "-sICONV_PATH=${DIRECTORY_VCPKG_INSTALLED}"
```

```{image} ../../_static/_medias/coding/clion/boostcmd.png
:width: 400px
:align: center
:class: vspace
```

### b2 info
Pour compiler Boost avec les paramètres donnés, vous pouvez utiliser la commande suivante :
```bash
b2 variant=debug,release link=static,shared threading=multi address-model=64 toolset=msvc-14.3 --build-type=complete --layout=versioned stage
```
Explication des paramètres :
- `variant=debug,release` : Compiler à la fois les versions de débogage et de production.
- `link=static,shared` : Générer à la fois des bibliothèques statiques (`.lib`) et des bibliothèques dynamiques (`.dll`).
- `threading=multi` : Activer le multi-threading.
- `address-model=64` : Cibler l'architecture x64.
- `toolset=msvc-14.3` : Utiliser le compilateur Visual C++ 14.3. Vous devrez peut-être ajuster cela en fonction de la version de Visual Studio que vous utilisez.
- `--build-type=complete` : Compiler toutes les variantes de bibliothèques.
- `--layout=versioned` : Générer des bibliothèques avec une disposition versionnée. Cette option ajoutera un suffixe aux noms des bibliothèques avec la version de Boost, le nom du compilateur et d'autres options.
- `stage` : Cela indique à `b2` de placer les bibliothèques construites dans le répertoire `stage`.

Vous pouvez remplacer `msvc-14.3` par la version du compilateur de votre choix. Vous pouvez également remplacer `stage` par `install` et ajouter `--prefix=chemin/vers/installation` si vous souhaitez installer Boost dans un répertoire spécifique au lieu de simplement mettre en scène les bibliothèques.
### Using Boost
```cmake
cmake_minimum_required(VERSION 3.26)  
project(Boost_testing)  
  
set(BOOST_ROOT "D:\\Coding\\Frameworks\\boost\\1.87.0")  
  
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

# --------------------------------------------------------------------------------
# Script d'installation de Boost 1.88.0 sur une distribution Debian/Ubuntu
# --------------------------------------------------------------------------------

# 1. Mise à jour de la liste des paquets et application des mises à jour système
sudo apt update && sudo apt upgrade -y

# 2. Installation des dépendances nécessaires à la compilation de Boost
sudo apt install -y build-essential g++ autotools-dev libicu-dev libbz2-dev \
                    liblzma-dev zlib1g-dev libiconv-hook-dev libpython3-dev \
                    libexpat1-dev libzstd-dev tar wget

# 3. Définition des variables relatives à Boost 1.88.0
ROOT_PATH="/opt/boost"                   # Répertoire d'installation principal
LIBRARY_VERSION="1.88.0"                 # Version officielle x.y.z
LIBRARY_VERSION_NAME="1_88"              # Version formatée pour nommage Boost
LIBRARY_NAME_SUB_BOOST="boost_1_88_0"     # Nom de l'archive et du dossier Boost
ARCHIVE_EXT="tar.gz"                      # Extension de l'archive
DOWNLOAD_URL="https://archives.boost.io/release/${LIBRARY_VERSION}/source/${LIBRARY_NAME_SUB_BOOST}.${ARCHIVE_EXT}"
ARCHIVE_NAME="${LIBRARY_NAME_SUB_BOOST}.${ARCHIVE_EXT}"  # Nom du fichier téléchargé

# 4. Création du répertoire d'installation et déplacement dans celui-ci
sudo mkdir -p "${ROOT_PATH}"
cd "${ROOT_PATH}" || { echo "Erreur : impossible d'accéder à ${ROOT_PATH}" >&2; exit 1; }

# 5. Téléchargement de l'archive Boost 1.88.0
wget "${DOWNLOAD_URL}"

# 6. Suppression de toute précédente installation de même version (pour nettoyage)
sudo rm -rf "${LIBRARY_VERSION}"

# 7. Extraction de l'archive .tar.gz
tar -xzf "${ARCHIVE_NAME}"

# 8. Renommage du dossier extrait pour indiquer directement la version
mv "${LIBRARY_NAME_SUB_BOOST}" "${LIBRARY_VERSION}"

# 9. Suppression de l'archive pour libérer de l'espace
rm "${ARCHIVE_NAME}"

# 10. Passage dans le dossier Boost nouvellement extrait
cd "${LIBRARY_VERSION}" || { echo "Erreur : impossible d'accéder à ${LIBRARY_VERSION}" >&2; exit 1; }

# 11. Initialisation du système de build Boost (script bootstrap)
./bootstrap.sh

# 12. Compilation de Boost
#    • Adresse 64 bits (address-model=64)
#    • Variantes Debug et Release
#    • Liens statiques et partagés
./b2 address-model=64 variant=debug link=static,shared
./b2 address-model=64 variant=release link=static,shared
```
### Using Boost
```cmake
cmake_minimum_required(VERSION 3.26)  
project(Boost_testing)  
  
set(BOOST_ROOT "/opt/boost/1.87.0")  
  
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