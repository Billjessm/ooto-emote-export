import bpy
from .OoTOE_utils import *


class OoTOE_OT_ExportAnim(bpy.types.Operator):
    bl_idname = "oot_online.export"
    bl_label = "Simple operator"
    bl_description = "Exports the animation"

    def execute(self,context):
        a = Animation()
        sce = bpy.context.scene
        armature = bpy.data.objects["skeleton"]

        a.anim_name = sce.OoTOE_Properties.ootoe_name
        a.repeat = sce.OoTOE_Properties.ootoe_repeat
        savepath = sce.OoTOE_Properties.ootoe_savepath

        #print(" -"*10)
        for f in range(sce.frame_start, sce.frame_end+1):
            sce.frame_set(f)
            #print("Frame %i" % f)
            #print(" -"*5)
            a.addframe()
            for bone in armature.pose.bones:
                if bone.name == "LinkRoot":
                    a.editframe(f-1,"LinkBase",[bone.location[0]*1547.9,bone.location[1]*1547.9,bone.location[2]*1547.9]) #3500
                a.editframe(f-1,bone.name,[convert_rad(bone.rotation_euler[0]),convert_rad(bone.rotation_euler[1]),convert_rad(bone.rotation_euler[2])])
                #print(bone.name)
                #print(convert_rad(bone.rotation_euler[0]),convert_rad(bone.rotation_euler[1]),convert_rad(bone.rotation_euler[2]))
        a.repeat_times[0] = len(a.frames)
        save_animation(False,a,savepath)
        return {'FINISHED'}

