@echo off
setlocal enabledelayedexpansion

for %%f in (*.*) do (
    set "filename=%%~nf"
    set "extension=%%~xf"
    rem Remove (Z-Lib.io) from the filename, Remove filename Zlib Z-lib.bat
    set "newname=!filename:(Z-Lib.io)=!!extension!"
    ren "%%f" "!newname!"
)

endlocal
pause
