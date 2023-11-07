from .factory import factory_connector

connector_db = factory_connector()
connector_db.connect()