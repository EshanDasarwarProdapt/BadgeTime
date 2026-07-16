from typing import Union, Sequence

InputData = Union[str, bytes]

def chatbots(inputs: Sequence[InputData]) -> None:
    for i in inputs:
        if isinstance(i,str):
            print(f"User texts: {i}")

        else:
            print("Image uploaded: (", len(i), "bytes)")


conversation = (
    "hi",
    "Show me nearby restaurant",
    b'\x89PNG',
    "Explain this image"

)

chatbots(conversation)