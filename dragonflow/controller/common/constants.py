# Copyright (c) 2015 OpenStack Foundation.
# All Rights Reserved.
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

# Pipline Table numbers
INGRESS_CLASSIFICATION_DISPATCH_TABLE = 0
SERVICES_CLASSIFICATION_TABLE = 9
ARP_TABLE = 10
DHCP_TABLE = 11
INGRESS_NAT_TABLE = 15
L2_LOOKUP_TABLE = 17
L3_LOOKUP_TABLE = 20
L3_PROACTIVE_LOOKUP_TABLE = 25
EGRESS_NAT_TABLE = 30
EGRESS_TABLE = 64
CANARY_TABLE = 200

# Flow Priorities
PRIORITY_DEFAULT = 1
PRIORITY_LOW = 50
PRIORITY_MEDIUM = 100
PRIORITY_HIGH = 200
PRIORITY_VERY_HIGH = 300


DRAGONFLOW_DEFAULT_BRIDGE = 'br-int'

"""
Cookie Mask
global cookie is used by flows of all table, but local cookie is used
by flows of a small part of table. In order to avoid conflict,
global cookies should not overlapped with each other, but local cookies
could be overlapped for saving space of cookie.
all cookie's mask should be kept here to avoid conflict.
"""
GLOBAL_AGING_COOKIE_MASK = 0x1
LOCAL_TUNNEL_KEY_COOKIE = 0x1fffffffe
LOCAL_TUNNEL_KEY_SHIFT_LEN = 1
GLOBAL_INIT_AGING_COOKIE = 0x1
