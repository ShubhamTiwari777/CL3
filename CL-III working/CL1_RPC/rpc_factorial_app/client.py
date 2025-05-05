import xmlrpc.client 
 
# Create a connection to the server 
server = xmlrpc.client.ServerProxy('http://localhost:8000') 
 
# Request input from the user (for Jupyter, use input()) 
number = int(input("Enter an integer to calculate its factorial: ")) 
 
# Call the remote procedure (factorial) and print the result 
result = server.factorial(number) 
print(f"The factorial of {number} is {result}")