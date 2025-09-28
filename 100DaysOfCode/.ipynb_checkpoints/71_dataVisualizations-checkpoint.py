""" Día 71: Visualizaciones de datos interactivos
Cree visualizaciones de datos interactivos con Plotly o Bokeh. """

import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool, ColumnDataSource
# Asegúrate de que las visualizaciones se muestren en el notebook
output_notebook()
# Crear un DataFrame de ejemplo
data = {
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valores': [23, 45, 12, 36],
    'Fechas': pd.date_range(start='2023-01-01', periods=4, freq='M')
}
df = pd.DataFrame(data)
# Visualización interactiva con Plotly
fig = px.bar(df, x='Categoría', y='Valores', title='Gráfico de Barras Interactivo con Plotly')
fig.show()
# Visualización interactiva con Bokeh
source = ColumnDataSource(df)
p = figure(x_range=df['Categoría'], title="Gráfico de Barras Interactivo con Bokeh",
    toolbar_location=None, tools="")
p.vbar(x='Categoría', top='Valores', width=0.9, source=source, legend_field="Categoría",
    line_color='white', fill_color='navy')
hover = HoverTool()
hover.tooltips = [("Categoría", "@Categoría"), ("Valores", "@Valores")]
p.add_tools(hover)
p.xgrid.grid_line_color = None
p.y_range.start = 0
show(p)
# Visualización de series temporales con Plotly
fig2 = px.line(df, x='Fechas', y='Valores', title='Series Temporales Interactivas con Plotly')
fig2.show()
# Visualización de series temporales con Bokeh
p2 = figure(x_axis_type='datetime', title="Series Temporales Interactivas con Bokeh",
            plot_height=300, plot_width=600)
p2.line(df['Fechas'], df['Valores'], line_width=2, color='green')
hover2 = HoverTool()
hover2.tooltips = [("Fecha", "@x{%F}"), ("Valores", "@y")]
hover2.formatters = {'@x': 'datetime'}
p2.add_tools(hover2)
show(p2)

# Output:
# Al ejecutar el script, se crearán y mostrarán varios gráficos interactivos
# utilizando Plotly y Bokeh, incluyendo gráficos de barras y series temporales.

# Comparación con el código del día 70:
# El código del día 70 se centra en la computación numérica utilizando NumPy,
# mientras que este código del día 71 se enfoca en la creación de visualizaciones
# de datos interactivas utilizando Plotly y Bokeh.