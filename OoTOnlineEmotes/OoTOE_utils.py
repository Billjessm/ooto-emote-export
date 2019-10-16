import math
import json
import os

def save_animation(load,animation, save_path = os.getcwd()):
    filename = animation.anim_name + '.json'
    if save_path[:2] == "//":
        save_path = save_path[:1].replace('/', '.') + save_path[1:]

    save_path = os.path.abspath(save_path)
    print(save_path, filename)

    if not load:
        with open(os.path.join(save_path,filename), 'w+') as f:
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
        'LinkHip':[0,0,0],
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
