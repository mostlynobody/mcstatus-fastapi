﻿# mcstatus-fastapi

This is a very small FastAPI Server that is supposed to run as a container next to a minecraft container.

## Configuration

| **Env Var Name**   | **Default Value**  | **Accepted Values**                                      | **Description**                                            |
|--------------------|--------------------|----------------------------------------------------------|------------------------------------------------------------|
| PROJECT_NAME       | `mcstatus-fastapi` | Any string                                               | The name of the project.                                   |
| PROJECT_VERSION    | `dev`              | Any string                                               | The version of the project.                                |
| MINECRAFT_EDITION  | `Java`             | `Java`, `Bedrock`                                        | The edition of the Minecraft server to connect to.         |
| MINECRAFT_ADDRESS  | `127.0.0.1`        | Any valid IP address or hostname                         | The address of the Minecraft server.                       |
| MINECRAFT_PORT     | `25565`            | Any integer                                              | The port number of the Minecraft server.                   |
| MINECRAFT_TIMEOUT  | `3`                | Any integer                                              | Timeout in seconds for connecting to the Minecraft server. |
| UVICORN_HOST       | `127.0.0.1`        | Any valid IP address or hostname                         | The host address for the Uvicorn server.                   |
| UVICORN_PORT       | `8565`             | Any integer                                              | The port for the Uvicorn server.                           |
| UVICORN_RELOAD     | `False`            | `True`, `False`                                          | Enable auto-reload for Uvicorn server.                     |
| UVICORN_LOG_LEVEL  | `info`             | `critical`, `error`, `warning`, `info`, `debug`, `trace` | The log level for Uvicorn server.                          |

## Current Issues / Drawbacks

1. There is no SSL. please do not expose this service without a Reverse-Proxy.
2. There is no Auth.
3. It is currently limited to listening to one minecraft server.
4. The way the ENV vars are set is probably not ideal.
