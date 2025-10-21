import json
import os
from datetime import datetime

class GestorJSON:
    """Clase para gestionar la persistencia de datos en JSON"""
    
    def __init__(self, archivo="cartillas.json"):
        self.archivo = archivo
    
    def guardar_cartillas(self, cartillas_dict):
        """Guarda todas las cartillas en JSON"""
        datos = {}
        for codigo, cartilla in cartillas_dict.items():
            datos[codigo] = {
                "codigo": codigo,
                "matriz": cartilla.matriz,
                "marcados": cartilla.marcados
            }
        
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Cartillas guardadas en '{self.archivo}'")
    
    def cargar_cartillas(self):
        """Carga cartillas desde JSON"""
        if not os.path.exists(self.archivo):
            print(f"⚠️  Archivo '{self.archivo}' no encontrado")
            return {}
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            print(f"✅ Cartillas cargadas desde '{self.archivo}'")
            return datos
        except json.JSONDecodeError:
            print(f"❌ Error al decodificar '{self.archivo}'")
            return {}
    
    def guardar_juego(self, juego, nombre_archivo="juego_guardado.json"):
        """Guarda el estado completo del juego"""
        datos_juego = {
            "timestamp": datetime.now().isoformat(),
            "patron_actual": juego.patron_actual,
            "numeros_sorteados": juego.numeros_sorteados,
            "cartillas_ganadoras": juego.cartillas_ganadoras,
            "cartillas": {}
        }
        
        for codigo, cartilla in juego.cartillas.items():
            datos_juego["cartillas"][codigo] = {
                "codigo": codigo,
                "matriz": cartilla.matriz,
                "marcados": cartilla.marcados
            }
        
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos_juego, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Juego guardado en '{nombre_archivo}'")
    
    def listar_archivos_json(self):
        """Lista todos los archivos JSON en el directorio"""
        archivos = [f for f in os.listdir('.') if f.endswith('.json')]
        if archivos:
            print("\n📁 Archivos JSON disponibles:")
            for i, archivo in enumerate(archivos, 1):
                tamaño = os.path.getsize(archivo)
                print(f"   {i}. {archivo} ({tamaño} bytes)")
            return archivos
        else:
            print("❌ No hay archivos JSON en el directorio")
            return []
