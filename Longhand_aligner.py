#Takes Blender scene of downloaded Sketchfab files and resizes then randomly distributes models according to their frequency in text corpus
#launch blender with terminal: !/Applications/Blender.app/Contents/MacOS/Blender
import bpy
import json
import random

#declarations
input = ".../Longhand/primativesTest.txt"
count = 0
multiplier = sum((-1)**(k+1) * k**2 for k in range(1, count + 1))

#enable critical add-ons
bpy.ops.preferences.addon_enable(module="space_view3d_align_tools")

#create dictionary from objects document
with open(input,'r') as f: 
    models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

#create temporary parent object for scaling
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(10, 10, 10))

#rescale downloads according to their relative frequency in corpus
for key,value in models.items():
    if len(value) > 2: 
        print(multiplier)
        Object = bpy.data.objects["" + value[1] + ""]
        print("Located " + (str(Object)) + " of scale: " + (str(Object.scale)))
        freq = value[0]
        Object.select_set(True)
        bpy.ops.object.align_tools(fit_x=True, fit_y=True, fit_z=True)
        Object.scale[0] = .1 * freq
        Object.scale[1] = .1 * freq
        Object.scale[2] = .1 * freq
        print((str(Object)) + "rescaled to: " + (str(Object.scale)))
        bpy.ops.object.select_all(action='DESELECT')
        print("\n")

#remove scaling cube
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects["Cube.001"].select_set(True)
bpy.ops.object.delete()

#create ground plane + rescale and align downloads to ground plane
bpy.ops.mesh.primitive_plane_add(size=250, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.align_tools(loc_z=True, ref1='0', ref2='0')
bpy.ops.object.select_all(action='DESELECT')

#add Hubs components to surface plane
bpy.data.objects["Plane"].select_set(True)
bpy.ops.wm.add_hubs_component(object_source="object", component_name="skybox")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="visible")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="nav-mesh")

#update viewport to Top Orthographic perspective
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        override = bpy.context.copy()
        override['area'] = area
        bpy.ops.view3d.view_axis(override, type='TOP')
print("\n")
