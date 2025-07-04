import tkinter as tk
from tkinter import messagebox
import random

# Definición de personajes, lugares y armas
personajes = [
    {"nombre": "Dr. Orquídea", "profesion": "Científica"},
    {"nombre": "Coronel Mostaza", "profesion": "Militar"},
    {"nombre": "Reverendo Verde", "profesion": "Religioso"},
    {"nombre": "Sra. Blanco", "profesion": "Ama de llaves"},
    {"nombre": "Profesor Ciruela", "profesion": "Profesor"}
]

lugares = ["Sala de estar", "Cocina", "Biblioteca", "Habitación", "Comedor"]
armas = ["Candelabro", "Revolver", "Cuerda", "Llave inglesa", "Daga"]

# Selección aleatoria del culpable
culpable = {
    "personaje": random.choice(personajes),
    "lugar": random.choice(lugares),
    "arma": random.choice(armas)
}

# Contador de pistas e intentos fallidos
contador_pistas = 0
intentos_fallidos = 0

# Función para generar la historia inicial
def generar_historia():
    historia = f"Bienvenido al juego de Clue. Esta noche, un crimen ha sido cometido en la mansión. "
    historia += f"Cinco personas estuvieron presentes en el lugar, cada una con sus propios secretos y motivos ocultos.\n"
    historia += f"El crimen ocurrió en el/la {culpable['lugar']}. Nadie sabe con certeza quién fue, pero se sospecha de todos los presentes."
    return historia

# Función para generar pistas menos obvias
def obtener_pista():
    global contador_pistas
    pista = ""
    
    # Primera pista: sobre el personaje (descripción de su personalidad o detalle de la profesión)
    if contador_pistas == 0:
        if "científica" in culpable["personaje"]["profesion"].lower():
            pista = "Alguien con un conocimiento profundo de la ciencia parece estar involucrado."
        elif "militar" in culpable["personaje"]["profesion"].lower():
            pista = "Parece que alguien que ha visto mucha disciplina en la vida pudo haber participado."
        elif "religioso" in culpable["personaje"]["profesion"].lower():
            pista = "Un aire de tranquilidad y calma rodea a uno de los sospechosos."
        elif "ama de llaves" in culpable["personaje"]["profesion"].lower():
            pista = "Tal vez alguien que conoce cada rincón de la casa esté involucrado."
        elif "profesor" in culpable["personaje"]["profesion"].lower():
            pista = "Una mente educada y aguda parece estar involucrada en el misterio."

    # Segunda pista: sobre el lugar (descripción ambiental)
    elif contador_pistas == 1:
        if "Sala de estar" in culpable["lugar"]:
            pista = "La escena parece haberse desarrollado en un lugar donde todos se relajan y conversan."
        elif "Cocina" in culpable["lugar"]:
            pista = "Hay rastros de actividad reciente en un lugar donde se suele preparar la comida."
        elif "Biblioteca" in culpable["lugar"]:
            pista = "El silencio de un lugar de estudios parece haber sido interrumpido."
        elif "Habitación" in culpable["lugar"]:
            pista = "Un lugar privado y cerrado parece haber sido testigo de algo inusual."
        elif "Comedor" in culpable["lugar"]:
            pista = "Un espacio donde todos se reúnen para comer ha visto un extraño acontecimiento."

    # Tercera pista: sobre el arma (descripción indirecta)
    elif contador_pistas == 2:
        if "Candelabro" in culpable["arma"]:
            pista = "Algo pesado y brillante parece haber sido utilizado."
        elif "Revolver" in culpable["arma"]:
            pista = "Hay olor a pólvora en el aire."
        elif "Cuerda" in culpable["arma"]:
            pista = "Algo largo y flexible parece haber sido parte del crimen."
        elif "Llave inglesa" in culpable["arma"]:
            pista = "Un objeto útil, pero peligroso, parece haber sido encontrado en la escena."
        elif "Daga" in culpable["arma"]:
            pista = "Un filo afilado y corto parece haber sido la herramienta de un ataque silencioso."
    else:
        pista = "¡No hay más pistas! Sigue intentando."
    
    contador_pistas += 1
    return pista

# Función para verificar la acusación del jugador
def verificar_acusacion():
    global intentos_fallidos
    personaje_seleccionado = personajes_opcion.get()
    lugar_seleccionado = lugares_opcion.get()
    arma_seleccionada = armas_opcion.get()

    if (
        personaje_seleccionado == culpable["personaje"]["nombre"] and
        lugar_seleccionado == culpable["lugar"] and
        arma_seleccionada == culpable["arma"]
    ):
        messagebox.showinfo("Resultado", "¡Correcto! Has encontrado al culpable.")
    else:
        intentos_fallidos += 1
        if intentos_fallidos >= 5:
            messagebox.showinfo("Resultado", "Has fallado demasiadas veces...\n"
                                             "La mansión se oscurece, las sombras te envuelven...\n"
                                             "Nadie volverá a saber de ti. La verdad del crimen se perderá para siempre.")
            ventana.quit()  # Cerrar la ventana del juego
        else:
            pista = obtener_pista()
            messagebox.showinfo("Resultado", f"Incorrecto. Pista: {pista}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Clue")
ventana.geometry("450x400")

# Historia inicial
historia = generar_historia()
historia_label = tk.Label(ventana, text=historia, wraplength=400, justify="left", font=("Arial", 10))
historia_label.pack(pady=10)

# Etiqueta de título
titulo = tk.Label(ventana, text="¿Quién es el culpable?", font=("Arial", 16))
titulo.pack(pady=10)

# Selección de personaje
tk.Label(ventana, text="Selecciona un personaje:").pack()
personajes_opcion = tk.StringVar(ventana)
personajes_opcion.set(personajes[0]["nombre"])
tk.OptionMenu(ventana, personajes_opcion, *[p["nombre"] for p in personajes]).pack()

# Selección de lugar
tk.Label(ventana, text="Selecciona un lugar:").pack()
lugares_opcion = tk.StringVar(ventana)
lugares_opcion.set(lugares[0])
tk.OptionMenu(ventana, lugares_opcion, *lugares).pack()

# Selección de arma
tk.Label(ventana, text="Selecciona un arma:").pack()
armas_opcion = tk.StringVar(ventana)
armas_opcion.set(armas[0])
tk.OptionMenu(ventana, armas_opcion, *armas).pack()

# Botón para verificar la acusación
boton_acusar = tk.Button(ventana, text="Acusar", command=verificar_acusacion)
boton_acusar.pack(pady=20)

# Iniciar la interfaz gráfica
ventana.mainloop()
