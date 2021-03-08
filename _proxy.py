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

from openstack import proxy
from openstack.shared_file_system.v2 import availability_zone
from openstack.shared_file_system.v2 import share_type


class Proxy(proxy.Proxy):

    def availability_zones(self):
        """Retrieve shared file system availability zones

        :returns: A generator of availability zone resources
        :rtype: :class:`~openstack.shared_file_system.v2.
                                    \availability_zone.AvailabilityZone`
        """
        return self._list(availability_zone.AvailabilityZone)

    def share_types(self):
        return self._list(share_type.ShareType, base_path=share_type.ShareType.details_path)

    def get_share_type(self, share_type_id):
        return self._get(share_type.ShareType, share_type_id)

    def delete_share_type(self, share_type_id):
        return self._delete(share_type.ShareType, share_type_id)

    def update_share_type(self, share_type_id, **kwargs):
        return self._update(share_type.ShareType, share_type_id, **kwargs)
    
    def create_share_type(self, **attrs):
        return self._create(share_type.ShareType, **attrs)

