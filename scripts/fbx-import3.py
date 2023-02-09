import bpy
import os
import math

'''
Preserves the names of imported files

+ assigns a newly created texture,
assigning a new texture requires a bit more than just adding the image.
Some of the material parameters like colors and normals may be subject
to use by different shaders.
Currently the basic Monogame shader use the Principled BSDF 'Base Color' input
as part of the diffuse coloration. Some other properties that are certain
include Specular and Alpha.

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
    bpy.context.scene.render.resolution_x = 720
    bpy.context.scene.render.resolution_y = 405
    bpy.ops.render.render(write_still=True)


def importFbx(filenamepath):
    bpy.ops.import_scene.fbx(filepath = filenamepath)

def exportFbx(filenamepath):
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.export_scene.fbx(filepath=filenamepath, path_mode='STRIP', axis_up='Z')

def getImageTextureFilepath():
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            return node.image.filepath
    return ''

def setImageTexture(filenamepath):
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            node.image.filepath = filenamepath

def conditionMesh():
    fbx_object = bpy.data.objects[0]
    for v in fbx_object.data.vertex_colors:
        fbx_object.data.vertex_colors.remove(v)
    for node in fbx_object.data.materials[0].node_tree.nodes:
        if node.name == 'Principled BSDF':
            node.inputs['Alpha'].default_value = 1.0

def createTexture(texturename, filenamepath):
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

# float
def setMaterialRoughness(value):
    bpy.data.objects[0].data.materials[0].roughness = value

# float
def setMaterialSpecularIntensity(value):
    bpy.data.objects[0].data.materials[0].specular_intensity = value

def setBsdfRoughness(value):
    bsdf = bpy.data.objects[0].data.materials[0].node_tree.nodes['Principled BSDF']
    bsdf.inputs['Roughness'].default_value = value

def setBsdfSpecular(value):
    bsdf = bpy.data.objects[0].data.materials[0].node_tree.nodes['Principled BSDF']
    bsdf.inputs['Specular'].default_value = value

def setBsdfEmissionStrength(value):
    bsdf = bpy.data.objects[0].data.materials[0].node_tree.nodes['Principled BSDF']
    bsdf.inputs['Emission Strength'].default_value = value

def setBsdfBaseColor(r, g, b, a):
    bsdf = bpy.data.objects[0].data.materials[0].node_tree.nodes['Principled BSDF']
    bsdf.inputs['Base Color'].default_value = (r, g, b, a)

def setShadeSmooth():
    fbx_object = bpy.data.objects[0]
    fbx_object.select_set(True)
    bpy.ops.object.shade_smooth()


# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Terrain\\CPT\\NoLOD\\M\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Bonus Assets\\Meshes\\Terrain\\'
importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\River\\CPT\\NoLOD\\M\\'

import_texturesdir = 'Z:\\github\\Blender-Python\\asset-textures\\'
# texture_filename = 'terrain-grass.png'
texture_filename = 'terrain-colors.png'
texture_filenamepath = import_texturesdir+texture_filename

exportdir_fbx = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\'
exportdir_renders = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\renders\\'


filecounter = 0
FILELIMIT = 1

for filename_import in listFiles(importdir, 'fbx'):
    deleteAllObjects()
    filenamepath_import = importdir+filename_import;
    bpy.ops.import_scene.fbx(filepath = filenamepath_import)

    img_texture = getImageTextureFilepath()
    # if img_texture == '':
    conditionMesh()
    setImageTexture(texture_filenamepath)
    fbx_name = filename_import[0:-4]
    createTexture(texture_filename[0:-4], texture_filenamepath)
    # scaleAndTranslateObject()
    setMaterialRoughness(0.69)
    setMaterialSpecularIntensity(0.0)
    setBsdfRoughness(0.69)
    setBsdfSpecular(0)
    setBsdfEmissionStrength(0)
    setBsdfBaseColor(1,1,1,1)
    setShadeSmooth()
    exportFbx(exportdir_fbx+fbx_name+'.fbx')

    # -- zoom to object, create render
    bpy.data.objects[0].select_set(True)
    createCamera()
    createLight()
    bpy.context.scene.camera = bpy.data.objects['Camera']
    bpy.ops.view3d.camera_to_view_selected()
    createRender(exportdir_renders+fbx_name+'.png')

    filecounter += 1
    # exit early (if desirable)
    if filecounter == FILELIMIT:
        break


