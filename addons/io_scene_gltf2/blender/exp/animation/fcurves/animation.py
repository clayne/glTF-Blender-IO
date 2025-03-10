# Copyright 2018-2022 The glTF-Blender-IO authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bpy
from .....io.com import gltf2_io
from .....io.exp.user_extensions import export_user_extensions
from ....com.extras import generate_extras
from .channels import gather_animation_fcurves_channels


def gather_animation_fcurves(
        obj_uuid: str,
        blender_action: bpy.types.Action,
        slot_identifier: str,
        export_settings
):

    channels, to_be_sampled, extra_samplers = __gather_channels_fcurves(obj_uuid, blender_action, slot_identifier, export_settings)

    if not channels:
        return None, to_be_sampled, extra_samplers

    blender_object = export_settings['vtree'].nodes[obj_uuid].blender_object
    export_user_extensions('animation_gather_fcurve', export_settings, blender_object, blender_action)

    return channels, to_be_sampled, extra_samplers


def __gather_channels_fcurves(
        obj_uuid: str,
        blender_action: bpy.types.Action,
        slot_identifier: str,
        export_settings):
    return gather_animation_fcurves_channels(obj_uuid, blender_action, slot_identifier, export_settings)
