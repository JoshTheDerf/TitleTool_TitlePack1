import sys
import os
import bpy


def init(params):
    bpy.data.objects["Text"].data.body = params['titleText']
    bpy.data.materials['Material'].diffuse_color = params['color1']
    bpy.data.materials['Material'].texture_slots[0].color = params['color2']

    if params['animation']:
        bpy.ops.render.render(animation=True)
