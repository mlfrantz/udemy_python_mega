#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:47:14 2021

@author: mlfrantz

Creates a web map using the Folium library.
"""

import folium
import pandas as pd

volcanoes = pd.read_csv("Volcanoes.txt")

# html = """<h4>Volcano information:</h4>
# Elevation: %s m
# """
html = """Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Elevation: %s m
"""

def elev_color(elevation):
    if elevation < 1600:
        return("green")
    elif elevation >= 1600 and elevation < 2800:
        return("orange")
    else:
        return("red")

map = folium.Map(location = [38.58, -99.09],
                 zoom_start=6,
                 tiles="Stamen Terrain"
                 )

fg = folium.FeatureGroup(name="My Map")

for i,v in volcanoes.iterrows():
    #iframe = folium.IFrame(html=html %str(v["ELEV"]), width=200, height=100) #html version basic
    iframe = folium.IFrame(html=html %(v["NAME"], v["NAME"], str(v["ELEV"])), width=200, height=100) #html version advance
    fg.add_child(folium.CircleMarker(location=[v["LAT"], v["LON"]],
                            #popup="Elevation: " + str(v["ELEV"]) + "m",
                            popup = folium.Popup(iframe), #html version
                            tooltip=v["NAME"],
                            color=elev_color(v["ELEV"]), #circlemarker
                            fill=True, #circlemarker
                            fillColor=elev_color(v["ELEV"]) #circlemarker
                            #icon=folium.Icon(color=elev_color(v["ELEV"])) #marker class
                            )
              )

fg.add_child(folium.GeoJson(data=(open("world.json", "r", encoding='utf-8-sig').read())))

map.add_child(fg)



#map.save("Map1.html")
map.save("Map1_html_basic.html")