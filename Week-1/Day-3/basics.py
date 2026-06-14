from pydantic import BaseModel   # type: ignore


class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    name: str
    age: int
    address: Address


user = User(
    name="Ali",
    age=20,
    address={
        "city": "Tehran",
        "country": "Iran"
    }
)

#print(user.model_dump())

#print(user.model_dump_json(indent=2))

class ChatMessage(BaseModel):
    role: str
    content: str
    timestamp: str | None = None


message = ChatMessage(
    role="user",
    content="Hello AI!"
)

message_response = ChatMessage(
    role="assistant",
    content="Hello human!",
    timestamp="2026-06-14 14:30"
)

print(message)

#bad_message = ChatMessage(
#    role=123,
#    content=True
#)

print(message_response)
print(message_response.model_dump_json(indent=2))
#print(bad_message)