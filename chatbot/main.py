import pathlib

from helper.loaders import load_documents

import ollama

BASE_DIR = pathlib.Path(__file__).cwd()


def main():
    load_documents(BASE_DIR)


if __name__ == "__main__":
    main()
