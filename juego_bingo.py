from cartilla import Cartilla
from gestor_json import GestorJSON
from gestor_rondas import GestorRondas
import os

class JuegoBingo:
    """Clase principal para gestionar el juego de bingo"""
    
    def __init__(self):
        self.cartillas = {}
        self.numeros_sorteados = []
        self.patron_actual = None
        self.cartillas_ganadoras = []
        self.gestor_json = GestorJSON()
        self.gestor_rondas = GestorRondas()
        # Establecer automáticamente el primer patrón (U)
        self.patron_actual = self.gestor_rondas.obtener_patron_actual()
        
        # Cargar cartillas automáticamente si existen
        self._cargar_automatico()
    
    def _cargar_automatico(self):
        """Carga cartillas automáticamente si existe cartillas.json y comienza en RONDA 5"""
        if os.path.exists("cartillas.json"):
            try:
                datos = self.gestor_json.cargar_cartillas()
                if datos:
                    for codigo, datos_cartilla in datos.items():
                        cartilla = Cartilla(codigo, [0]*25)
                        cartilla.matriz = datos_cartilla["matriz"]
                        cartilla.marcados = datos_cartilla["marcados"]
                        self.cartillas[codigo] = cartilla
                    
                    # Automáticamente iniciar en RONDA 5 (patrón APAGON - Premio Mayor)
                    # Hacer skip de las Rondas 1, 2, 3 y 4 directamente
                    self.gestor_rondas.ronda_actual = 4  # Índice 4 = Ronda 5
                    self.patron_actual = self.gestor_rondas.obtener_patron_actual()
                    self.cartillas_ganadoras = []
                    self.numeros_sorteados = []
                    
                    # Reiniciar marcados en todas las cartillas (excepto centro)
                    for cartilla in self.cartillas.values():
                        cartilla.marcados = [[False for _ in range(5)] for _ in range(5)]
                        cartilla.marcados[2][2] = True  # Centro siempre marcado
            except Exception as e:
                pass  # Si hay error, continúa sin cargar
    
    def agregar_cartilla(self, codigo, numeros):
        """
        Agrega una cartilla al juego
        Si el juego ya está en progreso, la nueva cartilla se adapta al estado actual
        
        Args:
            codigo (str): Identificador de la cartilla
            numeros (list): Lista de 25 números
            
        Returns:
            bool: True si se agregó correctamente
        """
        if codigo in self.cartillas:
            print(f"❌ La cartilla con código '{codigo}' ya existe")
            return False
        
        try:
            nueva_cartilla = Cartilla(codigo, numeros)
            
            # Si ya hay números sorteados, marcarlos en la nueva cartilla
            if self.numeros_sorteados:
                for numero in self.numeros_sorteados:
                    nueva_cartilla.marcar_numero(numero)
            
            self.cartillas[codigo] = nueva_cartilla
            print(f"✅ Cartilla '{codigo}' agregada correctamente")
            return True
        except ValueError as e:
            print(f"❌ Error: {e}")
            return False
    
    def ingresar_numero(self, numero):
        """
        Ingresa un número en el juego y lo marca en todas las cartillas
        Verifica automáticamente si hay ganadores
        
        Args:
            numero (int): Número a ingresar
            
        Returns:
            tuple: (cartillas_afectadas, ganadores_nuevos)
        """
        if numero in self.numeros_sorteados:
            print(f"⚠️  El número {numero} ya fue sorteado")
            return [], []
        
        self.numeros_sorteados.append(numero)
        cartillas_afectadas = []
        
        for codigo, cartilla in self.cartillas.items():
            if cartilla.marcar_numero(numero):
                cartillas_afectadas.append(codigo)
        
        print(f"\n📌 Número {numero} ingresado")
        print(f"   Total números sorteados: {len(self.numeros_sorteados)}")
        print(f"   Números: {sorted(self.numeros_sorteados)}")
        
        if cartillas_afectadas:
            print(f"   ✅ Marcado en cartillas: {', '.join(cartillas_afectadas)}")
        else:
            print(f"   ⊘ No aparece en ninguna cartilla")
        
        # Verificar ganadores automáticamente
        nuevos_ganadores = self._verificar_ganadores_automatico()
        
        return cartillas_afectadas, nuevos_ganadores
    
    def eliminar_numero(self, numero):
        """
        Elimina un número sorteado y desmarca en todas las cartillas
        
        Args:
            numero (int): Número a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False si no existía
        """
        if numero not in self.numeros_sorteados:
            print(f"⚠️  El número {numero} no fue sorteado")
            return False
        
        self.numeros_sorteados.remove(numero)
        cartillas_afectadas = []
        
        for codigo, cartilla in self.cartillas.items():
            # Buscar el número en la cartilla y desmarcarlo
            for i in range(5):
                for j in range(5):
                    if cartilla.matriz[i][j] == numero:
                        # Solo desmarcar si no es el centro (comodín)
                        if not (i == 2 and j == 2):
                            cartilla.marcados[i][j] = False
                        cartillas_afectadas.append(codigo)
        
        print(f"\n❌ Número {numero} eliminado")
        print(f"   Total números sorteados: {len(self.numeros_sorteados)}")
        print(f"   Números: {sorted(self.numeros_sorteados)}")
        
        if cartillas_afectadas:
            print(f"   ✅ Desmarcado en cartillas: {', '.join(set(cartillas_afectadas))}")
        
        return True

    def _verificar_ganadores_automatico(self):
        """
        Verifica automáticamente si hay nuevos ganadores
        Se llama cada vez que se ingresa un número
        Maneja el sistema de rondas progresivas
        """
        if not self.patron_actual:
            return []
        
        nuevos_ganadores = []
        
        for codigo, cartilla in self.cartillas.items():
            if codigo not in self.cartillas_ganadoras:
                if cartilla.verificar_patron(self.patron_actual):
                    nuevos_ganadores.append(codigo)
                    self.cartillas_ganadoras.append(codigo)
                    self.gestor_rondas.agregar_ganador_ronda(codigo)
        
        if nuevos_ganadores:
            self._mostrar_bingo_ganador(nuevos_ganadores)
            
            # Preguntar si continuar a siguiente ronda
            if self.gestor_rondas.hay_siguiente_ronda():
                print("\n" + "="*80)
                respuesta_valida = False
                while not respuesta_valida:
                    respuesta = input("¿Continuar a la siguiente ronda? (s/n): ").strip().lower()
                    if respuesta == 's':
                        self._avanzar_a_siguiente_ronda()
                        respuesta_valida = True
                    elif respuesta == 'n':
                        print("\n⏹️  Juego finalizado. Gracias por jugar.")
                        respuesta_valida = True
                    else:
                        print("❌ Respuesta inválida. Por favor ingresa 's' (sí) o 'n' (no)")
        
        return nuevos_ganadores
    
    def _avanzar_a_siguiente_ronda(self):
        """Avanza a la siguiente ronda del juego"""
        if self.gestor_rondas.avanzar_ronda():
            self.patron_actual = self.gestor_rondas.obtener_patron_actual()
            self.cartillas_ganadoras = []  # Reiniciar ganadores para nueva ronda
            self.numeros_sorteados = []     # Reiniciar números sorteados
            
            # Reiniciar marcados en todas las cartillas (excepto centro)
            for cartilla in self.cartillas.values():
                cartilla.marcados = [[False for _ in range(5)] for _ in range(5)]
                cartilla.marcados[2][2] = True  # Centro siempre marcado
            
            print(f"\n🎯 NUEVA RONDA - Ronda {self.gestor_rondas.obtener_numero_ronda()}")
            print(f"   Nuevo patrón: {self.patron_actual}")
            print(f"   Números reiniciados para nueva ronda")
        else:
            print("\n✅ ¡JUEGO FINALIZADO! No hay más rondas disponibles")
    
    def _mostrar_bingo_ganador(self, ganadores):
        """Muestra mensaje de BINGO formateado"""
        print("\n" + "🎉" * 35)
        print("🎉" + " " * 66 + "🎉")
        print("🎉" + "  ¡¡¡BINGO!!!".center(66) + "🎉")
        print("🎉" + " " * 66 + "🎉")
        print("🎉" * 35)
        
        for codigo in ganadores:
            cartilla = self.cartillas[codigo]
            print(f"\n✅ CARTILLA GANADORA: {codigo}")
            print(f"   Patrón: {self.patron_actual}")
            print(f"   Números ingresados para ganar: {sorted(self.numeros_sorteados)}")
            print(f"   Total de números: {len(self.numeros_sorteados)}")
            
            # Mostrar la cartilla ganadora
            print(f"\n   Cartilla ganadora:")
            self._mostrar_cartilla_detalle(cartilla)
        
        print("\n" + "🎉" * 35)
    
    def establecer_patron(self, patron):
        """
        Establece el patrón ganador para esta ronda
        
        Args:
            patron (str): Patrón a buscar ('LINEA', 'COLUMNA', 'X', 'L', 'Z', 'B', 'U', 'T', 'E', 'C', 'APAGON')
        """
        patrones_validos = ['LINEA', 'COLUMNA', 'DIAGONAL', 'X', 'L', 'Z', 'B', 'U', 'T', 'E', 'C', 'APAGON']
        patron = patron.upper()
        
        if patron not in patrones_validos:
            print(f"❌ Patrón no válido. Opciones: {', '.join(patrones_validos)}")
            return False
        
        self.patron_actual = patron
        print(f"🎯 Patrón establecido: {patron}")
        return True
    
    def verificar_ganadores(self):
        """
        Verifica si hay ganadores según el patrón actual
        
        Returns:
            list: Lista de códigos de cartillas ganadoras
        """
        if not self.patron_actual:
            print("⚠️  No hay patrón establecido")
            return []
        
        nuevos_ganadores = []
        
        for codigo, cartilla in self.cartillas.items():
            if codigo not in self.cartillas_ganadoras:
                if cartilla.verificar_patron(self.patron_actual):
                    nuevos_ganadores.append(codigo)
                    self.cartillas_ganadoras.append(codigo)
        
        if nuevos_ganadores:
            print(f"\n🎉 ¡BINGO! Cartillas ganadoras: {', '.join(nuevos_ganadores)}")
            for codigo in nuevos_ganadores:
                print(f"   ✅ Cartilla {codigo} completó patrón {self.patron_actual}")
        
        return nuevos_ganadores
    
    def mostrar_panel(self):
        """Muestra el panel con todas las cartillas"""
        print("\n" + "="*80)
        print(f"PANEL DE BINGO - Patrón: {self.patron_actual or 'No establecido'}")
        print(f"Números sorteados: {len(self.numeros_sorteados)} - {sorted(self.numeros_sorteados)}")
        print("="*80)
        
        for codigo, cartilla in self.cartillas.items():
            estado = "🏆 GANADOR" if codigo in self.cartillas_ganadoras else "En juego"
            print(f"\n{cartilla} [{estado}]")
    
    def mostrar_resumen(self):
        """Muestra un resumen del juego"""
        print("\n" + "="*80)
        print("RESUMEN DEL JUEGO")
        print("="*80)
        print(f"Cartillas activas: {len(self.cartillas)}")
        print(f"Números sorteados: {len(self.numeros_sorteados)}")
        print(f"Patrón ganador: {self.patron_actual or 'No establecido'}")
        print(f"Cartillas ganadoras: {len(self.cartillas_ganadoras)}")
        
        if self.cartillas_ganadoras:
            print(f"   Ganadores: {', '.join(self.cartillas_ganadoras)}")
    
    def _mostrar_cartilla_detalle(self, cartilla):
        """Muestra una cartilla con detalle de marcados"""
        print("   ┌───────────────────────────────┐")
        for i in range(5):
            print("   │ ", end="")
            for j in range(5):
                num = cartilla.matriz[i][j]
                if cartilla.marcados[i][j]:
                    print(f"✓{num:2d} ", end="")
                else:
                    print(f" {num:2d} ", end="")
            print("│")
        print("   └───────────────────────────────┘")
    
    def cambiar_ronda(self, numero_ronda):
        """
        Cambia a una ronda específica
        
        Args:
            numero_ronda (int): Número de ronda (1-5)
            
        Returns:
            bool: True si el cambio fue exitoso
        """
        if numero_ronda < 1 or numero_ronda > 5:
            print("❌ El número de ronda debe estar entre 1 y 5")
            return False
        
        ronda_index = numero_ronda - 1
        self.gestor_rondas.ronda_actual = ronda_index
        self.patron_actual = self.gestor_rondas.obtener_patron_actual()
        self.numeros_sorteados = []
        self.cartillas_ganadoras = []
        
        # Reiniciar marcados en todas las cartillas
        for cartilla in self.cartillas.values():
            cartilla.marcados = [[False for _ in range(5)] for _ in range(5)]
            cartilla.marcados[2][2] = True  # Centro siempre marcado
        
        print(f"\n✅ Cambiado a Ronda {numero_ronda} - Patrón: {self.patron_actual}")
        return True
    
    def reset_juego(self):
        """Reinicia el juego completamente"""
        self.numeros_sorteados = []
        self.cartillas_ganadoras = []
        self.gestor_rondas.reiniciar()
        self.patron_actual = self.gestor_rondas.obtener_patron_actual()
        
        for cartilla in self.cartillas.values():
            cartilla.marcados = [[False for _ in range(5)] for _ in range(5)]
            cartilla.marcados[2][2] = True  # Centro marcado
        
        print("\n🔄 Juego reiniciado - Volviendo a Ronda 1 (Patrón U)")
    
    def mostrar_estado_rondas(self):
        """Muestra el estado de todas las rondas progresivas"""
        self.gestor_rondas.mostrar_estado_rondas()
    
    def obtener_numero_ronda(self):
        """Obtiene el número de ronda actual"""
        return self.gestor_rondas.obtener_numero_ronda()
    
    def guardar_cartillas(self, nombre_archivo="cartillas.json"):
        """Guarda las cartillas en JSON"""
        self.gestor_json.guardar_cartillas(self.cartillas)
    
    def cargar_cartillas_desde_json(self, nombre_archivo="cartillas.json"):
        """Carga cartillas desde JSON"""
        from cartilla import Cartilla
        datos = self.gestor_json.cargar_cartillas()
        
        for codigo, datos_cartilla in datos.items():
            cartilla = Cartilla(codigo, [0]*25)
            cartilla.matriz = datos_cartilla["matriz"]
            cartilla.marcados = datos_cartilla["marcados"]
            self.cartillas[codigo] = cartilla
        
        print(f"✅ {len(self.cartillas)} cartillas cargadas")

    
    def guardar_juego(self, nombre_archivo="juego_guardado.json"):
        """Guarda el estado completo del juego"""
        self.gestor_json.guardar_juego(self, nombre_archivo)
