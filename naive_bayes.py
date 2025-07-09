from cleam_table import CleanTable
from model import Model


class ProbabilityCalculating:
    def __init__(self, dict_user_input, model, target_variable):
        self.dict_user_input = dict_user_input
        self.model = model
        self.target_variable = target_variable

    def calculation(self):
        result = {}
        for key, val in self.dict_user_input.items():
            for unique in self.model:
                if unique not in result:
                    result[unique] = (self.model[unique][key][val] + 0.001) * self.target_variable[unique]
                else:
                    result[unique] *= (self.model[unique][key][val] + 0.001)

        return result

    def result(self):
        result = self.calculation()
        return max(result, key=result.get)








ct = CleanTable("C:/Users/User/Downloads/buy_computer_data.csv")
ct.start_all()
m = Model(ct.table)
m.start_all()
pc = ProbabilityCalculating({'age' : 'middle_age','income':'low', 'student' : 'no', 'credit_rating': 'fair'}, m.model, m.target_variable())
print(pc.result())
print(pc.calculation())
# print(m.table)
# print(m.model)