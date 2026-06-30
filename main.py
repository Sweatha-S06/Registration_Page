from fastapi import FastAPI
import mysql.connector

app= FastAPI()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce"
    )

@app.post("/insert")
def insert_details():
     
     mycursor=mydb.cursor()
     mycursor.execute("insert into registration values(934584445,'Sweatha@28'),(94423159,'surya@22')")
     mydb.commit()
     return{"msg":"inserted successfully"}


@app.get("/login/{phone_number}/{password}")
def login(phone_number:int,password:str):
    mycursor = mydb.cursor()
    mycursor.execute(f"select * from registration where phone_number={phone_number} AND password='{password}'")
     
    result = mycursor.fetchall()
    
    if result:
         return{"Status":"Login"}
    
    else:
         return{"Status":"Invalid Login"}


