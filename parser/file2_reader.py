import calendar
import dateutil.parser
from base_reader import BaseFileReader
from structs import result

class File2Reader(BaseFileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def read_case(self):
        result_object = result.Result()
        for prefix, event, value in self.parser:
            if (prefix, event) == ('', 'end_map'):
                result_object = None
                break
            elif (prefix, event) == ('suites.item.cases.item.name', 'string'):
                result_object.name = value
            elif (prefix, event) == ('suites.item.cases.item.errors', 'number'):
                result_object.status = "success" if value == 0 else "fail"
            elif (prefix, event) == ('suites.item.cases.item.time', 'string'):
                result_object.time = value 
                date = dateutil.parser.parse(value)
                result_object.time = str(calendar.timegm(date.timetuple())) # to unixtime
                break
        return result_object

