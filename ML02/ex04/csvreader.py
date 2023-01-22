class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = max(0, skip_top)
        self.skip_bottom = max(0, skip_bottom)
        self.expected_columns = None
        self.file = None
        self.data = []
        self.header_data = []

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError:
            print(f'File {self.filename} not found')
            return None
        self.data = [[item for item in map(str.strip, line.split(self.sep)) if len(item)] for line in self.file]
        self.expected_columns = len(self.data[0])
        for row in self.data:
            if len(row) != self.expected_columns:
                print(f'Error: line {self.data.index(row) + 1} has {len(row)} columns, expected {self.expected_columns}')
                return None
        if self.header:
            self.header_data = self.data[0]
        if self.skip_top > 0:
            self.data = self.data[self.skip_top:]
        if self.skip_bottom > 0:
            self.data = self.data[:-self.skip_bottom]
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

    def getdata(self):
        ''' Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        '''
        return self.data


    def getheader(self):
        ''' Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        '''
        if not self.header:
            return None
        return self.header_data
