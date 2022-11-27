import os
import argparse
import shutil


def main():
    parser = argparse.ArgumentParser(prog="create-pyscript-app")
    parser.add_argument(dest="project_directory",
                        help="name of project directory")
    parser.add_argument("-V", "--version", action="version",
                        version="%(prog)s v0.0.1")
    args = parser.parse_args()

    try:
        shutil.copytree(f"{os.path.dirname(os.path.realpath(__file__))}/app",
                        f"{os.getcwd()}/{args.project_directory}")
    except FileExistsError as e:
        print(e)
        print('Run "python -m create-pyscript-app --help" to see all options.')


if __name__ == '__main__':
    main()
