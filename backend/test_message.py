import sys

if "pytest" in sys.modules:
    import pytest
    pytest.skip("Manual model preview script; run it directly, not through pytest.", allow_module_level=True)

from models.message import Message


message = Message(
    role="user",
    content="你好"
)


print(message.to_dict())
