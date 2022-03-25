#(placeholder) Takes Blender scene of downloaded Sketchfab files and distributes models according to their frequency in text corpus
#launch blender with terminal: !/Applications/Blender.app/Contents/MacOS/Blender --python-console
import bpy
import json

#declarations
input = "/Users/matthewcook/Dropbox/Viz/Longhand/objects.txt"
xtran = 3
ytran = 0

#create ground plane and align all downloads with the plane
bpy.ops.mesh.primitive_plane_add(size=250, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.align_tools(loc_z=True, ref1='0', ref2='0', scale_x=True, scale_y=True, scale_z=True, apply_scale=True)
#bpy.ops.object.align_tools(loc_z=True, ref1='0', ref2='0')
bpy.ops.object.select_all(action='DESELECT')

#create dictionary from objects document
with open(input,'r') as f: 
    models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

print
#rescale downloads according to their relative frequency in corpus
for key,value in models.items():
    if len(value) > 2:    
        name = value[1]
        #print(name)
        freq = value[0]
        #print(value)
        if name in bpy.data.objects:
            i = bpy.data.objects[name]
            print(i)
            i.scale[0] = .01 * freq
            i.scale[1] = .01 * freq
            i.scale[2] = .01 * freq
            print("rescaled to: ")
            print(i.scale)
            i.location[0] = 1.00 * xtran
            i.location[1] = 1.00 * ytran
            xtran = (xtran + 3.00) * -1
            ytran = (ytran + xtran) * -1
            print("\n")

#add Hubs components to surface plane
bpy.context.active_object.select_set(True)
bpy.ops.wm.add_hubs_component(object_source="object", component_name="skybox")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="visible")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="nav-mesh")

print("\n")
