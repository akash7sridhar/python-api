from multiprocessing import context
from typing import Optional

from fastapi import FastAPI, Request, Form

app = FastAPI()

@app.get("/hello/{name}")
def hello(name: str):
    result = "How are you"
    return {"name": name  }

@app.get("/min_of_two")
def minimum_of_two(num1: int, num2: int):
    if num1 < num2:
        return(num1)
    else:
        return(num2)

@app.get("/max_of_two")
def minimum_of_two(num1: int, num2: int):
    if num1 > num2:
        return(num1)
    else:
        return(num2)

@app.get("/profit_or_loss")
def profit_or_loss(CP: int, SP: int):
    if CP > SP:
        return("loss")
    else:
        return("profit")

@app.get("/is_vowel")
def isvowel(char: str):
    if char == 'a' or C == 'e' or C == 'i' or C == 'o' or C == 'u':
        return("This is a vowel")
    else:
        return("This is not a vowel")

@app.get("/multiplication_tables")
def tables(num: int):
    tables = []
    for i in range(1,11):
        list = (num, '*', i, '=', (num * i))
        tables.append(list)
    return tables
    