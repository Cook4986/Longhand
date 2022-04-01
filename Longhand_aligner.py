#Takes Blender scene of downloaded Sketchfab files and distributes models according to their frequency in text corpus
#launch blender with terminal: !/Applications/Blender.app/Contents/MacOS/Blender --python-console
import bpy
import json

#declarations
input = "....txt"
xtran = 10
ytran = 0

#enable add-ons
bpy.ops.preferences.addon_enable(module="space_view3d_align_tools")

#create ground plane and align all downloads with the plane
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
        name = value[1]
        print(name)
        freq = value[0]
        #print(value)
        #list(bpy.data.objects)
        for object in bpy.data.objects:
            print(object)
            check = str(object)
            check = check.lower()
            if name in check:
                print(name + " model")
                object.scale[0] = .01 * freq
                object.scale[1] = .01 * freq
                object.scale[2] = .01 * freq
                print("rescaled to: " + (str(object.scale)))
                object.location[0] = object.location[0] * xtran
                object.location[1] = object.location[1] * ytran
                xtran = (xtran + 5) * -1
                print("New X coordinate = " + (str(xtran)))
                ytran = (ytran + xtran) * -1
                print("New Y coordinate = " + (str(ytran)))
                print("\n")

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
