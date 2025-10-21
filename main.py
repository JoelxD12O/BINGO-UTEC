from juego_bingo import JuegoBingo
from gestor_json import GestorJSON

def agregar_cartilla_fila_por_fila(juego):
    """Agrega una cartilla ingresando fila por fila"""
    codigo = input("📋 Código de la cartilla: ").strip()
    
    if codigo in juego.cartillas:
        print(f"❌ La cartilla {codigo} ya existe")
        return
    
    numeros = []
    print("\n📝 Ingresa 5 filas de 5 números cada una")
    print("ℹ️  Usa 0 para el comodín del centro (obligatorio en fila 3, columna 3)")
    print("Separa los números con espacios o comas\n")
    
    for fila in range(1, 6):
        while True:
            print(f"Fila {fila}/5 (5 números): ", end="")
            entrada = input().replace(',', ' ')
            
            try:
                fila_numeros = [int(n) for n in entrada.split() if n.strip()]
                
                if len(fila_numeros) != 5:
                    print(f"❌ Debes ingresar exactamente 5 números (ingresaste {len(fila_numeros)})")
                    continue
                
                # Verificar que el centro sea 0
                if fila == 3:
                    if fila_numeros[2] != 0:
                        print("❌ El número central de la fila 3 debe ser 0 (comodín)")
                        continue
                else:
                    if 0 in fila_numeros:
                        print("❌ El 0 (comodín) solo debe estar en el centro (fila 3, columna 3)")
                        continue
                
                numeros.extend(fila_numeros)
                print(f"✅ Fila {fila} guardada: {fila_numeros}\n")
                break
                
            except ValueError:
                print("❌ Error: debes ingresar números enteros. Intenta de nuevo\n")
    
    print(f"\n📊 Cartilla completa ({len(numeros)} números):")
    print("   " + " ".join(f"{n:3d}" for n in numeros[:5]))
    print("   " + " ".join(f"{n:3d}" for n in numeros[5:10]))
    print("   " + " ".join(f"{n:3d}" for n in numeros[10:15]))
    print("   " + " ".join(f"{n:3d}" for n in numeros[15:20]))
    print("   " + " ".join(f"{n:3d}" for n in numeros[20:25]))
    
    juego.agregar_cartilla(codigo, numeros)

def agregar_cartilla_manual(juego):
    """Agrega una cartilla ingresada de una sola vez"""
    codigo = input("Código de la cartilla: ").strip()
    
    if codigo in juego.cartillas:
        print(f"❌ La cartilla {codigo} ya existe")
        return
    
    print("Ingresa 25 números separados por espacios o comas:")
    entrada = input().replace(',', ' ')
    
    try:
        numeros = [int(n) for n in entrada.split() if n]
        if len(numeros) != 25:
            print(f"❌ Error: ingresaste {len(numeros)} números, se requieren 25")
            return
        juego.agregar_cartilla(codigo, numeros)
    except ValueError:
        print("❌ Error: debes ingresar exactamente 25 números enteros")

def mostrar_patrones():
    """Muestra todos los patrones disponibles"""
    print("\n🎯 Patrones disponibles:")
    print("   U  - U (columna izq + fila inferior + columna der)")
    print("   T  - T (fila superior + columna central)")
    print("   E  - E (columna izq + 3 líneas horizontales)")
    print("   C  - C (columna izq + fila superior + inferior)")
    print("   L  - L (última fila + última columna)")
    print("   Z  - Z (primera fila + última fila + diagonal)")
    print("   B  - B (primera columna + línea media)")
    print("   X  - X (ambas diagonales)")
    print("   LINEA      - Fila completa")
    print("   COLUMNA    - Columna completa")
    print("   DIAGONAL   - Una diagonal")
    print("   APAGON     - Cartilla completamente llena")

def menu_principal():
    """Menú principal del juego"""
    juego = JuegoBingo()
    
    print("\n" + "🎰"*35)
    print("🎰" + " BINGO PROGRESIVO - RONDAS: U → T → E → C → APAGON ".center(68) + "🎰")
    print("🎰"*35)
    
    while True:
        # Mostrar ronda actual
        ronda = juego.obtener_numero_ronda()
        patron = juego.patron_actual or "No establecido"
        
        print("\n" + "="*70)
        print(f"🎰 BINGO INTERACTIVO - Ronda {ronda}/5 - Patrón: {patron}")
        print("="*70)
        print("📋 CARTILLAS")
        print("   1. Agregar cartilla (fila por fila)")
        print("   2. Agregar cartilla (25 números de una vez)")
        print("   3. Ver cartillas actuales")
        print("🎮 JUEGO")
        print("   4. Ingresar número sorteado")
        print("   5. Ver números sorteados")
        print("   5.5. Eliminar número sorteado")
        print("📊 PANEL Y DATOS")
        print("   6. Mostrar panel completo")
        print("   7. Mostrar resumen")
        print("   8. Ver estado de rondas (U→T→E→C→APAGON)")
        print("   8.5. Cambiar a otra ronda")
        print("💾 PERSISTENCIA")
        print("   9. Guardar cartillas en JSON")
        print("   10. Cargar cartillas desde JSON")
        print("   11. Guardar juego actual")
        print("🔄 OTROS")
        print("   0. Salir")
        print("="*70)
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == '1':
            agregar_cartilla_fila_por_fila(juego)
        
        elif opcion == '2':
            agregar_cartilla_manual(juego)
        
        elif opcion == '3':
            if not juego.cartillas:
                print("❌ No hay cartillas cargadas")
            else:
                print(f"\n✅ Total de cartillas: {len(juego.cartillas)}")
                for codigo in juego.cartillas.keys():
                    print(f"   - {codigo}")
        
        elif opcion == '4':
            if not juego.cartillas:
                print("❌ Debes agregar cartillas primero")
            else:
                numero_valido = False
                while not numero_valido:
                    try:
                        numero = int(input("Ingresa número sorteado (1-90): "))
                        if 1 <= numero <= 90:
                            juego.ingresar_numero(numero)
                            numero_valido = True
                        else:
                            print("❌ El número debe estar entre 1 y 90. Intenta de nuevo.")
                    except ValueError:
                        print("❌ Entrada inválida. Debes ingresar un número entero. Intenta de nuevo.")
        
        elif opcion == '5':
            if not juego.numeros_sorteados:
                print("❌ No hay números sorteados aún")
            else:
                print(f"\n📌 Números sorteados: {len(juego.numeros_sorteados)}")
                print(f"   {sorted(juego.numeros_sorteados)}")
        
        elif opcion == '5.5':
            if not juego.numeros_sorteados:
                print("❌ No hay números sorteados para eliminar")
            else:
                numero_valido = False
                while not numero_valido:
                    try:
                        numero = int(input("Ingresa número a eliminar (1-90): "))
                        if 1 <= numero <= 90:
                            juego.eliminar_numero(numero)
                            numero_valido = True
                        else:
                            print("❌ El número debe estar entre 1 y 90. Intenta de nuevo.")
                    except ValueError:
                        print("❌ Entrada inválida. Debes ingresar un número entero. Intenta de nuevo.")
        
        elif opcion == '6':
            if not juego.cartillas:
                print("❌ No hay cartillas para mostrar")
            else:
                juego.mostrar_panel()
        
        elif opcion == '7':
            juego.mostrar_resumen()
        
        elif opcion == '8':
            juego.mostrar_estado_rondas()
        
        elif opcion == '8.5':
            if not juego.cartillas:
                print("❌ Debes cargar cartillas primero")
            else:
                print("\n🎯 Rondas disponibles:")
                print("   1. Ronda 1 - Patrón U")
                print("   2. Ronda 2 - Patrón T")
                print("   3. Ronda 3 - Patrón E")
                print("   4. Ronda 4 - Patrón C")
                print("   5. Ronda 5 - Patrón APAGON (Premio Mayor)")
                
                ronda_valida = False
                while not ronda_valida:
                    try:
                        ronda = int(input("\nSelecciona el número de ronda (1-5): "))
                        if 1 <= ronda <= 5:
                            juego.cambiar_ronda(ronda)
                            ronda_valida = True
                        else:
                            print("❌ El número debe estar entre 1 y 5. Intenta de nuevo.")
                    except ValueError:
                        print("❌ Entrada inválida. Debes ingresar un número entero. Intenta de nuevo.")
        
        elif opcion == '9':
            if not juego.cartillas:
                print("❌ No hay cartillas para guardar")
            else:
                juego.guardar_cartillas()
        
        elif opcion == '10':
            juego.cargar_cartillas_desde_json()
        
        elif opcion == '11':
            if not juego.cartillas:
                print("❌ No hay juego para guardar")
            else:
                nombre = input("Nombre del archivo (default: juego_guardado.json): ").strip()
                if not nombre:
                    nombre = "juego_guardado.json"
                juego.guardar_juego(nombre)
        
        elif opcion == '0':
            print("\n👋 ¡Gracias por jugar! Hasta pronto...")
            break
        
        else:
            print("❌ Opción no válida. Ingresa un número del 0 al 11 (o 5.5, 8.5 para opciones adicionales)")
            print("   Presiona Enter para continuar...")
            input()

if __name__ == "__main__":
    menu_principal()
