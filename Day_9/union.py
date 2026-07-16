from typing import Union

def process_input(data: Union[str,bytes]) -> str:
    if isinstance(data,str):
        return f"Processing string data: {data}"
    elif isinstance(data,bytes):
        return f"Processing bytes data: {data}"

print(process_input("Hello, World!"))

print(process_input(b'\x89PNG\r\n'))


#89 Non printable bye used to identify PNG image
#PNG - PNG image
#\r - carriage return
#\ - new line