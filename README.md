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
## 4. Referencias
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

