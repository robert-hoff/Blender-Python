import bpy
import os

# list directory files of given extension
def listFiles(dir, ext):
    fileList = []
    for file in os.listdir(dir):
        if file[-len(ext):] == ext:
            fileList.append(file)
    return fileList


# delete everything in the file
def deleteAllObjects():
    for some_object in bpy.data.objects:
        bpy.data.objects.remove( some_object )

importdir = "Z:\\dev\\unity3d\\Rock and Vegetation Pack\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Terrain\\CPT\\NoLOD\\M"
exportdir = "Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\"

counter = 1

for filename in listFiles(importdir, 'fbx'):
    filenamepath = importdir+"\\"+filename;
    deleteAllObjects()
    bpy.ops.import_scene.fbx( filepath = filenamepath)
    my_texture_path = "Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\terrain-tiles\\terrain-texturemap.png"
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            node.image.filepath = my_texture_path
        if node.name == 'Principled BSDF':
            node.inputs['Alpha'].default_value = 1.0
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    newname = "terrain"+str(counter)+".fbx"
    # export scene operators:
    # https://docs.blender.org/api/current/bpy.ops.export_scene.html
    bpy.ops.export_scene.fbx(filepath=exportdir+newname, path_mode='STRIP', axis_up='Z')
    counter = counter + 1



