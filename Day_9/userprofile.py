from typing import TypedDict, Optional, List

class UserProfile(TypedDict):
    id: int
    name: str
    email: str
    bio : Optional[str]


# a = UserProfile(id=1, name="Alice", email="anything@email.com")

# b = UserProfile(id = 5, name= "Mayur", email = "mayur@gmail.com", bio = "I am a tool")

# print(a)
# print(b)

def format_user_profile(users: List[UserProfile]) -> List:
    return [f"{u['name']}({u['email']})" for u in users]


users = [
    {
        "id" : 1,
        "name" : "Alice",
        "email" : "anything@email.com"
    },
    {
        "id" : 5,
        "name" : "Mayur",
        "email" : "mayur@gmail.com"
    }

    
]

print(format_user_profile(users))
