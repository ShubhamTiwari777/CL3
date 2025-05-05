import grpc
import factorial_pb2
import factorial_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = factorial_pb2_grpc.FactorialServiceStub(channel)

    n = int(input("Enter Your Number:")) # Change this value to test different inputs
    request = factorial_pb2.FactorialRequest(n=n)
    response = stub.Calculate(request)
    print(f"Factorial of {n} is {response.factorial}")

if __name__ == '__main__':
    run()
