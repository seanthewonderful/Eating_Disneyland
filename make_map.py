import folium
from folium.plugins import MarkerCluster
from flask import url_for
from model import total_ratings, star_avg


def make_map(restaurants):
    
    disneyland_map = folium.Map(location=[33.812034, -117.918968], zoom_start=16, min_zoom=15, max_zoom=19)
    
    for each in restaurants:
        html = """
                <head>
                <base target="_parent">
                </head>
                <div class="card text-center" style="max-width: 22rem;">
                        <img class="card-img-top" src="{0}" alt="an image should be here..." style="max-width: 20rem;">
                                <div class="card-body">
                                        <h4 class="card-title">{1}</h4>
                                        <h4 class="card-title" style="color: green;">{2}</h4>
                                        <h6 class="card-text" style="font-style: italic;">{3}</h6>
                                        <h6 style="color:#E4BB23; font-weight:bold;">{5} ⭐️ 
                                        <span style="font-style:italic; font-size: smaller;"> ({6})</span></h6>
                                        <a type="button" href="{4}" class="btn btn-primary btn-sm" style="color:white;">See Details</a>
                                </div>
                </div>
                """
        popup = folium.Popup(html.format(each.image_url, 
                                         each.name, 
                                         each.expense, 
                                         each.land, 
                                         url_for('eating_place', rest_id=each.rest_id), 
                                         star_avg(each.rest_id, total_ratings(each.rest_id)),
                                         total_ratings(each.rest_id)), max_width=200)
        
        folium.Marker([each.x_coord, each.y_coord], tooltip=each.name, popup=popup,
                icon=folium.Icon(icon_color='white', icon='fa-cutlery', prefix='fa')).add_to(disneyland_map)
        
        disneyland_map.save('templates/disneyland_map.html')


def fountain_map(fountains):
        fountain_map = folium.Map(location=[33.812034, -117.918968], zoom_start=16, min_zoom=15, max_zoom=19)
        
        pass