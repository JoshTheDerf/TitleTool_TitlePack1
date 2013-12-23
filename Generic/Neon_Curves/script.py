import sys
import os
import bpy


def init(params):

    bpy.data.objects["Font"].data.body = params['titleText']
    bpy.data.materials["Material.line1"].diffuse_color = params['lineColor']
    bpy.data.materials["Material.line2"].diffuse_color = (
        params['lineColor'][0] + 0.4, params['lineColor'][1] + 0.4,
        params['lineColor'][1] + 0.4)

    bpy.data.materials["Material.line3"].diffuse_color = (
        params['lineColor'][0] - 0.5, params['lineColor'][1] - 0.5,
        params['lineColor'][1] - 0.5)

    bpy.data.materials["Material.line4"].diffuse_color = (
        params['lineColor'][0] - 0.4,
        params['lineColor'][1] - 0.4,
        params['lineColor'][1] - 0.4)

    bpy.data.materials["Material.title"].diffuse_color = params['textColor']

    if params['bgBlur'] == "More":
        bpy.data.materials["Material.line1"].use_shadeless = False
        bpy.data.materials["Material.line2"].use_shadeless = False
        bpy.data.materials["Material.line3"].use_shadeless = False
        bpy.data.materials["Material.line4"].use_shadeless = False

    if params['animation']:
        bpy.ops.render.render(animation=True)
