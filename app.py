import requests


def default_user_agent_present() -> bool:
    """Pure offline check — requests.utils.default_headers() builds the
    default header set without any network I/O, so this is safe to run in
    any environment and stable across requests versions."""
    headers = requests.utils.default_headers()
    return "User-Agent" in headers
