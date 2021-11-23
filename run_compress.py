# -*- coding:utf-8 -*-
import os
import tarfile

def get_filepaths(directory: str, filepaths: list = []) -> list:
    for (root, dir, files) in os.walk(directory):
        root = root + '/'
        for _file in files:
            if _file.endswith('.ann') and _file[0] is not ".":
                filepaths = root + _file
                filepaths.append(filepath)
    return filepaths
            

def make_tar(filepaths: str) -> None:
    with tarfile.open("Article.tar.gz" ,mode="w:gz") as tar:
        for _file in filepaths:
            tar.add(_file)


def run() -> None:
    filepaths = get_file('cti-articles/')
    make_tar(filepaths)


if __name__ == '__main__':
    run()