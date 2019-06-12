from file1_reader import File1Reader
from file2_reader import File2Reader
from file3_reader import File3Reader
from file_writter import FileWritter
from json_validator import Validator
from settings import *
import os, sys

class Parser(object):
    def __init__(self, fname1, fname2, fname3, ofname):
        is_valid = self.validate_file(fname1)
        if not is_valid:
            self.err_valid(fname1)

        is_valid = self.validate_file(fname2)
        if not is_valid:
            self.err_valid(fname2)

        is_valid = self.validate_file(fname3)
        if not is_valid:
            self.err_valid(fname3)


        self.fname3 = fname3
        self.json_file1 = File1Reader(fname1)
        self.json_file2 = File2Reader(fname2)
        self.json_write = FileWritter(ofname)


    def err_valid(self, fname):
        print(fname, "is not valid!")
        sys.exit(-1)

    def merge_objects(self, result_object, capture_object):
        capture_object.status = result_object.status
        capture_object.name = result_object.name
        return capture_object

    def find_capture_object(self, result_object):
        json_file3 = File3Reader(self.fname3)
        capture_object = json_file3.read_json(result_object)
        return self.merge_objects(result_object, capture_object)


    def get_schema_name(self, name):
        return name[:-5] + ".schema" + name[-5:]


    def validate_file(self, fname):
        return Validator.validate(fname, self.get_schema_name(fname))

    def run(self):
        self.json_write.start_write()

        self.json_file1.open_json()
        while True:
            result_object = self.json_file1.read_case()
            if result_object is None:
                break
            capture_object = self.find_capture_object(result_object)
            self.json_write.write(capture_object)         
        self.json_file1.close_json()
    
        self.json_file2.open_json()
        while True:
            result_object = self.json_file2.read_case()
            if result_object is None:
                break
            capture_object = self.find_capture_object(result_object)
            self.json_write.write(capture_object)
        self.json_file2.close_json()

        self.json_write.stop_write()





if __name__ == "__main__":
    dirname = os.path.dirname(__file__)

    fname1 = os.path.join(dirname, FNAME1)
    fname2 = os.path.join(dirname, FNAME2)
    fname3 = os.path.join(dirname, FNAME3)
    oname = os.path.join(dirname, OUTNAME)

    Parser(fname1, fname2, fname3, oname).run()
