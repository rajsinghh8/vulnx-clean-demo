from app import default_user_agent_present


def test_default_headers_include_user_agent():
    assert default_user_agent_present() is True
