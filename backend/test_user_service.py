import pytest

from database.database import SessionLocal
from repositories.user_repository import UserRepository
from services.user_service import UserService


@pytest.fixture
def session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def user_service(session):
    user_repository = UserRepository(session)
    return UserService(user_repository)


def test_get_user(user_service):
    user = user_service.get_user(1)

    assert user is not None
    assert user.id == 1


def test_get_user_not_found(user_service):
    user = user_service.get_user(999999)

    assert user is None


def test_get_users(user_service):
    users = user_service.get_users()

    assert isinstance(users, list)


def test_create_user(user_service):
    user = user_service.create_user("pytest Service测试用户")

    assert user.id is not None
    assert user.name == "pytest Service测试用户"

    user_service.delete_user(user)


def test_update_user(user_service):
    user = user_service.create_user("pytest Service修改前")

    user.name = "pytest Service修改后"

    updated_user = user_service.update_user(user)

    assert updated_user.id == user.id
    assert updated_user.name == "pytest Service修改后"

    user_service.delete_user(updated_user)


def test_delete_user(user_service):
    user = user_service.create_user("pytest Service删除测试")

    user_id = user.id

    user_service.delete_user(user)

    deleted_user = user_service.get_user(user_id)

    assert deleted_user is None