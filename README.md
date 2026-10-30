# Video Face Analyzer

Aplicación de línea de comandos en Python para detectar rostros en videos, dibujar rectángulos y exportar detecciones a CSV. Utiliza OpenCV y su clasificador Haar preentrenado.

## Funcionalidades

- Lee videos locales.
- Detecta rostros en fotogramas.
- Genera un video anotado.
- Exporta `frame`, tiempo, número de rostros y coordenadas a CSV.
- Permite analizar cada N fotogramas para reducir el tiempo de procesamiento.
- Incluye pruebas unitarias con pytest.

## Instalación

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
```

## Uso

```bash
python face_analyzer.py --input "data/demo.mp4" --output "output/annotated.mp4" --csv "output/detections.csv"
```

Analizar cada quinto fotograma:

```bash
python face_analyzer.py --input "data/demo.mp4" --sample-every 5
```

Ejecutar pruebas:

```bash
pytest -v
```

## Estructura

```text
video-face-analyzer/
├── face_analyzer.py
├── requirements.txt
├── tests/
│   └── test_face_analyzer.py
└── README.md
```

## Limitaciones

Haar es un detector clásico y puede fallar con rostros pequeños, perfiles, poca luz u oclusiones. Esta versión detecta rostros, no identifica a las personas. Para una evolución, se pueden comparar detectores y medir precisión/recall sobre un conjunto de datos autorizado.

## Privacidad

Utiliza únicamente videos propios o para los que tengas permiso. No publiques videos personales ni datos biométricos en el repositorio.
