@echo off

set "a=0"
set "mainFile=main.bat"

:loop
setlocal enabledelayedexpansion

set /p "mainContent="<"%mainFile%"

echo !mainContent!>"!a!.bat"

set /a "a+=1"

goto :loop
