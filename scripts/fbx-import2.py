import bpy
import os
import math

'''
This version preserves the names of imported files

'''

def degreesToRad(degrees):
    return math.pi * degrees / 180

def importFbx(filenamepath):
    bpy.ops.import_scene.fbx(filepath = filenamepath)

def exportFbx(filenamepath):
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.export_scene.fbx(filepath=filenamepath, path_mode='STRIP', axis_up='Z')

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
    light_data = bpy.data.lights.new(name='Light', type='SPOT')
    light = bpy.data.objects.new(name='Light', object_data=light_data)
    bpy.context.collection.objects.link(light)
    light.data.energy = 120000
    light.location = (77.289, -13.289, 31.443)
    light.rotation_euler[0] = degreesToRad(40.4)
    light.rotation_euler[1] = degreesToRad(52.2)
    light.rotation_euler[2] = degreesToRad(7.4)
    # light.data.angle = degreesToRad(15)
    light.data.spot_size = 45
    

def createCamera():
    camera_data = bpy.data.cameras.new(name='Camera')
    camera = bpy.data.objects.new('Camera', camera_data)
    bpy.context.collection.objects.link(camera)
    camera.location = (96.943, -43.903, 68.211)
    camera.rotation_euler[0] = degreesToRad(53.2)
    camera.rotation_euler[1] = degreesToRad(-0.0013)
    camera.rotation_euler[2] = degreesToRad(47.6)

def createRender(filenamepath):
    bpy.data.scenes['Scene'].camera = bpy.context.scene.objects['Camera']
    bpy.context.scene.render.filepath = filenamepath
    bpy.context.scene.render.resolution_x = 720
    bpy.context.scene.render.resolution_y = 405
    bpy.ops.render.render(write_still=True)


def getImageTextureFilepath():
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            return node.image.filepath
    return ''

def setImageTexture(filenamepath):
    print(filenamepath)
    node_image = bpy.data.objects[0].data.materials[0].node_tree.nodes['Image Texture']
    node_image.image.filepath = filenamepath
    
#    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
#        if node.name == 'Image Texture':
#            node.image.filepath = filenamepath

def conditionMesh():
    fbx_object = bpy.data.objects[0]
    for v in fbx_object.data.vertex_colors:
        fbx_object.data.vertex_colors.remove(v)
    for node in fbx_object.data.materials[0].node_tree.nodes:
        if node.name == 'Principled BSDF':
            node.inputs['Alpha'].default_value = 1.0

def setShadeSmooth():
    fbx_object = bpy.data.objects[0]
    fbx_object.select_set(True)
    bpy.ops.object.shade_smooth()




# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Terrain\\CPT\\NoLOD\\M\\'
# importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Modular Terrain Pack\\Terrain_Assets\\Meshes\\Mountains\\CPT\\NoLOD\\M\\'
importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\Low Poly Vegetation Pack\\Bonus Assets\\Meshes\\Terrain\\'


# import_texturesdir = 'Z:\\github\\Blender-Python\\asset-textures\\'
import_texturesdir = 'Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\terrain-tiles\\'

# texture_filenamepath = import_texturesdir+'terrain-grass.png'
texture_filenamepath = import_texturesdir+'terrain-colors.png'

exportdir_fbx = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\'
exportdir_renders = 'Z:\\active\\projects\\edinburgh-gamejam\\exportdir\\renders\\'


filecounter = 0
FILELIMIT = 1
for filename_import in listFiles(importdir, 'fbx'):
    deleteAllObjects()
    filenamepath_import = importdir+filename_import;
    bpy.ops.import_scene.fbx(filepath = filenamepath_import)
    img_texture = getImageTextureFilepath()
    if img_texture != '':
        conditionMesh()
        setImageTexture(texture_filenamepath)
        setShadeSmooth()
        fbx_name = filename_import[0:-4]        
        exportFbx(exportdir_fbx+fbx_name+'.fbx')    
        # -- create render
        bpy.data.objects[0].select_set(True)
        createCamera()
        createLight()
        bpy.context.scene.camera = bpy.data.objects['Camera']
        # bpy.ops.view3d.camera_to_view_selected()
        createRender(exportdir_renders+fbx_name+'.png')
    filecounter += 1
    # exit early (if desirable)
    if filecounter == FILELIMIT:
        break


