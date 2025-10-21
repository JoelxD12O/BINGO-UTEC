class Cartilla:
    """Clase para representar una cartilla de bingo (5x5)"""
    
    def __init__(self, codigo, numeros):
        """
        Inicializa una cartilla de bingo
        
        Args:
            codigo (str): Identificador único de la cartilla
            numeros (list): Lista de 25 números en una matriz 5x5
        """
        self.codigo = codigo
        self.matriz = self._convertir_a_matriz(numeros)
        self.marcados = [[False for _ in range(5)] for _ in range(5)]
        # Marcar el centro (posición 2,2) como especial
        self.marcados[2][2] = True  # Centro es automático en bingo tradicional
    
    def _convertir_a_matriz(self, numeros):
        """Convierte lista de 25 números en matriz 5x5"""
        if len(numeros) != 25:
            raise ValueError("La cartilla debe tener exactamente 25 números")
        matriz = []
        for i in range(5):
            fila = numeros[i*5:(i+1)*5]
            matriz.append(fila)
        return matriz
    
    def marcar_numero(self, numero):
        """
        Marca un número en la cartilla si existe
        
        Args:
            numero (int): Número a marcar
            
        Returns:
            bool: True si el número fue encontrado y marcado
        """
        for i in range(5):
            for j in range(5):
                if self.matriz[i][j] == numero:
                    self.marcados[i][j] = True
                    return True
        return False
    
    def obtener_estado(self):
        """Retorna el estado actual de marcados"""
        return self.marcados
    
    def verificar_linea(self):
        """Verifica si hay una línea completa (horizontal)"""
        for fila in self.marcados:
            if all(fila):
                return True
        return False
    
    def verificar_columna(self):
        """Verifica si hay una columna completa (vertical)"""
        for j in range(5):
            if all(self.marcados[i][j] for i in range(5)):
                return True
        return False
    
    def verificar_diagonal(self):
        """Verifica diagonales completas"""
        # Diagonal principal (arriba-izquierda a abajo-derecha)
        if all(self.marcados[i][i] for i in range(5)):
            return True
        # Diagonal secundaria (arriba-derecha a abajo-izquierda)
        if all(self.marcados[i][4-i] for i in range(5)):
            return True
        return False
    
    def verificar_x(self):
        """Verifica si forma una X (ambas diagonales)"""
        diagonal1 = all(self.marcados[i][i] for i in range(5))
        diagonal2 = all(self.marcados[i][4-i] for i in range(5))
        return diagonal1 and diagonal2
    
    def verificar_l(self):
        """Verifica si forma una L (última fila + última columna)"""
        ultima_fila = all(self.marcados[4])
        ultima_columna = all(self.marcados[i][4] for i in range(5))
        return ultima_fila and ultima_columna
    
    def verificar_z(self):
        """Verifica si forma una Z (primera fila + última fila + diagonal)"""
        primera_fila = all(self.marcados[0])
        ultima_fila = all(self.marcados[4])
        diagonal = all(self.marcados[i][4-i] for i in range(5))
        return primera_fila and ultima_fila and diagonal
    
    def verificar_b(self):
        """Verifica si forma una B (primera columna + líneas interiores)"""
        primera_columna = all(self.marcados[i][0] for i in range(5))
        if not primera_columna:
            return False
        
        # Verificar si hay línea en la fila 2 (medio)
        fila_media = all(self.marcados[2])
        
        # Primera mitad (filas 0-1)
        mitad_superior = all(self.marcados[i][4] for i in range(3))
        
        # Segunda mitad (filas 3-4)
        mitad_inferior = all(self.marcados[i][4] for i in range(2, 5))
        
        return primera_columna and fila_media and mitad_superior and mitad_inferior
    
    def verificar_u(self):
        """Verifica si forma una U (columna izq + fila inferior + columna der)"""
        columna_izq = all(self.marcados[i][0] for i in range(5))
        fila_inferior = all(self.marcados[4])
        columna_der = all(self.marcados[i][4] for i in range(5))
        
        return columna_izq and fila_inferior and columna_der
    
    def verificar_t(self):
        """Verifica si forma una T (fila superior + columna central)"""
        fila_superior = all(self.marcados[0])
        columna_central = all(self.marcados[i][2] for i in range(5))
        
        return fila_superior and columna_central
    
    def verificar_e(self):
        """Verifica si forma una E (primera columna + 3 líneas horizontales)"""
        primera_columna = all(self.marcados[i][0] for i in range(5))
        fila_superior = all(self.marcados[0])
        fila_media = all(self.marcados[2])
        fila_inferior = all(self.marcados[4])
        
        return primera_columna and fila_superior and fila_media and fila_inferior
    
    def verificar_c(self):
        """Verifica si forma una C (primera columna + fila superior + fila inferior)"""
        primera_columna = all(self.marcados[i][0] for i in range(5))
        fila_superior = all(self.marcados[0])
        fila_inferior = all(self.marcados[4])
        
        return primera_columna and fila_superior and fila_inferior
    
    def verificar_cartilla_llena(self):
        """Verifica si toda la cartilla está marcada (apagón)"""
        for fila in self.marcados:
            if not all(fila):
                return False
        return True
    
    def verificar_patron(self, patron):
        """
        Verifica un patrón específico
        
        Args:
            patron (str): 'LINEA', 'COLUMNA', 'DIAGONAL', 'X', 'L', 'Z', 'B', 'U', 'T', 'E', 'C', 'APAGON'
            
        Returns:
            bool: True si se cumple el patrón
        """
        patron = patron.upper()
        
        if patron == 'LINEA':
            return self.verificar_linea()
        elif patron == 'COLUMNA':
            return self.verificar_columna()
        elif patron == 'DIAGONAL':
            return self.verificar_diagonal()
        elif patron == 'X':
            return self.verificar_x()
        elif patron == 'L':
            return self.verificar_l()
        elif patron == 'Z':
            return self.verificar_z()
        elif patron == 'B':
            return self.verificar_b()
        elif patron == 'U':
            return self.verificar_u()
        elif patron == 'T':
            return self.verificar_t()
        elif patron == 'E':
            return self.verificar_e()
        elif patron == 'C':
            return self.verificar_c()
        elif patron == 'APAGON':
            return self.verificar_cartilla_llena()
        else:
            return False
    
    def __str__(self):
        """Representación en string de la cartilla"""
        resultado = f"\n╔ Cartilla {self.codigo} ╗\n"
        resultado += "┌─────────────────────────────┐\n"
        
        for i in range(5):
            resultado += "│ "
            for j in range(5):
                num = self.matriz[i][j]
                if self.marcados[i][j]:
                    resultado += f"[{num:2d}] "
                else:
                    resultado += f" {num:2d}  "
            resultado += "│\n"
        
        resultado += "└─────────────────────────────┘"
        return resultado
    
    def mostrar_simple(self):
        """Mostración simplificada de la cartilla"""
        print(f"\n📋 Cartilla {self.codigo}:")
        print("┌───────────────────────────┐")
        for i in range(5):
            print("│", end="")
            for j in range(5):
                num = self.matriz[i][j]
                if self.marcados[i][j]:
                    print(f" ✓{num:2d}", end="")
                else:
                    print(f"  {num:2d}", end="")
            print("  │")
        print("└───────────────────────────┘")
