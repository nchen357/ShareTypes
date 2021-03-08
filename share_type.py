# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack import resource


class ShareType(resource.Resource):
    resource_key = "type"
    resources_key = "types"
    base_path = "/types"
    details_path = "/types/default"

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True
    allow_head = False

    #: Properties
    #: The ID of the export location. x
    id = resource.Body("id", type=str)
    #: The path of the export location. x
    name = resource.Body("name", type=str)
    #: Indiciate if export location is admin only. x
    description = resource.Body("description", type=str)
    #: Indicates if share type is default x
    is_default = resource.Body("is_default", type=bool)
    #: Indicates if share type is default x
    extra_specs = resource.Body("extra_specs", type=object)
    #: Indicates if share type is default
    required_extra_specs = resource.Body("required_extra_specs", type=object)
    #: Indicates if share type is default
    is_public = resource.Body("share_type_access:is_public", type=bool)
