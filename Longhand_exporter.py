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

for obj in selection:
    obj.select_set(True)
    view_layer.objects.active = obj
    fn = ".../Longhand/outputs" + str(time.asctime(secs))
    bpy.ops.export_scene.gltf(filepath=fn + ".GLB", use_visible=True)
    obj.select_set(False)
    print("written:", fn)

print("have a nice day")