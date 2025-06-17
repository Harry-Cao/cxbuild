import enum

class Command(enum.Enum):
  LIST = "list"
  DELETE_CACHE = "dc"
  OPEN_CACHE = "oc"
  AUTO = "auto"
  UPDATE = "u"
  ROME_DOWNLOAD = "rd"
  BUILD = "b"
  
  def help(self):
    if self == Command.LIST:
      return "List projects"
    elif self == Command.DELETE_CACHE:
      return "Delete cache"
    elif self == Command.OPEN_CACHE:
      return "Open cache"
    elif self == Command.AUTO:
      return "Auto build"
    elif self == Command.UPDATE:
      return "Carthage update"
    elif self == Command.ROME_DOWNLOAD:
      return "Rome download"
    elif self == Command.BUILD:
      return "Carthage build"
  
class Options(enum.Enum):
  SELECT = "-s"
  
  def help(self):
    if self == Options.SELECT:
      return "Select project, value could be `index: int` or `name: str`"