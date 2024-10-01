# Django Vercel Template

Dieses Projekt bietet ein Django-Template, das auf Vercel gehostet wird. Die Datenbankvariablen werden direkt von Vercel bereitgestellt, nachdem du eine Datenbank im Vercel-Projekt unter "Storage" angelegt und mit dem Projekt verbunden hast. Es ist lediglich notwendig, das Projekt mit der Datenbank zu verbinden. Alle benötigten Variablen sind bereits im Template enthalten.

## Voraussetzungen

- **Python 3.x** auf dem lokalen Rechner installiert
- Ein **Vercel-Konto**
- **Django** installiert

## Schritte zur Einrichtung

### 1. Repository klonen oder Template verwenden

```bash
git clone https://github.com/henrymanke/django-vercel-template.git
cd django-vercel-template
```

> [!NOTE]  
> Erstelle nun ein neues Projekt auf Vercel und nutze das Repo als Codebase.

### 2. Abhängigkeiten installieren

Erstelle eine virtuelle Umgebung (venv):

*macOS / Linux*
```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
```
*Windows*
```bash
python -m venv env
.\env\Scripts\activate
pip install --upgrade pip
```

Installiere die benötigten Python-Pakete:

```bash
pip install -r requirements.txt
```

### 3. Datenbank in Vercel anlegen

1. Gehe zu deinem Vercel-Dashboard.
2. Erstelle eine neue Datenbank unter **Storage**.
3. Verbinde die Datenbank mit deinem Django-Projekt. Vercel stellt automatisch die benötigten Umgebungsvariablen für die Datenbankverbindung bereit.

### 4. Superuser lokal erstellen

Für die Superuser-Erstellung musst du **lokal** eine `.env`-Datei mit den Datenbank-Anmeldedaten anlegen. 

Die Datenbankvariablen findest du in Vercel unter [Dein Projekt] > **Storage** > [Deine Datenbank] > `.env.local` > **Copy Snippet**

Beispiel für die `.env`-Datei:

```
POSTGRES_URL="************"
POSTGRES_PRISMA_URL="************"
POSTGRES_URL_NO_SSL="************"
POSTGRES_URL_NON_POOLING="************"
POSTGRES_USER="************"
POSTGRES_HOST="************"
POSTGRES_PASSWORD="************"
POSTGRES_DATABASE="************"
```

Führe dann den folgenden Befehl aus, um einen Superuser zu erstellen:

```bash
python manage.py createsuperuser
```

### 5. Statische Dateien verwalten

Die statischen Dateien werden aktuell nur über die URLs und über das Repository bereitgestellt. Stelle sicher, dass die statischen Dateien korrekt gesammelt werden, bevor du die Anwendung auf Vercel bereitstellst.

#### Statische Dateien lokal sammeln:

```bash
python manage.py collectstatic
```

In den Django-Einstellungen (`settings.py`) sind folgende Konfigurationen für statische Dateien gesetzt:

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# URL where static files will be accessible
STATIC_URL = '/static/'

# Directory where static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

#### URL-Konfiguration für statische Dateien:

In der `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### 6. Projekt auf Vercel deployen

1. Verknüpfe dein GitHub-Repository mit Vercel.
2. Vercel erkennt automatisch, dass es sich um ein Django-Projekt handelt und wird die erforderlichen Befehle zum Bauen und Starten der App ausführen.

### 7. Lokale Entwicklung

Um die Anwendung lokal zu testen, kannst du den lokalen Entwicklungsserver starten:

```bash
python manage.py runserver
```

Rufe dann die URL [http://127.0.0.1:8000](http://127.0.0.1:8000) in deinem Browser auf.

## Hinweise

- **Superuser-Erstellung:** Da die Datenbank in der Produktion über Vercel läuft, sollte die Superuser-Erstellung lokal erfolgen.
- **Statische Dateien:** Aktuell werden statische Dateien nur über URLs und das Repository bereitgestellt.
