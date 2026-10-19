import arcpy, os
from arcpy import env
param0 = arcpy.GetParameterAsText(0)
for dirpath, dirnames, filenames in arcpy.da.Walk(param0, datatype="Container"):
    for dirname in dirnames:
        if ".gdb" in dirname:
            
            gdbname = arcpy.AddMessage(dirname)
            print(gdbname)
            if ' ' in dirname:
                dirnameName = os.path.basename(dirname)
                dirnameName = dirnameName.replace(" ", "_")
                oldpath = os.path.join(dirpath, dirname)
                newpath = os.path.join(dirpath, dirnameName)
                os.rename(oldpath, newpath)
                fin = arcpy.AddMessage('Geodatabase names have been updated')
                #upd = arcpy.AddMessage(oldpath, '->', newpath)
                #print(upd)
                print(fin)
