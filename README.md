# Barcode Ticket Generator

Generador de tickets de inventario con codigo de barras Code128. Aplicacion web con interfaz drag-and-drop para crear, previsualizar y descargar tickets en PNG (300 DPI) o imprimir directamente.

## Caracteristicas

- **Codigo de barras Code128** — genera barras validas con texto legible
- **Preview en tiempo real** — cambia nombre, SKU o Instagram y se actualiza al instante
- **Drag and drop** — arrastra nombre, codigo de barras e Instagram para reposicionar dentro del ticket
- **Dimensiones editables** — ancho y alto del ticket en milimetros (default: 60x40 mm)
- **Tamanos de fuente editables** — sliders para nombre, Instagram y texto del barcode
- **Descarga PNG 300 DPI** — imagen de alta resolucion lista para imprimir
- **Impresion** — genera ventana de impresion con el ticket renderizado
- **Codigo limpio** — nombre del archivo descargado: `Nombre_SKU.png`

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalacion

```bash
# 1. Clonar o copiar el proyecto
cd barcode-generator

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### Dependencias

| Paquete | Version | Uso |
|---------|---------|-----|
| fastapi | latest | Framework web |
| uvicorn | latest | Servidor ASGI |
| python-barcode | latest | Generacion de codigos de barras |
| Pillow | latest | Procesamiento de imagenes |
| jinja2 | latest | Templates HTML |

## Ejecucion

```bash
python main.py
```

El servidor arranca en `http://127.0.0.1:8005`. Abre esa URL en tu navegador.

## Uso

### 1. Configurar el ticket

| Campo | Descripcion |
|-------|-------------|
| **Dimensiones** | Ancho y alto del ticket en mm (default: 60x40) |
| **Nombre del Producto** | Texto que aparece arriba del barcode |
| **Codigo de Barras** | Contenido del barcode Code128 (letras, numeros, simbolos) |
| **Perfil de Instagram** | Handle de Instagram sin @ |

### 2. Personalizar tamanos de fuente

Usa los sliders para ajustar:
- Tamaño del nombre (6-24px)
- Tamaño del texto de Instagram (6-18px)
- Tamaño del texto del barcode (6-14px)

### 3. Reposicionar elementos

Haz hover sobre el ticket para ver las asas de arrastre. Arrastra el nombre, el codigo de barras o el Instagram a la posicion deseada.

### 4. Descargar o imprimir

- **Descargar Ticket PNG (300 DPI)** — genera un archivo `Nombre_SKU.png`
- **Imprimir Ticket** — abre ventana de impresion con el ticket renderizado

## Estructura del Proyecto

```
barcode-generator/
├── main.py              # Servidor FastAPI
├── requirements.txt     # Dependencias de Python
├── templates/
│   └── index.html       # Interfaz completa (HTML + Tailwind + JS)
├── static/              # Archivos estaticos
└── barcodes/            # Directorio de salida (no utilizado actualmente)
```

## Tecnologias

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: HTML5, Tailwind CSS (CDN), JavaScript vanilla
- **Librerias CDN**:
  - [JsBarcode](https://github.com/lindell/JsBarcode) — generacion de codigos de barras
  - [html2canvas](https://html2canvas.hertzen.com/) — captura de tickets como imagen
  - [Tailwind CSS](https://tailwindcss.com/) — estilos
