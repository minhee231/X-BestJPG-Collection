@echo off
setlocal

:loop
start python .\Scraping.py

start python .\Scraping.py

rem 6시간 마다 실행
timeout /t 21600 /nobreak >nul

goto loop