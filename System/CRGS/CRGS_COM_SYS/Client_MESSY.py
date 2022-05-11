def RobotClient(HOST):
    
    try:
        import socket
        PORT = 65431        # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("[CONNECTED TO GUIDANCE SYSTEM]")
            while True:
                data = s.recv(1024)
                print(data.decode('utf-8')) 
    
    except:
        print('[CONNECTION ERROR]')
