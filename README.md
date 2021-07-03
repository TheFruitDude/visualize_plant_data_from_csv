# Visualizer

This project aims to visualize plant population on Pilatus. Data is first loaded from a csv File. From there, it is simply a matter of mapping the values to the right range. (this was the tricky part) Ultimately, I plotted the coordinates on a Picture from map.geo.admin.ch.

## ipywidgets
ipywidgets are Interactive HTML widgets for Jupyter notebooks and the IPython kernel. In this project, I have used mainly two:
- Range Slider
- Dropdown Menus


# TODO:
-Dynamically update the content. (instead of having to press the damn button each time)
-Species density (per area) has not been examined. This would be an interesting idea as well. (Idea: Imagine a connection between density and Opacity)
-Transform everything to PyQt Gui (more user friendly


![](previews_visualizer.png?raw=true)


### Links
- https://www.bigendiandata.com/2017-06-27-Mapping_in_Jupyter/
- https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html
- https://www.swisstopo.admin.ch/en/maps-data-online/calculation-services/navref.html
- https://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.bluemarble
- 
### Näherungsformeln für die Transformation zwischen Schweizer Projektionskoordinaten und WGS84 :
https://www.google.ch/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiw8M6_4JzqAhXuUxUIHSjKAnQQFjACegQIBBAB&url=https%3A%2F%2Fwww.swisstopo.admin.ch%2Fcontent%2Fswisstopo-internet%2Fde%2Fonline%2Fcalculation-services%2F_jcr_content%2FcontentPar%2Ftabs%2Fitems%2Fdokumente_und_publik%2FtabPar%2Fdownloadlist%2FdownloadItems%2F7_1467103072612.download%2Fch1903wgs84_d.pdf&usg=AOvVaw24hIqsCbSgnMCmVzkvdw9I
