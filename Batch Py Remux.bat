@ECHO off
SETLOCAL ENABLEDELAYEDEXPANSION

Title Batch Py Remux

set pth=
set /p "pth=Enter path to folder containing mkv files, or press Enter if current folder: "

if [!pth!]==[] SET "pth=%~dp0"
set "curDir=%~dp0"

if not exist !pth! (
	echo Unable to find !pth!
	pause
	exit /b
)
if not exist "pyRemux" (
	echo Unable to find pyRemux directory
	pause
	exit /b
	)

cd /D !pth!

if exist "_pyremuxTmp" rmdir /s /q _pyremuxTmp
mkdir _pyremuxTmp
if exist "_pyremuxTmp\tracksInfo.txt" del _pyremuxTmp\tracksInfo.txt
if not exist "RemuxOut" mkdir RemuxOut

if not [!pth:~-1!]==[\] (
	if not [!pth:~-1!]==[^"] (
		set "pth=!pth!\"
	) else (
		set "pth=!pth:~1!"
		set "pth=!pth:~0,-1!\"
	)
)

FOR %%a IN ("*.mkv") DO (
	mkvmerge.exe -I "%%a" > _pyremuxTmp\tracksInfo.txt
	python "!curDir!run.py" "!pth!_pyremuxTmp\tracksInfo.txt" "!pth!"
	rmdir /s /q _pyremuxTmp
	mkdir _pyremuxTmp
	echo.
	)

if exist "_pyremuxTmp" rmdir /s /q _pyremuxTmp

cd /D "!curDir!"
pause