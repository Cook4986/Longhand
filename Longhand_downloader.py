#automatically downloads Sketchfab models corresponding to common words in corpus
import bpy
import json
import time

#declarations
start = time.time()
input = "/Users/matthewcook/Dropbox/Viz/Longhand/objects.txt"

#startup
bpy.ops.object.delete(use_global=False, confirm=False)
bpy.data.window_managers["WinMan"].sketchfab_api.email = "..."
bpy.data.window_managers["WinMan"].sketchfab_api.password = "..."
bpy.ops.wm.skfb_enable(enable=True)

#open and sort objects dict
with open(input,'r') as f: 
	models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

#iterate over dictionary objects, download and place
for key,value in models.items():
    print(value[1])
    freq = (value[0])
    print("Represents " + str(value[0]) + "%" + " of objects in scene.")
    query = (value[1])
    print(value[2])
    uid = (value[2])
    bpy.data.window_managers["WinMan"].sketchfab_browser_proxy.query = str(query)
    time.sleep(5)
    bpy.ops.wm.sketchfab_download(model_uid=(str(uid)))

end = time.time()
print(str(end - start) + " seconds to download all models into scene" )

print("have a nice day")


