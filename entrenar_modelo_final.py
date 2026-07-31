"""
entrenar_modelo_final.py

Proyecto: Predicción de la Resistencia a Compresión del Concreto
Grupo 06 - UPC

Objetivo:
Entrenar el modelo Random Forest final (sobre el 100% de los datos,
ya que ganó la comparación en modelo_comparacion.py) y guardarlo en
disco para poder reutilizarlo después sin tener que re-entrenar,
por ejemplo desde predecir_resistencia.py.

Entradas:
    - concrete_data.csv  (dataset original, en la misma carpeta)

Salidas:
    - modelo_random_forest.pkl  (modelo entrenado, listo para usar)
    - rangos_entrenamiento.json (min/max de cada variable, para poder
      avisar si una predicción futura se sale del rango conocido)
"""

import json
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib


RUTA_CSV = "concrete_data.csv"
COLUMNA_OBJETIVO = "concrete_compressive_strength"
RUTA_MODELO = "modelo_random_forest.pkl"
RUTA_RANGOS = "rangos_entrenamiento.json"


def cargar_datos(ruta_csv):
    """Carga el CSV, limpia nombres de columnas y elimina duplicados."""
    df = pd.read_csv(ruta_csv)
    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()
    return df


def entrenar_y_guardar():
    print("=" * 60)
    print("CARGANDO DATOS")
    print("=" * 60)
    df = cargar_datos(RUTA_CSV)
    X = df.drop(columns=[COLUMNA_OBJETIVO])
    y = df[COLUMNA_OBJETIVO]
    print(f"Registros de entrenamiento: {len(df)}")

    print("\n" + "=" * 60)
    print("ENTRENANDO RANDOM FOREST FINAL (100% de los datos)")
    print("=" * 60)
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X, y)
    print("Modelo entrenado.")

    # Guardar el modelo entrenado
    joblib.dump(modelo, RUTA_MODELO)
    print(f"Modelo guardado en: {RUTA_MODELO}")

    # Guardar los rangos (min/max) de cada variable vistos en entrenamiento.
    # Sirve para avisar si una predicción futura se sale del rango conocido
    # (el modelo "adivina" fuera de esa zona, no es confiable ahí).
    rangos = {
        columna: {"min": float(X[columna].min()), "max": float(X[columna].max())}
        for columna in X.columns
    }
    with open(RUTA_RANGOS, "w", encoding="utf-8") as f:
        json.dump(rangos, f, indent=2, ensure_ascii=False)
    print(f"Rangos de entrenamiento guardados en: {RUTA_RANGOS}")

    print("\n¡Listo! Ya puedes usar predecir_resistencia.py con este modelo.")


if __name__ == "__main__":
    entrenar_y_guardar()
