# GoogleTest ✅

```{image} ../../_static/_medias/coding/clion/gtestlogo.png
:width: 300px
:align: center
:class: vspace
```

## Description
- **Origine** 🌱
    **googletest** est un framework de tests unitaires pour C++ développé par Google. Il est conçu pour aider les développeurs à écrire des tests robustes et réutilisables rapidement.
- **Simplicité et Puissance** 🎯
    googletest fournit une combinaison de simplicité pour l'écriture de tests basiques et la puissance pour réaliser des tests avancés. Il permet de créer des tests standard et des tests paramétrés pour tester le code avec différents paramètres sans avoir à réécrire le test.
- **Assertions** 📝
    Le framework offre une vaste gamme d'assertions pour vérifier que le comportement du programme est correct. Si une assertion échoue, googletest affiche un message d'erreur bien formaté comprenant le nom du test et la trace d'appel.
- **Organisation des Tests** 📂
    Les tests dans googletest sont organisés en "test cases", chaque "test case" pouvant contenir plusieurs tests individuels. Cette structure facilite la catégorisation et l'exécution sélective des tests.
- **Fixtures de Test** 🛠
    googletest fournit des fonctionnalités pour définir des actions de configuration et de nettoyage à effectuer avant et après chaque test ou groupe de tests. Cela est particulièrement utile pour préparer l'environnement nécessaire à certains tests.
- **Death Tests** 💀
    Un trait distinctif de googletest est sa capacité à vérifier que le code provoque bien une interruption (comme une assertion ou un crash) lorsque c'est attendu.
- **Portabilité** 🌍
    googletest est portable et peut être utilisé sur diverses plateformes et systèmes, dont Windows, Linux et Mac OS. Il supporte plusieurs compilateurs C++.
- **Intégration et Extensions** 
    Le framework peut être facilement intégré à des systèmes de construction et des pipelines CI/CD. De plus, googletest est suffisamment flexible pour être étendu ou adapté selon les besoins spécifiques d'un projet.
- **Open Source** 📜
    googletest est un logiciel open source, ce qui signifie que n'importe qui peut le consulter, l'utiliser, le modifier et le distribuer. La communauté active derrière lui contribue régulièrement à son amélioration.
- **Intégration avec GoogleMock** 🤝
	Pour ceux qui recherchent des fonctionnalités de "mocking", googletest s'intègre parfaitement avec GoogleMock, un autre outil développé par Google, permettant de créer des objets mock et d'assurer que les méthodes sont appelées comme prévu.

En conclusion, googletest est un framework de tests unitaires pour C++ à la fois puissant et flexible. Conçu par Google, il est devenu l'un des outils de test les plus populaires et respectés dans la communauté C++ et est largement utilisé dans de nombreux projets, des petits aux grands. 🌟🔍🖥️
## Windows
```powershell
$BASE_PATH = "D:\Coding\Frameworks"
$NAME_LIBRARY = "GoogleTest"
$LIBRARY_VERSION = "1.16.0"
$EXTRACTED_DIR_NAME = "googletest-${LIBRARY_VERSION}"
$DOWNLOAD_URL = "https://github.com/google/googletest/archive/refs/tags/v${LIBRARY_VERSION}.zip"
$ARCHIVE_NAME = "v${LIBRARY_VERSION}.zip"

$BASE_LIBRARY_PATH = Join-Path -Path $BASE_PATH -ChildPath "$NAME_LIBRARY"

New-Item -ItemType Directory -Path $BASE_LIBRARY_PATH -Force
Set-Location -Path $BASE_LIBRARY_PATH

$ZIP_PATH = Join-Path -Path $BASE_LIBRARY_PATH -ChildPath $ARCHIVE_NAME
Invoke-WebRequest -Uri $DOWNLOAD_URL -OutFile $ZIP_PATH

# Ajouter la capacité de décompresser des fichiers ZIP
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($ZIP_PATH, $BASE_LIBRARY_PATH)

# Renommer le répertoire extrait pour qu'il corresponde à la version de la bibliothèque
$OLD_DIR = Join-Path -Path $BASE_LIBRARY_PATH -ChildPath $EXTRACTED_DIR_NAME
Rename-Item -Path $OLD_DIR -NewName ($LIBRARY_VERSION)

# Supprimer l'archive ZIP une fois qu'elle n'est plus nécessaire
Remove-Item -Path $ZIP_PATH

$VERSION_LIBRARY_PATH = Join-Path -Path $BASE_LIBRARY_PATH -ChildPath "$LIBRARY_VERSION"

function BuildAndInstallLibrary($build_directory, $config, $sharedLibs) {
    $directory = Join-Path -Path $VERSION_LIBRARY_PATH -ChildPath $build_directory
    # Créer un répertoire pour la construction
    New-Item -ItemType Directory -Path $directory -Force
    Set-Location -Path $directory

    # Exécuter les commandes CMake pour configurer, compiler et installer la bibliothèque
    $cmakeArgs = @(
        "..",
        "-DCMAKE_INSTALL_PREFIX=${VERSION_LIBRARY_PATH}",
        "-DCMAKE_BUILD_TYPE=$config",
        "-DBUILD_SHARED_LIBS=$sharedLibs",
        "-Dgtest_force_shared_crt=$sharedLibs"
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
cmake_minimum_required(VERSION 3.26)  
project(Google_Test CXX)  
set(CMAKE_CXX_STANDARD 23)  
  
SET(USE_DYNAMIC_GTEST OFF)  
MESSAGE("Type: ${CMAKE_BUILD_TYPE}")  
set(GTEST_BASE_PATH "D:/Coding/Frameworks/googletest/1.16.0")  
  
# Set the CMake prefix path to the install directory of GoogleTest  
list(APPEND CMAKE_PREFIX_PATH ${GTEST_BASE_PATH})  
include_directories("${GTEST_BASE_PATH}/include")  
# Find the GoogleTest package  
find_package(GTest REQUIRED)  
  
if (NOT USE_DYNAMIC_GTEST)  
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")  
endif ()  
  
add_executable(Google_Test main.cpp)  
  
if (USE_DYNAMIC_GTEST)  
    MESSAGE("Dynamic GTest")  
    MESSAGE("Link: Dynamic (DLL)")  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        set(GTEST_DLL_PATH "${GTEST_BASE_PATH}/build_debug_dll/bin/Debug")  
    else ()  
        set(GTEST_DLL_PATH "${GTEST_BASE_PATH}/build_release_dll/bin/Release")  
    endif ()  
  
    set(DLL_DEST_DIR ${CMAKE_BINARY_DIR})  
    MESSAGE("Copy the DLLs to the executable directory : ${DLL_DEST_DIR}")  
    file(GLOB GTEST_DLLS "${GTEST_DLL_PATH}/*.dll")  
    foreach (DLL ${GTEST_DLLS})  
        get_filename_component(DLL_NAME ${DLL} NAME)  
        MESSAGE("DLL : ${DLL_NAME}")  
        MESSAGE("SOURCE : ${GTEST_DLL_PATH}")  
        MESSAGE("DEST : ${DLL_DEST_DIR}")  
  
        configure_file("${GTEST_DLL_PATH}/${DLL_NAME}" "${DLL_DEST_DIR}/${DLL_NAME}" COPYONLY)  
    endforeach ()  
  
    target_link_libraries(Google_Test PRIVATE GTest::gtest GTest::gtest_main GTest::gmock GTest::gmock_main)  
else ()  
    MESSAGE("Static GTest")  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        MESSAGE("PASS HERE")  
        SET(GTEST_LIB_DEBUG_LIB_PATH "${GTEST_BASE_PATH}/build_debug/lib/Debug/")  
        target_link_libraries(Google_Test PRIVATE  
                "${GTEST_LIB_DEBUG_LIB_PATH}gtest.lib"  
                "${GTEST_LIB_DEBUG_LIB_PATH}gtest_main.lib"  
                "${GTEST_LIB_DEBUG_LIB_PATH}gmock.lib"  
                "${GTEST_LIB_DEBUG_LIB_PATH}gmock_main.lib")  
    else ()  
        SET(GTEST_LIB_RELEASE_LIB_PATH "${GTEST_BASE_PATH}/build_release/lib/Release/")  
        target_link_libraries(Google_Test PRIVATE  
                "${GTEST_LIB_RELEASE_LIB_PATH}gtest.lib"  
                "${GTEST_LIB_RELEASE_LIB_PATH}gtest_main.lib"  
                "${GTEST_LIB_RELEASE_LIB_PATH}gmock.lib"  
                "${GTEST_LIB_RELEASE_LIB_PATH}gmock_main.lib")  
    endif ()  
endif ()
```
## Linux

### Install Script 
```sh
#!/bin/bash
# -------------------------------------------------------------------------------
# Installation automatisée de GoogleTest 1.16.0 sur Debian / Ubuntu
# -------------------------------------------------------------------------------

# 1. Mise à jour du système et installation des dépendances indispensables
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential cmake ninja-build unzip wget

# 2. Définition des variables liées à GoogleTest 1.16.0
ROOT_PATH="/opt/gtest"                       # Dossier racine pour toutes les versions de GoogleTest
LIBRARY_VERSION="1.16.0"                     # Version x.y.z officielle
ARCHIVE_NAME="v${LIBRARY_VERSION}.zip"       # Nom de l’archive téléchargée
LIBRARY_NAME_SUB_GTEST="googletest-${LIBRARY_VERSION}" # Nom du dossier interne dans l’archive
DOWNLOAD_URL="https://github.com/google/googletest/archive/refs/tags/${ARCHIVE_NAME}"
INSTALL_PREFIX="${ROOT_PATH}/${LIBRARY_VERSION}"        # Préfixe d’installation isolée

# 3. Création (ou vérification) du répertoire racine puis déplacement
sudo mkdir -p "${ROOT_PATH}"
cd "${ROOT_PATH}" || { echo "Erreur : impossible d’accéder à ${ROOT_PATH}" >&2; exit 1; }

# 4. Téléchargement de l’archive GoogleTest 1.16.0
wget "${DOWNLOAD_URL}"

# 5. Nettoyage d’une éventuelle installation précédente
sudo rm -rf "${LIBRARY_VERSION}"

# 6. Extraction de l’archive ZIP
unzip "${ARCHIVE_NAME}"

# 7. Renommage du dossier extrait pour refléter directement la version
mv "${LIBRARY_NAME_SUB_GTEST}" "${LIBRARY_VERSION}"

# 8. Suppression de l’archive pour libérer de l’espace
rm "${ARCHIVE_NAME}"

# 9. Passage dans le dossier source de GoogleTest
cd "${LIBRARY_VERSION}" || { echo "Erreur : impossible d’accéder à ${LIBRARY_VERSION}" >&2; exit 1; }

# 10. Options CMake communes
CMAKE_BASE_OPTIONS="-DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX} -DBUILD_GMOCK=ON"

# 11. Compilation — quatre variantes
#     * Debug   statique
#     * Release statique
#     * Debug   partagée
#     * Release partagée

# 11-a Debug statique
mkdir build_debug && cd build_debug
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Debug   -DBUILD_SHARED_LIBS=OFF
cmake --build . --config Debug
cmake --install . --config Debug
cd ..

# 11-b Release statique
mkdir build_release && cd build_release
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF
cmake --build . --config Release
cmake --install . --config Release
cd ..

# 11-c Debug partagée
mkdir build_debug_so && cd build_debug_so
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Debug   -DBUILD_SHARED_LIBS=ON
cmake --build . --config Debug
cmake --install . --config Debug
cd ..

# 11-d Release partagée
mkdir build_release_so && cd build_release_so
cmake .. ${CMAKE_BASE_OPTIONS} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON
cmake --build . --config Release
cmake --install . --config Release
cd ..

# -------------------------------------------------------------------------------
# Fin de l’installation de GoogleTest 1.16.0
#     • Bibliothèques statiques et partagées disponibles sous : ${INSTALL_PREFIX}
# -------------------------------------------------------------------------------
```
### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.26)  
project(Google_Test CXX)  
set(CMAKE_CXX_STANDARD 23)  
  
SET(USE_DYNAMIC_GTEST ON)  
MESSAGE("Type: ${CMAKE_BUILD_TYPE}")  
set(GTEST_BASE_PATH "/opt/gtest/1.16.0")  
  
# Set the CMake prefix path to the install directory of GoogleTest  
list(APPEND CMAKE_PREFIX_PATH ${GTEST_BASE_PATH})  
include_directories("${GTEST_BASE_PATH}/include")  
# Find the GoogleTest package  
find_package(GTest REQUIRED)  
  
add_executable(Google_Test main.cpp)  
  
if (USE_DYNAMIC_GTEST)  
    MESSAGE("Dynamic GTest")  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        set(GTEST_SO_PATH "${GTEST_BASE_PATH}/build_debug_so/lib")  
    else ()  
        set(GTEST_SO_PATH "${GTEST_BASE_PATH}/build_release_so/lib")  
    endif ()  
  
    set(SO_DEST_DIR ${CMAKE_BINARY_DIR})  
    MESSAGE("Copy the SOs to the executable directory : ${SO_DEST_DIR}")  
    file(GLOB GTEST_SOS "${GTEST_SO_PATH}/*.so")  
    foreach (SO ${GTEST_SOS})  
        get_filename_component(SO_NAME ${SO} NAME)  
        MESSAGE("SO : ${SO_NAME}")  
        MESSAGE("SOURCE : ${GTEST_SO_PATH}")  
        MESSAGE("DEST : ${SO_DEST_DIR}")  
  
        configure_file("${GTEST_SO_PATH}/${SO_NAME}" "${SO_DEST_DIR}/${SO_NAME}" COPYONLY)  
    endforeach ()  
  
    target_link_libraries(Google_Test PRIVATE GTest::gtest GTest::gtest_main GTest::gmock GTest::gmock_main)  
else ()  
    MESSAGE("Static GTest")  
    if (CMAKE_BUILD_TYPE STREQUAL "Debug")  
        MESSAGE("PASS HERE")  
        SET(GTEST_LIB_DEBUG_A_PATH "${GTEST_BASE_PATH}/build_debug/lib/")  
        target_link_libraries(Google_Test PRIVATE  
                "${GTEST_LIB_DEBUG_A_PATH}libgtest.a"  
                "${GTEST_LIB_DEBUG_A_PATH}libgtest_main.a"  
                "${GTEST_LIB_DEBUG_A_PATH}libgmock.a"  
                "${GTEST_LIB_DEBUG_A_PATH}libgmock_main.a")  
    else ()  
        SET(GTEST_LIB_RELEASE_A_PATH "${GTEST_BASE_PATH}/build_release/lib/")  
        target_link_libraries(Google_Test PRIVATE  
                "${GTEST_LIB_DEBUG_A_PATH}libgtest.a"  
                "${GTEST_LIB_DEBUG_A_PATH}libgtest_main.a"  
                "${GTEST_LIB_DEBUG_A_PATH}libgmock.a"  
                "${GTEST_LIB_DEBUG_A_PATH}libgmock_main.a")  
    endif ()  
endif ()
```
## Test
```cpp
#include <gtest/gtest.h>  
#include <gmock/gmock.h>  
  
// Mock class  
class MockDatabase {  
public:  
    MOCK_METHOD(void, Save, (int), ());  
    MOCK_METHOD(int, Load, (), ());  
};  
  
// Actual class that you want to test  
class MyService {  
public:  
    MyService(MockDatabase& db) : db(db) {}  
  
    void DoSave(int data) {  
        db.Save(data);  
    }  
    int DoLoad() {  
        return db.Load();  
    }  
private:  
    MockDatabase& db;  
};  
  
// Test cases  
TEST(MyServiceTest, SaveTest) {  
    MockDatabase mockDb;  
    MyService service(mockDb);  
  
    // Expectations  
    EXPECT_CALL(mockDb, Save(42)).Times(1);  
  
    // Actual call  
    service.DoSave(42);  
}  
  
TEST(MyServiceTest, LoadTest) {  
    MockDatabase mockDb;  
    MyService service(mockDb);  
  
    // Stubbing  
    ON_CALL(mockDb, Load()).WillByDefault(::testing::Return(42));  
  
    // Expectations  
    EXPECT_CALL(mockDb, Load()).Times(1);  
  
    // Actual call  
    int result = service.DoLoad();  
  
    // Assertion  
    ASSERT_EQ(42, result);  
}  
  
int main(int argc, char** argv) {  
    ::testing::InitGoogleMock(&argc, argv);  
    return RUN_ALL_TESTS();  
}
```