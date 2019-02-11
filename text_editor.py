#!usr/bin/python


# Python class representing an abstracted file object.
class File:

    # Initialize File object with filename.
    def __init__(self, filename: str='mytxtfile'):
        if filename[-4:] != '.txt':
            self.filename = filename + '.txt'
        else:
            self.filename = filename

    # Materialize File object in current directory.
    def create(self):
        with open(file=self.filename, mode='w') as _f:
            _f.close()

    # Write text to materialized File object.
    def write(self, text: str):
        try:
            with open(file=self.filename, mode='a') as _f:
                _f.write(text + '\n')
        except FileNotFoundError:
            self.create()
            with open(file=self.filename, mode='a') as _f:
                _f.write(text + '\n')

    # Read all text from materialized File object.
    def read(self):
        with open(file=self.filename, mode='r') as _f:
            return _f.read()
