# 📈 Análisis de Compensación Tech: Maximizar sueldo como Web Developer

> **Proyecto de la Especializante en Big Data** > **Carrera:** Lic. en Tecnologías de la Información  
> **Institución:** Universidad de Guadalajara (CUCEA)

---

## 📝 1. Descripción del Proyecto

Este proyecto surge de la necesidad de identificar los factores críticos que determinan el éxito financiero de un desarrollador web en el ecosistema tecnológico de **Jalisco, México**.

Utilizando el dataset masivo de **Stack Overflow Annual Developer Survey 2025**, se aplican técnicas de **Big Data** y **Machine Learning** para analizar cómo la experiencia profesional y la elección de un stack tecnológico (React, Vue, Angular) impactan directamente en la remuneración económica.

---

## 🛠️ 2. Tecnologías Utilizadas

| Categoría             | Tecnología                                                                                             |
| :-------------------- | :----------------------------------------------------------------------------------------------------- |
| **Lenguaje**          | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **Análisis de Datos** | `Pandas` (DataFrames de gran escala)                                                                   |
| **Machine Learning**  | `Scikit-Learn` (Regresión Lineal)                                                                      |
| **Visualización**     | `Matplotlib` (Gráficas de tendencia)                                                                   |
| **Entorno**           | `VS Code` / `Jupyter Notebooks`                                                                        |

---

## 🌐 3. Características de Big Data (NIST Framework)

- **Volumen:** Procesamiento de más de **65,000 registros globales** con filtrado inteligente para la región de México.
- **Variedad:** Manejo de datos **estructurados** (salarios anuales) y **semi-estructurados** (stacks tecnológicos en formato string multivariado).
- **Veracidad:** Procesos de limpieza de datos nulos y eliminación de _outliers_ para garantizar la fiabilidad del modelo.

---

## 📊 4. Resultados Clave

Basado en las últimas visualizaciones generadas:

1.  **Liderazgo de Stacks:** En el mercado de 2025, **Angular** se posiciona como el framework con el promedio salarial más alto en México (~$34,265 USD), seguido muy de cerca por **React** (~$33,602 USD).
2.  **Tendencia de Experiencia:** El modelo de **Regresión Lineal** confirma una pendiente positiva constante; a pesar de la dispersión de datos, existe un incremento salarial predecible conforme aumentan los años de código profesional.

---

## 🚀 5. Instalación y Uso

### Prerrequisitos

Tener instalado Python 3.x y el gestor de paquetes `pip`.

### Paso a paso

1. **Clonar el repositorio:**

   ```bash
   git clone [https://github.com/GuillermoMayoral/analisis-sueldos-bigdata-2025.git](https://github.com/GuillermoMayoral/analisis-sueldos-bigdata-2025.git)

   ```

2. **Instalar dependencias:**

````bash
 pip install pandas matplotlib scikit-learn

3. **Preparar el Dataset:**
 Descarga el archivo survey_results_public.csv desde Stack Overflow Surveys. https://survey.stackoverflow.co/datasets/stack-overflow-developer-survey-2025.zip
 Colócalo en la carpeta raíz del proyecto.
 Nota: El dataset no se incluye en el repositorio por límites de tamaño y licencias.

4. **Ejecutar el análisis:**
```bash
 python regresionLineal.py

## 🚀 5. Autor e Información Académica

**Autor:** Guillermo Mayoral Mora

**Rol:** Analista de datos | Estudiante de la Lic. en Tecnologías de la Información, UdeG.

**Profesor:** Liliana Ibeth Barbosa Santillan
````
