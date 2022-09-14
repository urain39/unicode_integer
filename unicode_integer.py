'''Implements unicode based integer container.
'''


import abc


class UnicodeInteger(abc.ABC):
  '''A class converts a N bit integer to string.

  :param integer: A range-limited integer
  :type integer: int
  '''
  @abc.abstractmethod
  def __init__(self, integer):
    pass

  @abc.abstractmethod
  def to_integer(self):
    '''Returns a signed integer.

    :return: A signed integer
    :rtype: int
    '''


class UnicodeInteger16(UnicodeInteger):
  '''A class converts a 16 bit integer to string.

  :param integer: A range-limited integer
  :type integer: int
  '''
  def __init__(self, integer):
    assert -0x8000 <= integer <= +0x7fff
    self.string = chr(integer & 0xffff)

  def to_integer(self):
    '''Returns a signed integer.

    :return: A signed integer
    :rtype: int
    '''
    n = ord(self.string)
    return -(-n & 0xffff) if n & 0x8000 else n & 0xffff


class UnicodeInteger32(UnicodeInteger):
  '''A class converts a 32 bit integer to string.

  :param integer: A range-limited integer
  :type integer: int
  '''
  def __init__(self, integer):
    assert -0x80000000 <= integer <= +0x7fffffff
    self.string = chr((integer >> 16) & 0xffff) + chr(integer & 0xffff)

  def to_integer(self):
    '''Returns a signed integer.

    :return: A signed integer
    :rtype: int
    '''
    n = (ord(self.string[0]) << 16) | ord(self.string[1])
    return -(-n & 0xffffffff) if n & 0x80000000 else n & 0xffffffff


class UnicodeInteger53(UnicodeInteger):
  '''A class converts a 53 bit integer to string.

  :param integer: A range-limited integer
  :type integer: int
  '''
  def __init__(self, integer):
    assert -0x10000000000000 <= integer <= +0xfffffffffffff
    self.string = chr((integer >> 48) & 0x1f) + \
      chr((integer >> 32) & 0xffff) + \
        chr((integer >> 16) & 0xffff) + \
          chr(integer & 0xffff)

  def to_integer(self):
    '''Returns a signed integer.

    :return: A signed integer
    :rtype: int
    '''
    n = (ord(self.string[0]) << 48) | (ord(self.string[1]) << 32) | \
      (ord(self.string[2]) << 16) | ord(self.string[3])
    return -(-n & 0x1fffffffffffff) \
      if n & 0x10000000000000 \
      else n & 0x1fffffffffffff


class UnicodeInteger64(UnicodeInteger):
  '''A class converts a 64 bit integer to string.

  :param integer: A range-limited integer
  :type integer: int
  '''
  def __init__(self, integer):
    assert -0x8000000000000000 <= integer <= +0x7fffffffffffffff
    self.string = chr((integer >> 48) & 0xffff) + \
      chr((integer >> 32) & 0xffff) + \
        chr((integer >> 16) & 0xffff) + \
          chr(integer & 0xffff)

  def to_integer(self):
    '''Returns a signed integer.

    :return: A signed integer
    :rtype: int
    '''
    n = (ord(self.string[0]) << 48) | (ord(self.string[1]) << 32) | \
      (ord(self.string[2]) << 16) | ord(self.string[3])
    return -(-n & 0xffffffffffffffff) \
      if n & 0x8000000000000000 \
      else n & 0xffffffffffffffff
