"""
predecir_resistencia.py

Proyecto: Predicción de la Resistencia a Compresión del Concreto
Grupo 06 - UPC

Objetivo:
Cargar el modelo Random Forest ya entrenado (ver entrenar_modelo_final.py)
y predecir la resistencia a compresión (MPa) de una mezcla nueva a partir
de sus 8 variables de entrada.

IMPORTANTE (léalo antes de confiar en una predicción):
    - Este modelo es una herramienta COMPLEMENTARIA. NO reemplaza el
      ensayo normado de compresión en cilindros (NTP 339.034 / ASTM C39).
    - Solo es confiable dentro del rango de mezclas con las que fue
      entrenado (dataset UCI). Si su mezcla se sale mucho de esos rangos,
      la función se lo advierte, pero igual entrega un número: úselo con
      cautela y valide siempre con el ensayo físico.
    - Fue entrenado con datos de laboratorio genéricos, no con mezclas
      peruanas específicas (ver "Trabajo futuro" del informe final).

Requisitos previos:
    Ejecutar primero entrenar_modelo_final.py, que genera:
      - modelo_random_forest.pkl
      - rangos_entrenamiento.json
"""

import json
import joblib
import pandas as pd


RUTA_MODELO = "modelo_random_forest.pkl"
RUTA_RANGOS = "rangos_entrenamiento.json"

# Orden exacto de columnas con el que se entrenó el modelo.
# Debe respetarse siempre en el mismo orden al construir el DataFrame.
COLUMNAS = [
    "cement",
    "blast_furnace_slag",
    "fly_ash",
    "water",
    "superplasticizer",
    "coarse_aggregate",
    "fine_aggregate",
    "age",
]


def _cargar_modelo_y_rangos():
    try:
        modelo = joblib.load(RUTA_MODELO)
        with open(RUTA_RANGOS, "r", encoding="utf-8") as f:
            rangos = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            "No se encontró el modelo o los rangos guardados. "
            "Ejecute primero: python entrenar_modelo_final.py"
        ) from e
    return modelo, rangos


def predecir_resistencia(
    cement,
    blast_furnace_slag,
    fly_ash,
    water,
    superplasticizer,
    coarse_aggregate,
    fine_aggregate,
    age,
):
    """
    Predice la resistencia a compresión (MPa) de una mezcla de concreto.

    Todos los parámetros van en kg/m3, excepto `age` que va en días de curado.

    Devuelve:
        dict con:
          - 'resistencia_mpa': predicción del modelo (float)
          - 'fuera_de_rango': lista de variables que se salen del rango
             visto durante el entrenamiento (lista vacía si todo está
             dentro de rango normal)
    """
    modelo, rangos = _cargar_modelo_y_rangos()

    valores = {
        "cement": cement,
        "blast_furnace_slag": blast_furnace_slag,
        "fly_ash": fly_ash,
        "water": water,
        "superplasticizer": superplasticizer,
        "coarse_aggregate": coarse_aggregate,
        "fine_aggregate": fine_aggregate,
        "age": age,
    }

    # Verificar si alguna variable se sale del rango con el que se entrenó
    fuera_de_rango = []
    for columna, valor in valores.items():
        minimo = rangos[columna]["min"]
        maximo = rangos[columna]["max"]
        if valor < minimo or valor > maximo:
            fuera_de_rango.append(
                f"{columna}={valor} (rango de entrenamiento: {minimo:.1f} a {maximo:.1f})"
            )

    X_nuevo = pd.DataFrame([[valores[c] for c in COLUMNAS]], columns=COLUMNAS)
    prediccion = float(modelo.predict(X_nuevo)[0])

    return {
        "resistencia_mpa": prediccion,
        "fuera_de_rango": fuera_de_rango,
    }


def _ejemplo():
    """Ejemplo de uso con una mezcla de prueba."""
    resultado = predecir_resistencia(
        cement=380,
        blast_furnace_slag=0,
        fly_ash=0,
        water=180,
        superplasticizer=6,
        coarse_aggregate=1000,
        fine_aggregate=750,
        age=28,
    )

    print("=" * 60)
    print("PREDICCIÓN DE RESISTENCIA A COMPRESIÓN")
    print("=" * 60)
    print(f"Resistencia estimada: {resultado['resistencia_mpa']:.2f} MPa")

    if resultado["fuera_de_rango"]:
        print("\n⚠ Aviso: las siguientes variables se salen del rango con el que")
        print("  se entrenó el modelo. La predicción es menos confiable ahí:")
        for aviso in resultado["fuera_de_rango"]:
            print(f"   - {aviso}")
    else:
        print("Todas las variables están dentro del rango de entrenamiento.")

    print("\nRecuerde: esta predicción es una estimación preliminar y NO")
    print("reemplaza el ensayo normado de compresión en cilindros.")


if __name__ == "__main__":
    _ejemplo()
