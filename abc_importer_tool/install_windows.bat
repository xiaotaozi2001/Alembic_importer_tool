@echo off
chcp 65001 > nul
echo ABC Importer Tool - Windows Installation Script
echo.

set /p HOUDINI_VERSION="Please enter your Houdini version (e.g. 20.0): "

if "%HOUDINI_VERSION%"=="" (
    echo Error: Version number cannot be empty
    pause
    exit /b 1
)

set "USERPROFILE=%USERPROFILE%"
set "HOUDINI_PATH=%USERPROFILE%\Documents\houdini%HOUDINI_VERSION%"

echo.
echo Installing to: %HOUDINI_PATH%
echo.

echo Creating directories...
if not exist "%HOUDINI_PATH%" mkdir "%HOUDINI_PATH%"
if not exist "%HOUDINI_PATH%\python" mkdir "%HOUDINI_PATH%\python"
if not exist "%HOUDINI_PATH%\toolbar" mkdir "%HOUDINI_PATH%\toolbar"
if not exist "%HOUDINI_PATH%\packages" mkdir "%HOUDINI_PATH%\packages"

echo Copying files...
copy /Y "%~dp0python\abc_importer.py" "%HOUDINI_PATH%\python\"
copy /Y "%~dp0toolbar\default.shelf" "%HOUDINI_PATH%\toolbar\"
copy /Y "%~dp0packages\abc_importer.json" "%HOUDINI_PATH%\packages\"

echo.
echo Installation complete!
echo Please restart Houdini to use the ABC Importer tool.
echo The tool will be available in the shelf toolbar.
echo.
pause
