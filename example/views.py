# example/views.py
from datetime import datetime
from django.http import HttpResponse

def index(request):
    nowDate = datetime.now().strftime('%d.%m.%Y')
    nowTime = datetime.now().strftime('%H:%M:%S')
    html = f'''
    <html>
        <body style="
                background-color: #333;
            ">
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            ">
            <div style="font-size: 100">🧑‍💻👩‍💻</div>
            <small style="color: #fd5b4f;font-family: monospace;font-weight: 700;">🗓️ { nowDate }</small>
            <small id="time" style="color: #fd5b4f;font-family: monospace;font-weight: 700;">🕦 { nowTime }</small>
            </div>
            <script>
                function updateTime() {{
                    const now = new Date();
                    const formattedTime = now.toLocaleString('de-DE', {{
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit'
                    }});
                    document.getElementById('time').innerHTML = '🕦 ' + formattedTime;
                }}
                setInterval(updateTime, 1000);  // Aktualisiert die Zeit jede Sekunde
            </script>
        </body>
    </html>
    '''
    return HttpResponse(html)
