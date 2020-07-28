from typing import List, Tuple
from werkzeug.datastructures import FileStorage
import os 


def a6_say_hello(name: str): 
    return "hello " + name 

def a6_add(a: int, b: int):
    return a+b

def a6_sort_list(a: List[int]):
    return sorted(a)

def a6_dict_test(obj: dict):
    return obj

def a6_tuple_test(foo: Tuple[str, List[int]]):
    return foo

def a6_any_test(foo):
    return foo 
