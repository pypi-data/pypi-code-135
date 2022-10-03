# pyOCD debugger
# Copyright (c) 2006-2013 Arm Limited
# Copyright (c) 2021 Chris Reed
# SPDX-License-Identifier: Apache-2.0
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

from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import (RamRegion, DeviceRegion, MemoryMap)
from ...debug.svd.loader import SVDFile
from ...coresight import ap
from ...core.target import Target
from ...debug.breakpoints.provider import (Breakpoint, BreakpointProvider)
from typing import (Callable, Dict, List, Optional, overload, Sequence, Union, TYPE_CHECKING)

class SSE300MPS3(CoreSightTarget): #YX Modified

    VENDOR = "ARM"

    MEMORY_MAP = MemoryMap(
		# Arm Cortex-M55 Memory map from Arm Cortex-M55 Processor Technical Reference Manual r0p2
        RamRegion(name="ITCM_NS",       start=0x00000000, length=0x10000000, access='rwx'),
        RamRegion(name="ITCM_S",        start=0x10000000, length=0x10000000, access='rwxs', alias='ITCM_NS'),
        #RamRegion(name="ITCM_S",        start=0x10000000, length=0x10000000, access='rwxs'),
        RamRegion(name="DTCM_NS",       start=0x20000000, length=0x10000000, access='rwx'),
        RamRegion(name="DTCM_S",        start=0x30000000, length=0x10000000, access='rwxs', alias='DTCM_NS'),
        #RamRegion(name="DTCM_S",        start=0x30000000, length=0x10000000, access='rwxs'),
        DeviceRegion(name="Peripheral", start=0x40000000, length=0x20000000, access='rw'),
        RamRegion(name="ExtRAM",        start=0x60000000, length=0x40000000, access='rwx'),
        DeviceRegion(name="ExtDevice",  start=0xA0000000, length=0x40000000, access='rw'),
        DeviceRegion(name="PPB",        start=0xE0000000, length=0x20000000, access='rw'),
        DeviceRegion(name="Vendor_SYS", start=0xE0100000, length=0x1FF00000, access='rw')
        )

    def __init__(self, session):
        super(SSE300MPS3, self).__init__(session, self.MEMORY_MAP)
