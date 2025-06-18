import os
import helper
from constants import Command

# builder
builder = helper.setupBuilder()
# parser
parser = helper.setupParser()

project_list = [os.path.basename(value) for value in builder.project_list]

def select_project(selection):
  index = helper.str_to_int(selection)
  if index is not None:
    selection = index
  elif isinstance(selection, str):
    for index, value in enumerate(project_list):
      if value == selection:
        selection = index
        break
  if not isinstance(selection, int):
    raise ValueError("invalid selection, please check value of `-s`")
  builder.current_pro_path = builder.project_list[selection]
  os.chdir(builder.current_pro_path)
  print("selected project path:%s" % builder.current_pro_path)

if __name__ == "__main__":
  args = parser.parse_args()
  command = args.command
  if command == Command.LIST.value:
    print("Projects:" + "".join(
      ['\n%d.%s' % (index, value) for index, value in enumerate(project_list)]))
  elif command == Command.DELETE_CACHE.value:
    builder.delete_caches()
  elif command == Command.OPEN_CACHE.value:
    os.system("open ~/Library/Caches/org.carthage.CarthageKit")
  elif command == Command.AUTO.value:
    select_project(args.select)
    builder.carthage_update()
    builder.rome_download()
    builder.carthage_build()
  elif command == Command.UPDATE.value:
    select_project(args.select)
    builder.carthage_update()
  elif command == Command.ROME_DOWNLOAD.value:
    select_project(args.select)
    builder.rome_download()
  elif command == Command.BUILD.value:
    select_project(args.select)
    builder.carthage_build()