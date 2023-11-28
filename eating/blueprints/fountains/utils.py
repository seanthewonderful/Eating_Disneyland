from flask import url_for
from crud import total_ratings_fountain, star_avg_fountain
import folium

def make_fountain_map(fountains):
    fountain_map = folium.Map(
        location=[33.812034, -117.918968], zoom_start=16, min_zoom=13, max_zoom=19
    )

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
        popup = folium.Popup(
            html.format(
                each.image_url,
                each.name,
                each.land,
                star_avg_fountain(each.id, total_ratings_fountain(each.id)),
                total_ratings_fountain(each.id),
                url_for("fountain_place", fountain_id=each.id),
            ),
            max_width=200,
        )

        folium.Marker(
            [each.x_coord, each.y_coord],
            tooltip=each.name,
            popup=popup,
            icon=folium.Icon(icon_color="white", icon="fa-tint", prefix="fa"),
        ).add_to(fountain_map)

        fountain_map.save("templates/fountain_map.html")
