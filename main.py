from fastapi import FastAPI
from config import get_engine

app = FastAPI()

engine = get_engine()

@app.get("/health")
def health():
    return {"staus":"OK"}

@app.get("/CountryWiseVessels")
def CountryWiseVessels(inputYear :int):
    connection = engine.raw_connection()
    try:
        cursor = connection.cursor()
        cursor.callproc("sp_getCountryWiseVesselsCount",[inputYear])
        rows =[]
        for result in cursor.stored_results():
            columns = [column[0] for column in result.description]
            rows.extend(dict(zip(columns,row)) for row in result.fetchall())
        cursor.close()

        return rows
    finally:
        connection.close()
