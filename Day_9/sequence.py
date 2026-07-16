#RACE - Role, Action, Context, Expection - List of inputs

from typing import Sequence

def process_sequence(message: Sequence[str]) -> None:
    print(f"aagya bhai message: {message}")

    for i in message:
        print(i)

texts = [
    "Hello", 
    "Sup bro",
    "what is da happoning?"
]

text_tup = (
    "checking tuple",
    "tuple input",
    "working or not"
)

process_sequence(texts)
process_sequence(text_tup)