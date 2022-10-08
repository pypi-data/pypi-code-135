try:
  # import version included with old SymPy
  from sympy.mpmath import mp
except ImportError:
  # import newer version
  from mpmath import mp


def generate(n):
  """Function to generate pi number with n digits

  Args:
      n (integer): number of digits to generate. Max number of digits is 100000

  Returns:
      float: pi generated
  """
  if not isinstance(n, int):
    raise TypeError("The number of digits must be an integer")
  
  if n > 100000:
    raise ValueError("The value must be lower than 100000")
  
  mp.dps = n
  return mp.pi