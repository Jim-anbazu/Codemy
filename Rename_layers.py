#For layers that have been added to a map from an Enterprise Geodatabase
#You might have to remove the schema name from the layer name
#For example, a layer with the name LRS.Roads can be renamed to Roads to prepare the map for publishing
#This is relevant to avoid exposing the full layer name in published maps

import arcpy

path_to_project = "<path to projects>"
map_name = "<name of the map>"

aprx = arcpy.mp.ArcGISProject(path_to_project)
m = aprx.listMaps(map_name)[0]

lyrs = m.listLayers()
tb = m.listTables()

#Renaming layers in the map
for lyr in lyrs:
    if lyr.isFeatureLayer :
        #print(f"Original name: {lyr.name}")
        if "LRS." in lyr.name:
            l_cim = lyr.getDefinition("V3")
            print(f" Old name: {l_cim.name}")
            print("Renaming layer....")
            n_name = str(l_cim.name).replace("<specify text to replace>", "")
            l_cim.name = n_name
            n = lyr.setDefinition(l_cim)
            print(f"New name: {lyr.name}")
    else:
        print("No layer found")

#Renaming tables in the map
for t in tb:
    if "LRS." in t.name:
            t_cim = t.getDefinition("V3")
            print(f" Old name: {t_cim.name}")
            print("Renaming table....")
            n_name = str(t_cim.name).replace("<specify text to replace>", "")
            t_cim.name = n_name
            n = t.setDefinition(t_cim)
            print(f"New name: {t.name}")