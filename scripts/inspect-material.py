import bpy

# show number of materials defined on the object
def showMaterialCount():
    fbx_object = bpy.data.objects[0]
    materials = []
    for material in fbx_object.data.materials:
        materials.append(material)
    print('number of materials {}'.format(len(materials)))


def showBpyFloat4(label, f4):
    print('{}: {}, {}, {}, {}'.format(label, f4[0], f4[1], f4[2], f4[3]))

def formatBpyFloat4(f4):
    return '{:.4f}, {:.4f}, {:.4f}, {:.4f}'.format(f4[0], f4[1], f4[2], f4[3])

def formatBpyFloat3(f3):
    return '{:.4f}, {:.4f}, {:.4f}'.format(f3[0], f3[1], f3[2])


def showMaterialDiffuseColor():
    material = bpy.data.objects[0].data.materials[0]
    showBpyFloat4('diffuse_color', material.diffuse_color)

def showMaterialProperties():
    print('\n\n----- material properties')
    material = bpy.data.objects[0].data.materials[0]
    print('diffuse_color: {}'.format(formatBpyFloat4(material.diffuse_color)))
    print('material.alpha_threshold: {}'.format(material.alpha_threshold))
    print('material.blend_method: {}'.format(material.blend_method))
    print('material.metallic: {}'.format(material.metallic))
    print('material.pass_index: {}'.format(material.pass_index))
    print('material.refraction_depth: {}'.format(material.refraction_depth))
    print('material.roughness: {}'.format(material.roughness))
    print('material.shadow_method: {}'.format(material.shadow_method))
    print('material.specular_color: {}'.format(material.specular_color))
    print('material.specular_intensity: {}'.format(material.specular_intensity))
    print('material.use_nodes: {}'.format(material.use_nodes))
    print('material.use_backface_culling: {}'.format(material.use_backface_culling))
    print('material.use_preview_world: {}'.format(material.use_preview_world))
    print('material.use_screen_refraction: {}'.format(material.use_screen_refraction))
    print('material.use_sss_translucency: {}'.format(material.use_sss_translucency))
    print('material.texture_paint_images count: {}'.format(len(material.texture_paint_images)))
    print('material.texture_paint_slots count: {}'.format(len(material.texture_paint_slots)))
    print('material.cycles: {}'.format(material.cycles))
    print('material.grease_pencil: {}'.format(material.grease_pencil))
    print('material.is_grease_pencil: {}'.format(material.is_grease_pencil))
    # showBpyFloat4('line_color', material.line_color)
    print('material.line_priority: {}'.format(material.line_priority))
    print('material.lineart: {}'.format(material.lineart))
    print('material.node_tree: {}'.format(material.node_tree))


def showNodeTree():
    material_node_tree = bpy.data.objects[0].data.materials[0].node_tree
    print('material.node_tree: {}'.format(material_node_tree))
    material_nodes = material_node_tree.nodes
    for node in material_nodes:
        print(node)
    
# <bpy_struct, ShaderNodeOutputMaterial("Material Output")>
# <bpy_struct, ShaderNodeBsdfPrincipled("Principled BSDF")>
# <bpy_struct, ShaderNodeTexImage("Image Texture")>
# <bpy_struct, ShaderNodeNormalMap("Normal Map")>    
    
    
def showPrincipledBsdf():
    material_nodes = bpy.data.objects[0].data.materials[0].node_tree.nodes
    node_bsdf = material_nodes['Principled BSDF']
    print('node_bsdf.distribution: {}'.format(node_bsdf.distribution))
    print('node_bsdf.subsurface_method: {}'.format(node_bsdf.subsurface_method))
    print('node_bsdf.is_registered_node_type(): {}'.format(node_bsdf.is_registered_node_type()))
    print('node_bsdf.type: {}'.format(node_bsdf.type))
    print('node_bsdf.location: {}'.format(node_bsdf.location))
    print('node_bsdf.inputs: {}'.format(node_bsdf.inputs))
    print('node_bsdf.parent: {}'.format(node_bsdf.parent))
    print('node_bsdf.color: {}'.format(node_bsdf.color))


def showPrincipledBsdfInputs():
    material_nodes = bpy.data.objects[0].data.materials[0].node_tree.nodes
    bsdf_inputs = material_nodes['Principled BSDF'].inputs
    print(bsdf_inputs['Base Color'])
    print(bsdf_inputs['Subsurface'])
    print(bsdf_inputs['Subsurface Radius'])
    print(bsdf_inputs['Subsurface Color'])
    print(bsdf_inputs['Metallic'])
    print(bsdf_inputs['Specular'])
    print(bsdf_inputs['Specular Tint'])
    print(bsdf_inputs['Roughness'])
    print(bsdf_inputs['Anisotropic'])
    print(bsdf_inputs['Anisotropic Rotation'])
    print(bsdf_inputs['Sheen'])
    print(bsdf_inputs['Sheen Tint'])
    print(bsdf_inputs['Clearcoat'])
    print(bsdf_inputs['Clearcoat Roughness'])
    print(bsdf_inputs['IOR'])
    print(bsdf_inputs['Transmission'])
    print(bsdf_inputs['Transmission Roughness'])
    print(bsdf_inputs['Emission'])
    print(bsdf_inputs['Alpha'])
    print(bsdf_inputs['Normal'])
    print(bsdf_inputs['Clearcoat Normal'])
    print(bsdf_inputs['Tangent'])
    #    print(bsdf_inputs['Base Color'].default_value)
    #    print(bsdf_inputs['Subsurface'].default_value)
    #    print(bsdf_inputs['Subsurface Radius'].default_value)
    #    print(bsdf_inputs['Subsurface Color'].default_value)
    #    print(bsdf_inputs['Metallic'].default_value)
    #    print(bsdf_inputs['Specular'].default_value)
    #    print(bsdf_inputs['Specular Tint'].default_value)
    #    print(bsdf_inputs['Roughness'].default_value)
    #    print(bsdf_inputs['Anisotropic'].default_value)
    #    print(bsdf_inputs['Anisotropic Rotation'].default_value)
    #    print(bsdf_inputs['Sheen'].default_value)
    #    print(bsdf_inputs['Sheen Tint'].default_value)
    #    print(bsdf_inputs['Clearcoat'].default_value)
    #    print(bsdf_inputs['Clearcoat Roughness'].default_value)
    #    print(bsdf_inputs['IOR'].default_value)
    #    print(bsdf_inputs['Transmission'].default_value)
    #    print(bsdf_inputs['Transmission Roughness'].default_value)
    #    print(bsdf_inputs['Emission'].default_value)
    #    print(bsdf_inputs['Alpha'].default_value)
    #    print(bsdf_inputs['Normal'].default_value)
    #    print(bsdf_inputs['Clearcoat Normal'].default_value)
    #    print(bsdf_inputs['Tangent'].default_value)

def showPrincipledBsdfDefaultValues():
    # bsdf_inputs = bpy.data.objects[0].data.materials[0].node_tree.nodes['Principled BSDF'].inputs
    # bsdf_base_color = bsdf_inputs['Base Color']
    # bsdf_subsurface = bsdf_inputs['Subsurface']
    # bsdf_subsurface_radius = bsdf_inputs['Subsurface Radius']
    # bsdf_subsurface_color = bsdf_inputs['Subsurface Color']
    # bsdf_metallic = bsdf_inputs['Metallic']
    # bsdf_specular = bsdf_inputs['Specular']
    # bsdf_specular_tint = bsdf_inputs['Specular Tint']
    # bsdf_roughness = bsdf_inputs['Roughness']
    # bsdf_anisotropic = bsdf_inputs['Anisotropic']
    # bsdf_anisotropic_rotation = bsdf_inputs['Anisotropic Rotation']
    # bsdf_sheen = bsdf_inputs['Sheen']
    # bsdf_sheen_tint = bsdf_inputs['Sheen Tint']
    # bsdf_clearcoat = bsdf_inputs['Clearcoat']
    # bsdf_clearcoat_roughness = bsdf_inputs['Clearcoat Roughness']
    # bsdf_ior = bsdf_inputs['IOR']
    # bsdf_transmission = bsdf_inputs['Transmission']
    # bsdf_transmission_roughness = bsdf_inputs['Transmission Roughness']
    # bsdf_emission = bsdf_inputs['Emission']
    # bsdf_alpha = bsdf_inputs['Alpha']
    # bsdf_normal = bsdf_inputs['Normal']
    # bsdf_clearcoat_normal = bsdf_inputs['Clearcoat Normal']
    # bsdf_tangent = bsdf_inputs['Tangent']
    print('\n\n----- principled bsdf defaults')
    bsdf = bpy.data.objects[0].data.materials[0].node_tree.nodes['Principled BSDF'].inputs
    print("{:50s}{}".format("bsdf['Base Color'].default_value", formatBpyFloat4(bsdf['Base Color'].default_value)))
    print("{:50s}{}".format("bsdf['Subsurface'].default_value", bsdf['Subsurface'].default_value))
    print("{:50s}{}".format("bsdf['Subsurface Radius'].default_value", formatBpyFloat3(bsdf['Subsurface Radius'].default_value)))
    print("{:50s}{}".format("bsdf['Subsurface Color'].default_value", formatBpyFloat4(bsdf['Subsurface Color'].default_value)))
    print("{:50s}{}".format("bsdf['Metallic'].default_value", bsdf['Metallic'].default_value))
    print("{:50s}{}".format("bsdf['Specular'].default_value", bsdf['Specular'].default_value))
    print("{:50s}{}".format("bsdf['Specular Tint'].default_value", bsdf['Specular Tint'].default_value))
    print("{:50s}{}".format("bsdf['Roughness'].default_value", bsdf['Roughness'].default_value))
    print("{:50s}{}".format("bsdf['Anisotropic'].default_value", bsdf['Anisotropic'].default_value))
    print("{:50s}{}".format("bsdf['Anisotropic Rotation'].default_value", bsdf['Anisotropic Rotation'].default_value))
    print("{:50s}{}".format("bsdf['Sheen'].default_value", bsdf['Sheen'].default_value))
    print("{:50s}{}".format("bsdf['Sheen Tint'].default_value", bsdf['Sheen Tint'].default_value))
    print("{:50s}{}".format("bsdf['Clearcoat'].default_value", bsdf['Clearcoat'].default_value))
    print("{:50s}{:.4f}".format("bsdf['Clearcoat Roughness'].default_value", bsdf['Clearcoat Roughness'].default_value))
    print("{:50s}{:.4f}".format("bsdf['IOR'].default_value", bsdf['IOR'].default_value))
    print("{:50s}{}".format("bsdf['Transmission'].default_value", bsdf['Transmission'].default_value))
    print("{:50s}{}".format("bsdf['Transmission Roughness'].default_value", bsdf['Transmission Roughness'].default_value))
    print("{:50s}{}".format("bsdf['Emission'].default_value", formatBpyFloat4(bsdf['Emission'].default_value)))
    print("{:50s}{}".format("bsdf['Alpha'].default_value", bsdf['Alpha'].default_value))
    print("{:50s}{}".format("bsdf['Normal'].default_value", formatBpyFloat3(bsdf['Normal'].default_value)))
    print("{:50s}{}".format("bsdf['Clearcoat Normal'].default_value", formatBpyFloat3(bsdf['Clearcoat Normal'].default_value)))
    print("{:50s}{}".format("bsdf['Tangent'].default_value", formatBpyFloat3(bsdf['Tangent'].default_value)))


# float4
def setPrincipledBsdfBaseColorDefaultValue(r, g, b, a):
    bsdf_base_color = bpy.data.objects[0].data.materials[0].node_tree.nodes['Principled BSDF'].inputs['Base Color']
    bsdf_base_color.default_value = (r, g, b, a)

# float
def setRoughness(value):
    bpy.data.objects[0].data.materials[0].roughness = value

# float
def setSpecularIntensity(value):
    bpy.data.objects[0].data.materials[0].specular_intensity = value

# True / False
def setUseNodes(value):
    bpy.data.objects[0].data.materials[0].use_nodes = value


export_filenamepath1 = 'Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\terrain-tiles\\terrain001.fbx'
export_filenamepath2 = 'Z:\\github\\LSystemsMG\\LSystemsMG\\Content\\terrain-tiles\\terrain002.fbx'
def exportFbx(filenamepath):
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    # bpy.ops.export_scene.fbx(filepath=filenamepath, path_mode='STRIP', axis_up='Z')
    # bpy.ops.export_scene.fbx(filepath=filenamepath, path_mode='STRIP', axis_up='Z', use_tspace =True)
    # bpy.ops.export_scene.fbx(filepath=filenamepath, path_mode='STRIP', axis_up='Z', use_active_collection=True)
    bpy.ops.export_scene.fbx(filepath=filenamepath, path_mode='STRIP', axis_up='Z', axis_forward='X')    



print('---')
# showMaterialCount()
# showMaterialDiffuseColor()
# setRoughness(0.69)
# setSpecularIntensity(0)
# setUseNodes(True)
# showMaterialProperties()
# showNodeTree()
# showPrincipledBsdf()
# showPrincipledBsdfInputs()
# showPrincipledBsdfInputsBaseColor()

# --- export either as terrain001.fbx or terrain002.fbx
exportFbx(export_filenamepath1)
exportFbx(export_filenamepath2)









