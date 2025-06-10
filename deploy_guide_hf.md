# 🚀 Guía de Despliegue en Hugging Face Spaces

## 📋 Preparación de Archivos

### 1. Archivos Principales para Hugging Face

Asegúrate de tener estos archivos en tu proyecto:

```
IntelliGuard_HF/
├── gradio_app.py          # ✅ Creado - Aplicación principal
├── requirements_hf.txt    # ✅ Creado - Dependencias optimizadas
├── README_HF.md          # ✅ Creado - README para HF Spaces
├── Dockerfile_HF         # ✅ Creado - Docker optimizado
├── .dockerignore_hf      # ✅ Creado - Exclusiones Docker
├── utils/config_hf.py    # ✅ Creado - Configuración HF
├── core/                 # 📁 Carpeta de módulos principales
├── utils/                # 📁 Utilities (adaptados)
└── data/                 # 📁 Directorios de datos (vacíos)
```

### 2. Renombrar Archivos para HF

```bash
# Renombrar archivos para usar en HF Spaces
mv requirements_hf.txt requirements.txt
mv README_HF.md README.md
mv Dockerfile_HF Dockerfile
mv .dockerignore_hf .dockerignore
mv utils/config_hf.py utils/config.py
```

## 🌐 Crear Space en Hugging Face

### Paso 1: Crear Cuenta

1. Ve a https://huggingface.co/
2. Regístrate con tu email (GRATIS, sin tarjeta)
3. Verifica tu email

### Paso 2: Crear New Space

1. Click en tu avatar → "New Space"
2. **Owner**: Tu username
3. **Space name**: `intelliguard-ia`
4. **License**: MIT
5. **Select the SDK**: **Gradio**
6. **Space hardware**: **CPU basic** (gratuito)
7. **Visibility**: Public (para plan gratuito)

### Paso 3: Configurar Metadata

En el README.md, asegúrate que tenga al inicio:

```yaml
---
title: IntelliGuard IA
emoji: 🎓
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: gradio_app.py
pinned: false
license: mit
---
```

## 📁 Subir Archivos a HF Spaces

### Opción A: Interfaz Web (Recomendado)

1. **En tu Space recién creado**:

   - Click "Files" → "Upload files"
   - Arrastra y suelta:
     - `gradio_app.py`
     - `requirements.txt`
     - `README.md`

2. **Subir carpetas**:
   - Crea carpeta `core/` y sube los archivos de tu carpeta core
   - Crea carpeta `utils/` y sube los archivos de utils
   - Crea carpeta `data/` (vacía, se creará automáticamente)

### Opción B: Git (Avanzado)

```bash
# Clonar tu space
git clone https://huggingface.co/spaces/TU_USERNAME/intelliguard-ia
cd intelliguard-ia

# Copiar archivos
cp path/to/gradio_app.py .
cp path/to/requirements.txt .
cp path/to/README.md .
cp -r path/to/core/ .
cp -r path/to/utils/ .

# Commit y push
git add .
git commit -m "🚀 Deploy IntelliGuard IA to HF Spaces"
git push
```

## ⚙️ Configuración Específica

### 1. Variables de Entorno (Opcional)

En tu Space → Settings → Repository secrets:

```
HF_TOKEN=tu_token_hf
DEMO_MODE=true
MAX_USERS=50
```

### 2. Configurar Hardware

- **CPU basic**: Gratuito, 2 vCPU, 16GB RAM
- **CPU upgrade**: $0.05/hora, 8 vCPU, 32GB RAM
- **GPU T4**: $0.60/hora (solo si necesitas GPU)

Para este proyecto, **CPU basic es suficiente** ✅

## 🔧 Adaptaciones Específicas

### 1. Modificar core/reconocimiento/facial.py

```python
# Agregar al inicio del archivo
import os
import sqlite3

class ReconocimientoFacial:
    def __init__(self):
        # Usar rutas relativas para HF Spaces
        self.dataset_path = "data/dataset_facial"
        os.makedirs(self.dataset_path, exist_ok=True)

        # Usar Haar Cascade básico si no hay modelo entrenado
        try:
            self.detector = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
        except:
            print("⚠️ Usando detector básico para demo")
```

### 2. Modificar utils/database.py

```python
import sqlite3
import os

class Database:
    def __init__(self):
        # Usar SQLite en lugar de PostgreSQL para HF Spaces
        self.db_path = "intelliguard.db"
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.crear_tablas()

    def crear_tablas(self):
        cursor = self.conn.cursor()
        # SQL adaptado para SQLite...
```

## 🚀 Despliegue y Verificación

### 1. Build Automático

- HF Spaces construirá automáticamente tu aplicación
- Verás logs en tiempo real en la pestaña "Logs"
- El proceso toma 5-15 minutos

### 2. Verificar Funcionamiento

```bash
# Tu app estará disponible en:
https://TU_USERNAME-intelliguard-ia.hf.space

# Ejemplo:
https://xavierintelliaguard-intelliguard-ia.hf.space
```

### 3. Probar Funcionalidades

1. ✅ **Registro de estudiantes**: Subir foto y código
2. ✅ **Reconocimiento facial**: Probar con foto
3. ✅ **Gestión pertenencias**: Registrar objeto
4. ✅ **Detección IA**: Subir imagen para análisis
5. ✅ **Consultas**: Ver reportes y listas

## 🛠️ Solución de Problemas

### Error: "No module named 'core'"

```bash
# Asegúrate de que la estructura de carpetas sea correcta
core/
├── __init__.py
├── reconocimiento/
│   ├── __init__.py
│   └── facial.py
└── ...
```

### Error: "Requirements installation failed"

```bash
# Verificar requirements.txt
gradio==4.44.0  # Versión exacta
opencv-python-headless==4.8.1.78  # headless para servidores
# ... resto de dependencias
```

### Error: "Out of memory"

```bash
# Optimizar uso de memoria en gradio_app.py
def limpiar_memoria():
    gc.collect()
    # Llamar después de cada operación pesada
```

### Space se queda "Building"

1. Revisar logs en tiempo real
2. Verificar sintaxis de requirements.txt
3. Comprobar que app_file esté correcto
4. Restart space si es necesario

## 📊 Monitoreo y Mantenimiento

### 1. Ver Logs

- Pestaña "Logs" en tu Space
- Logs en tiempo real durante ejecución

### 2. Estadísticas de Uso

- Pestaña "Analytics"
- Número de usuarios, tiempo de uso, etc.

### 3. Actualizaciones

```bash
# Para actualizar tu app
git add .
git commit -m "📝 Update: nueva funcionalidad"
git push

# O usar interfaz web: Files → Upload files
```

## 🎯 Resultado Final

Tu IntelliGuard IA estará funcionando en:

- ✅ **URL pública**: `https://tu-usuario-intelliguard-ia.hf.space`
- ✅ **16 GB RAM gratuitos**
- ✅ **Sin límite de tiempo**
- ✅ **SSL automático**
- ✅ **CDN global**
- ✅ **0% costo** 💰

## 📞 Soporte

Si tienes problemas:

1. **Documentación HF**: https://huggingface.co/docs/hub/spaces
2. **Foro Community**: https://discuss.huggingface.co/
3. **Discord HF**: https://discord.gg/hugging-face
4. **Ejemplos**: https://huggingface.co/spaces

---

🎉 **¡Felicidades! Tu sistema IntelliGuard IA ya está funcionando en Hugging Face Spaces!**
