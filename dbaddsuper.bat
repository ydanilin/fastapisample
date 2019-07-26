@ECHO OFF
for /f "tokens=*" %%a in (postgres\database.env) do call :Foo "%%a"
goto End

:Foo
set _z=%~1
IF NOT %_z:~0,1%==# SET %_z%
goto :eof

:End
SET POSTGRES_HOST=localhost
SET POSTGRES_USER=postgres
SET POSTGRES_PASSWORD=hatikwah

SET FIRST_SUPERUSER=putin@sntozero.com
SET FIRST_SUPERUSER_PASSWORD=shalom

PUSHD web\backend\machine
If %errorlevel% NEQ 0 goto:eof

python initial_data.py

POPD
