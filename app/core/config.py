import os

PROJECT_NAME_DEFAULT = 'mcstatus-fastapi'
PROJECT_VERSION_DEFAULT = 'dev'

MINECRAFT_EDITION_DEFAULT = 'Java'
MINECRAFT_ADDRESS_DEFAULT = '127.0.0.1'
MINECRAFT_PORT_DEFAULT = '25565'
MINECRAFT_TIMEOUT_DEFAULT = '3'

UVICORN_HOST_DEFAULT = '127.0.0.1'
UVICORN_PORT_DEFAULT = '8565'
UVICORN_RELOAD_DEFAULT = 'False'
UVICORN_LOG_LEVEL_DEFAULT = 'info'


def get_var_or_default(name: str, default: str) -> str:
    val = os.environ.get(name)
    if val:
        return val
    return default


def get_var_or_default_allowed(name: str, default: str, allowed: list) -> str:
    val = get_var_or_default(name, default)
    if val not in allowed:
        raise ValueError(f'{name} must be one of {allowed}, is {val}')
    return val


def string_to_bool(v: str) -> bool:
    return v.lower() in ("yes", "true", "t", "1")


class Settings:
    project_name: str = get_var_or_default('PROJECT_NAME', PROJECT_NAME_DEFAULT)
    project_version: str = get_var_or_default('PROJECT_VERSION', PROJECT_VERSION_DEFAULT)

    minecraft_edition: str = get_var_or_default_allowed('MINECRAFT_EDITION', MINECRAFT_EDITION_DEFAULT,
                                                        ['Java', 'Bedrock'])
    minecraft_address: str = get_var_or_default('MINECRAFT_ADDRESS', MINECRAFT_ADDRESS_DEFAULT)
    minecraft_port: int = int(get_var_or_default('MINECRAFT_PORT', MINECRAFT_PORT_DEFAULT))
    minecraft_timeout: int = int(get_var_or_default('MINECRAFT_TIMEOUT', MINECRAFT_TIMEOUT_DEFAULT))

    uvicorn_host: str = get_var_or_default('UVICORN_HOST', UVICORN_HOST_DEFAULT)
    uvicorn_port: int = int(get_var_or_default('UVICORN_PORT', UVICORN_PORT_DEFAULT))
    uvicorn_log_level: str = get_var_or_default_allowed('UVICORN_LOG_LEVEL', UVICORN_LOG_LEVEL_DEFAULT,
                                                        ['critical', 'error', 'warning', 'info', 'debug', 'trace'])
    uvicorn_reload: bool = string_to_bool(get_var_or_default('UVICORN_RELOAD', UVICORN_RELOAD_DEFAULT))


settings = Settings()
