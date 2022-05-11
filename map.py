import folium
from folium.plugins import MarkerCluster
import pandas as pd


carnation_cafe_coords = [33.811067, -117.919103]
gibson_girl_coords = [33.811165, -117.919086]
refreshment_corner_coords = [33.811440, -117.919081]
plaza_inn_coords = [33.8116963939521, -117.91851581766903]
little_red_wagon_coords = [33.81148556711443, -117.9186905116349]
jolly_holliday_coords = [33.81168285912394, -117.9193818473908]
rancho_del_zocalo_coords = [33.81245859568607, -117.9199964482139]
edelweiss_snacks_coords = [33.81374305708073, -117.91773874128609]
red_rose_coords = [33.81346065509974, -117.9194651550013]
coords_list = []

# disneyland_map = folium.Map(location=[33.812034, -117.918968], zoom_start=15)

# icon_icecream = folium.features.CustomIcon('static/images/', icon_size=(100,100))

# class Map:
#     def __init__(self, center, zoom_start):
#         self.center = center
#         self.zoom_start = zoom_start
    
#     def showMap(self):
#         #Create the map
#         # disneyland_map = folium.Map(location=[33.812034, -117.918968], zoom_start=15)
#         disneyland_map = folium.Map(location = self.center, zoom_start = self.zoom_start)
        
#         folium.Marker(carnation_cafe_coords, tooltip="Carnation Cafe", popup = "<a href='https://eatingdisneyland.com'>Click Me</a>",
#                     icon=folium.Icon(icon_color='orange', icon='fa-coffee', prefix='fa')).add_to(disneyland_map)
#         folium.Marker(gibson_girl_coords, tooltip='Gibson Girl', popup = 'Gibson Girl Ice Cream').add_to(disneyland_map)
#         folium.Marker(refreshment_corner_coords, popup = 'Refreshment Corner',
#                     icon=folium.Icon(icon_color='red', icon='fa-spoon', prefix='fa')).add_to(disneyland_map)
#         folium.Marker(plaza_inn_coords, popup = 'Plaza Inn').add_to(disneyland_map)
#         folium.Marker(little_red_wagon_coords, popup = 'Little Red Wagon').add_to(disneyland_map)
#         folium.Marker(jolly_holliday_coords, popup = 'Jolly Holiday Bakery Cafe', 
#                     icon=folium.Icon(icon_color='dodgerblue', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#         folium.Marker(rancho_del_zocalo_coords, popup = 'Rancho Del Zocalo').add_to(disneyland_map)
#         folium.Marker(edelweiss_snacks_coords, popup = 'Edelweiss Snacks').add_to(disneyland_map)
#         folium.Marker(red_rose_coords, popup = 'Red Rose Taverne').add_to(disneyland_map)

#         disneyland_map.save('templates/disneyland_map.html')

disneyland_map = folium.Map(location=[33.812034, -117.918968], zoom_start=18)

folium.Marker(carnation_cafe_coords, tooltip="Carnation Cafe", popup = "<a href='https://eatingdisneyland.com'>Click Me</a>",
            icon=folium.Icon(icon_color='orange', icon='fa-coffee', prefix='fa')).add_to(disneyland_map)
folium.Marker(gibson_girl_coords, tooltip='Gibson Girl', popup = 'Gibson Girl Ice Cream').add_to(disneyland_map)
folium.Marker(refreshment_corner_coords, popup = 'Refreshment Corner',
            icon=folium.Icon(icon_color='red', icon='fa-spoon', prefix='fa')).add_to(disneyland_map)
folium.Marker(plaza_inn_coords, popup = 'Plaza Inn').add_to(disneyland_map)
folium.Marker(little_red_wagon_coords, popup = 'Little Red Wagon').add_to(disneyland_map)
folium.Marker(jolly_holliday_coords, popup = 'Jolly Holiday Bakery Cafe', 
            icon=folium.Icon(icon_color='dodgerblue', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
folium.Marker(rancho_del_zocalo_coords, popup = 'Rancho Del Zocalo').add_to(disneyland_map)
folium.Marker(edelweiss_snacks_coords, popup = 'Edelweiss Snacks').add_to(disneyland_map)
folium.Marker(red_rose_coords, popup = 'Red Rose Taverne').add_to(disneyland_map)

disneyland_map.save('templates/disneyland_map.html')















# import folium
# import webbrowser

