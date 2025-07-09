import pandas as pd

class CleanTable:
    def __init__(self, csv_file):
        self.table = pd.read_csv(csv_file)

    def drop_null(self):
        self.table = self.table.dropna()

    def drop_id(self):
        if "id" in self.table.columns:
            self.table.drop("id",axis=1, inplace=True)

    def drop_duplicate(self):
        duplicated = self.table.T.duplicated()
        self.table = self.table.loc[:, ~duplicated]

    def start_all(self):
        self.drop_id()
        self.drop_null()
        self.drop_duplicate()