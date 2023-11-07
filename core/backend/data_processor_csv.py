import pandas as pd
from constants import get_project_root_dir
from abc import ABC, abstractmethod
from pony.orm import db_session, Database

class IDataProcessor(ABC):
    @abstractmethod
    def convert_data_to_sql(self, db: Database):
        pass

class DataProcessor(IDataProcessor):
    def __init__(self):
        self.csv_data = pd.read_csv(
            get_project_root_dir() / "Mall_Customers.csv", 
            index_col="CustomerID")
        
    def convert_data_to_sql(self, db: Database):
        with db_session:
            self.csv_data.to_sql('mall_customer', db.get_connection())
        