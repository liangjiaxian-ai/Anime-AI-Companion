from models.message import Message


message = Message(
    role="user",
    content="你好"
)


print(message.to_dict())