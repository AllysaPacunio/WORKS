class Iterator:
  def __init__(self, *items):
    self.__items = items
    self.__index = 0

    self.__index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.__index > len(self.__items) - 1:
      raise StopIteration

    x = self.__items[self.__index]
    self.__index += 1

    return x


