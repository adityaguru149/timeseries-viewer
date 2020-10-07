import logging
from concurrent import futures
import grpc

from data_app.autogen import meter_pb2_grpc, meter_pb2
from data_app.services.readers import TimeseriesReader
from data_app.services.timers import timestamp_proto_from_datetime


class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        meter_pb2_grpc.add_SearchServiceServicer_to_server(Processor(), server)
        server_interface = '[::]:50051'
        server.add_insecure_port(server_interface)
        server.start()
        logging.warning(f"Server started at {server_interface}")
        server.wait_for_termination()


class Processor(meter_pb2_grpc.SearchServiceServicer):

    def Search(self, request, context):
        logging.warning(request)
        tr = TimeseriesReader("meterusage.csv")
        print(request.start.ToDatetime(), request.limit, request.precision)
        sliced, message = tr.get_data(
            request.start.ToDatetime(), request.limit, request.precision)
        time = list(map(timestamp_proto_from_datetime, sliced.index.tolist()))
        usage = sliced.meterusage.tolist()
        return meter_pb2.SearchResponse(time=time, usage=usage, message=message)
