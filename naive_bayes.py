from cleam_table import CleanTable
from model import NaiveBayesClassifier


class NaiveBayesPredictor:

    @staticmethod
    def calculate_posteriors(dict_user_input, model, target_variable):
        result = {}
        for key, val in dict_user_input.items():
            for unique in model:
                if unique not in result:
                    result[unique] = (model[unique][key][val] + 0.001) * target_variable[unique]
                else:
                    result[unique] *= (model[unique][key][val] + 0.001)

        return result

    @staticmethod
    def predict(dict_user_input, model, target_variable):
        result = NaiveBayesPredictor.calculate_posteriors(dict_user_input, model, target_variable)
        return max(result, key=result.get)








# ct = CleanTable("C:/Users/User/Downloads/buy_computer_data.csv")
# ct.start_all()
# m = Model(ct.table)
# m.start_all()
# pc = ProbabilityCalculating.result({'age' : 'middle_age','income':'low', 'student' : 'no', 'credit_rating': 'fair'}, m.model, m.target_variable())
# print(pc)
# print(m.target_variable())
# print(pc.calculation())
# print(m.table)
# print(m.model)