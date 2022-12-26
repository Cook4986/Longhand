#automatically downloads Sketchfab models corresponding to common words in corpus
import bpy
import json
import time
import os
from pathlib import Path

#I/O
start = time.time()
target = "/.../Longhand/Objects" #Objects dictionary output from "Longhand_notebook" script
for path in sorted(Path(target).rglob('*.txt')):
    if "_log" not in str(path):
        print("\n")
        print("Working from " + str(path))
        print("\n")
        input = str(path)

#prep scene
bpy.ops.object.delete(use_global=False, confirm=False)
bpy.ops.wm.skfb_enable(enable=True)
bpy.data.window_managers["WinMan"].addon_search = "sket"
bpy.data.window_managers["WinMan"].sketchfab_api.use_mail = False
bpy.data.window_managers["WinMan"].sketchfab_api.api_token = "..."
bpy.ops.wm.sketchfab_login(authenticate=True)
bpy.data.window_managers["WinMan"].sketchfab_browser.manualImportBoolean = True

#open and sort objects dict
with open(input,'r') as f: 
    models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}
print("\n")
print("Beginning downloads...")
print("\n")

#iterate over dictionary objects, download and place
for key,value in models.items():
    if len(value) > 2:
        print("Downloading: " + str(value[1]))
        freq = (value[0])
        print('"'+ str(key) + '"' + " occurs " + str(value[0]) + " times in target corpus.")
        query = (value[1])
        print("face count: " + str(value[4]))
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

context.scene.cursor.location = [0.0, 0.0, 0.0]
print("\n")
print("downloads complete")
print("\n")


