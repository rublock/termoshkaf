@echo off
setlocal

rem
set "SCRIPT_DIR=%~dp0"

start /B "MyApp" "%SCRIPT_DIR%venv\Scripts\pythonw.exe" "%SCRIPT_DIR%window.py"

endlocal
