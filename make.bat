@ECHO OFF
pushd %~dp0

REM Command file for Sphinx documentation with uv
REM Usage: make.bat [command]

set SOURCEDIR=.
set BUILDDIR=_build

REM Commandes personnalisées pour uv
if "%1" == "serve" goto serve
if "%1" == "watch" goto watch
if "%1" == "install" goto install

REM Commandes Sphinx standard
if "%1" == "" goto help
uv run sphinx-build -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
echo.Commandes Sphinx standard:
echo.  make.bat html       - Construire la documentation HTML
echo.  make.bat clean      - Nettoyer les fichiers generes
echo.  make.bat linkcheck  - Verifier les liens
echo.  make.bat help       - Afficher l'aide Sphinx complete
echo.
echo.Commandes supplementaires avec uv:
echo.  make.bat install    - Installer les dependances
echo.  make.bat serve      - Serveur avec livereload
echo.  make.bat watch      - Serveur avec auto-rebuild
echo.
echo.Pour plus d'options Sphinx:
uv run sphinx-build -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:install
echo.Installation des dependances avec uv...
uv sync
echo.Installation terminee!
goto end

:serve
echo.Demarrage du serveur livereload...
echo.Ouvrez http://localhost:5500 dans votre navigateur
echo.Appuyez sur Ctrl+C pour arreter
uv run python -m livereload %SOURCEDIR%
goto end

:watch
echo.Demarrage du serveur avec auto-rebuild...
uv run sphinx-autobuild %SOURCEDIR% %BUILDDIR%/html --open-browser
goto end

:end
popd