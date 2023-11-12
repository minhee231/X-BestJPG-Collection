@echo off
setlocal

:loop
python .\Scraping.py

rem 6시간 마다 실행
timeout /t 21600 /nobreak >nul

goto loop