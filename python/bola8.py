# juego de bola 8
# 31-03-2025

import random

opciones = ("✅ Sì, definitivamente.", "⭐️ Con toda certeza, que sì.", "🔒 Sin lugar a dudas.", "🤔 Respuesta confusa, intèntalo de nuevo", "🕙 Pregùntalo nuevamente màs tarde.", "😶‍🌫️ Mejor no decirte ahora.", "❌ Mis fuentes dicen que no.", "🌥️ El panorama no es muy favorable.", "🤷 Muy dudoso.")
respuestas = random.choice(opciones)

input("Hazme una pregunta 🎱✨: ")
print("respuesta:", respuestas)
