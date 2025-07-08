import pandas as pd

class NB:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.table = pd.read_csv(csv_file).dropna()
        self.target_column = self.table.columns[-1]
        self.features = [col for col in self.table.columns if col != self.target_column and col != "id"]
        self.model = {}

    def find_unique(self):
        for unique in self.table[self.target_column]:
            self.model[unique] = {}


    def feel_keys(self):
        for key in self.model:
            for feature in self.features:
                self.model[key][feature] = {}

    def statistical_values(self):
        for key in self.model:
            filtered_table = self.table[self.table[self.target_column] == key]
            for feature in self.features:
                value_count = filtered_table[feature].value_counts(normalize=True)
                for val, ratio in value_count.items():
                    self.model[key][feature][val] = round(ratio, 3)



    def target_variable(self):
        value_ratios = self.table[self.target_column].value_counts(normalize=True).to_dict()
        self.model['target_ratio'] = value_ratios


nb = NB("C:/Users/User/Downloads/buy_computer_data.csv")
# nb.target_variable()
nb.find_unique()
nb.feel_keys()
nb.statistical_values()
print(nb.model)
# print(nb.table)
# print(nb.statistical_values())
