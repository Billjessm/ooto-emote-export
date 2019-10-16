# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "OoTOnlineEmotes",
    "author" : "Raptorsw0rd",
    "description" : "test",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . test_op import Test_OT_Operator
#from . test_panel import Test_PT_Panel
class MyProperties(bpy.types.PropertyGroup):
    ootoe_name: bpy.props.StringProperty(name = "anim name")
    ootoe_savepath: bpy.props.StringProperty(name = "save path")
    ootoe_repeat: bpy.props.BoolProperty(name = "repeat", default = True)
    ootoe_repeat_resetto: bpy.props.IntProperty(name = "repeat resetto", default = 1, min = 0)
    ootoe_repeat_limit: bpy.props.IntProperty(name = "repeat limit", default = 30, min = 0)

class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "custom_panel"
    bl_label = "OoTOnlineEmote"
    bl_category = "OOTOE"
    bl_space_type = "VIEW_3D"
    #bl_space_type = "PROPERTIES"
    bl_region_type = "UI"
    #bl_region_type = "WINDOW"
    #bl_context = "object"

    def draw(self,context):
        layout = self.layout
        row = layout.row()
        row2 = layout.row()
        obj = context.object
        row2.prop(obj, "ootoe_repeat", text = "name Animation", expand=True)
        row.operator('oot_online.export',text = "Export Animation")
        #print(obj.ootoe_props)


classes = (MyProperties, Test_OT_Operator, Test_PT_Panel)
register, unregister = bpy.utils.register_classes_factory(classes)
#bpy.types.Object.ootoe_props = bpy.props.PointerProperty(type=MyProperties)

#def register():
#    print(classes)
#    bpy.utils.register_classes_factory(classes)
    #bpy.utils.register_class(MyProperties)
    #bpy.types.Scene.ootoe_props = bpy.props.PointerProperty(type=MyProperties)

#def unregister():
#    bpy.utils.register_classes_factory(classes)
    #del bpy.types.Scene.ootoe_props

#if __name__ == "__main__":
#    register()
