import sys
import os
import bpy


def init(params):
    bpy.data.objects["Font"].data.body = params['titleText']

    bpy.data.materials['Material'].diffuse_color = params['textcolor']
    bpy.data.materials['HaloMaterial'].diffuse_color = params['halocolor']
    bpy.data.materials['HaloMaterial'].specular_color = params['halocolor2']
    bpy.data.worlds['World'].horizon_color = params['worldcolor']

    if params['animation']:
        bpy.ops.render.render(animation=True)
