def Guidance_Server(HOST,MESSAGE):
   
        
    try:
        import socket 
        
        PORT = 65430       # Port to listen on (non-privileged ports are > 1023)
        
        print('[GUIDANCE SYSTEM Online]')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('[CONNECTION ESTABLISHED to ]', addr)
                while True:
                    message=MESSAGE
                    message=bytes(message, encoding="ascii")            
                    conn.sendall(message)    
                    
    except:
        print('[LAUNCHING ERROR:]')