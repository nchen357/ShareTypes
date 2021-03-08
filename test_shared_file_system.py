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

from openstack.tests.unit import base
import uuid

IDENTIFIER = str(uuid.uuid4())
MANILA_AZ_DICT = {
    "id": IDENTIFIER,
    "name": "manila-zone-0",
    "created_at": "2021-01-21T20:13:55.000000",
    "updated_at": None,
}

ST_ID = str(uuid.uuid4())
ST_DICT = {   
    "id": ST_ID,
    "name": "test_default1",
    "extra_specs": {
      "driver_handles_share_servers": "False"
    },
    "required_extra_specs": {
      "driver_handles_share_servers": "False"
    },
    "share_type_access:is_public": True,
    "description": None,
    "is_default": False
}


class TestSharedFileSystem(base.TestCase):

    def setUp(self):
        super(TestSharedFileSystem, self).setUp()
        self.use_manila()

    def test_list_availability_zones(self):
        self.register_uris([
            dict(method='GET',
                 uri=self.get_mock_url(
                     'shared-file-system',
                     'public',
                     append=['v2', 'availability-zones']),
                 json={'availability_zones': [MANILA_AZ_DICT]}),
        ])
        az_list = self.cloud.list_share_availability_zones()
        self.assertEqual(len(az_list), 1)
        self.assertEqual(MANILA_AZ_DICT['id'], az_list[0].id)
        self.assertEqual(MANILA_AZ_DICT['name'], az_list[0].name)
        self.assertEqual(MANILA_AZ_DICT['created_at'], az_list[0].created_at)
        self.assertEqual(MANILA_AZ_DICT['updated_at'], az_list[0].updated_at)

    def test_list_share_type(self):
        self.register_uris([
            dict(method='GET',
                 uri=self.get_mock_url(
                     'shared-file-system',
                     'public',
                     append=['v2', 'types', 'default']),
                 json={'types': [ST_DICT]}),
        ])
        list_shareType = self.cloud.list_share_types()
        self.assertEqual(len(list_shareType), 1)
        self.assertEqual(ST_DICT['id'], list_shareType[0].id)
        self.assertEqual(ST_DICT['name'], list_shareType[0].name)
        self.assertEqual(ST_DICT['required_extra_specs'], list_shareType[0].required_extra_specs)
        self.assertEqual(ST_DICT['description'], list_shareType[0].description)
        self.assertEqual(ST_DICT['is_default'], list_shareType[0].is_default)
        self.assertEqual(ST_DICT['extra_specs'], list_shareType[0].extra_specs)
        self.assertEqual(ST_DICT['share_type_access:is_public'], list_shareType[0].is_public)

    def test_get_share_type(self):
        self.register_uris([
            dict(method='GET',
                 uri=self.get_mock_url(
                     'shared-file-system',
                     'public',
                     append=['v2', 'types', ST_ID]),
                 json={'types': [ST_DICT]}),
        ])
        get_shareType = self.cloud.get_share_type(ST_ID)
        self.assertEqual(ST_DICT['id'], get_shareType.id)
        self.assertEqual(ST_DICT['required_extra_specs'], get_shareType.required_extra_specs)
        self.assertEqual(ST_DICT['description'], get_shareType.description)
        self.assertEqual(ST_DICT['is_default'], get_shareType.is_default)
        self.assertEqual(ST_DICT['extra_specs'], get_shareType.extra_specs)
        self.assertEqual(ST_DICT['share_type_access:is_public'], get_shareType.is_public)
        self.assertEqual(ST_DICT['name'], get_shareType.name)
    
    def test_delete_share_type(self):
        self.register_uris([
            dict(method='DELETE',
                 uri=self.get_mock_url(
                     'shared-file-system',
                     'public',
                     append=['v2', "types", ST_ID]),
                 json={'share_type': [ST_DICT]}),
        ])
        delete_share_type = self.cloud.delete_share_type(ST_ID)
        del delete_share_type
    
    def test_update_share_type(self):
        new_name = 'random'
        new_description = 'hello world'
        new_is_public = True
        self.register_uris([
            dict(method='PUT',
                 uri=self.get_mock_url(
                     'shared-file-system',
                     'public',
                     append=['v2', "types", ST_ID]),
                 json={'share_type': [ST_DICT]}),
        ])
        update_shareType = self.cloud.update_share_type(ST_ID, name=new_name, description=new_description, is_public=new_is_public)
        self.assertEqual(ST_DICT['id'], update_shareType.id)
        self.assertEqual(ST_DICT['name'], update_shareType.name)
        self.assertEqual(ST_DICT['required_extra_specs'], update_shareType.required_extra_specs)
        self.assertEqual(ST_DICT['description'], update_shareType.description)
        self.assertEqual(ST_DICT['is_default'], update_shareType.is_default)
        self.assertEqual(ST_DICT['extra_specs'], update_shareType.extra_specs)
        self.assertEqual(ST_DICT['share_type_access:is_public'], update_shareType.is_public)
    
    def test_create_share_type(self):
        self.register_uris([
            dict(method='POST',
                 uri=self.get_mock_url(
                     'shared-file-system',
                     'public',
                     append=['v2', 'types']),
                 json={'share_type': [ST_DICT]}),
        ])
        create_shareType = self.cloud.create_share_type()
        self.assertEqual(ST_DICT['id'], create_shareType.id)
        self.assertEqual(ST_DICT['name'], create_shareType.name)
        self.assertEqual(ST_DICT['required_extra_specs'], create_shareType.required_extra_specs)
        self.assertEqual(ST_DICT['description'], create_shareType.description)
        self.assertEqual(ST_DICT['is_default'], create_shareType.is_default)
        self.assertEqual(ST_DICT['extra_specs'], create_shareType.extra_specs)
        self.assertEqual(ST_DICT['share_type_access:is_public'], create_shareType.is_public)
