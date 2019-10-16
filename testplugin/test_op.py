import bpy
import math
import json
import os
def save_animation(load,animation):
    print(os.getcwd())
    if not load:
        with open(animation.anim_name + '.json', 'w+') as f:
            json.dump({"name":animation.anim_name,"repeat":animation.repeat,"repeat_limit":animation.repeat_times[0],"repeat_start":animation.repeat_times[1],"frames":animation.returnframes()}, f)
        f.closed
    else:
        try:
            with open(animation.anim_name + '.json') as f:
                filedata= json.load(f)
            f.closed
        except:
            print('error reading file!')
            return
        print(filedata)

class Skeleton(object):
    def __init__(self):
        self.bones = {
        'LinkBase':[0,0,0],
        'LinkRoot':[0,0,0],
        'LinkWaist':[0,0,0],
        'LinkButt':[0,0,0],
        "LinkLeg_R1":[0,0,0],
        "LinkLeg_R2":[0,0,0],
        "LinkLeg_R3":[0,0,0],
        "LinkLeg_L1":[0,0,0],
        "LinkLeg_L2":[0,0,0],
        "LinkLeg_L3":[0,0,0],
        "LinkTorso":[0,0,0],
        "LinkNeck":[0,0,0],
        "LinkHat":[0,0,0],
        "LinkCollar":[0,0,0],
        "LinkArm_L1":[0,0,0],
        "LinkArm_L2":[0,0,0],
        "LinkArm_L3":[0,0,0],
        "LinkArm_R1":[0,0,0],
        "LinkArm_R2":[0,0,0],
        "LinkArm_R3":[0,0,0],
        "LinkEquipment":[0,0,0],
        "LinkEyes":0
        }
    def getbones(self):
        return self.bones

class Frame(object):
    def __init__(self):
        a = Skeleton()
        self.frame = {"bones":a}
    def editbone(self,bonename,bone):
        a = self.frame["bones"]
        a.bones[bonename] = bone
        #self.frame[0][bonename] = bone
    def getframe(self):
        return {"bones":self.frame["bones"].getbones()}
    
class Animation(object):
    def __init__(self):
        self.frames = []
        self.repeat = True
        self.repeat_times = [1,1]
        self.anim_name = "new animation"
    def addframe(self):
        a = Frame()
        self.frames.append(a)
    def returnframes(self):
        b = []
        for a in self.frames:
            b.append(a.getframe())
        return b
    def editframe(self,i,bonename,bone):
        self.frames[i].editbone(bonename,bone)

def convert_rad(rad):
    a = (rad*65535)//(math.pi*2)
    while a < 0:
        a += 65535
    return a


class Test_OT_Operator(bpy.types.Operator):
    bl_idname = "oot_online.export"
    bl_label = "Simple operator"
    bl_description = "Center 3d cursor"
    #ootoe_name: bpy.props.StringProperty(name = "ootoe_name")
    #ootoe_savepath: bpy.props.StringProperty(name = "ootoe_savepath")
    #ootoe_repeat: bpy.props.BoolProperty(name = "ootoe_repeat", default = True)
    #ootoe_repeat_resetto: bpy.props.IntProperty(name = "ootoe_repeat_resetto", default = 1, min = 0)
    #ootoe_repeat_limit: bpy.props.IntProperty(name = "ootoe_repeat_limit", default = 30, min = 0)

    def execute(self,context):
        #bpy.ops.view3d.snap_cursor_to_center()
        a = Animation()
        sce = bpy.context.scene
        armature = bpy.data.objects["skeleton"]
        thing = armature.pose
        print(" -"*10)
        for f in range(sce.frame_start, sce.frame_end+1):
            sce.frame_set(f)
            print("Frame %i" % f)
            print(" -"*5)
            a.addframe()
            for bone in thing.bones:
                if bone.name == "LinkRoot":
                    a.editframe(f-1,"LinkBase",[bone.location[0]*1547.9,bone.location[1]*1547.9,bone.location[2]*1547.9]) #3500
                a.editframe(f-1,bone.name,[convert_rad(bone.rotation_euler[0]),convert_rad(bone.rotation_euler[1]),convert_rad(bone.rotation_euler[2])])
                print(bone.name)
                print(convert_rad(bone.rotation_euler[0]),convert_rad(bone.rotation_euler[1]),convert_rad(bone.rotation_euler[2]))
        a.repeat_times[0] = len(a.frames)
        print(a.repeat_times)
        save_animation(False,a)
        return {'FINISHED'}

