import os
from pathlib import Path

# Directorio raíz del proyecto (adaptado para Hugging Face Spaces)
ROOT_DIR = Path(__file__).parent.parent

# Directorios para almacenar datos en Hugging Face Spaces
PERTENENCIAS_DIR = os.path.join(ROOT_DIR, 'data', 'pertenencias')
DATASET_FACIAL = os.path.join(ROOT_DIR, 'data', 'dataset_facial')
DATASET_OBJETOS = os.path.join(ROOT_DIR, 'data', 'datasets', 'objetos')

# Configuración de la API para demo
API_URL = 'http://localhost:7860'

# Rutas base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas de modelos (simplificadas para demo)
MODELO_FACIAL = os.path.join(BASE_DIR, 'data', 'models', 'facial', 'modeloEstudiantes.xml')
MODELO_OBJETOS = os.path.join(BASE_DIR, 'data', 'models', 'objetos', 'ModelObjetoFinal.pt')

# Configuraciones de reconocimiento facial
CONFIANZA_MINIMA = 0.6
MAX_FOTOS = 5  # Reducido para demo

# Configuraciones de detección de objetos
CONFIANZA_OBJETO = 0.5

# Configuración de JWT para demo
JWT_SECRET_KEY = 'demo_secret_key_for_hf_spaces'

# Configuración de base de datos para Hugging Face Spaces (SQLite)
DB_CONFIG = {
    'type': 'sqlite',
    'database': 'intelliguard.db'
}

# Configuraciones específicas para Hugging Face Spaces
HF_SPACES_CONFIG = {
    'max_file_size': 10 * 1024 * 1024,  # 10MB máximo por archivo
    'max_images': 50,  # Máximo número de imágenes almacenadas
    'demo_mode': True,
    'cleanup_interval': 3600,  # Limpiar archivos temporales cada hora
}

# Lista de objetos que puede detectar la IA (para demo)
OBJETOS_DETECTABLES = [
    'laptop', 'teléfono', 'tablet', 'calculadora', 'audífonos',
    'mochila', 'libro', 'botella', 'llaves', 'cartera',
    'reloj', 'gafas', 'cargador', 'mouse', 'teclado'
]

# Tipos de objetos para el dropdown
TIPOS_OBJETOS = [
    "Laptop", "Tablet", "Teléfono", "Calculadora", "Audífonos", 
    "Mochila", "Libro", "Botella", "Reloj", "Gafas",
    "Cargador", "Mouse", "Teclado", "Otro"
]

def crear_directorios():
    """Crear directorios necesarios para la aplicación"""
    directorios = [
        PERTENENCIAS_DIR,
        DATASET_FACIAL,
        DATASET_OBJETOS,
        os.path.dirname(MODELO_FACIAL),
        os.path.dirname(MODELO_OBJETOS)
    ]
    
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)
            print(f"📁 Directorio creado: {directorio}")

def verificar_espacio_disponible():
    """Verificar espacio disponible en Hugging Face Spaces"""
    try:
        # Obtener espacio usado
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.exists(filepath):
                    total_size += os.path.getsize(filepath)
        
        # Convertir a MB
        size_mb = total_size / (1024 * 1024)
        
        # Límite aproximado para Hugging Face Spaces
        limit_mb = 1000  # 1GB aproximado
        
        if size_mb > limit_mb * 0.8:  # Advertir al 80%
            print(f"⚠️ Advertencia: Espacio usado {size_mb:.1f}MB de {limit_mb}MB")
            return False
        
        return True
        
    except Exception as e:
        print(f"Error verificando espacio: {e}")
        return True

def limpiar_archivos_temporales():
    """Limpiar archivos temporales antiguos"""
    try:
        import time
        from datetime import datetime, timedelta
        
        # Limpiar imágenes de más de 24 horas
        limite_tiempo = time.time() - (24 * 60 * 60)
        
        directorios_a_limpiar = [PERTENENCIAS_DIR, DATASET_FACIAL]
        
        for directorio in directorios_a_limpiar:
            if os.path.exists(directorio):
                for archivo in os.listdir(directorio):
                    ruta_archivo = os.path.join(directorio, archivo)
                    if os.path.isfile(ruta_archivo):
                        if os.path.getmtime(ruta_archivo) < limite_tiempo:
                            os.remove(ruta_archivo)
                            print(f"🗑️ Archivo temporal eliminado: {archivo}")
                            
    except Exception as e:
        print(f"Error limpiando archivos temporales: {e}")

# Inicializar configuración al importar
if __name__ == "__main__":
    crear_directorios()
    verificar_espacio_disponible()
else:
    # Crear directorios cuando se importe el módulo
    crear_directorios() 