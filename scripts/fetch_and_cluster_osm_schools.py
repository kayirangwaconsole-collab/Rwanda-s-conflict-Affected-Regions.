#!/usr/bin/env python3
import os
import json
import math
import urllib.request
import urllib.parse

OUT_DIR = 'docs/data'
os.makedirs(OUT_DIR, exist_ok=True)

overpass_query = '''[out:json][timeout:180];
area["name"="Rwanda"]["admin_level"="2"]->.searchArea;
(
  node["amenity"~"school|college|university|kindergarten"](area.searchArea);
  way["amenity"~"school|college|university|kindergarten"](area.searchArea);
  relation["amenity"~"school|college|university|kindergarten"](area.searchArea);
);
out center;'''

url = 'https://overpass-api.de/api/interpreter'
post_data = urllib.parse.urlencode({'data': overpass_query}).encode('utf-8')
req = urllib.request.Request(url, data=post_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
print('Querying Overpass API...')
with urllib.request.urlopen(req, timeout=300) as resp:
    raw = resp.read().decode('utf-8')
    data = json.loads(raw)

features = []
for el in data.get('elements', []):
    geom = None
    if el['type'] == 'node':
        lat = el.get('lat')
        lon = el.get('lon')
        if lat is not None and lon is not None:
            geom = { 'type': 'Point', 'coordinates': [lon, lat] }
    else:
        center = el.get('center')
        if center and 'lat' in center and 'lon' in center:
            geom = { 'type': 'Point', 'coordinates': [center['lon'], center['lat']] }
    if not geom:
        continue
    props = el.get('tags', {})
    props['_osm_type'] = el.get('type')
    props['_id'] = el.get('id')
    features.append({ 'type': 'Feature', 'geometry': geom, 'properties': props })

print(f'Total features: {len(features)}')

def haversine_meters(a, b):
    lon1, lat1 = a
    lon2, lat2 = b
    R = 6371000.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    t = math.sin(dphi/2.0)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2.0)**2
    c = 2*math.atan2(math.sqrt(t), math.sqrt(1-t))
    return R * c

THRESH_METERS = 1000.0
coords = [f['geometry']['coordinates'] for f in features]
clustered = []
non_clustered = []
for i,a in enumerate(coords):
    has_near = False
    for j,b in enumerate(coords):
        if i == j: continue
        if haversine_meters((a[0],a[1]), (b[0],b[1])) <= THRESH_METERS:
            has_near = True
            break
    if has_near:
        clustered.append(features[i])
    else:
        non_clustered.append(features[i])

print('Clustered:', len(clustered), 'Non-clustered:', len(non_clustered))

with open(os.path.join(OUT_DIR,'osm_schools.geojson'),'w',encoding='utf-8') as f:
    json.dump({'type':'FeatureCollection','features':features}, f)
with open(os.path.join(OUT_DIR,'schools_clustered.geojson'),'w',encoding='utf-8') as f:
    json.dump({'type':'FeatureCollection','features':clustered}, f)
with open(os.path.join(OUT_DIR,'schools_nonclustered.geojson'),'w',encoding='utf-8') as f:
    json.dump({'type':'FeatureCollection','features':non_clustered}, f)

print('Saved to', OUT_DIR)
