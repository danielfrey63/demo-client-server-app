# AI/LLM Umfrage

Eine einfache Webanwendung zur Durchführung einer Umfrage über die Nutzung von AI/LLMs mit Echtzeit-Ergebnisdarstellung.

## Features

- Einfache Ja/Nein-Umfrage
- Echtzeit-Aktualisierung der Ergebnisse
- Pie-Chart Visualisierung
- QR-Code für einfachen Zugriff auf die Umfrage
- Automatische Datenbankbereinigung beim Neustart

## Installation

1. Repository klonen
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Lokale Entwicklung

```bash
python app.py
```

Die Anwendung ist dann unter `http://localhost:5000` erreichbar:
- Umfrage: `http://localhost:5000/survey`
- Ergebnisse: `http://localhost:5000` oder `http://localhost:5000/results`

## Deployment auf Vercel

1. Forke dieses Repository
2. Gehe zu [Vercel](https://vercel.com)
3. Erstelle ein neues Projekt und verbinde es mit deinem Fork
4. Vercel erkennt automatisch die Python-Konfiguration
5. Klicke auf "Deploy"

Die Anwendung wird automatisch gebaut und deployed. Vercel stellt eine URL bereit, unter der die Anwendung erreichbar ist.

## Demo Vorbereitung

### 1. Main Branch auf v1.0.0 zurücksetzen

```bash
# Wechsle zum main Branch
git checkout main

# Setze den Branch hart auf v1.0.0 zurück
git reset --hard v1.0.0

# Pushe die Änderungen zum Remote Repository (force push erforderlich)
git push -f origin main
```

### 2. UI Modernisierung mit KI

Für die UI-Modernisierung kann folgender Prompt verwendet werden:

```text
Ich möchte für beide Screens (Survey und Results) ein wirklich modernes, ansprechendes UI haben. 
Mach nur Änderungen am UI. Berücksichtige dabei:

- Moderne Typographie mit der Inter Font Family
- Dunkles Theme mit modernen Farbverläufen
- Subtile Animationen und Hover-Effekte für Buttons und Container
- Responsives Design für mobile Geräte
- Verbesserte Lesbarkeit und visuelle Hierarchie
- Moderne Komponenten-Stile (Buttons, Container)
- Pie Chart (kein Doughnut/Ring Chart):
  - Keine Animationen im Chart
  - Klare, zum Dark Theme passende Farben
  - Prozentangaben direkt im Chart
```

### 3. Änderungen einchecken und synchronisieren

```bash
# Änderungen zum Staging hinzufügen
git add .

# Commit mit aussagekräftiger Nachricht erstellen
git commit -m "Modern UI improvements for survey and results pages"

# Änderungen zum Remote Repository pushen
git push origin main
