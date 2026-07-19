import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Cargando datos...")
df = pd.read_csv('concrete_data.csv')

# Limpiar espacios en blanco en los nombres de columnas (ej: "fine_aggregate ")
df.columns = df.columns.str.strip()

# --------------------------------------------------------
# PARTE 0: CALIDAD DE DATOS (nulos y duplicados)
# --------------------------------------------------------
print("\n--- CALIDAD DE DATOS ---")
print("Valores nulos por columna:\n", df.isnull().sum())
print("\nCantidad de filas duplicadas:", df.duplicated().sum())

# Calcular la Relación Agua/Cemento
df['Relacion_AC'] = df['water'] / df['cement']

# --------------------------------------------------------
# PARTE 1: RELACIONES ENTRE VARIABLES
# --------------------------------------------------------
print("\nGenerando Gráfico 1...")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Relacion_AC', y='concrete_compressive_strength', data=df, hue='age', palette='viridis', alpha=0.7)
plt.title('Relacion Agua/Cemento vs Resistencia a Compresion')
plt.xlabel('Relacion Agua / Cemento (w/c)')
plt.ylabel('Resistencia (MPa)')
plt.grid(True)
plt.tight_layout()
plt.savefig('grafico_relacion_ac.png')
plt.close()

print("Generando Gráfico 2...")
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlacion de Componentes')
plt.tight_layout()
plt.savefig('matriz_correlacion.png')
plt.close()

print("¡Proceso terminado con éxito!")

# --------------------------------------------------------
# PARTE 2: DETECCIÓN DE ANOMALÍAS Y DISTRIBUCIÓN
# --------------------------------------------------------

# 3. Histograma: Conteo de resistencias
plt.figure(figsize=(8, 6))
sns.histplot(df['concrete_compressive_strength'], bins=20, kde=True, color='steelblue')
plt.title('Cantidad de diseños por Resistencia (MPa)')
plt.xlabel('Resistencia a la compresión (MPa)')
plt.ylabel('Cantidad de ensayos')
plt.savefig('histograma_resistencia.png')
plt.close()

# 4. Boxplot: Detección de errores (Outliers)
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['concrete_compressive_strength'], color='darkorange')
plt.title('Detección de errores en la Resistencia (Boxplot)')
plt.xlabel('Resistencia a la compresión (MPa)')
plt.savefig('boxplot_resistencia.png')
plt.close()

# 5. Investigar los datos atípicos con criterio estadístico (IQR)
Q1 = df['concrete_compressive_strength'].quantile(0.25)
Q3 = df['concrete_compressive_strength'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"\n--- LÍMITES DE OUTLIERS (IQR) ---")
print(f"Q1: {Q1:.2f} | Q3: {Q3:.2f} | IQR: {IQR:.2f}")
print(f"Límite inferior: {limite_inferior:.2f} | Límite superior: {limite_superior:.2f}")

datos_sospechosos = df[
    (df['concrete_compressive_strength'] > limite_superior) |
    (df['concrete_compressive_strength'] < limite_inferior)
]

print(f"\n--- DOSIFICACIÓN DE LOS ENSAYOS ATÍPICOS (fuera del rango IQR) ---")
print(f"Cantidad de outliers detectados: {len(datos_sospechosos)}")
print(datos_sospechosos)
