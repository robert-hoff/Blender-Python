import bpy
import os
import math

def degreesToRad(degrees):
    return math.pi * degrees / 180

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

def createLight():
    light_data = bpy.data.lights.new(name='Sun', type='SUN')
    light = bpy.data.objects.new(name='Sun', object_data=light_data)
    bpy.context.collection.objects.link(light)
    light.data.energy = 2
    light.location = (50, -50, 140)
    light.rotation_euler[0] = degreesToRad(40)
    light.rotation_euler[1] = degreesToRad(4)
    light.rotation_euler[2] = degreesToRad(50)
    light.data.angle = degreesToRad(15)

def createCamera():
    camera_data = bpy.data.cameras.new(name='Camera')
    camera = bpy.data.objects.new('Camera', camera_data)
    bpy.context.collection.objects.link(camera)
    camera.location = (40, -75, 75)
    camera.rotation_euler[0] = degreesToRad(52)
    camera.rotation_euler[1] = degreesToRad(0)
    camera.rotation_euler[2] = degreesToRad(8)

def createRender(filenamepath):
    bpy.data.scenes['Scene'].camera = bpy.context.scene.objects['Camera']
    bpy.context.scene.render.filepath = filenamepath
    bpy.context.scene.render.resolution_x = 720
    bpy.context.scene.render.resolution_y = 405
    bpy.ops.render.render(write_still=True)

def setShadeSmooth():
    fbx_object = bpy.data.objects[0]
    fbx_object.select_set(True)
    bpy.ops.object.shade_smooth()

# -- plants
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Terrain\\CPT\\NoLOD\\M\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Mountains\\CPT\\NoLOD\\M\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Plants\\Reeds\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Plants\\Other_Plants\\TwoSided\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Mushrooms\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Grass\\MeshGrass\\TwoSided\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Grass\\GrassPlane\\TwoSide\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Flowers\\TwoSided\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Cactus\\No_Bottoms\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Bushes\\DeadBush\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Vegetation Assets\\Meshes\\Bushes\\FlowerBush\\'

# -- trees
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Thuja_Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Simple_Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Random_Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Pine_Trees\\TwoSided\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Palm_Trees\\TwoSided\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Oak_Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Fir_Trees\\TwoSided\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Dead Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Birch_Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Apple_Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Trees\\No_Bottoms\\Acacia_Trees\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Stumps\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Logs\\Oak_Logs\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Firewood\\Oak_Firewood\\FBX\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Trees Pack\\Tree Assets\\Meshes\\Firewood\\Birch_Firewood\\FBX\\'

# -- rocks
importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Rocks Pack\\Rock Assets\\Meshes\\1 Color\\Tiles\\'


# texture_filenamepath = 'Z:\\github\\Blender-Python\\asset-textures\\terrain-colors.png'
# texture_filenamepath = 'Z:\\github\\Blender-Python\\asset-textures\\vegetation-colors.png'
# texture_filenamepath = 'Z:\\github\\Blender-Python\\asset-textures\\trees-colors.png'
texture_filenamepath = 'Z:\\github\\Blender-Python\\asset-textures\\rocks-colors.png'

exportdir_fbx = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\'
exportdir_renders = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\renders\\'

filecounter = 0
filelabel = 'firewood2'
FILELIMIT = 10000


for filename_import in listFiles(importdir, 'fbx'):
    deleteAllObjects()

    filenamepath_import = importdir+filename_import;
    bpy.ops.import_scene.fbx(filepath = filenamepath_import)
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            node.image.filepath = texture_filenamepath
        if node.name == 'Principled BSDF':
            node.inputs['Alpha'].default_value = 1.0
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    export_filename_fbx = '{}{:03}.fbx'.format(filelabel,filecounter)
    export_filenamepath_fbx = exportdir_fbx+export_filename_fbx
    export_filename_render = '{}{:03}.png'.format(filelabel,filecounter)
    export_filenamepath_render = exportdir_renders+export_filename_render

    # setShadeSmooth()

    bpy.ops.export_scene.fbx(filepath=export_filenamepath_fbx, path_mode='STRIP', axis_up='Z')
    
    createLight()
    createCamera()

    bpy.context.scene.camera = bpy.data.objects['Camera']
    bpy.data.objects[0].select_set(True)        
    bpy.ops.view3d.camera_to_view_selected()    
    createRender(export_filenamepath_render)

    filecounter += 1
    # exit early (if desirable)
    if filecounter == FILELIMIT:
        break



