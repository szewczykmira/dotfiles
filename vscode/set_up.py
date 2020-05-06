from argparse import ArgumentParser
import os
import sys

def validate_python_version():
    if not sys.version.startswith("3"):
        raise OSError("This code must be run with python 3.6+")


def validate_code_instalation():
    if os.system("code --version") == 32512:
        raise OSError("Run this before: https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line")


def update_extensions_lists():
    os.system("code --list-extensions > extensions.txt")


def install_extensions():
    with open("./extensions.txt", "r") as extensions:
        for line in extensions.readlines():
            os.system(f"code --install-extension {line}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--update-extensions",
        dest="updating",
        action="store_true",
        help="Keeps list of VS Code extensions in file",
    )
    parser.add_argument(
        "--install-extensions",
        dest="install",
        action="store_true",
        help="Install VS Code extensions listed in extensions.txt",
    )
    validate_python_version()
    validate_code_instalation()
    args = parser.parse_args()
    if args.updating:
        update_extensions_lists()

    if args.install:
        install_extensions()
