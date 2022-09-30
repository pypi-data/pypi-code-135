# (c) 2021 Microchip Technology Inc. and its subsidiaries.

# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.

# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS".  NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
# PURPOSE. IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL,
# PUNITIVE, INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY
# KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP
# HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.

import os, time
import usb.core
from typing import List, Optional
from fastapi import File, UploadFile
from fastapi.routing import APIRouter
from tpds.devices import TpdsBoards
from tpds.devices.tpds_models import BoardDetails
from tpds.tp_utils.tp_settings import TPSettings
from tpds.flash_program import FlashProgram
from pykitinfo import pykitinfo
from fastapi import BackgroundTasks

router = APIRouter()

@router.get('/get_details/{board_name}', response_model=BoardDetails)
def get_details(board_name: str):
    """
    Fetches the board details

    Parameters
    ----------
        board_name (str):       Name of the board as string

    Returns
    -------
        Return the board details based on the board name
    """

    for board, details in TpdsBoards().boards.items():
        if board == board_name:
            return details

    return None 



@router.get('/get_supported', response_model=List)
def get_supported_boards():
    """
    Return the supported boards

    Parameters
    ----------
        None

    Returns
    -------
        Return the supported boards
    """
    supported_boards = []
    for board in TpdsBoards().boards.keys():
        supported_boards.append(board)

    return supported_boards


@router.get('/get_factory_programmed', response_model=List)
def get_factory_programmed_boards():
    """
    Function checks board has valid application programmed

    Parameters
    ----------
        None

    Returns
    -------
        Empty/board names based on if the board has valid application
    """
    resp_boards = []

    for board, details in TpdsBoards().boards.items():
        if details.connection and usb.core.find(
                            idVendor=details.connection.vid,
                            idProduct=0x2312,
                            product=details.description):
            resp_boards.append(board)

    return resp_boards


@router.get('/get_connected', response_model=List)
def get_connected_boards():
    """
    Function reads the .yaml file and check for the connected boards

    Parameters
    ----------
        None

    Returns
    -------
        Empty/board names based on what board are connected/recogonized
    """
    resp_boards = []
    all_kits = pykitinfo.detect_all_kits()
    for board, details in TpdsBoards().boards.items():
        if details.mcu_part_number and any(details.mcu_part_number in
                        kit.get('debugger').get('device') for kit in all_kits):
            resp_boards.append(board)

    return resp_boards

@router.post('/program/{board_name}')
async def program_hex_file(board_name: str, background_tasks: BackgroundTasks, hex_file: Optional[UploadFile] = File(None)):
    try:
        board = get_details(board_name)
        assert board, \
            f'{board_name} is not present in the Boards list. Try with other supported boards.'
        dev = usb.core.find(
                        idVendor=board.connection.vid,
                        idProduct=board.connection.pid)
        assert dev, \
            f'{board.description} with PID: 0x{board.connection.pid:04X} is not connected. Connect board and try again.'
        working_file = os.path.join(TPSettings().get_base_folder(), 'program.hex')
        if hex_file:
            with open(working_file, 'wb') as new_file:
                new_file.write(hex_file.file._file.getvalue())
        else:
            assert board_name == 'DM320118', 'Programming from internal hex file is currently supported only for DM320118'
            from tpds.proto_boards import get_board_path
            working_file =  os.path.join(get_board_path(board_name), 'DM320118.hex')
        assert os.path.exists(working_file), f'{working_file} does not exist'
        board_info = {
            'vendor_id': board.connection.vid,
            'debugger_pid': 0,
            'application_pid': board.connection.pid,
            'serial_series': board.serial_series,
            'kitname': '',
            'product_string': '',
            'mcu_part_number': board.mcu_part_number,
            'program_tool': board.program_tool}
        flash_program = FlashProgram(board_info)
        flash_program.load_hex_image_with_ipe(working_file)
        status = 'success'
    except BaseException as e:
        status = f'{e}'
    finally:
        # Cleanup
        time.sleep(2)  # delay to allow USB reenumeration

    return status
