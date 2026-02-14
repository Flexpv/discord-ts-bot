# 🎵 Discord TeamSpeak Sounds Bot

Ein Discord Bot der die klassischen TeamSpeak "User entered/left your channel" Sounds abspielt!

## 📋 Features

- ✅ Spielt TeamSpeak Sounds wenn User Voice Channels betreten/verlassen
- ✅ Ignoriert Bots automatisch
- ✅ Ignoriert den Channel "24/7 🔉"
- ✅ Bot verlässt Channel automatisch wenn niemand mehr drin ist
- ✅ Läuft 24/7 auf Railway.app kostenlos

---

## 🚀 Setup Anleitung

### **Teil 1: Discord Bot erstellen** (falls noch nicht gemacht)

1. Gehe zu https://discord.com/developers/applications
2. Klicke auf **"New Application"** → Gib einen Namen ein
3. Gehe zu **"Bot"** → **"Add Bot"**
4. Aktiviere unter **"Privileged Gateway Intents"**:
   - ✅ PRESENCE INTENT
   - ✅ SERVER MEMBERS INTENT  
   - ✅ MESSAGE CONTENT INTENT
5. Klicke auf **"Reset Token"** → **KOPIERE DEN TOKEN** (brauchst du später!)
6. Gehe zu **"OAuth2"** → **"URL Generator"**
   - Scopes: `bot`
   - Permissions: `Connect`, `Speak`, `View Channels`
7. Kopiere die URL und lade den Bot auf deinen Server ein

---

### **Teil 2: GitHub Repository erstellen**

1. Gehe zu https://github.com und logge dich ein
2. Klicke oben rechts auf **"+"** → **"New repository"**
3. Name: `discord-ts-bot` (oder was du willst)
4. Setze auf **Public** (wichtig für Railway.app kostenlos!)
5. ✅ **"Add a README file"** anhaken
6. Klicke **"Create repository"**

---

### **Teil 3: Dateien hochladen**

1. In deinem neuen Repository klicke auf **"Add file"** → **"Upload files"**
2. Lade diese 3 Dateien hoch:
   - `bot.py`
   - `requirements.txt`
   - `Aptfile`
3. Klicke **"Commit changes"**

---

### **Teil 4: Sound-Dateien hinzufügen**

#### **Wo bekommst du die TeamSpeak Sounds?**

**Option A: TeamSpeak installiert**
- Windows: `C:\Program Files\TeamSpeak 3 Client\sound\default\`
- Du brauchst: `user_join.wav` und `user_left.wav`

**Option B: Nicht installiert**
- Du kannst die Sounds online suchen (z.B. "teamspeak sounds download")
- Oder selbst aufnehmen / ähnliche Sounds verwenden

#### **Sounds hochladen:**

1. Erstelle in deinem Repository einen Ordner namens `sounds/`
   - Klicke auf **"Add file"** → **"Create new file"**
   - Tippe: `sounds/placeholder.txt` → Commit
2. Gehe in den `sounds/` Ordner
3. Klicke **"Add file"** → **"Upload files"**
4. Lade deine Sound-Dateien hoch und **benenne sie um**:
   - `user_joined.wav` (für "entered channel")
   - `user_left.wav` (für "left channel")
5. **WICHTIG:** Die Dateien müssen `.wav` Format haben!
6. Klicke **"Commit changes"**

**Dein Repository sollte jetzt so aussehen:**
```
discord-ts-bot/
├── bot.py
├── requirements.txt
├── Aptfile
├── README.md
└── sounds/
    ├── user_joined.wav
    └── user_left.wav
```

---

### **Teil 5: Railway.app Deployment**

1. Gehe zu https://railway.app
2. Klicke **"Login"** → Mit GitHub einloggen
3. Klicke **"New Project"** → **"Deploy from GitHub repo"**
4. Wähle dein `discord-ts-bot` Repository aus
5. Railway erkennt automatisch dass es Python ist
6. **WICHTIG:** Umgebungsvariable hinzufügen:
   - Klicke auf dein Projekt → **"Variables"** Tab
   - Klicke **"New Variable"**
   - Name: `DISCORD_TOKEN`
   - Value: [Dein Bot Token von Discord Developer Portal]
   - Klicke **"Add"**
7. Gehe zu **"Settings"** Tab
8. Unter **"Start Command"** trage ein: `python bot.py`
9. Klicke **"Deploy"**

---

### **Teil 6: Testen**

1. Warte 1-2 Minuten bis Railway den Bot deployed hat
2. In den Railway Logs siehst du: `✅ Bot ist online als [BotName]`
3. Gehe in einen Voice Channel auf Discord
4. Der Bot sollte joinen und den "User entered" Sound abspielen! 🎉

---

## 🛠️ Troubleshooting

### **Bot joint nicht / Keine Sounds**

- Prüfe ob der Bot die richtigen Permissions hat (Connect, Speak)
- Prüfe Railway Logs auf Fehlermeldungen
- Stelle sicher dass die Sound-Dateien `.wav` Format haben

### **"Sound-Datei nicht gefunden" Fehler**

- Prüfe ob die Dateien genau `user_joined.wav` und `user_left.wav` heißen
- Prüfe ob sie im `sounds/` Ordner sind

### **Bot geht offline nach paar Stunden**

- Prüfe deine Railway.app Stunden (500h/Monat)
- Stelle sicher dass dein Projekt nicht "pausiert" ist

---

## ⚙️ Anpassungen

### **Anderen Channel ignorieren:**

In `bot.py` Zeile 13:
```python
IGNORED_CHANNEL = "Dein Channel Name"
```

### **Mehrere Channels ignorieren:**

In `bot.py` Zeile 13:
```python
IGNORED_CHANNELS = ["24/7 🔉", "AFK", "Music Bot"]
```

Und dann in Zeile 33 und 44:
```python
if after.channel.name in IGNORED_CHANNELS:
```

---

## 📊 Railway.app Stunden-Check

- Gehe zu https://railway.app
- Klicke auf dein Projekt
- Unter **"Usage"** siehst du wie viele Stunden du noch hast

---

## 💡 Tipps

- Der Bot verlässt Channels automatisch wenn niemand mehr drin ist
- Sounds werden nur für Menschen gespielt, nicht für andere Bots
- Du kannst die Sound-Dateien jederzeit austauschen (einfach neue hochladen)

---

**Viel Spaß mit deinem TeamSpeak-Discord Bot! 🎮🔊**
