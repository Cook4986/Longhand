#Takes Blender scene of downloaded Sketchfab files and resizes then randomly distributes models according to their frequency in text corpus
#launch blender with terminal: !/Applications/Blender.app/Contents/MacOS/Blender
import bpy
import json

#declarations
input = "....txt"
count = 0

#enable critical add-ons
bpy.ops.preferences.addon_enable(module="space_view3d_align_tools")

#create dictionary from objects document
with open(input,'r') as f: 
    models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

#create temporary cube and spiral objects for scaling and model distribution
bpy.ops.curve.spirals(spiral_type='SPHERE',radius=(50))
bpy.context.object.scale[2] = 0.25
bpy.context.object.location[2] = 15
bpy.context.object.location[0] = 20.17
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(10, 10, 10))

#rescale and distributedownloads according to their relative frequency in corpus
for key,value in models.items():
    if len(value) > 2: 
        Object = bpy.data.objects["" + value[1] + ""]
        print("Located " + (str(Object)))
        print("\n")
        freq = (value[0])
        Object.select_set(True)
        
        #rescale to fit reference cube
        bpy.ops.object.align_tools(fit_x=True, fit_y=True, fit_z=True)
        Object.scale[0] = .1 * freq
        Object.scale[1] = .1 * freq
        Object.scale[2] = .1 * freq
        
        #distribute objects along spiral
        Object.select_set(True)
        Object.constraints.new(type='FOLLOW_PATH')
        Object.constraints["Follow Path"].target = bpy.data.objects["Spiral"]
        Object.constraints["Follow Path"].offset = (freq * -1)
        if bpy.context.object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        
        #print updated attributes console
        print((str(Object)) + "rescaled to: " + (str(Object.scale)) + " at " + (str(Object.location)))
        bpy.ops.object.select_all(action='DESELECT')
        count = count + 1
        
#remove scaling cube
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects["Cube.001"].select_set(True)
bpy.ops.object.delete()
#remove curves

#create ground plane + rescale and align downloads to ground plane
bpy.ops.mesh.primitive_plane_add(size=100, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.select_all(action='SELECT')
#bpy.ops.object.align_tools(loc_z=True, ref1='0', ref2='0')
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
print("have a nice day")