import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. CARGA DE DATOS (PROTEGIDA)
# ==========================================
nombre_archivo = 'survey_results_public.csv'

try:
    print("🚀 Cargando datos para Comparativa de Stacks 2025...")
    # low_memory=False para evitar advertencias de tipos de datos mixtos
    df = pd.read_csv(nombre_archivo, low_memory=False)
except FileNotFoundError:
    print(f"❌ Error: No encontré '{nombre_archivo}'.")
    exit()

# ==========================================
# 2. FILTRADO Y DETECCIÓN DE COLUMNAS
# ==========================================
# Verificamos que las columnas existan (en 2025 los nombres pueden variar levemente)
col_sueldo = 'ConvertedCompYearly'
col_webframe = 'WebframeHaveWorkedWith'

if col_webframe not in df.columns:
    print(f"⚠️ Alerta: No encontré '{col_webframe}'. Buscando alternativa...")
    # Intenta buscar alguna columna que contenga 'Webframe'
    alternativas = [c for c in df.columns if 'Webframe' in c]
    if alternativas:
        col_webframe = alternativas[0]
        print(f"🔍 Usando columna alternativa: {col_webframe}")
    else:
        print("❌ Error: No se encontró columna de Tecnologías Web.")
        exit()

# Filtrar por México y eliminar registros sin sueldo
df_mex = df[(df['Country'] == 'Mexico') & (df[col_sueldo].notnull())].copy()

# ==========================================
# 3. PROCESAMIENTO DE TECNOLOGÍAS (VARIETY)
# ==========================================
def tiene_tech(lista_tech, tecnologia):
    if pd.isna(lista_tech): 
        return False
    # Usamos lower() para que la búsqueda no sea sensible a mayúsculas
    return tecnologia.lower() in str(lista_tech).lower()

# Creamos columnas booleanas para cada tecnología
print("🧹 Procesando stacks tecnológicos...")
df_mex['Es_React'] = df_mex[col_webframe].apply(lambda x: tiene_tech(x, 'React'))
df_mex['Es_Vue'] = df_mex[col_webframe].apply(lambda x: tiene_tech(x, 'Vue.js'))
df_mex['Es_Angular'] = df_mex[col_webframe].apply(lambda x: tiene_tech(x, 'Angular'))

# ==========================================
# 4. CÁLCULO DE MÉTRICAS
# ==========================================
# Calculamos promedios (Agregación)
stats = {
    'React': df_mex[df_mex['Es_React'] == True][col_sueldo].mean(),
    'Vue.js': df_mex[df_mex['Es_Vue'] == True][col_sueldo].mean(),
    'Angular': df_mex[df_mex['Es_Angular'] == True][col_sueldo].mean()
}

# Limpiar posibles valores NaN si no hay suficientes datos para una tecnología
stats = {k: (v if not pd.isna(v) else 0) for k, v in stats.items()}

# ==========================================
# 5. VISUALIZACIÓN DE RESULTADOS
# ==========================================
plt.figure(figsize=(10, 6))
colores = ['#61DBFB', '#42b883', '#dd0031'] # Colores oficiales de React, Vue y Angular

# Crear gráfica de barras
bars = plt.bar(stats.keys(), stats.values(), color=colores, edgecolor='black', alpha=0.8)

# Añadir etiquetas de valor sobre las barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 500, f'${yval:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.title('Sueldo Promedio Anual por Stack Tecnológico en México (Datos 2025)', fontsize=14)
plt.ylabel('Promedio Salarial (USD)')
plt.xlabel('Framework Frontend')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar la gráfica para el reporte NIST
plt.savefig('comparativa_stacks_2025.png')

print("\n" + "="*40)
print("📊 PROMEDIOS CALCULADOS (MÉXICO 2025)")
for tech, sueldo in stats.items():
    print(f"• {tech}: ${sueldo:,.2f} USD")
print("="*40)
print("📸 Gráfica guardada como 'comparativa_stacks_2025.png'")

plt.show()