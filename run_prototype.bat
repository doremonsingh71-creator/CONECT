@echo off
title CONECT Prototype Server (FastAPI + Tailwind)
echo ================================================================
echo   CONECT: Women in STEM Career & Mentorship Platform
echo   Launching FastAPI Backend & Web Client on http://localhost:8000
echo ================================================================
echo.

cd /d "%~dp0backend"
start http://localhost:8000
"C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
pause
