# Taller · ¿Este correo es phishing?
**Analítica de texto para ciberseguridad** · expresiones regulares, spaCy, aprendizaje automático y LLM

Un solo cuaderno, cuatro partes: reglas con regex, tubería de NLP con spaCy, modelos de aprendizaje automático (árbol, regresión logística, SVM, LSTM) y un modelo de lenguaje (LLM). Todas resuelven el mismo problema (¿phishing o legítimo?) y se califican con la misma prueba.

## Cómo abrirlo
1. Abre el cuaderno en Google Colab: [Taller_Phishing.ipynb](https://colab.research.google.com/github/lsandinop/analitica-texto-ciberseguridad/blob/main/cuadernos/Taller_Phishing.ipynb)
2. Entra con tu cuenta de Google. Cada persona trabaja en **su propia copia temporal**: no puedes modificar este repositorio.
3. Ejecuta las celdas **en orden** (`Entorno de ejecución → Ejecutar todo` o `Shift + Enter` celda por celda). No hace falta instalar nada: el cuaderno descarga solo el modelo de español de spaCy.
4. Si la sesión se desconecta, vuelve a ejecutar desde la primera celda.

No necesitas GPU ni cuenta de pago. La Parte 4 es una demostración con resultados ya calculados; la llamada en vivo al LLM es opcional y requiere tu propia clave.

## Datos
`datos/phishing_curso.csv`: 1.389 correos en español (728 de phishing y 661 legítimos) con tres columnas: `subject`, `body` y `Label` (1 = phishing, 0 = legítimo).

**Fuente:** Bustio-Martinez, L., et al. *SpaPhish: A Spanish Dataset for Phishing and Psychological Pattern Detection.* Mendeley Data, V3. https://doi.org/10.17632/hz2d6gz7pc.3 · Licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Cambios respecto del original, hechos con fines académicos** (el script `scripts/preparar_phishing.py` los reproduce):
- Se conservan solo asunto, cuerpo y etiqueta.
- Los enlaces, las direcciones de correo y los números largos se reemplazaron por `<URL>`, `<CORREO>` y `<NUM>`.
- Se quitaron 6 correos con el cuerpo casi vacío y los 3 asuntos vacíos se rellenaron con `(sin asunto)`.
- Los nombres propios **no** se enmascararon; puede quedar información personal residual.

Otros archivos: `datos/respuestas_llm.csv` (respuestas del LLM `gpt-4.1-mini` sobre los correos de prueba) y `datos/reglas_llm.md` (reglas aprendidas del entrenamiento que se le entregan al LLM).
