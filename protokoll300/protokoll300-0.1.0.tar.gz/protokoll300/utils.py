from typing import Optional


def isolate_frame(frame_str: str) -> Optional[list[str]]:
    frame_list = frame_str.strip().split(" ")
    try:
        frame_list = frame_list[frame_list.index("41") :]
        return frame_list
    except ValueError:
        print("no start byte in frame")



def bytes_list_to_frame_string(bytes_list: list[bytes]) -> str:
    frame_str = ""
    for byte in bytes_list:
        hex_decimal_string = hex(int.from_bytes(byte, "little"))
        hex_decimal_string = hex_decimal_string[2:]  # delete "0x"
        if len(hex_decimal_string) < 2:
            hex_decimal_string = "0" + hex_decimal_string
        frame_str += hex_decimal_string + " "
    return frame_str

def string_to_bytes_list(frame_str: str) -> list[bytes]:
    return list(map(lambda x: bytes.fromhex(x), frame_str.strip().split(" ")))


def string_to_bytes(frame_str: str) -> bytes:
    return bytes.fromhex(frame_str)


def sum_list_bytes(bytes_list: list[bytes]) -> bytes:
    frame_length = len(bytes_list) - 1
    s = (
        sum(
            list(
                map(
                    lambda x: int.from_bytes(x, "little"),
                    bytes_list[1 : frame_length + 2],
                )
            )
        )
        % 256
    )
    return s.to_bytes(1, "little")