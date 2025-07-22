import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

class Loader:
    """
    A class to convert various file formats into CSV.
    """

    def __init__(self, file):
        if not os.path.exists(file):
            logger.error(f"File not found: {file}")
            raise FileNotFoundError(f"File not found: {file}")

        logger.info(f"Loading file: {file}")
        self.file = file
        self.extension = os.path.splitext(file)[-1].lower()

        try:
            self.table = self.load_file()
            logger.info(f"File loaded successfully: {file}")
        except Exception as e:
            logger.error(f"Failed to load file: {e}")
            raise

        try:
            self.convert_to_csv()
        except Exception as e:
            logger.error(f"Failed to convert file to CSV: {e}")
            raise

    def convert_to_csv(self, output_file=None):
        if output_file is None:
            output_file = os.path.splitext(self.file)[0] + ".csv"

        self.table.to_csv(output_file, index=False)
        logger.info(f"File converted and saved as CSV: {output_file}")

    def load_file(self):
        if self.extension == ".csv":
            return pd.read_csv(self.file)
        elif self.extension == ".json":
            return pd.read_json(self.file)
        elif self.extension in [".xls", ".xlsx"]:
            return pd.read_excel(self.file)
        elif self.extension == ".txt":
            return pd.read_csv(self.file, delimiter="\t")
        elif self.extension == ".html":
            return pd.read_html(self.file)[0]
        else:
            raise ValueError(f"Unsupported file format: {self.extension}")
