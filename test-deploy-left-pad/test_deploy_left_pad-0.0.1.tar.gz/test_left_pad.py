from left_pad import left_pad


def test_passing_number():
  num = 4
  assert left_pad(num, 3) == '  4'

def test_right_length():
  assert left_pad('mhmd', 5) == ' mhmd'

def test_string_exceeded_length():
  assert left_pad('mhmd', 2) == 'mhmd'

