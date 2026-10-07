"""
Prepara el archivo de trabajo del curso a partir de SpaPhish (borrador).

Fuente: Bustio-Martinez, L., et al. (2026). SpaPhish: A Spanish Dataset for Phishing and Psychological
Pattern Detection. Mendeley Data, V3. https://doi.org/10.17632/hz2d6gz7pc.3  ·  Licencia CC BY 4.0.

Qué hace (cambios respecto del original, que la licencia pide indicar):
  1. Se queda solo con subject, body y Label (1 = phishing, 0 = legítimo, como en el original).
     Se descartan identificador, fecha, metadatos (adjuntos, saltos, URLs como columna) y anotaciones de persuasión.
  2. Los nombres de columna y la codificación de Label no cambian.
  3. Enmascara datos personales y enlaces dentro del texto: URLs -> <URL>, correos -> <CORREO>,
     números largos (teléfonos, identificadores) -> <NUM>.
  4. Quita los cuerpos de menos de 20 caracteres (sin información) y pone "(sin asunto)" en los asuntos vacíos,
     para que ninguna herramienta los lea como valores nulos.

Uso (desde la carpeta curso_completo):
    python scripts/preparar_phishing.py
"""
import re
import pandas as pd

ORIGEN = "fuentes/Phishing.csv"
DESTINO = "datos/phishing_curso.csv"

df = pd.read_csv(ORIGEN, sep=";", encoding="utf-8-sig")

URL = re.compile(r"(?i)(?:https?://|hxxps?://|www\.)[^\s<>\]\)\"']+")
CORREO = re.compile(r"(?i)(?:mailto:)?[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
NUM = re.compile(r"(?<!\d)\+?\d[\d\s().-]{5,}\d(?!\d)")          # 7 o más dígitos, con separadores comunes


def enmascarar(texto):
    t = str(texto)
    t = URL.sub("<URL>", t)
    t = CORREO.sub("<CORREO>", t)
    t = NUM.sub(lambda m: "<NUM>" if sum(c.isdigit() for c in m.group()) >= 7 else m.group(), t)
    return t


out = pd.DataFrame({
    "subject": df.subject.fillna("(sin asunto)").map(enmascarar),
    "body": df.body.map(enmascarar),
    "Label": df.Label,
})
antes = len(out)
out = out[out.body.str.strip().str.len() >= 20].reset_index(drop=True)
out.to_csv(DESTINO, index=False, encoding="utf-8")
print(f"{DESTINO}: {len(out)} filas ({antes - len(out)} descartadas por cuerpo vacío) · {out.Label.value_counts().to_dict()}")
