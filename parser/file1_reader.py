import calendar
import dateutil.parser
from base_reader import BaseFileReader
from structs import result

class File1Reader(BaseFileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def read_case(self):
        result_object = result.Result()
        for prefix, event, value in self.parser:
            if (prefix, event) == ('', 'end_map'): #end file
                result_object = None
                break
            elif (prefix, event) == ('logs.item.time', 'string'):
                result_object.time = value 
            elif (prefix, event) == ('logs.item.test', 'string'):
                result_object.name = value
            elif (prefix, event) == ('logs.item.output', 'string'):
                result_object.status = value
                break
        return result_object

