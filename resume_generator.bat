@echo off
cls
echo =====================================
echo     ONLINE RESUME GENERATOR (CMD)
echo =====================================
echo.

:: Ask for user input
set /p NAME=Enter your full name: 
set /p EMAIL=Enter your email: 
set /p PHONE=Enter your phone number: 
set /p EDUCATION=Enter your education: 
set /p EXPERIENCE=Enter your experience: 
set /p SKILLS=Enter your skills (comma-separated): 
set /p HOBBIES=Enter your hobbies (comma-separated): 

:: Overwrite resume_data.txt with new input
(
echo %NAME%
echo %EMAIL%
echo %PHONE%
echo %EDUCATION%
echo %EXPERIENCE%
echo %SKILLS%
echo %HOBBIES%
) > resume_data.txt

echo.
echo Generating resume...
py generate_resume.py

echo.
echo Opening resume in browser...
for /f %%i in ('dir /b /o:-d output\resume_*.html') do (
    start "" output\%%i
    goto end
)

:end
pause
