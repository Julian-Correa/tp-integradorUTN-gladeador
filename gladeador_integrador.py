
nombre_del_gladeador = input("Ingrese el nombre del gladiador: ")


if nombre_del_gladeador.isalpha():
     print("Nombre válido.")
elif nombre_del_gladeador == "" or not nombre_del_gladeador.isalpha() or nombre_del_gladeador.isdigit():
     print("Nombre inválido. Solo se permiten letras.")

gladeador = nombre_del_gladeador
vida_del_gladeador = 100
vida_del_enemigo = 100
pociones_de_vida = 3
daño_base_ataque_pesado = 15
daño_base_enemigo = 12
turno_gladeador = True

while vida_del_gladeador > 0 and vida_del_enemigo > 0:
    if turno_gladeador:
        print(f"\nTurno de {gladeador}:")
        print("1. Ataque pesado (15 de daño)")
        print("2. Rafaga veloz ")
        print("3. Curar (restaura 20 de vida)")
        accion = input("Elige tu acción (1/2/3): ")

        if accion.isdigit() and accion == "1":
            vida_del_enemigo -= 15
            print(f"{gladeador} realiza un ataque pesado. Vida del enemigo: {vida_del_enemigo}")
            if vida_del_enemigo < 20:
                print("¡Golpe crítico!")
                daño_base_ataque_pesado *=  1.5
                vida_del_enemigo -= daño_base_ataque_pesado
                print(f"Daño adicional por golpe crítico: {daño_base_ataque_pesado}. Vida del enemigo: {vida_del_enemigo}")
        elif accion.isdigit() and accion == "2":
            for i in range(3):
                vida_del_enemigo -= 5
                print(f"Ataque veloz {i+1}: Vida del enemigo: {vida_del_enemigo}")
            print(f"{gladeador} realiza un ataque veloz¡. Vida del enemigo: {vida_del_enemigo}")
        elif accion.isdigit() and accion == "3":
            if pociones_de_vida > 0:
                vida_del_gladeador += 30
                pociones_de_vida -= 1
                print(f"{gladeador} usa una poción de vida. Vida actual: {vida_del_gladeador}, Pociones restantes: {pociones_de_vida}")
            else:
                print("¡No quedan pociones! Pierdes el turno.")
                continue
        else:
            print("Acción inválida. Intenta de nuevo.")
            continue

        turno_gladeador = False
    else:
        vida_del_gladeador -= daño_base_enemigo
        print(f"El enemigo te ataco por 12 puntos de daño¡. Vida de {gladeador}: {vida_del_gladeador}")
        turno_gladeador = True

if vida_del_gladeador <= 0:
    print(f"\n DERROTA. Has caído en combate.")
elif vida_del_enemigo <= 0:
    print(f"\n VICTORIA! {gladeador} has ganado la batalla.")
    
