import datetime
from typing import Dict, List
from pydantic import BaseModel

"""
    Declarative Typing as standard in fastAPI
"""


class Book(BaseModel):
    name: str = "Joe Doe Books Name"  # Setting default name
    price: float
    year: datetime.datetime


book1 = {"name": "book1", "price": 10, "year": datetime.datetime.now()}

book_object = Book(**book1)

print(book_object)


"""
def print_sample(book: Book):  # Declare all objects types
    pass


def print_name_of_the_book(bookname: str, year: datetime, price: float):
    return print(bookname, year, price)


def other_sample_name_of_the_book(name_book_list: List[str]):  # As List as Typing
    return print(name_book_list)


def dic_sample_name_of_the_book(name_of_the_book: Dict[str, int]):  # As List as Typing
    return print(name_of_the_book)


# print_name_of_the_book("O Homem que veio de Itu", 1978, 2000)

# other_sample_name_of_the_book(["E o Vento Levou"])

dic_sample_name_of_the_book({"nome": "nome"})
"""
