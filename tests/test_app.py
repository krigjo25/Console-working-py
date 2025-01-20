#   Importing libraries
import pytest
from app import convert


def test_Working():

  assert TestConvert()

def TestConvert():

  #   Coverting AM to PM
  a = "9 AM to 5 PM"
  b = "9:00 AM to 5:00 PM"
  c = "8 PM to 8 AM"
  d = "8:00 PM to 8:00 AM"
  e = "12 AM to 12 PM"
  f = "12:00 AM to 12:00 PM"


  assert convert(a) == '09:00 to 17:00'
  assert convert(b) == '09:00 to 17:00'
  assert convert(c) == '20:00 to 08:00'
  assert convert(d) == '20:00 to 08:00'
  assert convert(e) == '00:00 to 12:00'
  assert convert(f) == '00:00 to 12:00'

  return True


if __name__ == '__main__':
  test_Working()
