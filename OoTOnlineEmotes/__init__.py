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
    "description" : "A addon to create OoT Online Emotes",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . OoTOE_export import OoTOE_OT_ExportAnim

class OoTOE_Properties(bpy.types.PropertyGroup):
    ootoe_name: bpy.props.StringProperty(name = "anim name", default = "new animation")
    ootoe_savepath: bpy.props.StringProperty(name = "save path", subtype = 'FILE_PATH')
    ootoe_repeat: bpy.props.BoolProperty(name = "repeat", default = True)
    ootoe_repeat_resetto: bpy.props.IntProperty(name = "repeat resetto", default = 1, min = 0)
    ootoe_repeat_limit: bpy.props.IntProperty(name = "repeat limit", default = 30, min = 0)

class OoTOE_PT_ExportPanel(bpy.types.Panel):
    bl_idname = "custom_panel"
    bl_label = "OoTOnlineEmote"
    bl_category = "OOTOE"
    bl_space_type = "VIEW_3D"
    #bl_space_type = "PROPERTIES"
    bl_region_type = "UI"
    #bl_region_type = "WINDOW"
    #bl_context = "object"

    def draw(self,context):
        props = bpy.context.scene.OoTOE_Properties
        layout = self.layout
        row1 = layout.row()
        row2 = layout.row()
        row3 = layout.row()
        row4 = layout.row()

        row1.prop(props, "ootoe_name", text = "name Animation", expand=True)
        row2.prop(props, "ootoe_repeat", text = "Repeat?", expand=True)
        row3.prop(props, "ootoe_savepath", text = "savedir", expand=True)
        row4.operator('oot_online.export',text = "Export Animation")


classes = (OoTOE_Properties, OoTOE_OT_ExportAnim, OoTOE_PT_ExportPanel)

def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.OoTOE_Properties = bpy.props.PointerProperty(type=OoTOE_Properties)


def unregister():

    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    del(bpy.types.Scene.OoTOE_Properties)

