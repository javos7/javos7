# Definimos los datos de una sesión de entrenamiento de ejemplo
entrenamiento_del_dia = {
    "fecha": "2026-09-27",
    "deporte": "Ciclismo",
    "distancia_km": 75.5,
    "tiempo_minutos": 140,
    "frecuencia_cardiaca_media": 148,
    "sensaciones": "Viento racheado en contra en la vuelta. Sensación de pesadez en piernas los últimos 15 km.",
    "hidratacion_nutricion": "1 bidón isotónico y 2 geles"
}

# Mostramos un resumen claro por pantalla
print("=== RESUMEN DEL ENTRENAMIENTO REGISTRADO ===")
print(f"Deporte: {entrenamiento_del_dia['deporte']}")
print(f"Distancia: {entrenamiento_del_dia['distancia_km']} km")
print(f"Tiempo total: {entrenamiento_del_dia['tiempo_minutos']} minutos")
print(f"Pulsaciones medias: {entrenamiento_del_dia['frecuencia_cardiaca_media']} ppm")
print(f"Sensaciones: {entrenamiento_del_dia['sensaciones']}")
print("============================================")
