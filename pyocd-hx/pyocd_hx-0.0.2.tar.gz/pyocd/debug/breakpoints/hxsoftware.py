# pyOCD debugger
# Copyright (c) 2015-2019 Arm Limited
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
from typing import (Dict, Optional, TYPE_CHECKING)

from .provider import (Breakpoint, BreakpointProvider)
from ...core import exceptions
from ...core.target import Target
from .software import SoftwareBreakpointProvider

if TYPE_CHECKING:
    from ...core.core_target import CoreTarget

LOG = logging.getLogger(__name__)

class HxSoftwareBreakpointProvider(SoftwareBreakpointProvider): #YX 20220927
    SCS_BASE      = 0xE000E000
    # The ICIALLU invalidates all instruction caches to Point of Unification (PoU)
    ICIALLU       = (SCS_BASE | 0x00000F50)
    # The ICIMVAU invalidates instruction cache lines by address to Point of Unification (PoU)
    ICIMVAU       = (SCS_BASE | 0x00000F58)
    MSCR          = (SCS_BASE | 0x0001E000)
    MSCR_ICACTIVE = (1 << 13)

    def __init__(self, core: "CoreTarget") -> None:
        super(HxSoftwareBreakpointProvider, self).__init__(core)

    def remove_breakpoint(self, bp: Breakpoint) -> None:
        super(HxSoftwareBreakpointProvider, self).remove_breakpoint(bp)

        try:
            if (self._core.read32(self.MSCR) & self.MSCR_ICACTIVE): 
                self._core.write32(self.ICIMVAU, bp.addr)

        except exceptions.TransferError:
            LOG.debug("Failed to ICIMVAU addr 0x%x" % bp.addr)

    def set_breakpoint(self, addr: int) -> Optional[Breakpoint]:
        ret = super(HxSoftwareBreakpointProvider, self).set_breakpoint(addr)

        try:
            if (self._core.read32(self.MSCR) & self.MSCR_ICACTIVE): 
                self._core.write32(self.ICIMVAU, addr)

        except exceptions.TransferError:
            LOG.debug("Failed to ICIMVAU addr 0x%x" % addr)

        return ret
