import pytest

from database.database import SessionLocal
from models.user import User
from repositories.user_repository import UserRepository


@pytest.fixture
def session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def user_repository(session):
    return UserRepository(session)


def test_get_by_id(user_repository):
    user = user_repository.get_by_id(1)

    assert user is not None
    assert user.id == 1


def test_get_by_id_not_found(user_repository):
    user = user_repository.get_by_id(999999)

    assert user is None


def test_get_all(user_repository):
    users = user_repository.get_all()

    assert isinstance(users, list)


def test_create(user_repository):
    user = User(name="pytest测试用户")

    created_user = user_repository.create(user)

    assert created_user.id is not None
    assert created_user.name == "pytest测试用户"

    # 测试结束后清理
    user_repository.delete(created_user)


def test_update(user_repository):
    user = User(name="pytest修改测试用户")

    created_user = user_repository.create(user)

    created_user.name = "pytest修改后的用户"

    updated_user = user_repository.update(created_user)

    assert updated_user.id == created_user.id
    assert updated_user.name == "pytest修改后的用户"

    user_repository.delete(updated_user)


def test_delete(user_repository):
    user = User(name="pytest删除测试用户")

    created_user = user_repository.create(user)

    user_repository.delete(created_user)

    deleted_user = user_repository.get_by_id(created_user.id)

    assert deleted_user is None