# Screen Glitch Effect für Windows

Ein Programm für Windows, das einen periodischen Glitch-Effekt auf dem Bildschirm erzeugt mit:

- Zitter-/Shake-Effekt
- Farbinvertierung und Verzerrung
- Chromatischer Aberration (Pink/Cyan Farbverschiebung)
- **Zufälligen Tastatureingaben** (tippt random Buchstaben)
- **Rot-leuchtender Totenkopf mit Knochen** (erscheint alle 5 Minuten für ~10 Sekunden, detailliert im Low-Poly-Stil)
- Zufälligen Intervallen und Intensitäten
- **Läuft unsichtbar im Hintergrund**

## Option 1: Fertige .exe verwenden (Einfach)

Wenn du bereits eine fertige `ScreenGlitcher.exe` hast:

1. **Starten**: Einfach Doppelklick auf `ScreenGlitcher.exe`
1. Beim ersten Start wird das Programm automatisch zum Autostart hinzugefügt
1. Ein kleines Konsolenfenster erscheint kurz und verschwindet dann
1. Das Programm läuft jetzt unsichtbar im Hintergrund
1. Nach 30 Tagen löscht es sich automatisch

### Programm stoppen (vor Ablauf)

Öffne den Task-Manager (`Strg + Shift + Esc`):

1. Gehe zum Tab “Details”
1. Suche nach “ScreenGlitcher.exe”
1. Rechtsklick → “Task beenden”

### Aus Autostart entfernen

1. Drücke `Win + R`
1. Tippe `shell:startup` und drücke Enter
1. Falls dort eine Verknüpfung ist, lösche sie

Oder via Registry:

1. Drücke `Win + R`
1. Tippe `regedit` und drücke Enter
1. Navigiere zu: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
1. Lösche den Eintrag “ScreenGlitcher”

## Option 2: .exe selbst erstellen

### Voraussetzungen

- Windows 10 oder 11
- Python 3.8 oder höher ([Download](https://www.python.org/downloads/))
  - ✅ Wichtig: Bei Installation “Add Python to PATH” aktivieren!

### Build-Prozess

1. **Dateien vorbereiten**:
- `screen_glitch_windows.py` (das Hauptprogramm)
- `build_windows.bat` (das Build-Script)
1. **Build ausführen**:
- Doppelklick auf `build_windows.bat`
- Das Script installiert PyInstaller und erstellt die .exe
- Die fertige `ScreenGlitcher.exe` wird im gleichen Ordner erstellt
1. **Fertig!**
- Du hast jetzt eine standalone .exe ohne Python-Abhängigkeiten
- Die .exe kann auf jeden Windows-PC kopiert werden

### Build auf Linux/Mac (Cross-Compilation)

```bash
chmod +x build_windows.sh
./build_windows.sh
```

Die erstellte .exe dann auf Windows übertragen.

## Technische Details

### Was macht das Programm?

1. **Visuelle Effekte**:
- Nutzt Windows GDI (Graphics Device Interface)
- `BitBlt` für Bildmanipulation und Invertierung
- Erstellt zufällige Glitch-Bereiche auf dem Bildschirm
- Farbige Overlay-Streifen für chromatische Aberration
1. **Tastatureingaben**:
- Nutzt `keybd_event` API für Tastatur-Simulation
- Tippt 1-5 zufällige Zeichen (Buchstaben, Zahlen, Satzzeichen)
- Simuliert realistisches Tippen mit Verzögerungen
1. **Totenkopf-Effekt**:
- Nutzt tkinter Canvas für detaillierte grafische Darstellung
- **Low-Poly-Design**: Ausschließlich Dreiecke und Polygone
- **Anatomisch genauer Schädel**:
  - Gerundete Schädeldecke aus 12 Dreiecken
  - Realistische Seitenwände und Stirnpartie
  - Dreieckige Augenhöhlen
  - Herzförmige Nase aus zwei Dreiecken
  - Wangenknochen und Kieferstruktur
- **8 dreieckige Zähne** im Unterkiefer
- **Gekreuzte Knochen** (Jolly Roger Style):
  - Zwei sich kreuzende Knochen unter dem Schädel
  - Jeder Knochen mit detaillierten Gelenkkugel-Enden
  - Low-Poly-Konstruktion aus Polygonen
- Erscheint alle 5 Minuten automatisch
- Fade-In über 5 Sekunden (von dunkelrot zu neonrot)
- Hält für 3 Sekunden
- Fade-Out über 2 Sekunden
- Gesamtdauer: ~10 Sekunden
- Läuft im separaten Thread (blockiert nicht das Hauptprogramm)
1. **Autostart**:
- Trägt sich in die Windows Registry ein
- Pfad: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
- Startet automatisch bei jedem Windows-Start
1. **Unsichtbarer Betrieb**:
- Versteckt das Konsolenfenster nach dem Start
- Läuft komplett im Hintergrund
- Kein Taskleisten-Icon

### Anpassungen

Du kannst das Verhalten in `screen_glitch_windows.py` anpassen:

**Häufigkeit ändern** (Zeile ~206):

```python
wait_time = random.uniform(3.0, 10.0)  # Min, Max in Sekunden
```

**Glitch-Dauer ändern** (Zeile ~215):

```python
glitch_duration = random.uniform(0.05, 0.2)  # Min, Max in Sekunden
```

**Häufigkeit der Tastatureingaben ändern** (Zeile ~158):

```python
action = random.choice(['glitch', 'glitch', 'type'])  # 2/3 Glitch, 1/3 Typing
```

**Beispiele:**

- Mehr Typing: `['glitch', 'type', 'type']` (1/3 Glitch, 2/3 Typing)
- Nur Glitch: `['glitch', 'glitch', 'glitch']` (0% Typing)
- Nur Typing: `['type']` (100% Typing)
- 50/50: `['glitch', 'type']`

**Totenkopf-Intervall ändern** (Zeile ~22):

```python
self.skull_interval = 300  # 5 Minuten in Sekunden
```

**Beispiele:**

- Alle 2 Minuten: `self.skull_interval = 120`
- Alle 10 Minuten: `self.skull_interval = 600`
- Jede Minute: `self.skull_interval = 60`
- Deaktivieren: `self.skull_interval = 999999`

**Intensität ändern** (Zeile ~79):

```python
offsets = {
    'low': (2, 4),      # (x_pixels, y_pixels)
    'medium': (4, 8),
    'high': (6, 12)
}
```

Nach Änderungen: `.exe` neu erstellen mit `build_windows.bat`

## Deinstallation

**Schnellmethode**:

1. Task-Manager öffnen (`Strg + Shift + Esc`)
1. “ScreenGlitcher.exe” beenden
1. .exe Datei manuell löschen
1. Registry-Eintrag entfernen:
- `Win + R` → `regedit` → `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
- Lösche “ScreenGlitcher”

**Via PowerShell** (als Administrator):

```powershell
# Prozess beenden
Stop-Process -Name "ScreenGlitcher" -Force -ErrorAction SilentlyContinue

# Registry-Eintrag entfernen
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "ScreenGlitcher" -ErrorAction SilentlyContinue
```

## Sicherheitshinweise

- Das Programm benötigt KEINE Administrator-Rechte
- Es greift NUR auf den Bildschirm zu (visuell)
- Keine Netzwerk-Aktivität
- Keine Daten werden gesendet
- Quellcode ist vollständig einsehbar
- Manche Antivirus-Programme könnten es als “verdächtig” markieren (False Positive), weil:
  - Es sich selbst zum Autostart hinzufügt
  - Es Tastatureingaben simuliert
  - Es das Konsolenfenster versteckt
  
  → Das ist normales Verhalten für Hintergrund-Programme

## Fehlerbehebung

**Programm startet nicht:**

- Prüfe ob Python korrekt installiert ist (nur für Build nötig)
- Prüfe Task-Manager ob es bereits läuft
- Führe als Administrator aus

**Keine Glitches sichtbar:**

- Warte 3-10 Sekunden (zufälliges Intervall)
- Prüfe Task-Manager ob Prozess läuft
- Prüfe ob .exe wirklich gestartet wurde

**Build schlägt fehl:**

- Stelle sicher, dass Python zum PATH hinzugefügt wurde
- Installiere PyInstaller manuell: `pip install pyinstaller`
- Nutze Kommandozeile: `pyinstaller --onefile --noconsole screen_glitch_windows.py`

## Anforderungen

- **Betriebssystem**: Windows 10 oder 11
- **Für Ausführung**: Keine (standalone .exe)
- **Für Build**: Python 3.8+ und PyInstaller

## Lizenz & Haftungsausschluss

Dieses Programm ist nur für Bildungszwecke und den privaten Gebrauch gedacht.
Verwende es nicht auf fremden Computern ohne Erlaubnis.
Keine Garantie für Funktionalität oder Schäden.
