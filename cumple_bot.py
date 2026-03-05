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
    "Nico Juzwa": (5,2),
    "Bastian Aguilera": (11,2),
    "Homar Lapeire": (15,2),
    "Felicitas": (16,2),
    "Tío Chiquito": (22,2),
    "Tía Mari": (2,3),
    "Felipe": (2,3),
    "Toto Pernigotti": (8,3),
    "Mari Sirito": (8,3),
    "Martin Carrera": (26,3),
    "Tía Marta": (30,3),
    "Agustina Volpara": (15,4),
    "Pedro Gonzalo": (19,4),
    "Iliana Cabeza": (1,5),
    "Juan Gabriel Pérez": (1,5),
    "Mauricio Gianobile": (6,5),
    "Nacho Flores": (6,5),
    "Alma Aguilera": (8,5),
    "Tía Chola": (16,5),
    "Abuela Rosa": (22,6),
    "Ian Aguilera": (4,6),
    "Santiago Araguez": (11,6),
    "Juan Cruz": (7,7),
    "Jose Luis Pérez": (27,7),
    "Eva Aguilera": (3,8),
    "valentín (Hijo de Cristian)": (10,8),
    "Carolina Acerbi": (16,8),
    "Catalina Cabeza": (18,8),
    "Karen": (20,8),
    "Luciano Aguilera": (24,8),
    "Ramiro Aguilera": (24,8),
    "Rosario Aguilera": (30,8),
    "Francisco Aguilera (Chon)": (4,9),
    "Gonza": (9,9),
    "Julia Aguilera": (11,9),
    "Leandro Cabeza": (18,9),
    "Itatí Ibalos": (18,9),
    "Estela Leguizamon": (28,9),
    "Priscila Aguilera": (1,10),
    "Manolo Hermida": (7,10),
    "Francisco Aguilera (Hijo de Marcelo)": (7,10),
    "Marcelo Aguilera": (13,10),
    "Abuelo Kaque": (19,10),
    "Abuelo Carlos": (21,10),
    "Tío Cristian": (26,10),
    "Melina Pérez": (26,10),
    "Leo Cabeza": (29,10),
    "Tía Marcela": (4,11),
    "Alfonsina Aguilera": (7,11),
    "Fabricio Aguilera": (7,11),
    "Lucas Cabeza": (12,11),
    "Tía Coca": (19,11),
    "Nico Gianobile": (29,11),
    "Pablo Araguez": (19,12),
    "Tiziana Aguilera": (22,12)
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

