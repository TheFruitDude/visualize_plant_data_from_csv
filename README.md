# Visualizer

This project aims to visualize plant population on Pilatus. Data is first loaded from a csv File. From there, it is simply a matter of mapping the values to the right range. (this was the tricky part) Ultimately, I plotted the coordinates on a Picture from map.geo.admin.ch.

## ipywidgets
ipywidgets are Interactive HTML widgets for Jupyter notebooks and the IPython kernel. In this project, I have used mainly two:
- Range Slider
- Dropdown Menus


![](previews_visualizer.png?raw=true)


## TODO:
-Dynamically update the content. (instead of having to press the damn button each time)
-Species density (per area) has not been examined. This would be an interesting idea as well. (Idea: Imagine a connection between density and Opacity)
-Transform everything to PyQt Gui (more user friendly

### Links
- https://www.bigendiandata.com/2017-06-27-Mapping_in_Jupyter/
- https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html
- https://www.swisstopo.admin.ch/en/maps-data-online/calculation-services/navref.html
- https://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.bluemarble
- 
### Näherungsformeln für die Transformation zwischen Schweizer Projektionskoordinaten und WGS84 :
this was very useful for dealing with swiss coordinate formats. 

https://www.swisstopo.admin.ch/de/swisstopo/dokumente.detail.document.html/swisstopo-internet/de/documents/geo-documents/ch1903wgs84_d.pdf.html
