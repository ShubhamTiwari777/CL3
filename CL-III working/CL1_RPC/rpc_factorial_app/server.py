import xmlrpc.server 
import threading 
 
# Function to calculate factorial 
def factorial(n): 
    if n < 0: 
        raise ValueError("Factorial is not defined for negative numbers.") 
    if n > 100:  # Limit the maximum number to 100 
        raise ValueError("Input is too large! Try a smaller number.") 
    if n == 0 or n == 1: 
        return 1 
    else: 
        return n * factorial(n - 1) 
 
# Function to start the server 
def start_server(): 
    with xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000)) as server: 
        print("Server is running...") 
        server.register_function(factorial, 'factorial') 
        server.serve_forever() 
 
# Running the server in a separate thread 
server_thread = threading.Thread(target=start_server) 
server_thread.daemon = True 
server_thread.start() 

# Keep the main thread alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Server stopped.")
