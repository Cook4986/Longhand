#exports glb from Blender scene for use in Mozilla Hubs
import bpy
import time
import os

bpy.ops.object.select_all(action='SELECT')
view_layer = bpy.context.view_layer
obj_active = view_layer.objects.active
selection = bpy.context.selected_objects


for obj in selection:

    obj.select_set(True)

    # some exporters only use the active object
    view_layer.objects.active = obj

    name = bpy.path.clean_name(obj.name)
    fn = "/Users/matthewcook/Desktop/out5"

    bpy.ops.export_scene.gltf(filepath=fn + ".GLB", use_visible=True)

    obj.select_set(False)

    print("written:", fn)


view_layer.objects.active = obj_active

for obj in selection:
    obj.select_set(True)

print("have a nice day")