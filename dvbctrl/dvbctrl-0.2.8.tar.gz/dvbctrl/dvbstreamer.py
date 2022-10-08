"""dvbstreamer module."""
import os
from pathlib import Path
import sys
import time

import psutil

from dvbctrl.errors import errorNotify
from dvbctrl.shell import shellCommand


class DVBStreamer:
    def __init__(self, adaptor):
        try:
            self.adaptor = int(adaptor)
            self.user = "dvbctrl"
            self.password = "dvbctrl"
            self.running = False
            self.setPidFile()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def stop(self):
        """TODO connect to this instance and issue quit"""
        try:
            if self.isRunning():
                p = psutil.Process(self.pid)
                # print(f"{p=}")
                p.terminate()
                # wait 3 seconds for the process to end
                # if it is still alive after that, kill it with fire
                gone, alive = psutil.wait_procs([p], timeout=3)
                # print(f"{gone=}, {alive=}")
                if len(alive) > 0:
                    p.kill()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def start(self):
        try:
            hostname = os.uname().nodename
            hostname = "127.0.0.1"
            cmd = f"dvbstreamer -i {hostname} -a {self.adaptor} -d -D"
            cmd += f" -u {self.user} -p {self.password}"
            data, err = shellCommand(cmd)
            # give the dvbstreamer time to start up
            time.sleep(3)
            # isRunning tests that there is a pid file
            # and the pid in the pid file corresponds
            # to the pid found in the process table
            return self.isRunning()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def setPidFile(self):
        try:
            pidfn = f"dvbstreamer-{self.adaptor}.pid"
            fqpidfn = os.path.expanduser(f"~/.dvbstreamer/{pidfn}")
            self.pidfn = Path(fqpidfn)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def getProcessadaptor(self, pinfo):
        """Extracts the adaptor number from the cmd line of the process."""
        try:
            # psutil.process.cmdline should return a list of strings
            # we are looking for the value after a '-a'
            padaptor = None
            pcn = -1
            for cn, xstr in enumerate(pinfo["cmdline"]):
                if xstr == "-a":
                    pcn = cn + 1
                    break
            if pcn > 0:
                padaptor = int(pinfo["cmdline"][pcn])
            return padaptor
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def findMyProcessPid(self):
        try:
            mypid = None
            for p in psutil.process_iter(["pid", "name", "cmdline"]):
                if "dvbstreamer" in p.info["name"]:
                    # print(f"looking for adaptor in {p.info}")
                    padaptor = self.getProcessadaptor(p.info)
                    # print(f"{padaptor=}")
                    # print(f"{self.adaptor=}")
                    if padaptor == self.adaptor:
                        mypid = int(p.info["pid"])
            return mypid
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def isRunning(self):
        try:
            if self.pidfn.exists():
                with open(self.pidfn, "r") as ifn:
                    spid = ifn.read()
                # print(f"read pid file {spid}")
                self.pid = int(spid)
            pmypid = self.findMyProcessPid()
            # print(f"my process pid {pmypid}")
            if pmypid and pmypid == self.pid:
                return True
            return False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
