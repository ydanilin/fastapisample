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
PUSHD web\backend\machine
If %errorlevel% NEQ 0 goto:eof

START /WAIT /B "Velvet fast API" uvicorn app.main:app --reload
POPD
