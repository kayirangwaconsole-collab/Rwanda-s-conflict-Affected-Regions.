# Rwanda's Education Conflict Affected Regions - Complete Guide

## 🎯 What Is This Project?

This project maps and visualizes **all schools in Rwanda** using OpenStreetMap data, with special focus on **conflict-affected regions**. It's a web-based dashboard accessible to anyone on the internet.

---

## 📍 Available Maps & Pages

### 1. **Main Dashboard (Complex)**
- **URL:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/
- **What it shows:**
  - Interactive map with 1,602 schools
  - Sidebar with statistics
  - Toggle between clustered and individual views
  - Search and filter information
- **Best for:** Detailed analysis and research

### 2. **Simple Education Map (Easy)**
- **URL:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/education-map/
- **What it shows:**
  - Clean, simple map interface
  - All 1,602 schools as blue dots
  - Major cities as orange dots (reference points)
  - Click schools to see details
- **Best for:** Quick viewing and presentations

### 3. **Data Sources Page (Documentation)**
- **URL:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/data-sources.html
- **What it shows:**
  - Where the data comes from
  - Complete data file descriptions
  - School attributes and field names
  - Attribution and licensing
  - How data was collected
- **Best for:** Understanding the data behind the maps

---

## 📊 Data Files Available

All data is organized in the `/data/` folder:

### **GeoJSON Datasets** (Processed - Ready to Use)
Located in: `/data/geojson/`

| File | Schools | Size | Purpose |
|------|---------|------|---------|
| `schools_clustered.geojson` | 1,602 | 580 KB | Main dashboard view |
| `schools_nonclustered.geojson` | 1,602 | 273 KB | Individual school markers |
| `rwanda.geojson` | 3 | 530 B | Reference cities |

### **Raw Data** (Original OpenStreetMap Exports)
Located in: `/data/raw/`

| File | Size | Purpose |
|------|------|---------|
| `osm_schools.geojson` | 870 KB | Raw OSM export |
| `osm_raw.json` | 907 KB | OSM API response |

---

## 🔗 Direct Data Access

You can download or view any data file directly:

- **Clustered Schools:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/data/geojson/schools_clustered.geojson
- **Individual Schools:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/data/geojson/schools_nonclustered.geojson
- **Rwanda Reference:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/data/geojson/rwanda.geojson
- **Raw OSM Schools:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/data/raw/osm_schools.geojson
- **Raw OSM Data:** https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/data/raw/osm_raw.json

---

## 📁 Website Folder Structure

```
Rwanda-s-conflict-Affected-Regions/
│
└── docs/                    (← Your website starts here)
    ├── index.html          (Main dashboard)
    ├── data-sources.html   (Data documentation)
    ├── README.md           (This file)
    │
    ├── education-map/      (Simple map folder)
    │   └── index.html      (Simple education map)
    │
    ├── data/               (Shared data folder)
    │   ├── geojson/        (Processed data)
    │   │   ├── rwanda.geojson
    │   │   ├── schools_clustered.geojson
    │   │   └── schools_nonclustered.geojson
    │   │
    │   └── raw/            (Raw data)
    │       ├── osm_raw.json
    │       └── osm_schools.geojson
    │
    ├── css/                (Ready for stylesheets)
    └── js/                 (Ready for JavaScript)
```

---

## 🗺️ What Each School Marker Shows

When you click on any school dot, a popup appears with:
- **School Name** (e.g., "École Belge")
- **City** (e.g., "Kigali")
- **Street Address** (e.g., "Rue KN 78")

---

## 📊 Statistics

- **Total Schools Mapped:** 1,602
- **Data Source:** OpenStreetMap (Community-Contributed)
- **Last Updated:** April 2023
- **Geographic Coverage:** Rwanda (entire country)
- **Data Format:** GeoJSON (standard geospatial format)

---

## 🌍 Map Features

### Main Dashboard
✅ Interactive Leaflet map  
✅ Marker clustering (groups nearby schools)  
✅ Toggle between views  
✅ Sidebar with statistics  
✅ Click markers for details  
✅ Responsive design (works on mobile)

### Simple Education Map
✅ Clean interface  
✅ All schools visible  
✅ Reference cities highlighted  
✅ Fast loading  
✅ School info on click

---

## 📝 Data Attributes

Each school in the dataset includes:

```json
{
  "name": "École Belge",              // School name
  "addr:city": "Kigali",              // City location
  "addr:street": "Rue KN 78",         // Street address
  "amenity": "school",                // Type (always "school")
  "check_date": "2023-04-19",        // Last verified date
  "_id": 279245665                    // OpenStreetMap ID
}
```

---

## 🔗 How to Share

**Share the dashboard:**
- Simple link: https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/

**Share the simple map:**
- For presentations: https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/education-map/

**Share the data:**
- Data info: https://kayirangwaconsole-collab.github.io/Rwanda-s-conflict-Affected-Regions/data-sources.html
- Direct data links: See "Direct Data Access" section above

---

## 📜 Attribution & License

**Data Source:** © OpenStreetMap contributors  
**License:** Open Data Commons Open Database License (ODbL) v1.0  
**Map Library:** Leaflet.js (BSD 2-Clause License)

All data is freely available for use, distribution, and modification with proper attribution.

---

## 🚀 How to Use the Maps

### For Everyone
1. Visit any of the URLs above
2. Click on school dots to see details
3. Zoom in/out using mouse scroll or buttons
4. Pan by clicking and dragging

### For Researchers
1. Visit the Data Sources page to understand the data
2. Download GeoJSON files directly
3. Use in your own GIS software (QGIS, ArcGIS, etc.)

### For Developers
1. Clone the GitHub repository
2. The data is in `/docs/data/` folder
3. Modify the maps or create new visualizations
4. Deploy to your own GitHub Pages

---

## 💡 Common Questions

**Q: Can I download the data?**  
A: Yes! Visit the direct data access links or the GitHub repository.

**Q: Can I use this data for commercial purposes?**  
A: Yes, with proper attribution to OpenStreetMap.

**Q: Why are there 1,602 schools?**  
A: This is all schools registered in OpenStreetMap for Rwanda as of April 2023.

**Q: Can I add more schools?**  
A: Yes! You can edit OpenStreetMap directly to add schools.

---

## 📧 Contact & Feedback

- **GitHub Repository:** https://github.com/kayirangwaconsole-collab/Rwanda-s-conflict-Affected-Regions.
- **Project Owner:** kayirangwaconsole-collab

---

**Last Updated:** June 2024  
**Version:** 1.0
