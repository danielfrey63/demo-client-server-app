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
