from django.apps import AppConfig
from joblib import load
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class PredapiConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'predAPI'
    # #CLASSIFIER_FOLDER = Path("classifier")
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'predAPI/classifier/')
    #CLASSIFIER_FILE = CLASSIFIER_FOLDER / "resnet18.joblib"
    CLASSIFIER_FILE = resource_path("classifier/resnet18.joblib")
    # CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "resnet18.joblib")
    classifier = load(CLASSIFIER_FILE)
    labelfile = resource_path("classifier/labels.json")
    # labelfile = open(LABELS_FILE)
