import os
import json

class FileWritter(object):
    def __init__(self, filename):
        self.filename = filename
        
    def start_write(self):
        with open(self.filename, "w") as f:
            f.write('[\n')

    def stop_write(self):
        with open(self.filename, "rb+") as f:
            f.seek(-3, os.SEEK_END)
            f.truncate()
        with open(self.filename, "a+") as f:
            f.write('\n]')


    def write(self, capture_object):
        data = self.create_chunk(capture_object)
        with open(self.filename, "a+") as f:
            f.write(data + ',\n')



    def create_chunk(self, capture_object):
        dic = {
            "name": capture_object.name,
            "status": capture_object.status,
            "expected": capture_object.expected,
            "actual": capture_object.actual
        }
        return json.dumps(dic, sort_keys=True, indent=4, separators=(',', ': '))
