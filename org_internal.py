from scripts.commands_organize import organize
import os
import sys
import argparse
from scripts.commands_media import organize_media

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")

def create_parser():

    parser = argparse.ArgumentParser(
        description="Tool to bulk organize files"
    )

    exif_commands = ["media""]
    all_commands = exif_commands

    parser.add_argument("command", help="the command", choices=all_commands)

    parser.add_argument(
        "-d",
        "--date",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help=f"todo",
    )

    parser.add_argument(
        "-m",
        "--model",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help=f"todo",
    )

    return parser

def execute_command(command, args):
  if command == "media":
    organize_media(args)

def main():
  os.system(f"@echo on")
  parser = create_parser()
  args = parser.parse_args()

  args.exif_tool_exe = os.path.dirname(os.path.realpath(__file__)) + "/tools/exiftool.exe"

  try:
    execute_command(args.command, args)
  except:
    error = f"{sys.exc_info()[1]}"
    print(error)
    sys.exit(1)

if __name__ == "__main__":
    main()