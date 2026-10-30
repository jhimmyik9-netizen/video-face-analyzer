# Video Face Analyzer
![Python tests](https://github.com/jhimmyik9-netizen/video-face-analyzer/actions/workflows/tests.yml/badge.svg)
Aplicación desarrollada en Python para detectar rostros en videos utilizando OpenCV y un clasificador Haar preentrenado.

## Características

- Lectura de videos locales.
- Detección de rostros en cada fotograma analizado.
- Dibujo de rectángulos alrededor de los rostros detectados.
- Generación de un video con las detecciones.
- Exportación de resultados a un archivo CSV.
- Selección del intervalo de fotogramas para optimizar el procesamiento.
- Pruebas automatizadas con pytest.

## Tecnologías utilizadas

- Python 3.12
- OpenCV
- NumPy
- pytest
- Git y GitHub Actions

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/jhimmyik9-netizen/video-face-analyzer.git
cd video-face-analyzer
```

Crea un entorno virtual:

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Uso

Analizar un video:

```bash
python face_analyzer.py --input "data/demo.mp4" --output "output/annotated.mp4" --csv "output/detections.csv"
```

Analizar cada cinco fotogramas:

```bash
python face_analyzer.py --input "data/demo.mp4" --sample-every 5
```

Los archivos de salida se pueden guardar en la carpeta `output/`.

## Pruebas

Ejecuta las pruebas automatizadas con:

```bash
python -m pytest -v
```

## Estructura del proyecto

```text
video-face-analyzer/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_face_analyzer.py
├── face_analyzer.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Limitaciones

El detector Haar es un método clásico de detección de rostros. Puede presentar limitaciones ante rostros pequeños, perfiles, iluminación deficiente u oclusiones.

Esta aplicación detecta rostros, pero no identifica la identidad de las personas.

## Privacidad y uso responsable

Utiliza videos propios o materiales para los que tengas autorización. Evita publicar videos personales o datos biométricos sin consentimiento.