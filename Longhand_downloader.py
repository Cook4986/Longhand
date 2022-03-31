#automatically downloads Sketchfab models corresponding to common words in corpus
import bpy
import json
import time

#declarations
start = time.time()
input = ".../Longhand/objects.txt"

#startup and activate Sketchfab plugin
bpy.ops.object.delete(use_global=False, confirm=False)
bpy.data.window_managers["WinMan"].sketchfab_api.email = "matt_cook@harvard.edu"
bpy.data.window_managers["WinMan"].sketchfab_api.password = "SchnapTest1234"
bpy.ops.wm.skfb_enable(enable=True)
bpy.data.window_managers["WinMan"].sketchfab_browser.manualImportBoolean = True


#open and sort objects dict
with open(input,'r') as f: 
	models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

#iterate over dictionary objects, download and place
for key,value in models.items():
    if len(value) > 2:
        print(value[1])
        freq = (value[0])
        print("Represents " + str(value[0]) + "%" + " of objects in scene.")
        query = (value[1])
        print("uid: " + str(value[2]))
        uid = (value[2])
        url = (value[3])
        bpy.data.window_managers["WinMan"].sketchfab_browser.manualImportPath = str(url)
        bpy.ops.wm.sketchfab_download(model_uid=uid)
        time.sleep(5)
        print("\n")

#close processes
end = time.time()
print(str(end - start) + " seconds to download all models into scene" )
bpy.context.view_layer.update()
bpy.ops.object.select_all(action='DESELECT')
f.close()

print("\n")
print("downloads complete")
print("\n")
