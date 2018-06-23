# general imports
import osmnx as ox
import networkx as nx
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
from shapely.geometry import MultiPolygon, Polygon
from descartes import PolygonPatch

#ox configuration
ox.config(use_cache=True, log_console=True)

#fixe Grenoble as place 
place = 'Grenoble, France'
#Fixe Walk network as network type
network_type = 'walk'

#Generate graph from place
G = ox.graph_from_place(place, network_type=network_type)