def Guidance_Server(HOST):
       
        
    try:
        import socket 
        
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
        
        print('[GUIDANCE SYSTEM Online]')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('[CONNECTION ESTABLISHED to ]', addr)
                while True:
                    message=input("[Message>>>] ") 
                    message=bytes(message, encoding="ascii")            
                    conn.sendall(message)    
                    
    except:
        print('[LAUNCHING ERROR:]')