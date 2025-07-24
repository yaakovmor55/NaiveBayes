
import logging

logger = logging.getLogger(__name__)

class CleanTable:
    def __init__(self, csv_file):
        self.table = csv_file
        logger.info("CleanTable initialized")
        self.start_all()

    def drop_null(self):
        before = self.table.shape
        self.table = self.table.dropna()
        after = self.table.shape
        logger.info(f"drop_null: dropped {before[0] - after[0]} rows with nulls")

    def drop_index(self):
        cols_to_drop = [col for col in self.table.columns if self.table[col].nunique() == self.table.shape[0]]
        self.table = self.table.drop(columns=cols_to_drop)
        logger.info(f"drop_index: dropped {len(cols_to_drop)} columns considered as index")

    def drop_duplicate(self):
        before = self.table.shape[1]
        duplicated = self.table.T.duplicated()
        self.table = self.table.loc[:, ~duplicated]
        after = self.table.shape[1]
        logger.info(f"drop_duplicate: dropped {before - after} duplicated columns")

    def start_all(self):
        logger.info("Starting cleaning process")
        self.drop_index()
        self.drop_null()
        self.drop_duplicate()
        logger.info("Cleaning process completed")
