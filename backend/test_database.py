import sys

if "pytest" in sys.modules:
    import pytest
    pytest.skip("Manual database learning script; run it directly, not through pytest.", allow_module_level=True)

from database.database import Base, engine, SessionLocal
from models.user import User
from models.message import Message

"""
Base.metadata.create_all(bind=engine)


session = SessionLocal()

user = User(name="小明")

session.add(user)
session.commit()
session.refresh(user)

print("用户创建成功：", user.id, user.name)


message1 = Message(
    user_id=user.id,
    role="user",
    content="我叫小明"
)

message2 = Message(
    user_id=user.id,
    role="user",
    content="我喜欢猫"
)

session.add_all([message1, message2])
session.commit()

print("消息创建成功")


session.close()
"""


"""
session = SessionLocal()

user = session.get(User, 1)

print("用户：", user.name)

print("他的消息：")

for message in user.messages:
    print(
        message.id,
        message.role,
        message.content
    )

session.close()
"""


session = SessionLocal()

user = session.get(User, 1)

print("用户：", user.name)

for message in user.messages:
    print(
        message.id,
        message.role,
        message.content
    )

message = session.get(Message, 1)

print("这条消息属于：", message.user.name)

session.close()



session = SessionLocal()

user = session.get(User, 1)

print("修改前：", user.name)

user.name = "小红"

session.commit()

print("修改后：", user.name)

session.close()



session = SessionLocal()

test_user = User(name="测试用户")

session.add(test_user)
session.commit()
session.refresh(test_user)

print("创建测试用户：", test_user.id, test_user.name)

test_user_id = test_user.id

session.delete(test_user)
session.commit()

print("删除完成")

deleted_user = session.get(User, test_user_id)

print("删除后查询：", deleted_user)

session.close()
