import ijson

class BaseFileReader(object):
    def __init__(self, filename):
        self.f = None
        self.filename = filename
        
    def open_json(self):
        self.f = open(self.filename, 'rb')
        self.parser = ijson.parse(self.f)

    def close_json(self):
        if self.f is not None:
            self.f.close()

    def read_case(self):
        raise NotImplementedError

    def read_json(self, result_object):
        raise NotImplementedError

    def read_capture_object(self):
        raise NotImplementedError