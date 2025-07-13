import pandas as pd
from cleam_table import CleanTable


class Model:
    def __init__(self, table):
        self.table = table
        self.target_column = self.table.columns[-1]
        self.features = [col for col in self.table.columns if col != self.target_column]
        self.model = {}
        self.start_all()


    def create_dict(self):
        for unique_target in self.table[self.target_column].unique():
            self.model[unique_target] = {}
            for col in self.features:
                self.model[unique_target][col] = {}
                for uniq_value in self.table[col].unique():
                    self.model[unique_target][col][uniq_value] = 0


    def statistical_values(self):
        for key in self.model:
            filtered_table = self.table[self.table[self.target_column] == key]
            for feature in self.features:
                value_count = filtered_table[feature].value_counts(normalize=True)
                for val, ratio in value_count.items():
                    self.model[key][feature][val] = round(ratio, 3)



    def target_variable(self):
        value_ratios = self.table[self.target_column].value_counts(normalize=True).to_dict()
        return value_ratios

    def start_all(self):
        self.create_dict()
        self.target_variable()
        self.statistical_values()

