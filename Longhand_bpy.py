import bpy

uid = open(".../objects.txt", "r")
terms = []

bpy.ops.object.delete(use_global=False, confirm=False)

bpy.data.window_managers["WinMan"].sketchfab_api.email = "xxx"
bpy.data.window_managers["WinMan"].sketchfab_api.password = "xxx"
bpy.ops.wm.skfb_enable(enable=True)

for line in uid.readlines():
    word = line.split(",")
    terms.append(word[0])

print(terms) 

for term in terms:
	bpy.ops.wm.sketchfab_search(str(term))