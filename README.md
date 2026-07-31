# Análisis de Resistencia a Compresión del Concreto
## Objetivo del Proyecto
El presente proyecto tiene como finalidad predecir la resistencia a compresión del concreto (medida en MPa) a partir de las proporciones de sus componentes (cemento, escoria de alto horno, cenizas volantes, agua, superplastificante, agregado grueso, agregado fino) y su edad de curado (en días), utilizando técnicas de ciencia de datos y aprendizaje automático.
Este objetivo responde a un problema real de ingeniería estructural: actualmente, determinar la resistencia del concreto requiere ensayos físicos de compresión que toman hasta 28 días de curado. Un modelo predictivo confiable permitiría estimar la resistencia con anticipación, optimizando el diseño de mezclas y reduciendo tiempos y costos en obra, sin reemplazar —pero sí complementar— los ensayos de laboratorio tradicionales.
## 1. Dataset
### **Nombre:** Concrete Compressive Strength Data Set
### **Fuente:** UCI Machine Learning Repository / Kaggle
Este dataset contiene 1030 registros de mezclas de concreto probadas en laboratorio. 
Cada fila representa una mezcla distinta, con 8 variables de entrada (ingredientes y edad) 
y 1 variable de salida (la resistencia a compresión resultante, medida en MPa).
**Variables del dataset:**
- Cemento (kg/m³)
- Escoria de alto horno (kg/m³)
- Cenizas volantes (kg/m³)
- Agua (kg/m³)
- Superplastificante (kg/m³)
- Agregado grueso (kg/m³)
- Agregado fino (kg/m³)
- Edad del concreto (días)
- Resistencia a compresión (MPa) — variable objetivo
## 2. Análisis de dominio
La resistencia a compresión del concreto es una de las propiedades mecánicas más 
importantes en ingeniería estructural, ya que determina la capacidad de un elemento 
(columna, viga, losa, etc.) para soportar cargas sin fallar. Es un valor fundamental 
en el diseño de cualquier estructura de concreto armado, desde edificios hasta puentes.
A diferencia de otros materiales de construcción, el concreto no tiene una resistencia 
fija: depende de la proporción de sus ingredientes (cemento, agua, agregados y aditivos) 
y del tiempo de curado (edad). Tradicionalmente, esta resistencia se estima mediante 
fórmulas empíricas o pruebas físicas de laboratorio (como el ensayo de compresión en 
cilindros de concreto a los 7, 14 o 28 días).
Sin embargo, la relación entre los ingredientes y la resistencia final **no es lineal**: 
por ejemplo, aumentar el agua reduce la resistencia (relación agua-cemento), pero 
aumentar el cemento no siempre la mejora de forma proporcional. Esta complejidad hace 
que el análisis de datos y las técnicas de aprendizaje automático sean útiles para 
predecir la resistencia sin necesidad de esperar los tiempos de curado tradicionales 
(hasta 28 días), lo cual representa un ahorro de tiempo y costos en obra.
Este dataset ha sido ampliamente utilizado en investigaciones de ingeniería civil para 
modelar y predecir la resistencia del concreto usando redes neuronales y otros modelos 
estadísticos, sentando un precedente en el uso de ciencia de datos aplicada a materiales 
de construcción.
## 3. Marco VDS (PCS Framework)
Siguiendo el framework PCS propuesto por Yu, B., & Barter, R. (2024). Veridical Data Science. MIT Press (vdsbook.com), se justifican a continuación los tres principios fundamentales — Predictibilidad, Computabilidad y Estabilidad — aplicados a este proyecto.
### 3.1 Predictibilidad (Predictability)
Se espera que el modelo tenga buena capacidad predictiva porque:
La resistencia a compresión del concreto está determinada por relaciones físico-químicas conocidas entre sus componentes (relación agua-cemento, efecto puzolánico de las cenizas volantes y la escoria, curado en el tiempo), lo que da una base teórica sólida para que existan patrones aprendibles.
El dataset ha sido validado en múltiples estudios previos (Yeh, 1998; Yeh, 2006) donde modelos de redes neuronales lograron predicciones con buen ajuste, lo que sugiere que la señal predictiva en estos datos es real y replicable.
Al tratarse de una relación no lineal entre variables (como ya se explicó en el Análisis de dominio), un modelo de aprendizaje automático puede capturar interacciones que las fórmulas empíricas tradicionales no logran representar completamente.
### 3.2 Computabilidad (Computability)
El problema es computacionalmente viable dado que:
El dataset tiene un tamaño moderado (1030 registros, 9 variables numéricas), lo que permite entrenar y validar modelos sin requerir infraestructura especializada (se puede trabajar en un notebook estándar con librerías como scikit-learn, pandas o TensorFlow).
Todas las variables son numéricas continuas, sin necesidad de codificación compleja de variables categóricas.
No se reportan datos faltantes en la fuente original, lo que simplifica el preprocesamiento y reduce el riesgo de introducir sesgos por imputación.
### 3.3 Estabilidad (Stability)
Para garantizar la estabilidad de los resultados, se plantea evaluar:
Estabilidad ante el muestreo: usando validación cruzada (k-fold) para verificar que el desempeño del modelo no dependa de una partición específica de entrenamiento/prueba.
Estabilidad ante perturbaciones en los datos: comprobando que pequeños cambios (ruido leve, remuestreo con reemplazo tipo bootstrap) no alteren drásticamente las predicciones ni las variables más importantes identificadas por el modelo.
Estabilidad ante la elección del modelo: comparando al menos dos algoritmos distintos (por ejemplo, regresión lineal/regularizada vs. un modelo no lineal como random forest o red neuronal) para verificar que las conclusiones principales (qué variables importan más, qué tan predecible es la resistencia) se mantengan consistentes independientemente del método usado.
## 4. Resultados del Análisis (EDA)

### 4.1. Relación Agua/Cemento vs. Resistencia
![Gráfico Relación A/C](grafico_relacion_ac.png)
**Análisis:** Existe una correlación negativa: a mayor relación agua/cemento, menor resistencia (f'c). La variable "age" (días) muestra que la resistencia aumenta con el tiempo de curado.

### 4.2. Matriz de Correlación
![Matriz de Correlación](matriz_correlacion.png)
**Análisis:** El cemento presenta la correlación más alta con la resistencia. La relación negativa del agua confirma que es la variable crítica a controlar en obra para garantizar la calidad del concreto.

### 4.3 Distribución de Resistencias (Histograma)
![Histograma de Resistencia](histograma_resistencia.png)
**Análisis:** El histograma muestra la frecuencia de los diseños de mezcla agrupados por su resistencia a la compresión. Se observa que la mayor concentración de datos empíricos se encuentra en el rango de 24 a 46 MPa, confirmando que la base de datos es representativa para concretos de resistencia media a alta.

### 4.4 Detección de Valores Atípicos (Boxplot)
![Boxplot de Resistencia](boxplot_resistencia.png)
**Análisis:** El diagrama de caja (boxplot) evalúa la dispersión estadística de la resistencia y detecta valores atípicos (outliers). Se identificaron ensayos anómalos que superan los 80 MPa; estos registros han sido aislados para verificar su dosificación y descartar posibles errores de laboratorio antes de entrenar el modelo predictivo.

## 5. Modelado y Comparación de Resultados

Se entrenaron y compararon dos algoritmos de aprendizaje automático (`modelo_comparacion.py`) mediante validación cruzada de 5 particiones (5-fold cross-validation):

| Modelo | R² | RMSE (MPa) | MAE (MPa) |
|---|---|---|---|
| Regresión Ridge | 0.594 | 10.33 | 8.21 |
| Random Forest | 0.907 | 4.92 | 3.47 |

### 5.1 Comparación de Modelos
![Comparación de Modelos](comparacion_modelos.png)
**Análisis:** Random Forest superó ampliamente a la Regresión Ridge en las tres métricas evaluadas, explicando el 90.7 % de la variabilidad en la resistencia frente a un 59.4 % del modelo lineal. Esto confirma que la relación entre los componentes del concreto y su resistencia es predominantemente no lineal, tal como se anticipó en el marco PCS (sección 3.1).

### 5.2 Importancia de Variables
![Importancia de Variables](importancia_variables.png)
**Análisis:** Las variables más influyentes en la predicción del Random Forest fueron la edad de curado (34.0 %) y el cemento (32.0 %), seguidas por el agua (10.7 %). Este resultado es consistente con el análisis de dominio (sección 2) y con la matriz de correlación (sección 4.2), validando que el modelo capturó relaciones físicamente coherentes con la teoría de diseño de mezclas.

**Código fuente:** [`modelo_comparacion.py`](modelo_comparacion.py)
**Informe completo:** [`Informe_Final_Grupo06.docx`](Informe_Final_Grupo06.docx) (formato IEEE, con metodología, resultados y conclusiones detalladas).

## 6. Implementación y Despliegue del Modelo Predictivo

Para la consolidación de la etapa final del proyecto (T3), el algoritmo de mayor rendimiento empírico (Random Forest) ha sido operacionalizado mediante dos módulos ejecutables. Esta arquitectura permite la simulación de escenarios de dosificación e inferencia de resistencias sin requerir el reentrenamiento computacional del modelo.

### 6.1 Módulo de Consolidación: `entrenar_modelo_final.py`

Este script ejecuta el entrenamiento definitivo del algoritmo utilizando la totalidad del conjunto de datos depurado (1,005 registros). Su propósito fundamental es la persistencia de los metadatos y la parametrización del modelo para su uso en entornos de producción.

* **Artefactos generados:**
  * `modelo_random_forest.pkl`: Archivo binario que contiene el modelo predictivo serializado mediante la librería `joblib`.
  * `rangos_entrenamiento.json`: Diccionario de control de calidad que almacena los límites físicos (valores máximos y mínimos) de cada variable independiente (features) procesada durante la fase de entrenamiento.

### 6.2 Motor de Inferencia: `predecir_resistencia.py`

Constituye la herramienta de estimación final. Este script carga el modelo serializado e ingesta los parámetros de diseño de una mezcla inédita (cuantías de cemento, agua, agregados, aditivos y tiempo de curado) para proyectar su comportamiento mecánico.

* **Protocolo de Validación de Contornos (Boundary Check):** De forma automatizada, el algoritmo contrasta los parámetros de entrada del usuario con los límites almacenados en el archivo `.json`. Si se detecta una dosificación que excede el dominio de los datos de entrenamiento, el sistema emite una alerta de extrapolación, advirtiendo sobre la reducción en la confiabilidad de la predicción.
* **Salida de Datos:** Retorna la estimación cuantitativa de la resistencia a la compresión expresada en Megapascales (**MPa**).

> **Aviso de Cumplimiento Normativo:**
> *Esta herramienta computacional ha sido desarrollada exclusivamente para la optimización teórica e iteración de diseños de mezcla en fase de gabinete. Bajo ninguna circunstancia exime al ingeniero responsable de ejecutar el control de calidad experimental ni reemplaza el ensayo físico normado de compresión en especímenes cilíndricos, de acuerdo con los lineamientos estipulados en la **NTP 339.034** y la **ASTM C39**.*

## 7.Referencias
1. Yeh, I-C. (1998). *Modeling of strength of high performance concrete using 
   artificial neural networks*. Cement and Concrete Research, 28(12), 1797-1808.
2. Yeh, I-C. (2006). *Analysis of strength of concrete using design of experiments 
   and neural networks*. Journal of Materials in Civil Engineering, ASCE, 18(4), 597-604.
3. Yu, B., & Barter, R. (2024). Veridical Data Science. MIT Press. https://vdsbook.com/
4. Chou, J. S., & Pham, A. D. (2013). *Enhanced artificial intelligence for ensemble approach to predicting high performance concrete compressive strength*. Automation in Construction, 29, 43-53.
5. ACI Committee 318. (2019). *Building Code Requirements for Structural Concrete (ACI 318-19) and Commentary*. American Concrete Institute.
6. INDECOPI. (2015). *NTP 339.034: Hormigón (concreto). Método de ensayo para la determinación de la resistencia a la compresión de especímenes cilíndricos de hormigón*. Lima, Perú.
## INTEGRANTES:
### Daniel Francisco Burgos Jaime.
### Jose Fernando Vargas Zolorzano.
### Juan Martin Ubillus Limo.
### Stefhano Felipe Sinarahua Ramos.

## BITACORIA IA
### Bitácora de Desarrollo: Análisis Exploratorio (EDA) y Modelado IA
Actividad:

Entorno de Trabajo: Se configuró el entorno de desarrollo en Python utilizando Visual Studio Code, gestionando las dependencias (pandas, matplotlib, seaborn, scikit-learn) necesarias para el tratamiento de datos estructurales.

Análisis Exploratorio de Datos (EDA): Se ejecutó el script eda_concreto.py para analizar la correlación entre los componentes de la mezcla y la resistencia a la compresión (f'c).

Resultados Técnicos:

Se ejecutó el script modelo_comparacion.py para entrenar y comparar dos algoritmos de aprendizaje automático (Regresión Ridge y Random Forest) mediante validación cruzada de 5 particiones.

Resultados Técnicos:

Se graficó la Comparación de Modelos (R²), confirmando que Random Forest (R² = 0.907) supera ampliamente a la Regresión Ridge (R² = 0.594) en capacidad predictiva.

Se generó el gráfico de Importancia de Variables, validando que la edad de curado (34.0 %) y el cemento (32.0 %) son los factores con mayor influencia sobre la resistencia a compresión.

Conclusión: Los resultados confirman la hipótesis planteada en el marco PCS (sección 3.1): la relación entre los componentes del concreto y su resistencia es no lineal, por lo que un modelo de ensamble como Random Forest resulta más adecuado que un modelo lineal regularizado para este problema.
