@echo off
chcp 65001 > nul
title ABC Importer Tool - Uninstall Script

echo ABC Importer Tool - Uninstall Script
echo.

:VERSION_INPUT
set "HOUDINI_VERSION="
set /p HOUDINI_VERSION="Please enter your Houdini version (e.g. 20.0): "

if "%HOUDINI_VERSION%"=="" (
    echo Error: Version number cannot be empty
    echo.
    goto VERSION_INPUT
)

set "HOUDINI_PATH=%USERPROFILE%\Documents\houdini%HOUDINI_VERSION%"

echo.
echo Uninstalling from: %HOUDINI_PATH%
echo.

echo Removing files...

if exist "%HOUDINI_PATH%\python\abc_importer.py" (
    del /F /Q "%HOUDINI_PATH%\python\abc_importer.py"
    echo Removed: abc_importer.py
)

if exist "%HOUDINI_PATH%\toolbar\default.shelf" (
    del /F /Q "%HOUDINI_PATH%\toolbar\default.shelf"
    echo Removed: default.shelf
)

if exist "%HOUDINI_PATH%\packages\abc_importer.json" (
    del /F /Q "%HOUDINI_PATH%\packages\abc_importer.json"
    echo Removed: abc_importer.json
)

echo.
echo Cleaning up empty directories...

for %%D in (python toolbar packages) do (
    dir /b /a "%HOUDINI_PATH%\%%D\*" >nul 2>nul || (
        rmdir "%HOUDINI_PATH%\%%D" 2>nul && echo Removed empty directory: %%D
    )
)

echo.
echo Uninstallation complete!
echo Please restart Houdini for the changes to take effect.
echo.

pause
