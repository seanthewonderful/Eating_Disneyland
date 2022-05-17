import folium
from folium.plugins import MarkerCluster
import pandas as pd
from flask import url_for


def make_map(restaurants):
    
    disneyland_map = folium.Map(location=[33.812034, -117.918968], zoom_start=16, min_zoom=15, max_zoom=19)
    
    for each in restaurants:
        html = """
                <div class="card text-center" style="max-width: 22rem;">
                        <img class="card-img-top" src="{0}" alt="an image should be here..." style="max-width: 20rem;">
                                <div class="card-body">
                                        <h3 class="card-title">{1}</h3>
                                        <h5 class="card-text" style="-webkit-text-stroke: 1px green; color: green;">{2}</h5>
                                        <h6 class="card-text" style="font-style: italic;">{3}</h6>
                                        <a href="{{ url_for('eating_place', rest_id={4}) }}" class="btn btn-primary">See Details</a>
                                </div>
                </div>
                """
        popup = folium.Popup(html.format(each.image_url, each.name, each.expense, each.land, each.rest_id), max_width=200)
        folium.Marker([each.x_coord, each.y_coord], tooltip=each.name, popup=popup,
                icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
        
        disneyland_map.save('templates/disneyland_map.html')
        # return disneyland_map.render()









# carnation_cafe_coords = [33.811067, -117.919103]
# gibson_girl_coords = [33.811165, -117.919086]
# market_house_coords = [33.810929374836455, -117.91888406625188]
# refreshment_corner_coords = [33.811440, -117.919081]
# jolly_holliday_coords = [33.81168285912394, -117.9193818473908]
# plaza_inn_coords = [33.8116963939521, -117.91851581766903]
# pizza_planet_coords = [33.811728031793685, -117.91691154585381]
# galactic_grill_coords = [33.8123815226415, -117.91715260949891]
# edelweiss_snacks_coords = [33.81374305708073, -117.91773874128609]
# troubador_tavern_coords = [33.8144856242707, -117.91875940912425]
# daisys_diner_coords = [33.81551618186138, -117.91871838555176]
# plutos_doghouse_coords = [33.81554960890238, -117.91871033892531]
# clarabelles_coords = [33.81557802187698, -117.91868821070254]
# red_rose_coords = [33.81346065509974, -117.9194651550013]
# milk_stand_coords = [33.814428886234296, -117.92069637808706]
# ogas_cantina_coords = [33.8147258031444, -117.920964585531]
# docking_bay_coords = [33.81469267859092, -117.92147272989884]
# ronto_roasters_coords = [33.814462613156586, -117.92153869443413]
# hungry_bear_coords = [33.812590935972715, -117.92260721018377]
# harbour_galley_coords = [33.812041180621804, -117.9219757109676]
# mint_julep_coords = [33.811182398373205, -117.92166376575899]
# french_market_coords = [33.81125204155685, -117.92162085041623]
# cafe_orleans_coords = [33.811243684377416, -117.92120041416223]
# blue_bayou_coords = [33.811113869426435, -117.9210944669072]
# river_belle_coords = [33.81149662796846, -117.92051108644743]
# bengal_bbq_coords = [33.81154732802444, -117.92031126189028]
# stage_door_coords = [33.81189888473691, -117.9203206496091]
# golden_horseshoe_coords = [33.812048755541824, -117.9202844397871]
# turkey_leg_cart = [33.812423735113434, -117.92057041285449]
# rancho_del_zocalo_coords = [33.81245859568607, -117.9199964482139]
# maurices_treats_coords = [33.81250160079871, -117.91931709893191]
# little_red_wagon_coords = [33.81148556711443, -117.9186905116349]
# royal_street_veranda_coords = [33.811242012942394, -117.92095096871431]


# def make_map(restaurant):
#     name = restaurant.name
#     html = """
#             <div>
#             <img style="max-width: 175px;" src="https://farm8.static.flickr.com/7384/12143860156_c84d299f7e_b.jpg"><br>
#             <h4>{0}</h4>
#             <p>Here's the Harbour Galley</p>
#             </div>
#             """
#     # iframe = folium.Element.IFrame(html=html, width=500, height=400)
#     popup = folium.Popup(html.format(name), max_width=200)

#     disneyland_map = folium.Map(location=[33.812034, -117.918968], zoom_start=16, min_zoom=15, max_zoom=19)

#     folium.Marker(carnation_cafe_coords, tooltip="Carnation Cafe", popup = "<a href='https://eatingdisneyland.com'>Click Me</a>",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(gibson_girl_coords, tooltip='Gibson Girl', popup = 'Gibson Girl Ice Cream',
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(refreshment_corner_coords, tooltip='Refreshment Corner', popup = 'Refreshment Corner',
#                 icon=folium.Icon(icon_color='white', icon='fa-spoon', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(plaza_inn_coords, tooltip="Plaza Inn", popup = 'Plaza Inn',
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(little_red_wagon_coords, tooltip='Little Red Wagon', popup = 'Little Red Wagon',
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(jolly_holliday_coords, tooltip='Jolly Holiday Bakery Cafe', popup = 'Jolly Holiday Bakery Cafe', 
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(rancho_del_zocalo_coords, tooltip="Rancho del Zocalo", popup = 'Rancho Del Zocalo',
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(edelweiss_snacks_coords, tooltip="Edelweiss Snacks", popup = 'Edelweiss Snacks',
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(red_rose_coords, tooltip="Red Rose Taverne", popup = 'Red Rose Taverne',
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(pizza_planet_coords, tooltip="Alien Pizza Planet", popup="Alien Pizza Planet",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(galactic_grill_coords, tooltip="Galactic Grill", popup="Galactic Grill",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(edelweiss_snacks_coords, tooltip="Edelweiss Snacks", popup="Edelweiss Snacks",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(troubador_tavern_coords, tooltip="Troubador Tavern", popup="Troubador Tavern",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(daisys_diner_coords, tooltip="Daisy's Diner", popup="Daisy's Diner",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(plutos_doghouse_coords, tooltip="Pluto's Doghouse", popup="Pluto's Doghouse",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(clarabelles_coords, tooltip="Clarabelle's", popup="Clarabelle's",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(milk_stand_coords, tooltip="Milk Stand", popup="Milk Stand",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(ogas_cantina_coords, tooltip="Oga's Cantina", popup="Oga's Cantina",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(docking_bay_coords, tooltip="Docking Bay 7 Food & Cargo", popup="Docking Bay 7 Food & Cargo",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(ronto_roasters_coords, tooltip="Ronto Roasters", popup="Ronto Roasters",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(hungry_bear_coords, tooltip="Hungry Bear Restaurant", popup="Hungry Bear Restaurant",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(harbour_galley_coords, tooltip="Harbour Galley", popup=popup,
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(mint_julep_coords, tooltip="Mint Julep Bar", popup="Mint Julep Bar",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(french_market_coords, tooltip="French Market Restaurant", popup="French Market Restaurant",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(cafe_orleans_coords, tooltip="Cafe Orleans", popup="Cafe Orleans",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(blue_bayou_coords, tooltip="Blue Bayou", popup="Blue Bayou",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(royal_street_veranda_coords, tooltip="Royal Street Veranda", popup="Royal Street Veranda",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(river_belle_coords, tooltip="River Belle Terrace", popup="River Belle Terrace",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(bengal_bbq_coords, tooltip="Bengal Barbecue", popup="Bengal Barbecue",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(stage_door_coords, tooltip="Stage Door Cafe", popup="Stage Door Cafe",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(golden_horseshoe_coords, tooltip="The Golden Horseshoe", popup="The Golden Horseshoe",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(turkey_leg_cart, tooltip="Turkey Leg Cart", popup="Turkey Leg Cart",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
#     folium.Marker(maurices_treats_coords, tooltip="Maurice's Treats", popup="Maurice's Treats",
#                 icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)

#     # folium.TileLayer('stamenwatercolor').add_to(disneyland_map)
    
#     disneyland_map.save('templates/disneyland_map.html')















# import folium
# import webbrowser

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