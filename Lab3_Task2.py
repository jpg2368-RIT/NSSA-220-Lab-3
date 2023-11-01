#!/bin/python3
import sys
from dataclasses import dataclass


@dataclass
class Hash:
    file: str
    md5: str

    def __init__(self, file, md5):
        self.file = file
        self.md5 = md5


def read_hashes(hash_file):
    hashes = []
    with open(hash_file) as file:
        for line in file:
            fields = line.split(" ")
            hashes.append(Hash(fields[0], fields[1]))
    return hashes


def main(args):
    if len(args) != 3:
        print(f"Expected 3 arguments, got {len(args)}")
        exit(1)
    original_hashes = read_hashes(args[1])
    new_hashes = read_hashes(args[2])
    print(f"Possible affected files:")
    for i in range(len(original_hashes)):
        if original_hashes[i].md5 != new_hashes[i].md5:
            print(f"{original_hashes[i].file}:\n\tOriginal MD5: {original_hashes[i].md5}\n\tNew MD5: {new_hashes[i].md5}")


if __name__ == "__main__":
    main(sys.argv)
