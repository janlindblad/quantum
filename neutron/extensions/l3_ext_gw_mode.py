# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Nicira Networks, Inc.
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Salvatore Orlando, Nicira, Inc
#

from neutron.api import extensions
from neutron.api.v2 import attributes as attrs
from neutron.extensions import l3


EXTENDED_ATTRIBUTES_2_0 = {
    'routers': {l3.EXTERNAL_GW_INFO:
                {'allow_post': True,
                 'allow_put': True,
                 'is_visible': True,
                 'default': None,
                 'enforce_policy': True,
                 'validate':
                 {'type:dict_or_nodata':
                  {'network_id': {'type:uuid': None, 'required': True},
                   'enable_snat': {'type:boolean': None, 'required': False,
                                   'convert_to': attrs.convert_to_boolean}}
                  }}}}


class L3_ext_gw_mode(extensions.ExtensionDescriptor):

    @classmethod
    def get_name(cls):
        return "Neutron L3 Configurable external gateway mode"

    @classmethod
    def get_alias(cls):
        return "ext-gw-mode"

    @classmethod
    def get_description(cls):
        return ("Extension of the router abstraction for specifying whether "
                "SNAT should occur on the external gateway")

    @classmethod
    def get_namespace(cls):
        return "http://docs.openstack.org/ext/neutron/ext-gw-mode/api/v1.0"

    @classmethod
    def get_updated(cls):
        return "2013-03-28T10:00:00-00:00"

    def get_required_extensions(self):
        return ["router"]

    def get_extended_resources(self, version):
        if version == "2.0":
            return dict(EXTENDED_ATTRIBUTES_2_0.items())
        else:
            return {}
