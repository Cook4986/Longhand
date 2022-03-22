#(placeholder) Takes Blender scene of downloaded Sketchfab files and distributes models according to their frequency in text corpus
#launch blender with terminal: !/Applications/Blender.app/Contents/MacOS/Blender
import bpy
import json

#declarations
input = "/Users/matthewcook/Dropbox/Viz/Longhand/objects.txt"

#create dictionary from objects document
with open(input,'r') as f: 
    models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

print
#iterate over downloads
for key,value in models.items():    
    name = value[1]
    #print(name)
    freq = value[0]
    #print(value)
    i = bpy.data.objects[name]
    print(i)
    i.scale[0] = .1 * freq
    i.scale[1] = .1* freq
    i.scale[2] = .1 * freq
    print("rescaled to: ")
    print(i.scale)
    print("\n")
    
#create ground plane and align all downloads with the plane
bpy.ops.mesh.primitive_plane_add(size=1000, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.align_tools(loc_z=True, ref1='0', ref2='0')
bpy.context.active_object.select_set(False)

print("\n")


