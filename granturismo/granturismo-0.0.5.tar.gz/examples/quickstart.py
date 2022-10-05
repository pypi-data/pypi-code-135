from src.granturismo.intake import Listener

if __name__ == '__main__':
  listener = Listener('192.168.1.207')
  packet = listener.get()
  print(packet)

  del listener