from CRGS_COM_SYS import Server_RONALDO
host=input("[Enter the RONALDO Robot IP]:")
while(True):
    try:
       
        Server_RONALDO.Guidance_Server(host)
    except:
        print('[ERROR]')