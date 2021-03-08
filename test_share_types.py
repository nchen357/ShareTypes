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

from openstack.shared_file_system.v2 import share_type
from openstack.tests.unit import base


IDENTIFIER = '52a6d881-ba4e-4c50-aa0c-041e4e3756aa'
EXAMPLE = {
    "required_extra_specs": {
        "driver_handles_share_servers": "True"
    },
    "share_type_access:is_public": True,
    "extra_specs": {
        "driver_handles_share_servers": "True"
    },
    "id": "2780fc88-526b-464a-a72c-ecb83f0e3929",
    "name": "default-share-type",
    "is_default": True,
    "description": "manila share type"
}


class TestShareType(base.TestCase):

    def test_basic(self):
        types = share_type.ShareType()
        self.assertEqual('types', types.resources_key)
        #self.assertEqual('/types/%(share_type_id)s', types.base_path)
        self.assertEqual('/types/default', types.details_path)
        self.assertEqual('/types', types.base_path)
        self.assertTrue(types.allow_list)

    def test_share_type(self):
        types = share_type.ShareType(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], types.id)
        self.assertEqual(EXAMPLE['name'], types.name)
        self.assertEqual(EXAMPLE['required_extra_specs'], types.required_extra_specs)
        self.assertEqual(EXAMPLE['description'], types.description)
        self.assertEqual(EXAMPLE['is_default'], types.is_default)
        self.assertEqual(EXAMPLE['extra_specs'], types.extra_specs)
        self.assertEqual(EXAMPLE['share_type_access:is_public'], types.is_public)
