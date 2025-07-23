import logging
from App.model import NaiveBayesClassifier
from App.naive_bayes import NaiveBayesPredictor

logger = logging.getLogger(__name__)

class TestTable:
    def __init__(self, table):
        self.table = table
        self.row_dict = {}

        logger.info("Initializing TestTable...")

        total_rows = len(table)
        split_index = int(total_rows * 0.7)
        logger.info(f"Splitting table: {split_index} train / {total_rows - split_index} test")

        train_data = table.iloc[:split_index]
        test_data = table.iloc[split_index:]

        self.model = NaiveBayesClassifier(train_data)
        self.target = test_data[self.model.target_column]
        self.test_table = test_data.iloc[:, :-1]

        logger.info("TestTable initialized successfully")

    def test(self):
        logger.info("Running test...")
        for i in range(len(self.test_table)):
            self.row_dict[i] = self.test_table.iloc[i].to_dict()

        total = len(self.row_dict)
        correct = 0
        for i in range(total):
            user_row = self.row_dict[i]
            result = NaiveBayesPredictor.predict(user_row, self.model.model, self.model.target_variable())
            if result == self.target.iloc[i]:
                correct += 1

        success_message = f"Successful on {correct} from {total}, -> {int((correct * 100) / total)}% success"
        logger.info(success_message)
        return int((correct * 100) / total)


