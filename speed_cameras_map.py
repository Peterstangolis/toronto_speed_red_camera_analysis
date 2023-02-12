

def speed_cameras_map(camera_state):

    from variables import speed_cam_url, city_wards_geo, map_styles

    import folium
    import geopandas as gpd
    from streamlit_folium import folium_static

    gdf_speed_cameras = gpd.read_file(speed_cam_url)

    gdf_speed_cameras['lon'] = gdf_speed_cameras.geometry.x
    gdf_speed_cameras['lat'] = gdf_speed_cameras.geometry.y

    gdf_speed_cameras_state = gdf_speed_cameras[gdf_speed_cameras["Status"]==camera_state]


    if camera_state == 'Active':
        color = 'darkgreen'
    else:
        color = 'gray'

    m = folium.Map(location=[43.653225, -79.383186],
                   tiles=map_styles["EsriNatGeoWorldMap"][0],
                   attr=map_styles["EsriNatGeoWorldMap"][1],
                   width='100%',
                   height='100%',
                   zoom_start=10, max_zoom=16, min_zoom=5)

    bordersStyle = {
        'color': '#33709E',
        'weight': .6,
        'fillColor': '#63B0EB',
        'fillOpacity': 0.0
    }

    highlightStyle = {
        'color': '#33709E',
        'weight': .5,
        'fillColor': '#63B0EB',
        'fillOpacity': 0.3
    }

    f = folium.GeoJson(
        data=city_wards_geo,
        name='geometry',
        style_function=lambda x: bordersStyle,
        highlight_function=lambda x: highlightStyle,
        tooltip=folium.features.GeoJsonTooltip(fields=["AREA_NAME"], aliases=["WARD: "],
                                               labels=True, sticky=False,
                                               style=('background-color: #63B0EB; color:white; font-family:'
                                                      'arial; font-size: 12px; padding: 10px;'))

    ).add_to(m)

    for i in range(0, len(gdf_speed_cameras_state)):
        popup_text = folium.Popup(
            html=f"""<h4 style= 'font-family:Arial;font-size:14px;'><strong>{gdf_speed_cameras_state.iloc[i]['location']}</strong></center></h4>""",
            max_width=160, min_width=130
        )

        folium.Marker(
            location=[gdf_speed_cameras_state.iloc[i]["lat"], gdf_speed_cameras_state.iloc[i]["lon"]],
            popup=popup_text,
            icon=folium.Icon(color=f'{color}', icon="camera", icon_color='white', prefix='glyphicon')
        ).add_to(m)


    folium_static(m, width=1000, height=600)

