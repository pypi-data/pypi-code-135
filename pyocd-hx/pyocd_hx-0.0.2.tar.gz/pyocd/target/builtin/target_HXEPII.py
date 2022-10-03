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

import logging
from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import (RomRegion, RamRegion, DeviceRegion, MemoryMap)
from ...debug.svd.loader import SVDFile
from ...coresight import ap
from ...core.target import Target
from ...debug.breakpoints.provider import (Breakpoint, BreakpointProvider)
from typing import (Callable, Dict, List, Optional, overload, Sequence, Union, TYPE_CHECKING)

class HXEPII(CoreSightTarget):

    VENDOR = "Himax"

    MEMORY_MAP = MemoryMap(
        RamRegion(name="ITCM",            start=0x00000000, length=0x10000000, access='rwx'),
        RamRegion(name="ITCM_S",          start=0x10000000, length=0x10000000, access='rwxs', alias='ITCM'),
        RomRegion(name="Bootrom",         start=0x08000000, length=0x08000000, access='rx'),
        RomRegion(name="Bootrom_S",       start=0x18000000, length=0x08000000, access='rx', alias='Bootrom'),
        RamRegion(name="DTCM",            start=0x20000000, length=0x04000000, access='rwx'),
        RamRegion(name="DTCM_S",          start=0x30000000, length=0x04000000, access='rwxs', alias='DTCM'),
        RamRegion(name="SRAM0",           start=0x24000000, length=0x00100000, access='rwx'),
        RamRegion(name="SRAM0_S",         start=0x34000000, length=0x00100000, access='rwxs', alias='SRAM0'),
        RamRegion(name="SRAM1",           start=0x24100000, length=0x00100000, access='rwx'),
        RamRegion(name="SRAM1_S",         start=0x34100000, length=0x00100000, access='rwxs', alias='SRAM1'),
        RamRegion(name="SRAM2",           start=0x26000000, length=0x00100000, access='rwx'),
        RamRegion(name="SRAM2_S",         start=0x36000000, length=0x00100000, access='rwxs', alias='SRAM2'),
        DeviceRegion(name="Flash1_R",     start=0x28000000, length=0x02000000, access='rw'),
        DeviceRegion(name="Flash1_R_S",   start=0x38000000, length=0x02000000, access='rws', alias='Flash1_R'),
        DeviceRegion(name="Flash1_W",     start=0x2A000000, length=0x02000000, access='rw'),
        DeviceRegion(name="Flash1_W_S",   start=0x3A000000, length=0x02000000, access='rws', alias='Flash1_W'),
        DeviceRegion(name="Flash2",       start=0x2A000000, length=0x02000000, access='rw'),
        DeviceRegion(name="Flash2_S",     start=0x3A000000, length=0x02000000, access='rws', alias='Flash2'),
        DeviceRegion(name="Peripheral",   start=0x40000000, length=0x07000000, access='rw'),
        DeviceRegion(name="Peripheral_S", start=0x50000000, length=0x07000000, access='rws', alias='Peripheral'),
        DeviceRegion(name="PPB",          start=0xE0000000, length=0x20000000, access='rw'),
        )

    def __init__(self, session):
        super(HXEPII, self).__init__(session, self.MEMORY_MAP)
