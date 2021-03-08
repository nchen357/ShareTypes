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

from openstack.tests.functional.shared_file_system import base


class ShareTypeTest(base.BaseSharedFileSystemTest):

    min_microversion = '2.58'

    def test_share_types(self):
        sts = self.conn.shared_file_system.share_type()
        self.assertGreater(len(list(sts)), 0)
        for st in sts:
            for attribute in ('id', 'name', 'description'):
                self.assertTrue(hasattr(st, attribute))
                self.assertIsInstance(getattr(st, attribute), 'str')
            for attribute in ('is_default', 'share_type_access:is_public'):
                self.assertTrue(hasattr(st, attribute))
                self.assertIsInstance(getattr(st, attribute), 'bool')
            for attribute in ('required_extra_specs', 'extra_specs'):
                self.assertTrue(hasattr(st, attribute))
                self.assertIsInstance(getattr(st, attribute), 'object')
