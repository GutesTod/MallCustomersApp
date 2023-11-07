from abc import ABC, abstractmethod
from typing import Optional, Any

class AbstractConnector(ABC):
    """ Родительский класс для коннекторов БД """
    def __init__(self, datastore: str):
        # общие атрибуты
        """
        Допустимые форматы строк подключения datastore:

        SQLite: "sqlite:///test.db" (файл БД в локальной папке приложения)
                "sqlite:///C:\\databases\\test.db" (полный путь до файла БД)

        MySQL: "pymysql://usr:qwerty@192.168.56.104/testdb"
        PostgreSQL: "postgresql://user:password@localhost/dbname"
        """
        self._datastore = datastore   # путь к хранилищу данных (БД)
        self.connection = None       # данный атрибут хранит инициализированное в методе connect() подключение к БД

    @abstractmethod
    def connect(self) -> bool:
        """ Инициализация соединение с БД """
        pass

    @abstractmethod
    def execute(self, query: str) -> Optional[Any]:
        """ Выполнение SQL-запроса """
        pass

    @abstractmethod
    def start_transaction(self) -> None:
        """ Метод, подготавливающий коннектор к выполнению запросов в БД (начало транзакции) """
        pass

    @abstractmethod
    def end_transaction(self) -> None:
        """ Метод, завершающий выполнение запросов в БД (завершение транзакции) """
        pass

    @abstractmethod
    def close(self) -> None:
        """ Завершение соединения с БД """
        pass