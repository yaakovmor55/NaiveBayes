
import logging


logger = logging.getLogger(__name__)

class NaiveBayesClassifier:
    def __init__(self, dataset):
        self.table = dataset
        self.target_column = self.table.columns[-1]
        self.features = [col for col in self.table.columns if col != self.target_column]
        self.model = {}
        logger.info("NaiveBayesClassifier initialized")
        self.start_all()

    def create_dict(self):
        logger.info("Creating initial structure for model")
        for unique_target in self.table[self.target_column].unique():
            self.model[unique_target] = {}
            for col in self.features:
                self.model[unique_target][col] = {}
                for uniq_value in self.table[col].unique():
                    self.model[unique_target][col][uniq_value] = 0
        logger.info("Initial structure created successfully")

    def statistical_values(self):
        logger.info("Calculating conditional probabilities")
        for key in self.model:
            filtered_table = self.table[self.table[self.target_column] == key]
            for feature in self.features:
                value_count = filtered_table[feature].value_counts(normalize=True)
                for val, ratio in value_count.items():
                    self.model[key][feature][val] = round(ratio, 3)
        logger.info("Probabilities assigned successfully")

    def target_variable(self):
        logger.info("Calculating target value ratios")
        value_ratios = self.table[self.target_column].value_counts(normalize=True).to_dict()
        return value_ratios

    def start_all(self):
        logger.info("Starting model creation process")
        self.create_dict()
        self.target_variable()  # הערה: התוצאה לא נשמרת כאן
        self.statistical_values()
        logger.info("Model created successfully")
