import argparse
import json
from build import PyBuilder
import os
from constants import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_JSON = os.path.join(BASE_DIR, 'config.json')
with open(CONFIG_JSON, 'r') as f:
  config = json.load(f)

def setupParser():
  parser = argparse.ArgumentParser(description="Description of your program")
  subparsers = parser.add_subparsers(title="commands", dest="command")
  # list
  subparsers.add_parser(Command.LIST.value, help=Command.LIST.help())
  # delete_cache
  subparsers.add_parser(Command.DELETE_CACHE.value, help=Command.DELETE_CACHE.help())
  # open_cache
  subparsers.add_parser(Command.OPEN_CACHE.value, help=Command.OPEN_CACHE.help())
  # auto
  auto_build_parser = subparsers.add_parser(Command.AUTO.value, help=Command.AUTO.help())
  auto_build_parser.add_argument(Options.SELECT.value, "--select", help=Options.SELECT.help(), default=None)
  # update
  update_parser = subparsers.add_parser(Command.UPDATE.value, help=Command.UPDATE.help())
  update_parser.add_argument(Options.SELECT.value, "--select", help=Options.SELECT.help(), default=None)
  # rome_download
  rd_parser = subparsers.add_parser(Command.ROME_DOWNLOAD.value, help=Command.ROME_DOWNLOAD.help())
  rd_parser.add_argument(Options.SELECT.value, "--select", help=Options.SELECT.help(), default=None)
  # build
  build_parser = subparsers.add_parser(Command.BUILD.value, help=Command.BUILD.help())
  build_parser.add_argument(Options.SELECT.value, "--select", help=Options.SELECT.help(), default=None)
  return parser

def getProjectList():
  folder_list = [path[1] for path in config['input_paths'] if path[0] == 0]
  folder_list = [list(map(lambda x: path + "/" + x, os.listdir(path))) for path in folder_list]
  folder_list = list(filter(lambda x: "ios" in os.path.basename(x), sum(folder_list, [])))
  path_list = [path[1] for path in config['input_paths'] if path[0] == 1]
  total_list = path_list + folder_list
  return total_list

def setupBuilder():
  builder = PyBuilder()
  builder.cache_paths = config['cache_paths']
  builder.proxy = config['proxy']
  builder.artifactory_key = config['artifactory_key']
  builder.project_list = getProjectList()
  return builder

def str_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None