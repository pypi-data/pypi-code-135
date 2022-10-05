import socket
import time
import datetime as dt
import threading
import signal
from model import Packet
from security import Decrypter
from typing import Dict, Union

class SocketNotBoundError(Exception):
  pass

class ReadError(Exception):
  pass

class UnknownStatusError(Exception):
  pass


class Listener(object):
  _HEARTBEAT_PORT = 33739
  _BIND_PORT = 33740
  _BUFFER_LEN = 0x128  # in bytes
  _HEARTBEAT_DELAY = 10 # in seconds
  _HEARTBEAT_MESSAGE = b'A'

  def __init__(self, addr: str):
    """
    Initialize the telemetry listener
    :param addr: Address to the PlayStation so we can send a heartbeat
    """
    # set this first so that if we fail to connect to socket we wont fail the __del__
    self._terminate_event = threading.Event()

    # setup signal handlers so we can make sure we close the socket and kill daemon threads properly
    def kill(*args):
      self._terminate_event.set()
      signal.getsignal(signal.SIGINT)()
    signal.signal(signal.SIGINT, kill)

    def kill(*args):
      self._terminate_event.set()
      signal.getsignal(signal.SIGTERM)()
    signal.signal(signal.SIGTERM, kill)

    self._heartbeat_thread = threading.Thread(
      target=self._send_heartbeat,
      #daemon=True,
      name='HeartbeatBackgroundThread')

    # connect to socket
    self._attr = addr
    self._sock = self._init_sock_(self._BIND_PORT)
    self._sock_bounded = True
    self._decrypter = Decrypter()

    # start heartbeat thread
    self._heartbeat_thread.start()

  def __del__(self):
    self._terminate_event.set()
    if self._heartbeat_thread.is_alive():
      self._heartbeat_thread.join()

  def get(self) -> Packet:
    if not self._sock_bounded:
      raise SocketNotBoundError('Socket is not bounded')

    packet = self._read_udp(self._sock)
    if packet['status'] == -1:
      raise ReadError(f'Failed to read message on port {self._BIND_PORT}')
    elif packet['status'] == -2:
      raise TimeoutError(f'Timeout after {self._HEARTBEAT_DELAY}s. No massages received on port {self._BIND_PORT}')
    elif packet['status'] != 0:
      raise UnknownStatusError(f'Unknown response status {packet["status"]} on port {self._BIND_PORT}')
    else:
      buffer = packet['body']
      buffer = self._decrypter.decrypt(buffer)
      return Packet.from_bytes(buffer)

  def _send_heartbeat(self) -> None:
    last_heartbeat = 0
    while not self._terminate_event.is_set():
      curr_time = time.time()
      if curr_time - last_heartbeat >= self._HEARTBEAT_DELAY:
        last_heartbeat = curr_time
        timestamp = dt.datetime.fromtimestamp(curr_time).isoformat().split(".", 1)[0]
        print(f'[{timestamp}] Sending heartbeat')
        self._sock.sendto(self._HEARTBEAT_MESSAGE, (self._attr, self._HEARTBEAT_PORT))
    self._sock.close()
    self._sock_bounded = False
    timestamp = dt.datetime.fromtimestamp(time.time()).isoformat().split(".", 1)[0]
    print(f'[{timestamp}] Exiting heartbeat thread')

  @staticmethod
  def _init_sock_(port: int, addr: str='') -> socket.socket:
    # Create a datagram socket
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    # Enable immediate reuse of IP address
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    sock.bind((addr, port))
    # Set a timeout so the socket does not block indefinitely when trying to receive data
    sock.settimeout(0.5)

    return sock

  @staticmethod
  def _read_udp(sock: socket.socket) -> Dict[str, Union[bytearray, str]]:
    try:
      data, addr = sock.recvfrom(Listener._BUFFER_LEN)
    except socket.timeout:
      return {'body': bytes(), 'status': -2}
    except Exception as e:
      return {'body': bytes(), 'status': -1, 'error': e}
    else:
      return {'body': data, 'status': 0}
