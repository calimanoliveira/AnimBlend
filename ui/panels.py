import bpy
from bpy.types import Panel, UILayout
from ..operators.ops_tweenmachine import *

class AB_PT_TweenMachine(Panel):
    bl_label = "TweenMachine"
    bl_category = "AnimBlend"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_idname = "AB.tweenmachine"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row()

        rd = context.scene.render
        view = context.space_data
        scene = context.scene
        ob = context.object
        space = context.space_data
        toolsettings = context.tool_settings
        screen = context.screen

        col = layout.column(align=True)
        row = layout.row(align=True)
        row.operator("ab.breakdown0", text="0%", icon="REW")
        row.operator("ab.breakdown10", text="10%", icon="REW")
        row.operator("ab.breakdown33", text="33%", icon="REW")
        row = layout.row(align=True)
        row.operator("ab.breakdown50", text="50%", icon="PAUSE")
        row = layout.row(align=True)
        row.operator("ab.breakdown66", text="66%", icon="FF")
        row.operator("ab.breakdown90", text="90%", icon="FF")
        row.operator("ab.breakdown100", text="100%", icon="FF")
        row = layout.box()
        row.label(text="TweenMachine Variable")
        row.label(text="use SHIFT + E")


class AB_PT_PlayBlast(bpy.types.Panel):
    bl_label = "Playblast"
    bl_category = "AnimBlend"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_idname = "AB.playblast"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout

        col = layout.column(align=True)

        rd = context.scene.render
        # am = context.active_object.data
        view = context.space_data
        scene = context.scene
        ob = context.object
        space = context.space_data
        toolsettings = context.tool_settings
        screen = context.screen
        userpref = context.preferences
        edit = userpref.edit
        #        arm = context.object.data
        #        ad = context.active_object.animation_data
        interpolation = context.preferences.edit.keyframe_new_interpolation_type

        image_settings = rd.image_settings
        file_format = image_settings.file_format

        col = layout.column(align=True)
        col.label(text="Playblast:")

        row = layout.row(align=True)
        row.operator("render.opengl", text="Still", icon='RENDER_STILL')
        row.operator("render.opengl", text="Animation", icon='RENDER_ANIMATION').animation = True
        row.operator("render.play_rendered_anim", text="Play", icon='PLAY')
        row = layout.row()

        layout.template_image_settings(image_settings, color_management=False)
        layout.prop(rd.ffmpeg, "format")

        row = layout.row(align=True)
        row.prop(scene, "use_preview_range", text="", toggle=True)
        if not scene.use_preview_range:
            row.prop(scene, "frame_start", text="Start")
            row.prop(scene, "frame_end", text="End")
        else:
            row.prop(scene, "frame_preview_start", text="Start")
            row.prop(scene, "frame_preview_end", text="End")

        layout.prop(rd, "filepath", text="")
        #        layout.template_image_settings(image_settings, color_management=False)

        col = layout.column(align=True)
        col.prop(edit, "keyframe_new_interpolation_type", text='Keys')
        col.prop(edit, "keyframe_new_handle_type", text="Handles")

        row = layout.row()
        row.prop(bpy.context.space_data.overlay, "show_overlays", text="Only Render View")

class AB_PT_FrameRange(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AnimBlend"

    bl_idname = "AB.animblend"
    bl_label = "AnimBlend UI"

#    @classmethod
#    def poll(cls, context):
#        return

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row()

        rd = context.scene.render
        view = context.space_data
        scene = context.scene
        ob = context.object
        space = context.space_data
        toolsettings = context.tool_settings
        screen = context.screen

        col = layout.column(align=True)
        row = layout.row(align=True)


class AB_PT_animtools_GE(bpy.types.Panel):
    bl_idname = 'ab.animtools_GE_Panel'
    bl_label = "Graph Editor Panel"
    bl_space_type = "GRAPH_EDITOR"
    bl_region_type = "UI"
    bl_category = "Animation"

    # bl_options = {'REGISTER'}

    def draw(self , context):
        layout = self.layout
        scene = context.scene
        my_Properties = scene.my_properties
        layout.operator("ab.curveLocY" , text="LocY")
        # layout.operator("render.opengl", text="Still", icon='RENDER_STILL')
        #        layout.operator("object.animtools", text="Loc Y")
        #        layout.operator("animtools.mover_objeto",text="Move")
        #        layout.operator("animblend.translate_wrapper",text="Move")

        layout.prop(my_Properties , "LocY")

