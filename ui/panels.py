import bpy
from bpy.types import Panel, UILayout

class AB_PT_Anim_Blend(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "ABTools"

    bl_idname = "AB_PT_anim_blend"
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
        userpref = context.user_preferences
        edit = userpref.edit
        interpolation = context.user_preferences.edit.keyframe_new_interpolation_type

        col = layout.column(align=True)
        row = layout.row(align=True)


class AB_PT_Tween_Machine(Panel):
    bl_label = "TweenMachine"
    bl_category = "ABTools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_idname = "AB_PT_tween_machine"
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
        userpref = context.user_preferences
        edit = userpref.edit
        interpolation = context.user_preferences.edit.keyframe_new_interpolation_type
"""
        col = layout.column(align=True)
        row = layout.row(align=True)
        row.operator("pose.breakdown0", text="0%", icon="REW")
        row.operator("pose.breakdown10", text="10%", icon="REW")
        row.operator("pose.breakdown33", text="33%", icon="REW")
        row = layout.row(align=True)
        row.operator("pose.breakdown50", text="50%", icon="PAUSE")
        row = layout.row(align=True)
        row.operator("pose.breakdown66", text="66%", icon="FF")
        row.operator("pose.breakdown90", text="90%", icon="FF")
        row.operator("pose.breakdown100", text="100%", icon="FF")
        row = layout.box()
        row.label("TweenMachine Variable")
        row.label("use SHIFT + E")
"""

classes = (
    AB_PT_Anim_Blend,
    AB_PT_Tween_Machine
)

def register(reg):
    for cls in classes:
        bpy.utils.register_class(cls)
        #reg(cls)

def unregister(unreg):
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        #unreg(cls)