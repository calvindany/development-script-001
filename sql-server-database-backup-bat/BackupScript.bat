@ECHO OFF

:: Set path to save backup files
set BACKUPPATH=C:\Google Drive\Ticket_Portal_Backup

:: Set server and database details
set SERVERNAME=localhost\SQLEXPRESS
set DATABASENAME=DBName

:: Generate date and time stamp
:: FOR /F "tokens=2-4 delims=/- " %%A IN ('DATE /T') DO (SET mydate=%%C-%%A-%%B)
:: FOR /F "tokens=1-2 delims=:. " %%A IN ("%TIME%") DO (SET mytime=%%A%%B)

set TIME_STAMP=%DATE:/=-%

:: Create timestamp and backup filename
set DATESTAMP=%TIME_STAMP%
set BACKUPFILENAME=%BACKUPPATH%\%DATABASENAME%_%DATESTAMP%.bak

:: Debugging outputs
ECHO "Backup Path: %BACKUPPATH%"
ECHO "Server Name: %SERVERNAME%"
ECHO "Database Name: %DATABASENAME%"
ECHO "Backup Filename: %BACKUPFILENAME%"
ECHO "Timestamp: %DATESTAMP%"

:: Ensure the backup folder exists
IF NOT EXIST "%BACKUPPATH%" (
    ECHO "Backup folder does not exist. Creating it..."
    mkdir "%BACKUPPATH%"
)

:: Check if more than 5 backup files exist in the folder
PUSHD "%BACKUPPATH%"
SETLOCAL ENABLEDELAYEDEXPANSION

SET count=0
FOR /F "delims=" %%F IN ('DIR /B /O-D *.bak') DO (
    SET /A count+=1
    IF !count! GTR 4 (
        ECHO "Deleting old backup: %%F"
        DEL "%%F"
    )
)

ENDLOCAL
POPD

:: Execute SQL backup (quotes added here instead of in the variable)
SqlCmd -E -S %SERVERNAME% -d master -Q "BACKUP DATABASE [%DATABASENAME%] TO DISK = N'%BACKUPFILENAME%' WITH INIT, NOUNLOAD, NAME = N'%DATABASENAME% backup', NOSKIP, STATS = 10, NOFORMAT"

:: Completion message
::IF %ERRORLEVEL% EQU 0 (
::    ECHO "Backup completed successfully."
::) ELSE (
::    ECHO "Backup failed with error code %ERRORLEVEL%."
::)

::PAUSE
