from cleam_table import CleanTable
from model import Model
from naive_bayes import ProbabilityCalculating


class TestTable:
    def __init__(self, table):
        self.table = table
        self.row_dict = {}
        self.model = Model(self.table)
        self.target = self.table[self.model.target_column]


    def test(self):
        self.table = self.table.iloc[:,:-1]
        for i in range(len(self.table)):
            self.row_dict[i] = self.table.iloc[i].to_dict()

        total = len(self.row_dict)
        correct = 0
        for i in range(total):
            user_row = self.row_dict[i]
            result = ProbabilityCalculating.result(user_row, self.model.model, self.model.target_variable())
            if result == self.target[i]:
                correct += 1

        return f"Successful on {correct} from {total}, -> {int((correct * 100) / total)}% success"



#
# ct = CleanTable("C:/Users/User/Downloads/buy_computer_data.csv")
# tt = TestTable(ct.table)
# print(tt.test())

