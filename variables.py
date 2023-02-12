from datetime import datetime
red_light_camera_charges_link = 'https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/6ae000e1-9899-4f6e-8e7d-96dca267db80/resource/8dd4a83e-3284-4b16-9295-c256dcf62954/download/Red%20Light%20Camera%20Annual%20Charges.xlsx'

ase_charges_link = 'https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/537923d1-a6c8-4b9c-9d55-fa47d9d7ddab/resource/a388bc08-622c-4647-bad8-ecdb7e62090a/download/Automated%20Speed%20Enforcement%20-%20Monthly%20Charges.xlsx'

speed_cam_url = 'https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/a154790c-4a8a-4d09-ab6b-535ddb646770/resource/9842895b-2b8b-4b60-9320-c0a1fde4afd8/download/Automated%20Speed%20Enforcement%20Locations.geojson'
city_wards_geo = 'https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/5e7a8234-f805-43ac-820f-03d7c360b588/resource/737b29e0-8329-4260-b6af-21555ab24f28/download/City%20Wards%20Data.geojson'

map_styles = {'basemap': ['https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png',
                          'Tiles &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'],

              'NatGeoWorldMap': [
                  'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
                  'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC'],

              'EsriDeLorme': [
                  'https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}',
                  'Tiles &copy; Esri &mdash; Copyright: &copy;2012 DeLorme'],

              'EsriNatGeoWorldMap':[
                  'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
                  'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC'
              ],

              'WorldTopoMap': ['https://{s}.tile.jawg.io/jawg-sunny/{z}/{x}/{y}{r}.png?access-token={accessToken}',
                               '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'],

              'StamenTonerLite': ['https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.png',
                                  'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'],
              'CartoDBVoyager': [
                  'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
                  '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
              ],
              'CartoDBPosition': [
                  'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
                  '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
              ]
              }

red_light_camera_fine_amt = 260.00
red_light_victim_surcharge = 60.00
red_light_court_costs = 5.00

revenue_since_start = 34000000

speed_colors = [
]

active_speed_cameras = 50

light_colors = [
    '#EB3810',
    '#F7831E',
    '#239E70'

]

city_colors = [
    '#63B0EB',
    '#123652',
    '#33709E',
    '#63B0EB'
]

speed_cameras_site_lastUpdated = datetime.strptime('Nov 29, 2022', '%b %d, %Y').date()