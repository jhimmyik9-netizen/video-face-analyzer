"""Analiza un video y detecta rostros usando el clasificador Haar de OpenCV.

Esta versión realiza detección facial, no reconocimiento de identidad.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable

import cv2


def detect_faces(frame, classifier=None):
    """Devuelve rectángulos (x, y, w, h) de rostros detectados."""
    if classifier is None:
        classifier = cv2.CascadeClassifier(
            str(Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml")
        )
    if classifier.empty():
        raise RuntimeError("No se pudo cargar el clasificador Haar de OpenCV.")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    return [tuple(map(int, face)) for face in faces]


def analyze_video(input_path: str, output_path: str, csv_path: str, sample_every: int = 1):
    """Procesa el video y guarda un MP4 anotado y un CSV de detecciones."""
    source = Path(input_path)
    if not source.is_file():
        raise FileNotFoundError(f"No existe el video de entrada: {source}")
    if sample_every < 1:
        raise ValueError("sample_every debe ser mayor o igual a 1.")

    cap = cv2.VideoCapture(str(source))
    if not cap.isOpened():
        raise ValueError(f"No se pudo abrir el video: {source}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if width <= 0 or height <= 0:
        cap.release()
        raise ValueError("El video no contiene dimensiones válidas.")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    csv_file = Path(csv_path)
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    writer = cv2.VideoWriter(
        str(output), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )
    if not writer.isOpened():
        cap.release()
        raise RuntimeError("No se pudo crear el video de salida.")

    classifier = cv2.CascadeClassifier(
        str(Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml")
    )
    frame_index = 0
    try:
        with csv_file.open("w", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(["frame", "timestamp_seconds", "face_count", "x", "y", "width", "height"])
            while True:
                ok, frame = cap.read()
                if not ok:
                    break

                if frame_index % sample_every == 0:
                    faces = detect_faces(frame, classifier)
                    timestamp = frame_index / fps
                    for x, y, w, h in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        csv_writer.writerow([frame_index, round(timestamp, 3), len(faces), x, y, w, h])
                    if not faces:
                        csv_writer.writerow([frame_index, round(timestamp, 3), 0, "", "", "", ""])
                    cv2.putText(
                        frame, f"Rostros detectados: {len(faces)}",
                        (12, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
                    )
                writer.write(frame)
                frame_index += 1
    finally:
        cap.release()
        writer.release()

    return {"frames_processed": frame_index, "fps": fps, "output_video": str(output), "csv_report": str(csv_file)}


def main():
    parser = argparse.ArgumentParser(description="Detecta rostros en un video y genera un CSV.")
    parser.add_argument("--input", required=True, help="Ruta del video de entrada")
    parser.add_argument("--output", default="output/annotated.mp4", help="Ruta del video anotado")
    parser.add_argument("--csv", default="output/detections.csv", help="Ruta del reporte CSV")
    parser.add_argument("--sample-every", type=int, default=1, help="Analizar cada N fotogramas")
    args = parser.parse_args()

    result = analyze_video(args.input, args.output, args.csv, args.sample_every)
    print("Análisis finalizado:")
    for key, value in result.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
