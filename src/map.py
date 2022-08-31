#Libraries
#Libraries
from collections import Counter
from dotenv import load_dotenv
import geopandas as gpd
import geopy.distance
import json
import os
import pandas as pd
from pymongo import MongoClient, GEOSPHERE
import requests
from folium import Choropleth, Circle, FeatureGroup, GeoJson, Icon, LayerControl, Map, Marker, Popup

#Credentials
load_dotenv()
key = os.getenv("key")

# Location on the Mission disctrict
location = [37.7615584,-122.4155738]
radius=3000
limit=10

def foursquare (key, query, location, radius, limit):
    '''
    This function takes a query with parameters and returns a df with the results. 

    Parameters
    ----------
    key: Authorization
    query: Keywords of the search
    location: Starting location in [latt,long]
    radius: Distance in meters
    limit: amount of allowed results (1-50)

    Returns
    -------
    df : Closest results and locations
    '''
# Strip query and replace spaces by %20
    if " " in query.strip():
        query_ok = query.strip().replace(" ","%20")
    else:
        query_ok = query.strip()
#url has to be formated to fit the search

    url = f"https://api.foursquare.com/v3/places/search?query={query_ok}&ll={str(location[0]).strip()}%2C{str(location[1]).strip()}&radius={radius}&categories=17069%2C%2017070&sort=RELEVANCE&limit={limit}"
    headers =  { "Accept": "application/json",
             "Authorization": f"{key}" }
    response = requests.get(url, headers=headers)
    
#If we don't get matches, we still want to know
    if response:
        try:
            results=response.json()['results']
            new_list = [ {"name" : i["name"],
                      "lat"  : i["geocodes"]["main"]["latitude"],
                      "long" : i["geocodes"]["main"]["longitude"] ,
                          "type" : {"typepoint": {"type": "Point"}} } for i in results]

            df = pd.DataFrame(new_list)
            return df
        except:
            return f"Sorry, no matches for {query} in the coordinates {location}"
    else:
        return f"Sorry, no matches for {query} in the coordinates {location}"

def walking(m, location):
    '''
    This function takes a map and location and returns a map with walking areas. 

    Parameters
    ----------
    m: Map
    location: Starting location in [latt,long]

    Returns
    -------
    m : Map with walking areas.
    '''

    #1km circle - Up to 12 min walking
    km1 = FeatureGroup(name="Circle 1km").add_to(m)
    Circle(
        location=location,
        color='green',
        radius=1000,
        fill=True,
        opacity=0.5,
        fill_opacity=0.5,
        tooltip='1km'
    ).add_to(km1)
    
    #2km circle - Up to 24 min walking
    km2 = FeatureGroup(name="Circle 2km").add_to(m)
    Circle(
        location=location,
        color='yellow',
        radius=2000,
        fill=True,
        opacity=0.6,
        fill_opacity=0.4,
        tooltip='2km'
    ).add_to(km2)
    
    #3km circle - Up to 36 min walking
    km3 = FeatureGroup(name="Circle 3km").add_to(m)
    Circle(
        location=location,
        color='red',
        radius=3000,
        fill=True,
        opacity=0.4,
        fill_opacity=0.3,
        tooltip='3km'
    ).add_to(km3)
    
    return m


def mapping(m, df, location):
    '''
    This function takes a map, df and location and returns a map with walking areas. 

    Parameters
    ----------
    m: Map
    df: Dataframe
    location: Starting location in [latt,long]

    Returns
    -------
    m : Map with walking areas.
    '''
    groceries = FeatureGroup(name="Grocery Stores").add_to(m)
    company = Marker(location, tooltip="Location", icon=Icon(color="black",
           opacity=0.1,
           prefix="fa", #It comes from Font Awesome
           icon="database",
           icon_color="green"))
    company.add_to(m)

    for index, row in df.iterrows():

         # 1. Location (and some other things like the tooltip)
        place = {"location": [row["lat"], row["long"]], "tooltip": row["name"]}

        #color based on distance (in km) to the starting location
        distance = geopy.distance.geodesic(location, place['location']).km
        if  distance <= 1 :
            color = 'lightgreen'
        elif 1 < distance <= 2 :
            color = 'lightblue'
        elif 2 < distance <= 3 :
            color = 'lightred'
        else:
            color = 'lightgray'

        # 2. Icon based on the value

        if row["name"]!=0:
            icon = Icon (
                color=color,
                prefix="fa",
                icon="cutlery",
                icon_color = "black")
            new_marker = Marker(**place, icon=icon)
            new_marker.add_to(groceries)
    return m