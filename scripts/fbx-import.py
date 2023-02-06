import bpy
import os
import sys

# delete everything
def deleteAllObjects():
    deleteListObjects = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'HAIR', 'POINTCLOUD', 'VOLUME', 'GPENCIL',
                     'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']
    for o in bpy.context.scene.objects:
        for i in deleteListObjects:
            if o.type == i:
                o.select_set(False)
            else:
                o.select_set(True)
    bpy.ops.object.delete()



importdir = "Z:\\dev\\unity3d\\Rock and Vegetation Pack\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Terrain\\CPT\\NoLOD\\M"
testdir = "Z:\\active\\projects\\edinburgh-gamejam\\blender"
exportdir = "Z:\active\projects\edinburgh-gamejam\exportdir"


def listFiles(dir, ext):
    fileList = []
    for file in os.listdir(dir):
        if file[-len(ext):] == ext:
            fileList.append(file)
    return fileList


# files = listFiles(importdir,"fbx")
# print(files[0])
# print(files[1])

singlefile = importdir+"\\CPT_Terrain_M_a_01.fbx"

# deleteAllObjects()
# bpy.ops.import_scene.fbx(filepath=singlefile)

# imports target fbx
# bpy.ops.import_scene.fbx( filepath = "Z:\\dev\\unity3d\\Rock and Vegetation Pack\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Terrain\\CPT\\NoLOD\\M\\CPT_Terrain_M_a_01.fbx")




my_texture_path = "Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\terrain-tiles\\terrain-texturemap.png"
for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
    if node.name == 'Image Texture':
        node.image.filepath = my_texture_path
    if node.name == 'Principled BSDF':
        node.inputs['Alpha'].default_value = 1.0


bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)












