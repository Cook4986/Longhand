#Takes Blender scene of downloaded Sketchfab files and resizes then randomly distributes models according to their frequency in text corpus
#launch blender with terminal: !/Applications/Blender.app/Contents/MacOS/Blender
import bpy
import json

#declarations
input = ".../objects.txt"

#enable add-ons
bpy.ops.preferences.addon_enable(module="space_view3d_align_tools")

#create ground plane + rescale and align downloads to ground plane
bpy.ops.mesh.primitive_plane_add(size=250, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.align_tools(scale_x=True, scale_y=True, scale_z=True, apply_scale=True)
bpy.ops.object.align_tools(loc_z=True, ref1='0', ref2='0')
bpy.ops.object.select_all(action='DESELECT')

#create dictionary from objects document
with open(input,'r') as f: 
    models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

#rescale downloads according to their relative frequency in corpus
for key,value in models.items():
    if len(value) > 2:    
        Object = bpy.data.objects["" + value[1] + ""]
        print((str(Object)) + " of scale: " + (str(Object.scale)) + " situated at: " + (str(Object.location)))
        freq = value[0]
        Object.scale[0] = .1 * freq
        Object.scale[1] = .1 * freq
        Object.scale[2] = .1 * freq
        Object.select_set(True)
        bpy.ops.object.randomize_transform(loc=(200.00, 000.00, 200.00))
        print((str(Object)) + "rescaled to: " + (str(Object.scale)) + " and moved to: " + (str(Object.location)))
        print("\n")

#Align all downloads with the plane
bpy.ops.object.select_all(action='SELECT')

bpy.ops.object.select_all(action='DESELECT')

#add Hubs components to surface plane
bpy.context.active_object.select_set(True)
bpy.ops.wm.add_hubs_component(object_source="object", component_name="skybox")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="visible")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="nav-mesh")

#update to Top Orthogrpahic view
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        override = bpy.context.copy()
        override['area'] = area
        bpy.ops.view3d.view_axis(override, type='TOP')

print("\n")
