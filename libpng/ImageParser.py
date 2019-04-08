#! /usr/bin/env python3


class PNG_Reader(object):

    def __init__(self, filename=None):
        if filename:
            self.filename = filename
            self.read(filename)

    def read(self, filename):
        self.png_file = open(filename, "wb")
        # self.signature = self.png_file.read(8)

    def read_IHDR(self):
        data = self.png_file.read(33)
        return data

