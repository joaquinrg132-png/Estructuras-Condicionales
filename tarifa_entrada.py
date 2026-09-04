try:
    edad = int(input("Ingresa la edad de la persona: "))

    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad < 12:
        print("El costo de entrada es: $50")
    elif 12 <= edad <= 17:
        print("El costo de entrada es: $80")
    else:
        print("El costo de entrada es: $120")
except ValueError:
    print("Por favor, ingresa una edad válida (número entero).")
