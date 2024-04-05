from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

conn = psycopg2.connect(
    dbname="users1",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

app = FastAPI()

class UserData(BaseModel):
    first_name: str
    last_name: str


@app.post("/user")
async def create_user(user_data: UserData):

    if len(user_data.first_name) == 0 or len(user_data.last_name) == 0:
        return {"error": "Пожалуйста, введите имя и фамилию"}

    
    cur.execute("INSERT INTO users2 (first_name, last_name) VALUES (%s, %s)", (user_data.first_name, user_data.last_name))
    conn.commit()
    
    return {"message": "Пользователь успешно добавлен"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    

  
