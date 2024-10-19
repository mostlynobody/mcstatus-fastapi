import string
import os


def get_var_or_default(name: string, default: string) -> string:
    val = os.environ.get(name)
    if val:
        return val
    return default


def get_var_or_default_allowed(name: string, default: string, allowed: list) -> string:
    val = get_var_or_default(name, default)
    if val not in allowed:
        raise ValueError(f'{name} must be one of {allowed}, is {val}')
    return val


def string_to_bool(v):
    return v.lower() in ("yes", "true", "t", "1")


class Settings:
    project_name: str = get_var_or_default('PROJECT_NAME', 'mcstatus-fastapi')
    project_version: str = get_var_or_default('PROJECT_VERSION', 'dev')

    minecraft_edition: str = get_var_or_default_allowed('MINECRAFT_EDITION', 'Java', ['Java', 'Bedrock'])
    minecraft_address: str = get_var_or_default('MINECRAFT_ADDRESS', '127.0.0.1')
    minecraft_port: int = int(get_var_or_default('MINECRAFT_PORT', '25565'))
    minecraft_timeout: int = int(get_var_or_default('MINECRAFT_TIMEOUT', '3'))

    uvicorn_host: str = get_var_or_default('UVICORN_HOST', '127.0.0.1')
    uvicorn_port: int = int(get_var_or_default('UVICORN_PORT', "8565"))
    uvicorn_reload: bool = (string_to_bool(get_var_or_default('UVICORN_RELOAD', "False")))
    uvicorn_log_level: str = get_var_or_default_allowed('UVICORN_LOG_LEVEL', 'info',
                                                        ['critical', 'error', 'warning', 'info', 'debug', 'trace'])


settings = Settings()
