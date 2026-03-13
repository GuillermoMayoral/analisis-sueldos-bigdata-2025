import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ==========================================
# 1. CARGA DE DATOS (INTELIGENTE)
# ==========================================
nombre_archivo = 'survey_results_public.csv'

try:
    print("🚀 Iniciando Pipeline de Big Data 2025...")
    # low_memory=False es vital para datasets grandes con tipos de datos mixtos
    df = pd.read_csv(nombre_archivo, low_memory=False)
    print(f"✅ ¡Archivo cargado! Total de registros globales: {len(df)}")
except FileNotFoundError:
    print(f"❌ Error: No se encontró '{nombre_archivo}' en la carpeta.")
    exit()

# ==========================================
# 2. DETECCIÓN AUTOMÁTICA DE COLUMNAS
# ==========================================
# Stack Overflow a veces cambia 'YearsCodePro' por 'WorkExp' en versiones nuevas
col_sueldo = 'ConvertedCompYearly'
posibles_cols_exp = ['YearsCodePro', 'WorkExp', 'YearsCode']

col_exp = None
for c in posibles_cols_exp:
    if c in df.columns:
        col_exp = c
        break

if not col_exp:
    print("❌ Error: No se encontró una columna de experiencia válida.")
    print(f"Columnas disponibles: {df.columns.tolist()[:10]}...") 
    exit()

print(f"🔍 Usando columna de experiencia: '{col_exp}'")

# ==========================================
# 3. FILTRADO Y LIMPIEZA (VERACIDAD)
# ==========================================
# 1. Filtrar por México
df_mex = df[df['Country'] == 'Mexico'].copy()

# 2. Eliminar nulos en las columnas críticas
df_mex = df_mex.dropna(subset=[col_sueldo, col_exp])

# 3. Limpieza de texto a número (para casos como 'More than 50 years')
df_mex[col_exp] = df_mex[col_exp].astype(str).str.replace('More than ', '').str.replace('Less than ', '').str.replace(' years', '')
df_mex[col_exp] = pd.to_numeric(df_mex[col_exp], errors='coerce')

# 4. Segunda limpieza de nulos tras la conversión
df_mex = df_mex.dropna(subset=[col_exp])

# 5. Filtro de Outliers (Sueldos razonables en USD para México)
df_mex = df_mex[(df_mex[col_sueldo] > 3000) & (df_mex[col_sueldo] < 250000)]

print(f"📊 Registros de México listos para el modelo: {df_mex.shape[0]}")

# ==========================================
# 4. MACHINE LEARNING: REGRESIÓN LINEAL
# ==========================================
X = df_mex[col_exp].values.reshape(-1, 1)
y = df_mex[col_sueldo].values.reshape(-1, 1)

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir valores para la línea de tendencia
y_pred = modelo.predict(X)

# ==========================================
# 5. VISUALIZACIÓN PROFESIONAL
# ==========================================
plt.figure(figsize=(12, 7))

# Graficar puntos reales
plt.scatter(X, y, color='royalblue', alpha=0.5, label='Sueldos Reales (México 2025)')

# Graficar línea de regresión
plt.plot(X, y_pred, color='red', linewidth=3, label='Modelo Predictivo (Tendencia)')

plt.title('Análisis de Regresión: Impacto de la Experiencia en el Sueldo (México 2025)', fontsize=14)
plt.xlabel('Años de Experiencia Profesional', fontsize=12)
plt.ylabel('Sueldo Anual (USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Guardar evidencia para el reporte NIST
plt.savefig('evidencia_regresion_2025.png')

# Resultados en consola
print("\n" + "="*40)
print("🎯 RESULTADOS DEL MODELO")
print(f"Puntaje R² (Precisión): {r2_score(y, y_pred):.4f}")
print(f"Incremento anual estimado: ${modelo.coef_[0][0]:,.2f} USD")
print(f"Salario base estimado (0 años): ${modelo.intercept_[0]:,.2f} USD")
print("="*40)
print("📸 Gráfica guardada como 'evidencia_regresion_2025.png'")



# Estadisticas Mexico
salario_min = df_mex[col_sueldo].min()
salario_max = df_mex[col_sueldo].max()
salario_promedio = df_mex[col_sueldo].mean()

print("\n" + "💸" + " análisis de rangos salariales ".upper().center(40, "="))
print(f"Salario más bajo detectado:  ${salario_min:,.2f} USD")
print(f"Salario más alto detectado: ${salario_max:,.2f} USD")
print(f"Salario promedio:           ${salario_promedio:,.2f} USD")
print("="*42 + "\n")

plt.show()