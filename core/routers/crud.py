from fastapi import APIRouter
from backend.database import connector_db, MallCustomerModel, sql_api
from typing import Union

crud_router = APIRouter()

@crud_router.post(path="/create")
async def create_data(data: MallCustomerModel):
    return {sql_api.insert_data_in_table(connector=connector_db, data=data) : sql_api.select_full_table(connector=connector_db)}

@crud_router.post(path="/update")
async def update_data(id: int, data: str, data_value: Union[str, int]):
    return {sql_api.update_by_id(connector=connector_db, id=id, data=data, data_value=data_value) : sql_api.select_full_table(connector=connector_db)}

@crud_router.get(path="/select-all-info")
async def select_all_data():
    return {'data' : sql_api.select_full_table(connector=connector_db)}

@crud_router.get(path='/select-by-id')
async def select_by_id(id: int = 0):
    return {'data' : sql_api.select_by_id(connector=connector_db, id=id)}

@crud_router.delete(path='/delete-by-id')
async def delete_by_id(id: int):
    return { sql_api.delete_by_id(connector=connector_db, id=id) : sql_api.select_full_table(connector=connector_db)}