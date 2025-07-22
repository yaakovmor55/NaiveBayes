import logging


logger = logging.getLogger(__name__)

class NaiveBayesPredictor:

    @staticmethod
    def calculate_posteriors(dict_user_input, model, target_variable):
        logger.info("Calculating posteriors...")
        result = {}
        for key, val in dict_user_input.items():
            for unique in model:
                prob = model[unique][key].get(val, 0) + 0.001
                if unique not in result:
                    result[unique] = prob * target_variable[unique]
                else:
                    result[unique] *= prob
        logger.info("Posterior calculation completed")
        return result

    @staticmethod
    def predict(dict_user_input, model, target_variable):
        logger.info("Making prediction...")
        result = NaiveBayesPredictor.calculate_posteriors(dict_user_input, model, target_variable)
        prediction = max(result, key=result.get)
        logger.info(f"Prediction result: {prediction}")
        return prediction
