#Takes Blender scene of downloaded Sketchfab files and resizes then randomly distributes models according to their frequency in text corpus
#launch blender with terminal: !/Applications/Blender.app/Contents/MacOS/Blender
import bpy
from bpy import context
import json

#declarations
input = "..." #objects textfile output from "Longhand_notebook" script
count = 0

#enable critical add-ons
bpy.ops.preferences.addon_enable(module="space_view3d_align_tools")
bpy.ops.preferences.addon_enable(module="add_curve_extra_objects")

#reposition/increase energy of scene lighting
light = bpy.data.objects["Light"]
light.location = (0,0,50)
light.data.energy = 100000

#create dictionary from objects document
with open(input,'r') as f: 
    models = json.load(f)
{key: value for key, value in sorted(models.items(), key=lambda item: item[1])}

#create spiral object for model distribution
bpy.ops.curve.spirals(spiral_type='SPHERE',radius=(50))
bpy.context.object.scale[2] = 0.25
bpy.context.object.location[2] = 15
bpy.context.object.location[0] = 20.17

#create ground plane + rescale and align downloads to ground plane
bpy.ops.mesh.primitive_plane_add(size=100, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.select_all(action='DESELECT')

#rescale and distributedownloads according to their relative frequency in corpus
for key,value in models.items():
    if len(value) > 2: 
        Object = bpy.data.objects["" + value[1] + ""]
        #print("Located " + (str(Object)))
        print("\n")
        freq = (value[0])
        Object.select_set(True)
        
        #normalize object scale script from Athanaze (https://github.com/Athanaze/Blender-Normalize-Object)
        context.scene.cursor.location = [0.0, 0.0, 0.0]
        bpy.ops.object.rotation_clear(clear_delta=False)
        bpy.ops.object.location_clear(clear_delta=False)
        bpy.ops.object.scale_clear(clear_delta=False)

        if Object.type == 'MESH':
            #obj = context.active_object
            v = Object.data.vertices

            highest = [v[0].co[0], v[0].co[1], v[0].co[2]]
            lowest = [v[0].co[0], v[0].co[1], v[0].co[2]]

            for v in Object.data.vertices:
                c = v.co
                
                if c[0] > highest[0]:
                    highest[0] = c[0]
                
                if c[0] < lowest[0]:
                    lowest[0] = c[0]
                
                if c[1] > highest[1]:
                    highest[1] = c[1]
                
                if c[1] < lowest[1]:
                    lowest[1] = c[1]
                
                if c[2] > highest[2]:
                    highest[2] = c[2]
                
                if c[2] < lowest[2]:
                    lowest[2] = c[2]
                    
            bpy.ops.transform.translate(
                value=(-0.5*(highest[0]+lowest[0]), -0.5*(highest[1]+lowest[1]), -0.5*(highest[2]+lowest[2])),
                orient_type='GLOBAL',
                orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                orient_matrix_type='GLOBAL',
                mirror=True,
                use_proportional_edit=False,
                proportional_edit_falloff='SMOOTH',
                proportional_size=1,
                use_proportional_connected=False,
                use_proportional_projected=False
            )

            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
            size = [highest[0]-lowest[0], highest[1]-lowest[1],highest[2]-lowest[2]]
            s = 50/sorted(size)[2] #numerator represents target scale

            bpy.ops.transform.resize(
                value=(s, s, s),
                orient_type='GLOBAL',
                orient_matrix=((1, 0, 0),(0, 1, 0), (0, 0, 1)),
                orient_matrix_type='GLOBAL',
                mirror=True,
                use_proportional_edit=False,
                proportional_edit_falloff='SMOOTH',
                proportional_size=1,
                use_proportional_connected=False,
                use_proportional_projected=False
                
        )
        #rescale by relative frequency in corpus
        Object.scale[0] = freq/100
        Object.scale[1] = freq/100
        Object.scale[2] = freq/100
        
        #create spiral object for model distribution 
        bpy.ops.curve.spirals(spiral_type='SPHERE',radius=(50))
        bpy.context.object.scale[2] = 0.5
        bpy.context.object.rotation_euler[2] = 1.5 * count
        bpy.context.object.location[2] = 25
        
        #distribute objects along spiral
        Object.select_set(True)
        Object.constraints.new(type='FOLLOW_PATH')
        
        if count == 0:
            Object.constraints["Follow Path"].target = bpy.data.objects["Spiral"]
            Object.constraints["Follow Path"].offset = (freq * -1.0)
        elif (count > 0) & (count < 10):
            Object.constraints["Follow Path"].target = bpy.data.objects["Spiral"+".00"+ (str(count))]
            Object.constraints["Follow Path"].offset = (freq * -1.0)
        elif count > 9:
            Object.constraints["Follow Path"].target = bpy.data.objects["Spiral"+".0"+ (str(count))]
            Object.constraints["Follow Path"].offset = (freq * -1.0)
        if bpy.context.object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        
        #print updated attributes console
        print((str(Object)) + " rescaled to: " + (str(Object.scale)) + " and moved to " + (str(Object.matrix_world.translation)))
        bpy.ops.object.select_all(action='DESELECT')
        count = count + 1

#add Hubs components to surface plane
bpy.data.objects["Plane"].select_set(True)
bpy.ops.wm.add_hubs_component(object_source="object", component_name="skybox")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="visible")
bpy.ops.wm.add_hubs_component(object_source="object", component_name="nav-mesh")
bpy.ops.object.select_all(action='DESELECT')

#update viewport to Top Orthographic perspective
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        override = bpy.context.copy()
        override['area'] = area
        bpy.ops.view3d.view_axis(override, type='TOP')
print("\n")
print("have a nice day")


