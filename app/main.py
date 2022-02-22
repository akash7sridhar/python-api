from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}") # noqa
def hello(name: str):
    return {"name": name}

@app.get("/min_of_two") # noqa
def minimum_of_two(num1: int, num2: int):
    if num1 < num2:
        return(num1)
    else:
        return(num2)

@app.get("/max_of_two") # noqa
def maximum_of_two(num1: int, num2: int):
    if num1 > num2:
        return(num1)
    else:
        return(num2)

@app.get("/profit_or_loss") # noqa
def profit_or_loss(CP: int, SP: int):
    if CP > SP:
        return("loss")
    else:
        return("profit")

@app.get("/is_vowel") # noqa
def isvowel(char: str):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return("This is a vowel")
    else:
        return("This is not a vowel")

@app.get("/multiplication_tables") # noqa
def tables(num: int):
    tables = []
    for i in range(1, 11):
        list = (num, '*', i, '=', (num * i))
        tables.append(list)
    return tables
