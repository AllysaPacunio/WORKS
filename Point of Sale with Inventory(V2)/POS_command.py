class Command:
  def __init__(self, cmd, *args):
    self.__cmd = cmd
    self.__args = args

  def __call__(self):
    return self.__cmd(*self.__args)

