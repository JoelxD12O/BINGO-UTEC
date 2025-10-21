# 🎰 BINGO INTERACTIVO - Sistema de Juego Progresivo

**Autor:** Joel M Cayllahua Hilario  
**Institución:** UTEC (Universidad de Ingeniería y Tecnología)  
**Versión:** 3.0  
**Fecha:** Octubre 2025

---

## 📋 Descripción General

Sistema interactivo de **BINGO PROGRESIVO** desarrollado en Python que permite jugar bingo con rondas progresivas (U → T → E → C → APAGÓN). Incluye gestión completa de cartillas, números sorteados, patrones de ganancia y persistencia de datos.

### 🎯 Características Principales

- ✅ **5 Rondas Progresivas** con patrones específicos: U, T, E, C, APAGÓN
- ✅ **Gestión de Cartillas** (agregar, visualizar, guardar/cargar)
- ✅ **Números Sorteados** (del 1 al 90)
- ✅ **Detección Automática de Ganadores** por patrón
- ✅ **Persistencia de Datos** en JSON
- ✅ **Panel Visual Completo** con estado de cartillas
- ✅ **Sistema de Cambio de Rondas** en cualquier momento
- ✅ **Eliminación de Números Sorteados** para correcciones

---

## 🛠️ Requisitos del Sistema

### Requisitos Mínimos
- **Python:** 3.7 o superior
- **Sistema Operativo:** Windows, macOS o Linux
- **Memoria RAM:** Mínimo 512 MB
- **Espacio en Disco:** Mínimo 50 MB
- **Git:** (Opcional, para clonar el repositorio)

### Verificar Python
```powershell
python --version
```

---

## 📦 Instalación

### Opción 1: Descargar o Clonar el Proyecto

**Si tienes Git instalado:**
```powershell
git clone <URL-DEL-REPOSITORIO>
cd bingo
```

**Si descargas manualmente:**
1. Descarga el proyecto como ZIP
2. Extrae en tu carpeta deseada
3. Abre PowerShell o Terminal en esa carpeta

### Opción 2: Verificar Estructura de Archivos

Asegúrate de que tengas estos archivos:
```powershell
ls -Name
```

Debería ver:
- `main.py` - Menú principal
- `juego_bingo.py` - Lógica del juego
- `cartilla.py` - Clase de cartillas
- `gestor_json.py` - Gestión de persistencia
- `gestor_rondas.py` - Control de rondas
- `cartillas.json` - Almacenamiento de cartillas
- `README.md` - Este archivo

### Opción 3: Instalación con Entorno Virtual (Recomendado)

```powershell
# 1. Navegar a la carpeta del proyecto
cd tu-carpeta-bingo

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno (Windows)
.\venv\Scripts\Activate.ps1

# 4. Activar entorno (macOS/Linux)
source venv/bin/activate

# 5. Verificar que Python está activado
# Deberías ver (venv) al inicio de tu línea de comandos
```

---

## 🚀 Cómo Ejecutar

### Ejecución Rápida (Windows, macOS, Linux)

```powershell
# 1. Navega a la carpeta del proyecto
cd ruta-a-tu-carpeta-bingo

# 2. Ejecuta el programa
python main.py
```

### Ejecución Paso a Paso

```powershell
# 1. Abre PowerShell o Terminal en tu carpeta del proyecto
cd ruta-a-tu-carpeta-bingo

# 2. (Opcional) Activa el entorno virtual si lo creaste
.\venv\Scripts\Activate.ps1

# 3. Ejecuta el programa
python main.py

# 4. El programa mostrará el menú principal
🎰 BINGO INTERACTIVO - Ronda 1/5 - Patrón: U
```

### En Caso de Errores

**"command not found: python"**
- Asegúrate de que Python está instalado desde https://www.python.org/
- Marca la opción "Add Python to PATH" durante la instalación
- Reinicia PowerShell/Terminal

**"No such file or directory"**
- Verifica que estés en la carpeta correcta del proyecto
- Usa `ls` o `dir` para ver los archivos

---

## 📖 Guía de Uso

### Menú Principal

```
📋 CARTILLAS
   1. Agregar cartilla (fila por fila)
   2. Agregar cartilla (25 números de una vez)
   3. Ver cartillas actuales
🎮 JUEGO
   4. Ingresar número sorteado
   5. Ver números sorteados
   5.5. Eliminar número sorteado
📊 PANEL Y DATOS
   6. Mostrar panel completo
   7. Mostrar resumen
   8. Ver estado de rondas (U→T→E→C→APAGON)
   8.5. Cambiar a otra ronda
💾 PERSISTENCIA
   9. Guardar cartillas en JSON
   10. Cargar cartillas desde JSON
   11. Guardar juego actual
🔄 OTROS
   0. Salir
```

---

## 🎯 Opciones Detalladas

### 1️⃣ Agregar Cartilla (Fila por Fila)
Ingresa 5 filas de 5 números cada una. El centro (fila 3, columna 3) debe ser 0.

```
Código de la cartilla: 4604
Fila 1/5: 1 2 3 4 5
Fila 2/5: 6 7 8 9 10
Fila 3/5: 11 12 0 13 14
Fila 4/5: 15 16 17 18 19
Fila 5/5: 20 21 22 23 24
```

### 2️⃣ Agregar Cartilla (25 Números de Una Vez)
Ingresa los 25 números separados por espacios o comas.

```
Código de la cartilla: 4700
Ingresa 25 números: 1 2 3 4 5 6 7 8 9 10 11 12 13 0 14 15 16 17 18 19 20 21 22 23 24
```

### 3️⃣ Ingresar Número Sorteado
Ingresa números del 1 al 90. Se marcan automáticamente en todas las cartillas.

```
Ingresa número sorteado (1-90): 25
📌 Número 25 ingresado
✅ Marcado en cartillas: 4604, 4605, 3769
```

### 3.5️⃣ Eliminar Número Sorteado
Elimina un número por error. Desmarca automáticamente de todas las cartillas.

```
Ingresa número a eliminar (1-90): 25
✅ Número 25 eliminado
```

### 4️⃣ Cambiar de Ronda
Cambiar entre las 5 rondas progresivas del juego.

```
Rondas disponibles:
   1. Ronda 1 - Patrón U
   2. Ronda 2 - Patrón T
   3. Ronda 3 - Patrón E
   4. Ronda 4 - Patrón C
   5. Ronda 5 - Patrón APAGON
```

### 🎮 Patrones de Ganancia

| Patrón | Descripción | Ronda |
|--------|-------------|-------|
| **U** | Columna izq + Fila inferior + Columna der | 1 |
| **T** | Fila superior + Columna central | 2 |
| **E** | Columna izq + 3 líneas horizontales | 3 |
| **C** | Columna izq + Fila superior + Fila inferior | 4 |
| **APAGÓN** | Cartilla completamente llena | 5 |

---

## 💾 Persistencia de Datos

### Guardar Cartillas
```
Opción: 10
✅ Cartillas guardadas en 'cartillas.json'
```

### Cargar Cartillas
```
Opción: 11
✅ Cartillas cargadas desde 'cartillas.json'
```

### Guardar Juego Actual
```
Opción: 12
Nombre del archivo: mi_juego.json
✅ Juego guardado en 'mi_juego.json'
```

---

## 📂 Estructura de Archivos

```
bingo/
├── main.py                 # Menú principal e interfaz
├── juego_bingo.py          # Lógica principal del juego
├── cartilla.py             # Clase Cartilla (5x5)
├── gestor_json.py          # Gestión de persistencia
├── gestor_rondas.py        # Control de rondas progresivas
├── cartillas.json          # Base de datos de cartillas
├── README.md               # Este archivo
└── __pycache__/            # Caché de Python
```

---

## 🔧 Solución de Problemas

### Error: "No module named 'main'"
**Solución:** Asegúrate de estar en el directorio correcto:
```powershell
cd c:\Users\Joel\Desktop\2025-II-DELL\2025-2-dell\bingo
python main.py
```

### Error: "cartillas.json not found"
**Solución:** El archivo se crea automáticamente. Si no existe:
```powershell
# Crear archivo vacío
'{}' | Out-File cartillas.json -Encoding utf8
```

### Error: "Python not found"
**Solución:** Instala Python desde https://www.python.org/
Asegúrate de marcar "Add Python to PATH" durante la instalación.

### Cartillas no cargan automáticamente
**Solución:** Verifica que `cartillas.json` contenga datos válidos en formato JSON:
```powershell
# Ver contenido
Get-Content cartillas.json
```

---

## 📝 Ejemplos de Uso

### Ejemplo 1: Jugar una Ronda Completa

```powershell
# 1. Abre PowerShell/Terminal en la carpeta del proyecto
cd tu-carpeta-bingo

# 2. Ejecuta el programa
python main.py

# 3. Agregar cartilla fila por fila (opción 1)
Selecciona una opción: 1
Código de la cartilla: CART-001
Fila 1/5: 1 2 3 4 5
Fila 2/5: 6 7 8 9 10
Fila 3/5: 11 12 0 13 14
Fila 4/5: 15 16 17 18 19
Fila 5/5: 20 21 22 23 24
✅ Cartilla 'CART-001' agregada correctamente

# 4. Ingresar números sorteados (opción 4)
Selecciona una opción: 4
Ingresa número sorteado (1-90): 15
📌 Número 15 ingresado
✅ Marcado en cartillas: CART-001

# 5. Ver panel completo (opción 6)
Selecciona una opción: 6
# Visualiza todas las cartillas con números marcados

# 6. Cambiar de ronda (opción 8.5)
Selecciona una opción: 8.5
Selecciona el número de ronda (1-5): 2
✅ Cambiado a Ronda 2 - Patrón: T
```

### Ejemplo 2: Guardar y Cargar Cartillas

```powershell
# 1. Después de jugar un rato con cartillas...

# 2. Guardar cartillas (opción 9)
Selecciona una opción: 9
✅ Cartillas guardadas en 'cartillas.json'

# 3. Cerrar el programa
Selecciona una opción: 0
👋 ¡Gracias por jugar! Hasta pronto...

# 4. Reabre el programa en otro momento
python main.py

# 5. Las cartillas se cargarán automáticamente
✅ Cartillas cargadas desde 'cartillas.json'
```

### Ejemplo 3: Eliminar un Número por Error

```powershell
# 1. Si sorteaste un número por error...

# 2. Ver números sorteados (opción 5)
Selecciona una opción: 5
📌 Números sorteados: 10
   [3, 7, 15, 22, 25, 28, 30, 35, 42, 50]

# 3. Eliminar número sorteado (opción 5.5)
Selecciona una opción: 5.5
Ingresa número a eliminar (1-90): 15
✅ Número 15 eliminado

# 4. El número ahora está desmarcado de todas las cartillas
```

---

## 🐛 Reportar Errores

Si encuentras un error, por favor:

1. Toma una captura de pantalla del error
2. Anota los pasos exactos que seguiste
3. Contacta al desarrollador

**Información de Contacto:**
- **Desarrollador:** Joel M Cayllahua Hilario
- **Institución:** UTEC

---

## 📜 Licencia

Este proyecto fue desarrollado como parte del curso de programación en UTEC.

---

## 🎓 Créditos

Desarrollado por **Joel M Cayllahua Hilario**  
Universidad de Ingeniería y Tecnología - UTEC

### Herramientas Utilizadas
- **Python 3.7+**
- **JSON** para persistencia
- **OOP** para arquitectura

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 3.0 | Oct 2025 | Sistema completo con 5 rondas, persistencia y UI mejorada |
| 2.0 | Sep 2025 | Agregadas rondas progresivas |
| 1.0 | Ago 2025 | Versión inicial |

---

## ✅ Checklist de Funcionalidades

- ✅ Agregar cartillas (3 métodos)
- ✅ Ver cartillas actuales
- ✅ Ingresar números sorteados
- ✅ Ver números sorteados
- ✅ Eliminar números (corrección)
- ✅ Panel completo visual
- ✅ Resumen de estado
- ✅ 5 rondas progresivas
- ✅ Cambio de rondas
- ✅ Guardar/cargar cartillas
- ✅ Guardar juego actual
- ✅ Detección automática de ganadores
- ✅ Soporte para 12 patrones diferentes

---

**¡Disfruta jugando BINGO! 🎉**

Para más información, consulta los comentarios en el código fuente.
