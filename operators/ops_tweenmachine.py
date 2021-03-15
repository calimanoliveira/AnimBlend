import bpy


class AB_OT_ValBreakdown_0(bpy.types.Operator):
    bl_idname = "ab.breakdown0"
    bl_label = "Val0"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class AB_OT_ValBreakdown_10(bpy.types.Operator):
    bl_idname = "ab.breakdown10"
    bl_label = "Val10"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current
        print(posAnterior)
        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current
        print(posPosterior)

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(percentage=0.1,prev_frame=posAnterior, next_frame=posPosterior)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class AB_OT_ValBreakdown_33(bpy.types.Operator):
    bl_idname = "ab.breakdown33"
    bl_label = "Val0"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.33)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class AB_OT_ValBreakdown_50(bpy.types.Operator):
    bl_idname = "ab.breakdown50"
    bl_label = "Val50"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.5)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class AB_OT_ValBreakdown_ab(bpy.types.Operator):
    bl_idname = "pose.breakdown66"
    bl_label = "Val66"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.66)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class AB_OT_ValBreakdown_90(bpy.types.Operator):
    bl_idname = "ab.breakdown90"
    bl_label = "Val90"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.9)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class AB_OT_ValBreakdown_100(bpy.types.Operator):
    bl_idname = "ab.breakdown100"
    bl_label = "Val100"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=1)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}
'''
def register():
    bpy.utils.register_class(ValBreakdown_0)
    bpy.utils.register_class(ValBreakdown_10)
    bpy.utils.register_class(ValBreakdown_33)
    bpy.utils.register_class(ValBreakdown_50)
    bpy.utils.register_class(ValBreakdown_66)
    bpy.utils.register_class(ValBreakdown_90)
    bpy.utils.register_class(ValBreakdown_100)

    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_class(ValBreakdown_0)
    bpy.utils.unregister_class(ValBreakdown_10)
    bpy.utils.unregister_class(ValBreakdown_33)
    bpy.utils.unregister_class(ValBreakdown_50)
    bpy.utils.unregister_class(ValBreakdown_66)
    bpy.utils.unregister_class(ValBreakdown_90)
    bpy.utils.unregister_class(ValBreakdown_100)

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
'''