from models.message import Message


message = Message(
    "user",
    "今天很累"
)


print(message.to_dict())