#exports Blender scene to Sketchfab
import bpy
import time
import os
from pathlib import Path

#ensure max output size is 100MB
input = ".../Longhand/Objects" #Objects dictionary output from "Longhand_notebook" script
for path in sorted(Path(input).rglob('*.txt')):
    if "_log" not in str(path):
        print("Working from " + str(path))
        name = str(path.stem)

#declarations
secs = time.localtime()
outPath = name + " longhandTest_" + str(time.asctime(secs))

#sketchfab plugin exporter
bpy.data.window_managers["WinMan"].sketchfab_export.draft = False
bpy.data.window_managers["WinMan"].sketchfab_export.private = False
bpy.data.window_managers["WinMan"].sketchfab_export.title = outPath
bpy.ops.wm.sketchfab_export()

print("have a nice day")