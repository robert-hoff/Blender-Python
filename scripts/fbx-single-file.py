import bpy

def checkAlpha(obj):
    bsdf_alpha = obj.data.materials[0].node_tree.nodes['Principled BSDF'].inputs['Alpha']
    if bsdf_alpha.default_value == 0:
        bsdf_alpha.default_value = 1.0

# note that shade-auto may be useful with certain models
# for giving a mix between flat and smooth surfaces
def setShadeSmoothOrFlat(obj):
    if USE_SHADE_SMOOTH:
        bpy.ops.object.shade_smooth()

def setTextureFilePath(obj, file):
    img_texture = obj.data.materials[0].node_tree.nodes['Image Texture']
    # img_texture.image.name = 'new name'
    img_texture.image.filepath = file

def getMeshObjects():
    mesh_objects = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            mesh_objects.append(obj)
    return mesh_objects

# wehere no directory is given, will export to the same location as the blender file
def exportFbx():
    mesh_objects = getMeshObjects()
    if len(mesh_objects) != 1:
        raise Exception('wrong number of mesh objects present {}'.format(len(mesh_objects)))
    mesh_objects[0].select_set(True)
    checkAlpha(mesh_objects[0])
    setShadeSmoothOrFlat(mesh_objects[0])
    setTextureFilePath(mesh_objects[0], TEXTURE_FILE)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.export_scene.fbx(filepath = EXPORT_TARGET_FILE, path_mode = 'STRIP', axis_up = 'Z', object_types={'MESH'})

def showObjectProperties(obj):
    members = dir(obj)
    members.sort()
    print('\n\n--- object properties')
    for name in members:
        print('{:40s} {}'.format(name, getattr(obj, name)))



textureFiles = {
    'plant': 'Z:\\active\\projects\\game-development-2023\\blender-FBX-import-export\\vegetation-colors.png',
    'tree': 'Z:\\active\\projects\\game-development-2023\\blender-FBX-import-export\\trees-colors.png',
    'rock': 'Z:\\active\\projects\\game-development-2023\\blender-FBX-import-export\\rocks-colors.png',
    
    # 'plant': 'vegetation-colors.png',
    # 'tree': 'trees-colors.png',
    # 'rock': 'rocks-colors.png',        
}

exportTargets = {
    'plant_ex': 'Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\plants\\plant-example.fbx',
    'tree_ex': 'Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\trees\\tree-example.fbx',
}

USE_SHADE_SMOOTH = True
TEXTURE_FILE = textureFiles['plant']
EXPORT_TARGET_FILE = exportTargets['plant_ex']
exportFbx()





