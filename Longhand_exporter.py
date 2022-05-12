#exports glb from Blender scene for use in Mozilla Hubs
import bpy
import time
import os

secs = time.localtime()

#declarations
bpy.ops.object.select_all(action='SELECT')
view_layer = bpy.context.view_layer
obj_active = view_layer.objects.active
selection = bpy.context.selected_objects
outPath = ".../outputs" + str(time.asctime(secs))

for obj in selection:
    obj.select_set(True)
    view_layer.objects.active = obj
    bpy.ops.export_scene.gltf(filepath=outPath + ".GLB", use_visible=True)
    obj.select_set(False)

print("have a nice day")