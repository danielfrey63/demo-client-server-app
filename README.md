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

## Starten der Anwendung

```bash
python app.py
```

Die Anwendung ist dann unter `http://localhost:5000` erreichbar:
- Umfrage: `http://localhost:5000/survey`
- Ergebnisse: `http://localhost:5000` oder `http://localhost:5000/results`
