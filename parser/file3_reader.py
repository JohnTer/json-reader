import calendar
import dateutil.parser
from base_reader import BaseFileReader
from structs import capture

class File3Reader(BaseFileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def read_json(self, result_object):
        self.open_json()
        capture_object = capture.Capture()
        while capture_object is not None:
            capture_object = self.read_capture_object()
            if capture_object is not None and result_object.time == capture_object.time:
                break
        self.close_json()
        return capture_object

    def read_capture_object(self):
        capture_object = capture.Capture()
        for prefix, event, value in self.parser:
            if (prefix, event) == ('', 'end_map'):
                capture_object = None
                break
            elif (prefix, event) == ('captures.item.expected', 'string'):
                capture_object.expected = value
            elif (prefix, event) == ('captures.item.actual', 'string'):
                capture_object.actual = value
            elif (prefix, event) == ('captures.item.time', 'string'):
                date = dateutil.parser.parse(value)
                capture_object.time = str(calendar.timegm(date.timetuple())) # to unixtime
                break
        return capture_object
