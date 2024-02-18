@echo off
setlocal enabledelayedexpansion

set "file=.\config\tags.txt"
set /p user_id=<.\config\user_id.txt
set /p password=<.\config\password.txt
set user_index=0

:loop
for /f "delims=" %%a in (%file%) do (
    rem user_id 뒤에 숫자 붙이기
    set "_user_id=!user_id!!user_index!"

    rem echo !_user_id!
    rem echo %%a
    
    echo !user_index!
    start python .\Task.py %%a !_user_id! !password!
    set /a user_index+=1
    call :resetUserIdIndex
    
    pause

    rem 10분 후 다음 태그 진행
    rem timeout /t 600 /nobreak >nul
)

rem 3시간 대기
rem timeout /t 10800 /nobreak >nul

goto loop

:resetUserIdIndex 
if !user_index! gtr 20 (
    set "user_index=0"
)

goto :eof

endlocal
