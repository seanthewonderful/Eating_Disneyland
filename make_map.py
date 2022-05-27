import folium
from folium.plugins import MarkerCluster
from flask import url_for
from model import total_ratings, star_avg, total_ratings_fountain, star_avg_fountain


def make_map(restaurants):
    
    disneyland_map = folium.Map(location=[33.812034, -117.918968], zoom_start=16, min_zoom=13, max_zoom=19)
    
    for each in restaurants:
        html = """
                <head>
                <base target="_parent">
                </head>
                <div class="card text-center" style="max-width: 22rem;">
                        <img class="card-img-top" src="{0}" alt="an image should be here..." style="max-width: 20rem;">
                                <div class="card-body">
                                        <h4 class="card-title fw-bold" style="text-shadow: #cc9a07 0 1px 1px;">{1}</h4>
                                        <h4 class="card-title" style="color: green; text-shadow: #a3cfbc 1px 0 3px;">{2}</h4>
                                        <h6 class="card-text" style="font-style: italic;">{3}</h6>
                                        <h4 style="color: #f4c109; font-weight:bold; text-shadow: #172c65 0 1px 1px;">{5} ⭐️ 
                                        <span style="font-style:italic; font-size: smaller;"> ({6})</span></h4>
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


def make_fountain_map(fountains):
        fountain_map = folium.Map(location=[33.812034, -117.918968], zoom_start=16, min_zoom=13, max_zoom=19)
        
        for each in fountains:
            html = """
                <head>
                <base target="_parent">
                </head>
                <div class="card text-center" style="max-width: 22rem;">
                        <img class="card-img-top" src="/static/images/{0}" alt="an image should be here..." style="max-width: 20rem; max-height:20rem;">
                                <div class="card-body">
                                        <h4 class="card-title">{1}</h4>
                                        <h6 class="card-text" style="font-style: italic;">{2}</h6>
                                        <h6 style="color:#E4BB23; font-weight:bold;">{3} ⭐️ 
                                        <span style="font-style:italic; font-size: smaller;"> ({4})</span></h6>
                                        <a type="button" href="{5}" class="btn btn-primary btn-sm" style="color:white;">See Details</a>
                                </div>
                </div>
                """
            popup = folium.Popup(html.format(each.image_url, 
                                         each.name, 
                                         each.land,  
                                         star_avg_fountain(each.id, total_ratings_fountain(each.id)),
                                         total_ratings_fountain(each.id),
                                         url_for('fountain_place', fountain_id=each.id)), max_width=200)
        
            folium.Marker([each.x_coord, each.y_coord], tooltip=each.name, popup=popup,
                icon=folium.Icon(icon_color='white', icon='fa-tint', prefix='fa')).add_to(fountain_map)
        
            fountain_map.save('templates/fountain_map.html')