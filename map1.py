import folium
import pandas as pd


a = pd.read_csv('Volcanoes.txt') 
Lat = list(a["LAT"])
Long = list(a["LON"])
elev = list(a["ELEV"])
map = folium.Map(location=[Lat[0], Long[0]],zoom_start=5,title = "Mapbox Bright")

def get_color(eleveation):
    if eleveation>=3000:
        return 'red'
    elif eleveation>=1000 and eleveation<3000:
        return 'orange'
    else:
        return 'green'



fgv = folium.FeatureGroup(name="Volcanoes")
for i in range(len(Lat)):
    
    fgv.add_child(folium.Marker(location=[Lat[i],Long[i]],popup=elev[i],icon=folium.Icon(color=get_color(elev[i]))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<15000000 else 'black' if 15000000<=x['properties']['POP2005']<25000000  else 'black'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")