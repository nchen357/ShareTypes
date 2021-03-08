# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from openstack.cloud import _normalize


class SharedFileSystemCloudMixin(_normalize.Normalizer):

    def list_share_availability_zones(self):
        """List all availability zones for the Shared File Systems service.

        :returns: A list of Shared File Systems Availability Zones.
        """
        return list(self.share.availability_zones())

    def list_share_types(self):
        """List all export locations for Shared File Systems service.

        :returns: A list of Shared File Systems Export Locations.
        """
        return list(self.share.share_types())
        
    def get_share_type(self, share_type_id):
        """Get all export locations for the Shared File Systems service.

        :returns: A list of Shared File Systems Export Locations.
        """
        return self.share.get_share_type(share_type_id)

    def delete_share_type(self, share_type_id):
        """Get all export locations for the Shared File Systems service.

        :returns: A list of Shared File Systems Export Locations.
        """
        return self.share.delete_share_type(share_type_id)

    def update_share_type(self, share_type_id, **kwargs):
        """Get all export locations for the Shared File Systems service.

        :returns: A list of Shared File Systems Export Locations.
        """
        return self.share.update_share_type(share_type_id, **kwargs)

    def create_share_type(self, **attrs):
        """Get all export locations for the Shared File Systems service.

        :returns: A list of Shared File Systems Export Locations.
        """
        return self.share.create_share_type(**attrs)
