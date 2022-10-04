from tarfile import LENGTH_NAME
import pykd
import ctypes
from ctypes import *
from ctypes.wintypes import DWORD, LPVOID, HANDLE, LPCVOID, BOOL
import win32api
import win32con
import sys
import math

# https://stackoverflow.com/questions/59610466/python3-get-process-base-address-from-pid

# Pull in kernel32 from ctypes becaue pywin32 doesn't implement VirutallAllocEx or WriteProcessMemory.
k32 = ctypes.WinDLL('kernel32', use_last_error=True)
PAGE_READWRITE = 0x04
PAGE_EXECUTE_READWRITE = 0x40
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000

k32.VirtualAllocEx.restype = LPVOID
k32.VirtualAllocEx.argtypes = [HANDLE, LPVOID, ctypes.c_size_t, DWORD, DWORD]
k32.WriteProcessMemory.restype = BOOL
k32.WriteProcessMemory.argtypes = [HANDLE, LPVOID, LPCVOID, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
k32.VirtualProtectEx.restype = BOOL
k32.VirtualProtectEx.argtypes = [HANDLE, LPVOID, ctypes.c_size_t, DWORD, LPVOID]

# yapf: disable

# yapf: enable

# https://gist.github.com/Andoryuuta/e498f029f518e3235d44b6a763232fe2


def allocate_page_near_address(process: HANDLE, target_addr) -> LPVOID:
    tuple = win32api.GetSystemInfo()
    PAGE_SIZE = tuple[1]
    lpMinimumApplicationAddress = tuple[2]
    lpMaximumApplicationAddress = tuple[3]

    start_addr = target_addr & ~(PAGE_SIZE - 1)
    min_addr = min(start_addr - 0x7FFFFF00, lpMinimumApplicationAddress)
    max_addr = max(start_addr + 0x7FFFFF00, lpMaximumApplicationAddress)
    start_page = start_addr - (start_addr & PAGE_SIZE)
    page_offset = 1
    while True:
        byte_offset = page_offset * PAGE_SIZE
        high_addr: LPVOID = start_page + byte_offset
        low_addr = start_page - byte_offset if start_page > byte_offset else 0

        needs_exit = high_addr > max_addr and low_addr < min_addr
        if needs_exit:
            break

        if high_addr < max_addr:
            out_addr = k32.VirtualAllocEx(process, high_addr, PAGE_SIZE, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
            if out_addr:
                return out_addr
        if low_addr > min_addr:
            out_addr = k32.VirtualAllocEx(process, low_addr, PAGE_SIZE, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
            if out_addr:
                return out_addr

        page_offset += 1

    return 0


def int_to_bytes(n: int) -> bytearray:
    # https://www.geeksforgeeks.org/python-program-to-print-an-array-of-bytes-representing-an-integer/ 
    # if n < 0:
    #     n = -n
    # size = int(math.log(n, 256)) + 1
    # arr = n.to_bytes(size, "big")
    # return arr
    arr = bytearray()
    while(n):
        r = n % 256
        n = n//256
        arr.append(r)
    arr.reverse()
    return arr

def write_absolute_jump64(process: HANDLE, abs_jump_memory: LPVOID, addr_to_jumpto: int) -> bool:
    if not pykd.is64bitSystem():
        return False

    abs_jump_instructions = bytearray([0x49, 0xBA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x41, 0xFF, 0xE2])
    # arr = int_to_bytes(addr_to_jumpto)
    arr = addr_to_jumpto.to_bytes(8, sys.byteorder, signed=True)
    length = len(arr)
    for i, k in enumerate(arr):
        abs_jump_instructions[10 - length + i] = arr[i]

    buf = ctypes.create_string_buffer(bytes(abs_jump_instructions))
    bytes_written = ctypes.c_size_t(0)
    length = k32.WriteProcessMemory(process, abs_jump_memory, ctypes.addressof(buf), 13, ctypes.byref(bytes_written))
    return length > 0


def write_relative_jump(process: HANDLE, func_to_hook: LPVOID, jump_target: LPVOID) -> bool:
    jmp_instruction = bytearray([0xE9, 0x0, 0x0, 0x0, 0x0])
    relative_to_jump_target: DWORD = jump_target - (func_to_hook + 5)
    print(hex(relative_to_jump_target))

    # jmp_instruction[1:] = relative_to_jump_target
    arr = relative_to_jump_target.to_bytes(4, sys.byteorder, signed=True)
    length = len(arr)
    for i, k in enumerate(arr):
        jmp_instruction[5 - length + i] = arr[i]

    old_protection = ctypes.pointer(DWORD())
    err = k32.VirtualProtectEx(process, func_to_hook, 1024, PAGE_EXECUTE_READWRITE, old_protection)
    if err == 0:
        print(f'[-] VirtualProtectEx() Failed - Error Code: {k32.GetLastError()}')
        return False

    buf = ctypes.create_string_buffer(bytes(jmp_instruction))
    bytes_written = ctypes.c_size_t(0)
    length = k32.WriteProcessMemory(process, func_to_hook, ctypes.addressof(buf), 5, ctypes.byref(bytes_written))
    return length > 0


def get_processid_by_name(name) -> int:
    processid = 0
    lower_name = name.lower()
    for (pid, pname, user) in pykd.getLocalProcesses():
        if pname.lower() == lower_name:
            processid = pid
            break
    return processid


def process():
    pykd.initialize()
    pid = get_processid_by_name('HelloWidget.exe')
    pykd.attachProcess(pid)

    process: HANDLE = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
    if not process:
        print(f'[*] Couldn\'t acquire a handle to PID: {pid}')
        sys.exit(1)

    offset = pykd.getOffset('HelloWidget!MainWidget::handleButton')
    target_offset = pykd.getOffset('HelloWidget!MainWidget::targetButton')

    # write the relay function
    relay_func = allocate_page_near_address(process.handle, offset)
    if not relay_func:
        print('[*] Could not allocate memory for relay function')
        sys.exit(1)

    write_absolute_jump64(process.handle, relay_func, target_offset)

    # write the actual "hook" into the target function.
    write_relative_jump(process.handle, offset, relay_func)

    win32api.CloseHandle(process)
    pykd.detachAllProcesses()


if __name__ == '__main__':
    process()
