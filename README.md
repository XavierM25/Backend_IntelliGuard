# IntelliGuard IA - Backend

Sistema de reconocimiento facial y gestión de pertenencias para instituciones educativas.

## Características

- Reconocimiento facial en tiempo real
- Gestión de pertenencias de estudiantes
- Detección de objetos
- Sistema de autenticación para administradores
- Generación de reportes en PDF

## Requisitos

- Python 3.8+
- PostgreSQL
- OpenCV
- PyTorch
- Flask

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/XavierM25/Backend_IntelliGuard.git
cd Backend_IntelliGuard
```

2. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
   Crear un archivo `.env` con las siguientes variables:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=intelliguard
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
JWT_SECRET=tu_secreto_jwt
```

## Uso

1. Iniciar el servidor:

```bash
python app.py
```

2. Para producción, usar Gunicorn:

```bash
gunicorn app:app --workers 1 --threads 2
```

## API Endpoints

### Autenticación

- `POST /ia/login/administrador` - Login de administrador
- `POST /ia/login/estudiante` - Login de estudiante

### Reconocimiento Facial

- `POST /ia/reconocimiento/capturar` - Capturar rostro
- `POST /ia/reconocimiento/verificar` - Verificar rostro

### Gestión de Pertenencias

- `POST /ia/pertenencias/registrar` - Registrar pertenencia
- `GET /ia/pertenencias/consultar` - Consultar pertenencias
- `POST /ia/pertenencias/registrar-salida` - Registrar salida de pertenencia
- `GET /ia/pertenencias/reporte/pdf` - Generar reporte PDF

### Estudiantes

- `POST /ia/estudiantes/registrar` - Registrar estudiante
- `GET /ia/estudiantes/listar` - Listar estudiantes

## Despliegue

El proyecto está configurado para ser desplegado en Render. Para desplegar:

1. Crear una nueva aplicación web en Render
2. Conectar con el repositorio de GitHub
3. Configurar las variables de entorno necesarias
4. Establecer el comando de inicio: `gunicorn app:app --workers 1 --threads 2`

## Contribución

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
