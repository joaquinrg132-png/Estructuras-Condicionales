try:
    calificacion = float(input("Ingresa tu calificación numérica (0-100): "))

    if 90 <= calificacion <= 100:
        print("Tu calificación en letra es: A")
    elif 80 <= calificacion < 90:
        print("Tu calificación en letra es: B")
    elif 70 <= calificacion < 80:
        print("Tu calificación en letra es: C")
    elif 60 <= calificacion < 70:
        print("Tu calificación en letra es: D")
    elif 0 <= calificacion < 60:
        print("Tu calificación en letra es: F")
    else:
        print("La calificación debe estar entre 0 y 100.")
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")
