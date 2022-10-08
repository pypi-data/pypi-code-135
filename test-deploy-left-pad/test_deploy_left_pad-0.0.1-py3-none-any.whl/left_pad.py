def left_pad(string, length, character=' '):
  string = str(string)
  return f'{(length - len(string)) * character}{string}'

