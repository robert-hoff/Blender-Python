import bpy
import os
import math

'''
This version preserves the names of imported files

'''

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
    bpy.context.scene.render.resolution_x = 480
    bpy.context.scene.render.resolution_y = 270
    bpy.ops.render.render(write_still=True)


def importFbx(filenamepath):
    bpy.ops.import_scene.fbx(filepath = filenamepath)

def getImageTextureFilepath():
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            return node.image.filepath
    return ''

def setImageTexture(filenamepath):
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            node.image.filepath = filenamepath

def setAlpha():
    fbx_object = bpy.data.objects[0]
    for node in fbx_object.data.materials[0].node_tree.nodes:
        if node.name == 'Principled BSDF':
            node.inputs['Alpha'].default_value = 1.0

def removeVertexColors():
    fbx_object = bpy.data.objects[0]
    for v in fbx_object.data.vertex_colors:
        fbx_object.data.vertex_colors.remove(v)


'''
# -- prints
<bpy_struct, NodeSocketColor("Base Color")>
<bpy_struct, NodeSocketFloatFactor("Subsurface")>
# ...

'''
def showMaterialInputs():
    fbx_object = bpy.data.objects[0]
    for node in fbx_object.data.materials[0].node_tree.nodes:
        if node.name == 'Principled BSDF':
            for node_input in node.inputs:
                print(node_input)

def assignTexture(texturename, filenamepath):
    fbx_object = bpy.data.objects[0]
    for node in fbx_object.data.materials[0].node_tree.nodes:
        if node.name == 'Principled BSDF':
            mat = bpy.data.materials.new(name = texturename)
            mat.use_nodes = True
            bsdf = mat.node_tree.nodes['Principled BSDF']
            texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
            texImage.image = bpy.data.images.load(filenamepath)
            mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
            fbx_object.data.materials[0] = mat

def scaleAndTranslateObject():
    fbx_object = bpy.data.objects[0]
    fbx_object.select_set(True)
    bpy.ops.transform.resize(value = (0.5, 0.5, 0.5))
    bpy.ops.transform.translate(value = (0, 50, 0))

def exportFbx(filenamepath):
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.export_scene.fbx(filepath=filenamepath, path_mode='STRIP', axis_up='Z', use_tspace =True)


# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\PolygonNature\\Models\\'
# import_texturesdir = 'Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\polygon-nature\\'
# texture_filenamepath = import_texturesdir+'polygon-nature.png'

# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Terrain\\CPT\\NoLOD\\M\\'
importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Bonus Assets\\Meshes\\Terrain\\'
import_texturesdir = 'Z:\\github\\Blender-Python\\'
texture_filename = 'terrain-grass.png'
texture_filenamepath = import_texturesdir+texture_filename

# exportdir_fbx = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\'
# exportdir_renders = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\renders\\'


# filenamepath_singlefile = importdir+'Terrain_m_06.fbx'
# deleteAllObjects()
# bpy.ops.import_scene.fbx(filepath = filenamepath_singlefile)
# setAlpha()
# assignTexture(texture_filename[0:-4], texture_filenamepath)
# scaleAndTranslateObject()



export_filenamepath1 = 'Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\terrain-tiles\\terrain001.fbx'
exportFbx(export_filenamepath1)




