
#Traceback annotation code examples

class Article:
   def __init__(self, title, author=None) -> None:
       self.title = title
       self.author = author

article_1 = Article(title="Introducing Python 3.11", author="Ahmad")
article_2 = Article(title="Python runtime speed enhanced")
article_3 = Article(title="Enhance Python Error", author="Mustapha")

print(article_1.title.upper(), article_2.author.upper(), article_3.author.upper())


#ExceptionGroup and the except* syntax
#raise SyntaxError("Just raising a syntax error")


try:
    print(34/0)
except ZeroDivisionError:
    print("You can't divide a value by 0, how about try dividing by 2?") 
    print(34/2)


try:
    prin(34/2)
except NameError:
    print("There is an undefined name up there, take a look at it again!")
except SyntaxError:
    print("hey! There could be a syntax error there!")


try:
    prin(34/0)
except (ZeroDivisionError, NameError) as exc:
    print(exc)

try:
    prin(3/0)
except NameError:
    print(3/0)

#The ExceptionGroup
issubclass(ExceptionGroup, Exception)

raise ExceptionGroup("exception groups", [ValueError(1), TypeError(2)]) 

try:
    raise ExceptionGroup("An exception group", [ValueError(), TypeError(1)])
except ExceptionGroup:
    print("I caught an exception group")

ExceptionGroup("An exception group", [ValueError("a value error"), SyntaxError("a syntax error")])

ExceptionGroup("An exception group", [])
print(ExceptionGroup("An exception group", [ValueError("a value error"), SyntaxError("a syntax error")]).exceptions)

raise ExceptionGroup("An exception group", [ValueError("a value error"), SyntaxError("a syntax error")])\

# The except statement
try:
     raise ExceptionGroup("An exception group", [ValueError(), TypeError(1)])
except TypeError:
     print("I am handling the TypeError in the exception group")

try:
    raise ExceptionGroup("An exception group", [ValueError(), TypeError(1)])
except * TypeError:
    print("I am handling a Type error")
except * ValueError:
    print("I am handling a ValueError")


try:
     raise ExceptionGroup("An exception group", [TypeError(1), TypeError(2)])
except * TypeError as eg:
    print("I am handling TypeError")
    print(eg.exceptions)


try:
    raise ExceptionGroup("An exception group", [ValueError(), TypeError(1), ValueError(2)])
except * ValueError:
    print("This is value error")
    
except TypeError:
   print("This is a type error")

eg = ExceptionGroup("An exception group", [ValueError(1), TypeError(2), SyntaxError(3)])
type_error, other_errors = eg.split(TypeError)
print(type_error)
print(other_errors)


#Exceptions with Notes
try:
    obj = {"key": "value"}
    print(obj["error"])
except KeyError as exc:
    unavailable_info_b4_exc = "This is just new information" 
    exc.add_note(unavailable_info_b4_exc)
    print("The exception note: ", exc.__notes__)
    raise exc

#Typing Ferature
from typing import Set, List, Tuple, TypeVar, TypedDict, Required, NotRequired

def example(value_1:List[int], value_2:Set[str]) -> Tuple[bool]:
    ...


T = TypeVar("T")
def example(value_1: List[T]) -> T:
   ...

TS = TypeVarTuple("TS")
T = TypeVar("T")
def example(value_1:Tuple[T, *TS]):
   ...

class ArticleType(TypedDict):
   article_id: int
   title: str
   rating: float


article_1: ArticleType = {
   "article_id": 23,
   "title": "Introducing the new features in Python 3.11",
   "rating":4.5
}


class ArticleType(TypedDict):
   article_id: Required[int]
   title: NotRequired[str]
   rating: float

#The TOML Library
import tomllib

toml_string = """
   [database]
enabled = true
ports = [ 5432 ]
host = "127.0.0.1"

[servers]

[servers.frontend]
host = "12.3.55.1"
port = [ 3000 ]
role = "frontend"

[servers.backend]
host = "12.4.55.3"
ports = [ 8000 ]
role = "backend"
"""
data = tomllib.loads(toml_string)
print(data)

with open("earthly.toml", "rb") as file:
    data = tomllib.load(file)

#Performance Optimization
#$ python3.11 -m timeit '"-".join(str(n) for n in range(100))'
#$ python3.10 -m timeit '"-".join(str(n) for n in range(100))'
