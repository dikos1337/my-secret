import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DIST_DIR = os.path.join(BASE_DIR, 'dist')
DJANGO_STATIC_DIR = os.path.join(BASE_DIR, "backend", "static", "mysecret")
DJANGO_TEMPLATES_DIR = os.path.join(BASE_DIR, "backend", "mysecret",
                                    "templates", "mysecret")

# STATIC
shutil.copytree(os.path.join(DIST_DIR, 'js'),
                os.path.join(DJANGO_STATIC_DIR, "js"),
                dirs_exist_ok=True)
shutil.copytree(os.path.join(DIST_DIR, 'css'),
                os.path.join(DJANGO_STATIC_DIR, "css"),
                dirs_exist_ok=True)
shutil.copyfile(os.path.join(DIST_DIR, 'favicon.ico'),
                os.path.join(DJANGO_STATIC_DIR, "favicon.ico"))

# # TEMPLATES
shutil.copyfile(os.path.join(DIST_DIR, 'index.html'),
                os.path.join(DJANGO_TEMPLATES_DIR, "index.html"))

print("Files successfully copied.")