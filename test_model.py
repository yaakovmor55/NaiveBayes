from cleam_table import CleanTable
from model import Model
from naive_bayes import ProbabilityCalculating



class TestTable:
    def __init__(self, table):
        self.table = table
        self.row_dict = {}


        total_rows = len(table)
        split_index = int(total_rows * 0.7)

        train_data = table.iloc[:split_index]
        test_data = table.iloc[split_index:]

        self.model = Model(train_data)
        self.target = test_data[self.model.target_column]
        self.test_table = test_data.iloc[:, :-1]

    def test(self):
        for i in range(len(self.test_table)):
            self.row_dict[i] = self.test_table.iloc[i].to_dict()

        total = len(self.row_dict)
        correct = 0
        for i in range(total):
            user_row = self.row_dict[i]
            result = ProbabilityCalculating.result(user_row, self.model.model, self.model.target_variable())
            if result == self.target.iloc[i]:
                correct += 1

        return f"Successful on {correct} from {total}, -> {int((correct * 100) / total)}% success"


# ct = CleanTable("C:/Users/User/Downloads/buy_computer_data.csv")
# tt = TestTable(ct.table)
# print(tt.test())