import string
import os

def get_var_or_default(var: string, default: string)-> string :
    val = os.environ.get(var)
    if val:
        return val
    return default

class Settings:
    PROJECT_NAME: str = get_var_or_default("PROJECT_NAME", "mcstatus-fastapi")
    PROJECT_VERSION: str = get_var_or_default("PROJECT_VERSION", "dev")

settings = Settings()