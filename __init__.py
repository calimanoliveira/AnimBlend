'''
Copyright (C) 2018 Edgard Caliman
edgard_caliman@yahoo.com.br

Created by Edgard Caliman and Team

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "AnimBlend",
    "description": "Tools of Animators",
    "author": "Edgard Caliman and Ares Deveaux (AnimAide Graph Editor Tools)",
    "version": (0, 0, 2),
    "blender": (2, 91, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Animation"}

import bpy,bgl,blf
from bpy.utils import register_class, unregister_class
from .ui.panels import *
from .operators.ops_tweenmachine import *
classes = (
    AB_PT_AnimBlend,
    AB_PT_TweenMachine,
    AB_OT_ValBreakdown_0,
    AB_OT_ValBreakdown_10,
    AB_OT_ValBreakdown_33,
    AB_OT_ValBreakdown_50,
    AB_OT_ValBreakdown_66,
    AB_OT_ValBreakdown_90,
    AB_OT_ValBreakdown_100,
    AB_PT_PlayBlast
)

def register():
    for cls in classes:
        register_class(cls)
#    register_all()

def unregister():
    for cls in reversed(classes):
        unregister_class(cls)
#    unregister_all()

"""
#from . import auto_load

#auto_load.init()

#import bpy

# load and reload submodules
##################################

import importlib
#from . import developer_utils
#from animblend.ui.AnimTools import
#importlib.reload(developer_utils)
#modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())

# register
##################################

import traceback


def register():
    #auto_load.register()

#    from bpy.types import WindowManager as wm, Scene as scn
#    from bpy.props import PointerProperty
    from .ui.panels import register as register_ui
    #from .ui.panels import register
    from bpy.utils import register_class
    try:
        bpy.utils.register_module(__name__)
    except:
        traceback.print_exc()

    #print("Registered {} with {} modules".format(bl_info["name"], len(modules)))
    register_ui(register_class)

def unregister():
    from .ui.panels import unregister as unregister_ui
    #from .ui.panels import unregister
#    from bpy.utils import unregister_class
    try:
        bpy.utils.unregister_module(__name__)
    except:
        traceback.print_exc()
#    from bpy.types import WindowManager as wm, Scene as scn

    #print("Unregistered {}".format(bl_info["name"]))
    unregister_ui(unregister_class)
#    auto_load.unregister()

"""