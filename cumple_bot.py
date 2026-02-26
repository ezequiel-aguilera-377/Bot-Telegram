import requests
from datetime import datetime

# ==============================
# CONFIGURACIÓN
# ==============================

TOKEN = "8625204532:AAFenogoRPh7X_FPZg8nxPZtGbr6oA3cnAA"
CHAT_ID = "7638035451"

# Lista de cumpleaños
# Formato: "Nombre": (día, mes)
cumpleanios = {
    "Mara Cabeza": (3,1),
    "Dylan Durán": (3,1),
    "Mamá": (4,1),
    "Mateo Henrique": (14,1),
    "Papá": (18,1),
    "Camila Cabeza": (20,1),
    "Jeremi Briguez": (30,1),
    "Emiliano Irazu": (1,2),
    "Maxi Perez": (2,2),
    "Claudio Aguilera": (3,2),
    "Bastian Aguilera": (11,2),
    "Prueba del Bot": (26,2)
}

# ==============================
# FUNCIONES
# ==============================

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    requests.post(url, data=payload)

def revisar_cumpleanios():
    hoy = datetime.now()
    dia = hoy.day
    mes = hoy.month

    for nombre, (d, m) in cumpleanios.items():
        if d == dia and m == mes:
            mensaje = f"🎉 Hoy es el cumpleaños de {nombre}! 🎂"
            enviar_mensaje(mensaje)

# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    revisar_cumpleanios()