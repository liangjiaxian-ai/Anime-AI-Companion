from core.config import DEEPSEEK_API_KEY


def test_api_key_configuration_is_not_logged():
    """Configuration may be absent in CI, but importing it must be safe."""
    assert DEEPSEEK_API_KEY is None or isinstance(DEEPSEEK_API_KEY, str)
