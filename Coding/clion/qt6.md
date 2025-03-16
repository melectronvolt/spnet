# QT6 😺

```{image} ../../_static/_medias/coding/clion/qtlogo.png
:width: 600px
:align: center
:class: vspace
```

```{caution}
La première version de ce tutorial a été fait pour QT 6.5.2, je l’ai mis à jour pour 6.6.0 mais n’ai pas réenregistré les screenshots.
```

## Description
- **Origine** 🌱
    **Qt** est un framework de développement logiciel libre et open source, initialement développé par Trolltech en 1995, et qui a été racheté par Nokia, puis par Digia, qui est devenue par la suite The Qt Company.
- **Finalité** 🎯
    Qt est principalement utilisé pour développer des applications avec une interface graphique (GUI), mais il est aussi très adapté pour le développement d'applications sans GUI. Il est célèbre pour son mécanisme de signaux et slots et pour son framework d'événements.
- **Plateformes supportées** 🌍
    Une des grandes forces de Qt est sa capacité à être multiplateforme. Avec Qt, vous pouvez écrire une application une fois, puis la compiler et l'exécuter sur de multiples plateformes, telles que Windows, macOS, Linux, Android, iOS, et bien d'autres.
- **Modules** 🧩
    Qt est organisé en différents modules. Certains des modules les plus populaires sont : QtCore (pour les fonctionnalités non-GUI de base), QtGui (fonctionnalités GUI de base), QtWidgets (widgets pour les applications de bureau), QtNetwork (fonctionnalités réseau), et bien d'autres.
- **Qt Quick et QML** 🚀
    À partir de Qt 5, et renforcé dans Qt 6, Qt propose Qt Quick, un moyen de créer des interfaces utilisateur fluides et animées en utilisant le langage de déclaration QML. C'est particulièrement utile pour les applications mobiles et les appareils embarqués.
- **Licence** 📜
    Qt est disponible sous différentes licences, dont la LGPL et la GPL, qui sont des licences open source, ainsi qu'une licence commerciale qui offre des avantages supplémentaires et une plus grande flexibilité, en particulier pour ceux qui ne veulent pas se conformer aux obligations des licences open source.
- **Outils associés** 🛠️
    Qt vient avec plusieurs outils pour faciliter le développement, comme Qt Creator (un environnement de développement intégré), l'outil de conception d'interfaces (Qt Designer), et d'autres utilitaires pour la traduction, l'accès aux bases de données, et plus encore.
- **Évolution vers Qt 6** ⏫
    Qt 6, en tant que successeur de Qt 5, introduit de nombreuses améliorations, refactorisations et nouvelles fonctionnalités tout en supprimant certaines anciennes pour moderniser le framework. Il mise fortement sur l'amélioration de l'efficacité, l'intégration 3D, et la facilité d'utilisation pour les développeurs.

En résumé, Qt 6 est un framework puissant et polyvalent qui peut être utilisé pour développer des applications multiplateformes de haute qualité, qu'il s'agisse d'applications de bureau, mobiles, embarquées, ou même pour le web avec WebAssembly. C'est une solution de choix pour les développeurs cherchant à maximiser la portabilité et la réutilisabilité de leur code. 🌟🖥️📱
### Remarques sur les obligations concernant l’open source
- Lire la page [https://www.qt.io/licensing/open-source-lgpl-obligations](https://www.qt.io/licensing/open-source-lgpl-obligations)
Avec la licence LGPL, vous pouvez utiliser les bibliothèques essentielles et certaines supplémentaires de Qt tout en gardant le code source de votre application fermé, tant que toutes les exigences de LGPLv3 sont respectées. La page mentionne également les quatre libertés fournies par la licence LGPL, notamment la liberté d'exécuter, d'étudier, de redistribuer et d'améliorer le programme.

```{admonition} Linkage Dynamic
On choisira pour ne pas avoir de problème un linkage dynamique (DLL ou SO)
```


On notera :
	- Fournir un mécanisme de re-linking pour les bibliothèques Qt (utilisation de DLL)
	- Fournir une copie de la licence et reconnaître explicitement l'utilisation de Qt
	- Mettre à disposition une copie du code source de Qt pour les clients
	- Accepter que les modifications du code source Qt ne sont pas propriétaires
	- Créer des appareils "ouverts" pour les consommateurs
	- Accepter les termes de la Gestion des Droits Numériques, veuillez consulter la FAQ GPL
	- Prendre en considération lors de la tentative d'application des brevets logiciels, voir la FAQ
## Installation sur Windows
- S’inscrire en tant qu’utilisateur souhaitant utilisant la version opensource [https://www.qt.io/download-open-source](https://www.qt.io/download-open-source)
- Se rendre ici pour télécharger le logiciel [https://www.qt.io/download-qt-installer-oss](https://www.qt.io/download-qt-installer-oss)

```{image} ../../_static/_medias/coding/clion/qt/maintainqt.png
:width: 600px
:align: center
:class: vspace
```

```{image} ../../_static/_medias/coding/clion/qt/installqt.png
:width: 600px
:align: center
:class: vspace
```


- Installer le logiciel (dans mon cas `F:\Frameworks\Qt`)
- Vous pourrez ensuite tout gérer (installation/maj) avec l’application `MaintenanceTool.exe`

### Utilisation
#### CMakeList
```cpp
cmake_minimum_required(VERSION 3.25)  
project(QT_HelloWorld)  
  
set(CMAKE_CXX_STANDARD 23)  
  
# Tell cmake where Qt is located  
set(QT_PREFIX_PATH "F:/Frameworks/Qt/6.6.0/msvc2019_64")  
list(APPEND CMAKE_PREFIX_PATH ${QT_PREFIX_PATH})  
  
  
# Tell cmake to find the modules Qt5Core and Qt6widgets  
find_package(Qt6 COMPONENTS Core Widgets REQUIRED)  
  
# WIN32 is important to avoid the console windows  
add_executable(QT_HelloWorld WIN32 main.cpp)  
  
# Link the library to the executable  
target_link_libraries(QT_HelloWorld Qt6::Core Qt6::Widgets)  
  
# Before building, delete all DLLs from the output directory  
add_custom_command(TARGET QT_HelloWorld PRE_BUILD  
    COMMAND ${CMAKE_COMMAND} -E remove_directory "${CMAKE_BINARY_DIR}/*.dll"  
    MESSAGE( "Deleting old DLLs...")  
)  
  
# After building the project, deploy the necessary DLLs to the output directory  
set(QT_EXECUTABLE ${CMAKE_BINARY_DIR})  
  
add_custom_command(TARGET QT_HelloWorld POST_BUILD  
    COMMAND "${QT_PREFIX_PATH}/bin/windeployqt.exe" ARGS ${QT_EXECUTABLE}  
    COMMENT "Deploying Qt dependencies..."  
)
```
#### Test app
```cpp
#include <QApplication>
#include <QPushButton>

int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    QPushButton button("Bonjour Rémi !");
    button.setFixedSize(400, 100);
    button.show();
    return app.exec();
}
```
En principe tout fonctionne et vous devriez voir une fenêtre s’ouvrir :

```{image} ../../_static/_medias/coding/clion/qt/hwqt.png
:width: 600px
:align: center
:class: vspace
```

> [!NOTE] Unicode
> Comme vous le remarquez, QT gère l’unicode convenablement, cependant je vous invite sous windows à ajouter le BOM. (BOM, ou Byte Order Mark, est un caractère Unicode utilisé pour signaler l'ordre des octets (endianness) dans un texte codé en UTF-16 ou UTF-32)

```{image} ../../_static/_medias/coding/clion/qt/utf1.png
:width: 600px
:align: center
:class: vspace
```

```{image} ../../_static/_medias/coding/clion/qt/utf2.png
:width: 200px
:align: center
:class: vspace
```


## Installation sur Linux
- S’inscrire en tant qu’utilisateur souhaitant utilisant la version opensource [https://www.qt.io/download-open-source](https://www.qt.io/download-open-source)
- Se rendre ici pour télécharger le logiciel [https://www.qt.io/download-qt-installer-oss](https://www.qt.io/download-qt-installer-oss)

```bash
sudo apt-get install libxcb-xinerama0
chmod +x ./qt-unified-linux-x64-4.6.1-online.run
./qt-unified-linux-x64-4.6.1-online.run
sudo apt-get update libgl1-mesa-dev libxcb-cursor0
```

```{image} ../../_static/_medias/coding/clion/qt/maintainqt.png
:width: 600px
:align: center
:class: vspace
```

```{image} ../../_static/_medias/coding/clion/qt/installqt.png
:width: 600px
:align: center
:class: vspace
```

- Installer le logiciel (dans mon cas `/home/remi/Frameworks/Qt`)
### Utilisation
#### CMakeList
```cpp
cmake_minimum_required(VERSION 3.25)  
project(QT_HelloWorld)  
  
set(CMAKE_CXX_STANDARD 23)  
  
# Tell cmake where Qt is located  
list(APPEND CMAKE_PREFIX_PATH "/home/remi/Frameworks/Qt/6.6.0/gcc_64/")  
  
find_package(Qt6 COMPONENTS Core Widgets REQUIRED)  

add_executable(QT_HelloWorld main.cpp)  
  
# Link the library to the executable  
target_link_libraries(QT_HelloWorld Qt6::Core Qt6::Widgets)

# Before building, delete all .so files from the output directory
add_custom_command(TARGET QT_HelloWorld PRE_BUILD
    COMMAND ${CMAKE_COMMAND} -E remove "${CMAKE_CURRENT_BINARY_DIR}/*.so"
    COMMENT "Deleting old .so files..."
)

add_custom_command(TARGET QT_HelloWorld POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CMAKE_PREFIX_PATH}/lib/libQt6Core.so"
        "${CMAKE_CURRENT_BINARY_DIR}"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CMAKE_PREFIX_PATH}/lib/libQt6Widgets.so"
        "${CMAKE_CURRENT_BINARY_DIR}"
)
```
#### Test app
```cpp
#include <QApplication>
#include <QPushButton>

int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    QPushButton button("Bonjour Rémi !");
    button.setFixedSize(400, 100);
    button.show();
    return app.exec();
}
```

```{image} ../../_static/_medias/coding/clion/qt/hwqtl.png
:width: 600px
:align: center
:class: vspace
```

## Autres petites choses utiles

Dans les paramètres :
```{image} ../../_static/_medias/coding/clion/qt/param.png
:width: 600px
:align: center
:class: vspace
```
On ajoute les outils : 
```{image} ../../_static/_medias/coding/clion/qt/tool.png
:width: 500px
:align: center
:class: vspace
```

Name : `QT Creator`
Program : `C:\Qt\Tools\QtCreator\bin\qtcreator.exe`
Arguments : `$FilePath$`
Working Directory : `C:\Qt\Tools\QtCreator\bin`

Name : `QT Designer`
Program : `C:\Qt\Tools\QtDesignStudio\qt6_design_studio_reduced_version\bin\designer.exe`
Arguments : `$FilePath$`
Working Directory : `C:\Qt\Tools\QtDesignStudio\qt6_design_studio_reduced_version\bin`

Name : `QT Design Studio`
Program : `C:\Qt\Tools\QtDesignStudio\bin\qtdesignstudio.exe`
Arguments : `$FilePath$`
Working Directory : `C:\Qt\Tools\QtDesignStudio\bin`

```{image} ../../_static/_medias/coding/clion/qt/menu.png
:width: 600px
:align: center
:class: vspace
```

## Static build of QT 6

```{image} ../../_static/_medias/coding/clion/qt/sources.png
:width: 600px
:align: center
:class: vspace
```

- Soyez certain d’installer les sources dans l’installateur de QT. Elles seront nécessaire pour la compilation.
- En principe CMake est installé sur votre ordinateur sinon rendez-vous sur le site web [cmake.org](https://cmake.org)

```{image} ../../_static/_medias/coding/clion/qt/cmake.png
:width: 300px
:align: center
:class: vspace
```

- Ninja doit aussi être installé, vous le trouverez dans les outils de l'installateur

```{image} ../../_static/_medias/coding/clion/qt/otherinstall.png
:width: 600px
:align: center
:class: vspace
```

### Modifier l’environnement pour permettre la compilation (C++ ATL)

```{image} ../../_static/_medias/coding/clion/qt/atl.png
:width: 700px
:align: center
:class: vspace
```

```powershell
CALL "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x64
SET _ROOT=F:\Frameworks\Qt\6.7.2\Src
SET _NINJA=F:\Frameworks\Qt\Tools\Ninja
SET PATH=%_ROOT%;%_NINJA%;%PATH%
```
### Compilation static simple
```powershell
configure -debug-and-release -opensource -static -platform win32-msvc -nomake examples -nomake tests -prefix F:\Frameworks\Qt\6.7.2\static
cmake --build . --parallel
ninja install
```

```cmake
cmake_minimum_required(VERSION 3.25)
project(QT_HelloWorld)

# Tell cmake where Qt is located
set(QT_PREFIX_PATH "F:/Frameworks/Qt/6.7.0/static")
list(APPEND CMAKE_PREFIX_PATH ${QT_PREFIX_PATH})

# Tell cmake to find the modules Qt5Core and Qt6widgets
find_package(Qt6 COMPONENTS Core Widgets REQUIRED)

# WIN32 is important to avoid the console windows
add_executable(QT_HelloWorld WIN32 main.cpp)

# Link the library to the executable
target_link_libraries(QT_HelloWorld Qt6::Core Qt6::Widgets)
```

### Compilation static avec Link Time Optimization

```powershell
configure -debug-and-release -opensource -static -ltcg -platform win32-msvc -nomake examples -nomake tests -prefix F:\Frameworks\Qt\6.7.2\staticLTO
cmake --build . --parallel
ninja install
```

```cmake
cmake_minimum_required(VERSION 3.25)
project(QT_HelloWorld)

# Tell cmake where Qt is located
set(QT_PREFIX_PATH "F:/Frameworks/Qt/6.7.0/staticLTO")
list(APPEND CMAKE_PREFIX_PATH ${QT_PREFIX_PATH})

# Tell cmake to find the modules Qt5Core and Qt6widgets
find_package(Qt6 COMPONENTS Core Widgets REQUIRED)

# WIN32 is important to avoid the console windows
add_executable(QT_HelloWorld WIN32 main.cpp)
set_property(TARGET QT_HelloWorld PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)

# Link the library to the executable
target_link_libraries(QT_HelloWorld Qt6::Core Qt6::Widgets)
```
## Sources et remerciements
- [Documentation Jetbrains - CMake - QT](https://www.jetbrains.com/help/clion/qt-tutorial.html#cmake-settings)
- [Setup QT with Clion Easily from Aloïs Micard](https://blog.creekorful.org/2019/08/setup-qt-with-clion-easily/)