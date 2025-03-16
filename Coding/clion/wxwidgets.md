# wxWidgets 🖼️

```{image} ../../_static/_medias/coding/clion/wxwidgetslogo.png
:width: 300px
:align: center
:class: vspace
```

## Description
- **Origine** 🌱 
	**wxWidgets** est une bibliothèque C++ mature et complète qui permet aux développeurs de créer des applications natives pour Windows, Mac, Linux et d'autres plateformes avec une seule base de code. Elle a été conçue pour offrir une approche portable à la création d'interfaces utilisateur (GUI).
- **Portabilité** 🌍
	L'un des principaux avantages de wxWidgets est sa portabilité. Écrivez votre code une fois, puis compilez-le pour différentes plateformes, tout en conservant l'apparence et le comportement natifs de chaque système.
- **Riche en Composants** 🛠️
    wxWidgets propose une vaste gamme de composants pré-conçus, tels que des boutons, des listes, des boîtes de dialogue, des menus et plus encore. Cette richesse de composants facilite la création d'applications interactives et fonctionnelles.
- **Aspect Natif** 👁️
    Les applications développées avec wxWidgets ont une apparence native sur chaque plateforme, car la bibliothèque utilise les contrôles natifs du système d'exploitation sous-jacent.
- **Extensibilité** 
    Au-delà des widgets standard, wxWidgets est extensible, permettant aux développeurs de créer leurs propres widgets personnalisés pour répondre à des besoins spécifiques.
- **Intégration des Systèmes** 🔄
    wxWidgets offre également des fonctionnalités pour intégrer des éléments non GUI, tels que le travail avec des fichiers, des threads, des bases de données, des réseaux et plus encore.
- **Licence** 📜
    wxWidgets est distribué sous une licence de type "LGPL avec exception", ce qui permet de l'utiliser gratuitement, même pour des applications commerciales, sans avoir à rendre votre code source public.
- **Communauté** 💬
    La bibliothèque est soutenue par une communauté active qui contribue à son développement depuis des décennies. Cela garantit non seulement un support continu, mais aussi une richesse de ressources, de tutoriels et de forums pour aider les nouveaux venus.
- **Documentation** 📖
    wxWidgets est accompagné d'une documentation complète, aidant les développeurs à comprendre rapidement ses fonctionnalités et à démarrer leurs projets.
- **Performances et Sécurité** 🔐
    wxWidgets est optimisé pour offrir de bonnes performances, et étant donné sa maturité, beaucoup de ses éventuelles failles ont été identifiées et corrigées au fil des ans.

En conclusion, wxWidgets est une solution robuste et éprouvée pour le développement d'applications GUI en C++. Sa capacité à produire des applications au look natif sur plusieurs plateformes avec un seul code source en fait un choix populaire parmi les développeurs C++ qui cherchent à maximiser la portabilité et la ré-utilisabilité de leur code. 🌐🖼️🖥️👥

```bash
$BASE_PATH = "D:\Coding\Frameworks"
$NAME_LIBRARY = "wxWidgets"
$DOWNLOAD_URL = "https://github.com/wxWidgets/wxWidgets.git"
$BASE_LIBRARY_PATH = Join-Path -Path $BASE_PATH -ChildPath $NAME_LIBRARY

# Clone wxWidgets repository with submodules
Set-Location -Path $BASE_PATH
git clone --recurse-submodules $DOWNLOAD_URL

Set-Location -Path $BASE_LIBRARY_PATH

# Create a build directory for CMake
mkdir build-cmake
cd build-cmake

# 🔧 Force a static build
cmake .. -DCMAKE_INSTALL_PREFIX="${BASE_LIBRARY_PATH}" -DwxBUILD_SHARED=OFF -DwxUSE_UNICODE=ON

# Build wxWidgets in Release mode
cmake --build . --config Release
cmake --install . --config Release

# Build wxWidgets in Debug mode
cmake --build . --config Debug
cmake --install . --config Debug
```

And for using

```cmake
cmake_minimum_required(VERSION 3.26)
project(WxWidgets_testing)
set(CMAKE_CXX_STANDARD 23)

set(wxWidgets_USE_STATIC ON)
list(APPEND CMAKE_PREFIX_PATH "D:/Coding/Frameworks/wxWidgets")

find_package(wxWidgets REQUIRED COMPONENTS core base)
include(${wxWidgets_USE_FILE})

add_executable(WxWidgets_testing WIN32 main.cpp)
target_link_libraries(WxWidgets_testing ${wxWidgets_LIBRARIES})
```

> [!WARNING] Copie de DLL
> Il faudra copier une tonne de DLL si vous ne compilez pas en static.

# Test
```cpp
#include <wx/wx.h>

// Définir une nouvelle classe d'application
class MyApp : public wxApp
{
public:
    virtual bool OnInit();
};

// Définir une nouvelle classe de frame (fenêtre)
class MyFrame : public wxFrame
{
public:
    MyFrame(const wxString& title);

    // Evénement pour la fermeture de la fenêtre
    void OnQuit(wxCommandEvent& event);
};

// Implementer l'application
wxIMPLEMENT_APP(MyApp);

bool MyApp::OnInit()
{
    MyFrame *frame = new MyFrame("Hello World using wxWidgets!");
    frame->Show(true);
    return true;
}

MyFrame::MyFrame(const wxString& title)
    : wxFrame(NULL, wxID_ANY, title, wxDefaultPosition, wxSize(250, 150))
{
    // Créer un menu
    wxMenu *menuFile = new wxMenu;
    menuFile->Append(wxID_EXIT, "&Quit");
    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append(menuFile, "&File");
    SetMenuBar(menuBar);

    // Connecter l'événement de fermeture
    Connect(wxID_EXIT, wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler(MyFrame::OnQuit));

    // Afficher un message statique au centre
    wxPanel *panel = new wxPanel(this, wxID_ANY);
    wxBoxSizer *sizer = new wxBoxSizer(wxVERTICAL);
    panel->SetSizer(sizer);
    wxStaticText *text = new wxStaticText(panel, wxID_ANY, "Hello World!", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER);
    sizer->Add(text, 0, wxALL | wxEXPAND, 20);
}

void MyFrame::OnQuit(wxCommandEvent& event)
{
    Close(true);
}

```