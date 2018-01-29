# Copyright 2018 ZTE Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rest_framework import serializers


class VmResponseSerializer(serializers.Serializer):
    vmid = serializers.CharField(help_text="vmid", required=True)
    vimid = serializers.CharField(help_text="the vim id", required=True)
    resouceid = serializers.CharField(help_text="the resouce id", required=True)
    tenant = serializers.CharField(help_text="tenant", required=True, allow_null=True)
    instid = serializers.CharField(help_text="the inst id", required=True)
    vmname = serializers.CharField(help_text="vmname", required=True)
    insttype = serializers.IntegerField(help_text="insttype", required=True)
    operationalstate = serializers.CharField(help_text="operationalstate", required=True, allow_null=True)
    is_predefined = serializers.IntegerField(help_text="is_predefined", required=True)
    security_groups = serializers.CharField(help_text="security_groups", required=True)
    flavor_id = serializers.CharField(help_text="flavor_id", required=True)
    availability_zone = serializers.CharField(help_text="availability_zone", required=True)
    server_group = serializers.CharField(help_text="server_group", required=True)
    volume_array = serializers.CharField(help_text="volume_array", required=True)
    metadata = serializers.CharField(help_text="metadata", required=True)
    nic_array = serializers.CharField(help_text="nic_array", required=True)


class VmInfoSerializer(serializers.Serializer):
    resp_data = VmResponseSerializer(help_text="the response data", many=True)


class FlavorResponseSerializer(serializers.Serializer):
    flavourid = serializers.CharField(help_text="flavourid", required=True)
    vimid = serializers.CharField(help_text="the vim id", required=True)
    resouceid = serializers.CharField(help_text="the resouce id", required=True)
    tenant = serializers.CharField(help_text="tenant", required=True, allow_null=True)
    instid = serializers.CharField(help_text="the inst id", required=True)
    name = serializers.CharField(help_text="name", required=True)
    extraspecs = serializers.CharField(help_text="extraspecs", required=True)
    create_time = serializers.CharField(help_text="create_time", required=True, allow_null=True)
    memory = serializers.IntegerField(help_text="memory", required=True)
    vcpu = serializers.IntegerField(help_text="vcpu", required=True)


class FlavorInfoSerializer(serializers.Serializer):
    resp_data = FlavorResponseSerializer(help_text="the response data", many=True)


class NetworkResponseSerializer(serializers.Serializer):
    networkid = serializers.CharField(help_text="networkid", required=True)
    vimid = serializers.CharField(help_text="the vim id", required=True)
    resouceid = serializers.CharField(help_text="the resouce id", required=True)
    insttype = serializers.IntegerField(help_text="the inst type", required=True)
    instid = serializers.CharField(help_text="the inst id", required=True)
    name = serializers.CharField(help_text="name", required=True)


class NetworkInfoSerializer(serializers.Serializer):
    resp_data = NetworkResponseSerializer(help_text="the response data", many=True)


class SubnetResponseSerializer(serializers.Serializer):
    subnetworkid = serializers.CharField(help_text="the subnetwork id", required=True)
    vimid = serializers.CharField(help_text="the vim id", required=True)
    resouceid = serializers.CharField(help_text="the resouce id", required=True)
    networkid = serializers.CharField(help_text="the network id", required=True)
    insttype = serializers.IntegerField(help_text="the inst type", required=True)
    instid = serializers.CharField(help_text="the inst id", required=True)
    name = serializers.CharField(help_text="name", required=True)
    cidr = serializers.CharField(help_text="cidr", required=True)


class SubnetInfoSerializer(serializers.Serializer):
    resp_data = SubnetResponseSerializer(help_text="the response data", many=True)


class CpResponseSerializer(serializers.Serializer):
    cpinstanceid = serializers.CharField(help_text="the cp instance id", required=True)
    cpdid = serializers.CharField(help_text="the cpd id", required=True)
    cpinstancename = serializers.CharField(help_text="the cp instance name of vnf", required=True)
    vlinstanceid = serializers.CharField(help_text="the vl instance id of vnf", required=True)
    ownertype = serializers.IntegerField(help_text="the owner type of vnf", required=True)
    ownerid = serializers.CharField(help_text="the owner id of vnf", required=True)
    relatedtype = serializers.IntegerField(help_text="the related type", required=True)


class CpsInfoSerializer(serializers.Serializer):
    resp_data = CpResponseSerializer(help_text="the response data", many=True)


class VolumeResponseSerializer(serializers.Serializer):
    storageid = serializers.CharField(help_text="the storage id", required=True)
    vimid = serializers.CharField(help_text="the vim id", required=True)
    resouceid = serializers.CharField(help_text="the resouce id of vnf", required=True)
    insttype = serializers.IntegerField(help_text="the inst type of vnf", required=True)
    instid = serializers.CharField(help_text="the inst id of vnf", required=True)
    storagetype = serializers.CharField(help_text="the storage type of vnf", required=True)
    size = serializers.CharField(help_text="the size of storage", required=True)


class VolumeInfoSerializer(serializers.Serializer):
    resp_data = VolumeResponseSerializer(help_text="the response data", many=True)
