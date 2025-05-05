import grpc
from concurrent import futures
import time
import factorial_pb2
import factorial_pb2_grpc

class FactorialServiceServicer(factorial_pb2_grpc.FactorialServiceServicer):
    def Calculate(self, request, context):
        n = request.n
        result = 1
        for i in range(2, n + 1):
            result *= i
        return factorial_pb2.FactorialResponse(factorial=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    factorial_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
