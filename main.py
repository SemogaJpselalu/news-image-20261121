"""News-image-daily entry: copy the front-page image to /output/entry.png.

The image is a one-page newspaper front page summing up the world's news
of Saturday 21 November 2026: six verified stories (Iran strikes US bases
in Bahrain; Russian barrage spills into Poland; Mexico captures Chapo
Isidro; Nasdaq plunges 5.3%; COP31 deadlocks; BepiColombo reaches
Mercury) plus a ticker of three more, composed with PIL and AI
illustrations. Deterministic: the same bytes every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
