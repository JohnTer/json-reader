import subprocess

class Validator(object):
    def __init__(self, json_fname, schema_fname):
        self.json_fname = json_fname
        self.schema_fname = schema_fname

    @staticmethod
    def validate(json_fname, schema_fname):
        open(json_fname)
        command = ["jsonschema", "-i", json_fname, schema_fname]
        is_valid = True
        try:
            subprocess.check_output(command)
        except subprocess.CalledProcessError:
            is_valid = False
        return is_valid



if  __name__ == "__main__":
    fname1 = "data/file2.json"
    schema = "data/file2.schema.json"
    Validator.validate(fname1, schema)

