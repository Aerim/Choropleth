import plotly.express as px
import pandas as pd
import os
import json

geometry_gj = json.load(open('C:/Users/samsung/Desktop/GGG.geojson',encoding='utf-8'))
dong = pd.read_csv('C:/Users/samsung/Desktop/최종_북구_동별.csv',encoding='utf-8')

fig = px.choropleth(dong, geojson=geometry_gj, locations = 'gid', color='sum_sum', color_continuous_scale='Blues',featureidkey='properties.gid')
fig.update_geos(fitbounds='locations')
fig.update_layout(title_text="python 단계구분도",title_font_size=20)


fig.write_image('choropleth.png')