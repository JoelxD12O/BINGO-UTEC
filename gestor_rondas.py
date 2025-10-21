class GestorRondas:
    """Gestiona las rondas progresivas del BINGO (U, T, E, C, APAGON)"""
    
    def __init__(self):
        self.patrones_orden = ['U', 'T', 'E', 'C', 'APAGON']
        self.ronda_actual = 0
        self.ganadores_por_ronda = {
            'U': [],
            'T': [],
            'E': [],
            'C': [],
            'APAGON': []
        }
    
    def obtener_patron_actual(self):
        """Obtiene el patrón de la ronda actual"""
        if self.ronda_actual < len(self.patrones_orden):
            return self.patrones_orden[self.ronda_actual]
        return None
    
    def obtener_numero_ronda(self):
        """Obtiene el número de ronda (1-5)"""
        return self.ronda_actual + 1
    
    def hay_siguiente_ronda(self):
        """Verifica si hay una siguiente ronda"""
        return self.ronda_actual < len(self.patrones_orden) - 1
    
    def avanzar_ronda(self):
        """Avanza a la siguiente ronda"""
        if self.hay_siguiente_ronda():
            self.ronda_actual += 1
            return True
        return False
    
    def agregar_ganador_ronda(self, codigo_cartilla):
        """Agrega un ganador a la ronda actual"""
        patron = self.obtener_patron_actual()
        if patron:
            self.ganadores_por_ronda[patron].append(codigo_cartilla)
    
    def obtener_ganadores_ronda(self):
        """Obtiene los ganadores de la ronda actual"""
        patron = self.obtener_patron_actual()
        if patron:
            return self.ganadores_por_ronda[patron]
        return []
    
    def obtener_resumen_rondas(self):
        """Obtiene un resumen de todas las rondas"""
        return self.ganadores_por_ronda
    
    def mostrar_estado_rondas(self):
        """Muestra el estado de todas las rondas"""
        print("\n" + "="*80)
        print("📊 ESTADO DE RONDAS PROGRESIVAS")
        print("="*80)
        
        for i, patron in enumerate(self.patrones_orden, 1):
            estado = "✅" if i <= self.ronda_actual + 1 else "⏳"
            actual = " ← RONDA ACTUAL" if i == self.ronda_actual + 1 else ""
            ganadores = self.ganadores_por_ronda[patron]
            
            if patron == 'APAGON':
                print(f"{estado} Ronda 5: APAGÓN (Premio Mayor){actual}")
            else:
                print(f"{estado} Ronda {i}: Patrón {patron}{actual}")
            
            if ganadores:
                print(f"    Ganadores: {', '.join(ganadores)}")
            print()
    
    def reiniciar(self):
        """Reinicia todas las rondas"""
        self.ronda_actual = 0
        self.ganadores_por_ronda = {
            'U': [],
            'T': [],
            'E': [],
            'C': [],
            'APAGON': []
        }
