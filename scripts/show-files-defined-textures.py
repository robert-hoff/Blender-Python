import bpy
import os


'''
# -- example output
('MountainSkybox.fbx', 'U:\\Dropbox\\SyntyStudios\\PolygonNature\\_Working\\_Andrew\\PolygonNature.png')
('River_Plane_01.fbx', '')
('River_Plane_Dip_01.fbx', '')
('River_Plane_Dip_02.fbx', '')
('River_Plane_WaterFall_01.fbx', '')
('SM_Plant_01.fbx', 'U:\\Dropbox\\SyntyStudios\\PolygonNature\\_Working\\_Andrew\\PolygonNature.png')
('SM_Plant_02.fbx', 'U:\\Dropbox\\SyntyStudios\\PolygonNature\\_Working\\_Andrew\\PolygonNature.png')
('SM_Plant_03.fbx', 'U:\\Dropbox\\SyntyStudios\\PolygonNature\\_Working\\_Andrew\\PolygonNature.png')
('SM_Plant_04.fbx', 'U:\\Dropbox\\SyntyStudios\\PolygonNature\\_Working\\_Andrew\\PolygonNature.png')
('SM_Plant_05.fbx', 'U:\\Dropbox\\SyntyStudios\\PolygonNature\\_Working\\_Andrew\\PolygonNature.png')

'''


# list files in directory, of given extension
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

def importFbx(filenamepath):
    bpy.ops.import_scene.fbx(filepath = filenamepath)

def getImageTextureFilepath():
    for node in bpy.data.objects[0].data.materials[0].node_tree.nodes:
        if node.name == 'Image Texture':
            return node.image.filepath
    return ''

importdir = 'Z:\\dev\\unity3d\\Rock and Vegetation Pack\\Assets\\PolygonNature\\Models\\'
filecounter = 0
FILELIMIT = 10
texturenames = []

for filename_import in listFiles(importdir, 'fbx'):
    deleteAllObjects()
    importFbx(importdir+filename_import)
    img_texture = getImageTextureFilepath()
    texturenames.append((filename_import, img_texture))
    filecounter += 1
    # exit early (if desirable)
    if filecounter == FILELIMIT:
        break

for name in texturenames:
    print(name)


