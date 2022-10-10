# -*- coding: utf-8 -*-
# @Time     :  
# @Author   : lll
import wda

from mtatweditor.web.utils import get_free_port

device_url = "92ca5cdfb8fc916ef79124095e5b270d2ca1307c"
c = wda.USBClient(device_url, "8100")
get_free_port()
c.status()