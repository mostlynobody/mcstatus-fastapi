import mcstatus

def init_mc_server(settings):
    if settings.minecraft_edition == 'Java':
        return mcstatus.JavaServer.lookup(f'{settings.minecraft_address}:{settings.minecraft_port}', settings.minecraft_timeout)
    elif settings.minecraft_edition == 'Bedrock':
        return mcstatus.BedrockServer.lookup(f'{settings.minecraft_address}:{settings.minecraft_port}', settings.minecraft_timeout)
