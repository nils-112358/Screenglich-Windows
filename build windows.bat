@echo off
REM Build Script für Screen Glitch Windows .exe
REM Benötigt: Python 3 und PyInstaller

echo ==========================================
echo Screen Glitch - Windows EXE Builder
echo ==========================================
echo.

REM Prüfe ob Python installiert ist
python --version >nul 2>&1
if errorlevel 1 (
    echo FEHLER: Python ist nicht installiert!
    echo Bitte Python von https://www.python.org/downloads/ herunterladen
    pause
    exit /b 1
)

echo [1/3] Installiere PyInstaller...
python -m pip install --upgrade pip
python -m pip install pyinstaller

echo.
echo [2/3] Erstelle .exe Datei...
python -m PyInstaller --onefile --noconsole --icon=NONE ^
    --name "ScreenGlitcher" ^
    --add-data "screen_glitch_windows.py;." ^
    screen_glitch_windows.py

echo.
echo [3/3] Kopiere EXE...
if exist "dist\ScreenGlitcher.exe" (
    copy "dist\ScreenGlitcher.exe" "ScreenGlitcher.exe"
    echo.
    echo ==========================================
    echo Build erfolgreich!
    echo ==========================================
    echo.
    echo Die Datei "ScreenGlitcher.exe" wurde erstellt.
    echo.
    echo Um das Programm zu starten:
    echo 1. Doppelklick auf ScreenGlitcher.exe
    echo 2. Das Programm wird automatisch zum Autostart hinzugefuegt
    echo 3. Es laeuft unsichtbar im Hintergrund
    echo 4. Loescht sich nach 30 Tagen automatisch
    echo.
) else (
    echo.
    echo FEHLER: Build fehlgeschlagen!
    echo Bitte pruefe die Fehlermeldungen oben.
)

echo.
pause
