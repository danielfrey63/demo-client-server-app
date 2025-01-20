from app import app

# Vercel erwartet diese Handler-Funktion
def handler(request, context):
    return app(request)
