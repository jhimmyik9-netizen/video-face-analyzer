import numpy as np
import pytest

from face_analyzer import detect_faces, analyze_video


class EmptyClassifier:
    def empty(self):
        return False

    def detectMultiScale(self, *args, **kwargs):
        return []


def test_detect_faces_returns_list_for_blank_frame():
    frame = np.zeros((120, 160, 3), dtype=np.uint8)
    assert detect_faces(frame, EmptyClassifier()) == []


def test_sample_every_must_be_positive(tmp_path):
    missing = tmp_path / "missing.mp4"
    with pytest.raises(FileNotFoundError):
        analyze_video(str(missing), str(tmp_path / "out.mp4"), str(tmp_path / "out.csv"), 0)
