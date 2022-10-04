#!/usr/bin/env python3

import sys
import win32api as wapi
import win32process as wproc
import win32con as wcon
import ctypes as ct
from ctypes import wintypes as wt
import traceback as tb


class MODULEINFO(ct.Structure):
    _fields_ = [
        ("lpBaseOfDll", ct.c_void_p),
        ("SizeOfImage", wt.DWORD),
        ("EntryPoint", ct.c_void_p),
    ]

get_module_information_func_name = "GetModuleInformation"
GetModuleInformation = getattr(ct.WinDLL("kernel32"), get_module_information_func_name, getattr(ct.WinDLL("psapi"), get_module_information_func_name))
GetModuleInformation.argtypes = [wt.HANDLE, wt.HMODULE, ct.POINTER(MODULEINFO)]
GetModuleInformation.restype = wt.BOOL


def get_base_address_original(process_handle, module_handle):
    module_file_name = wproc.GetModuleFileNameEx(process_handle, module_handle)
    print("    File for module {0:d}: {1:s}".format(module_handle, module_file_name))
    module_base_address = wapi.GetModuleHandle(module_file_name)
    return module_base_address


def get_base_address_new(process_handle, module_handle):
    module_info = MODULEINFO()
    res = GetModuleInformation(process_handle.handle, module_handle, ct.byref(module_info))
    print("    Result: {0:}, Base: {1:d}, Size: {2:d}".format(res, module_info.lpBaseOfDll, module_info.SizeOfImage))
    if not res:
        print("    {0:s} failed: {1:d}".format(get_module_information_func_name, getattr(ct.WinDLL("kernel32"), "GetLastError")()))
    return module_info.lpBaseOfDll


def main(*argv):
    pid = int(argv[0]) if argv and argv[0].isdecimal() else wapi.GetCurrentProcessId()
    print("Working on pid {0:d}".format(pid))
    process_handle = wapi.OpenProcess(wcon.PROCESS_ALL_ACCESS, False, pid)
    print("Process handle: {0:d}".format(process_handle.handle))
    module_handles = wproc.EnumProcessModules(process_handle)
    print("Loaded modules: {0:}".format(module_handles))
    module_index = 0  # 0 - the executable itself
    module_handle = module_handles[module_index]
    get_base_address_funcs = [
        #get_base_address_original,  # Original behavior moved in a function
        get_base_address_new,
    ]
    for get_base_address in get_base_address_funcs:
        print("\nAttempting {0:s}".format(get_base_address.__name__))
        try:
            module_base_address = get_base_address(process_handle, module_handle)
            print("    Base address: 0x{0:016X} ({1:d})".format(module_base_address, module_base_address))
        except:
            tb.print_exc()
    process_handle.close()
    #input("\nPress ENTER to exit> ")


if __name__ == "__main__":
    print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    main(*sys.argv[1:])
    print("\nDone.")
   