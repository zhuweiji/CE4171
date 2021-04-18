# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dlserver.dlserver_pb2 as dlserver__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DLServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Infer = channel.unary_unary(
            "/info.shenghaoyang.ntu.ntu_iot.dlserver.DLServer/Infer",
            request_serializer=dlserver__pb2.InferenceRequest.SerializeToString,
            response_deserializer=dlserver__pb2.InferenceResponse.FromString,
        )
        self.Train = channel.unary_unary(
            "/info.shenghaoyang.ntu.ntu_iot.dlserver.DLServer/Train",
            request_serializer=dlserver__pb2.TrainingRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class DLServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Infer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Train(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DLServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Infer": grpc.unary_unary_rpc_method_handler(
            servicer.Infer,
            request_deserializer=dlserver__pb2.InferenceRequest.FromString,
            response_serializer=dlserver__pb2.InferenceResponse.SerializeToString,
        ),
        "Train": grpc.unary_unary_rpc_method_handler(
            servicer.Train,
            request_deserializer=dlserver__pb2.TrainingRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "info.shenghaoyang.ntu.ntu_iot.dlserver.DLServer", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DLServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Infer(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/info.shenghaoyang.ntu.ntu_iot.dlserver.DLServer/Infer",
            dlserver__pb2.InferenceRequest.SerializeToString,
            dlserver__pb2.InferenceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Train(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/info.shenghaoyang.ntu.ntu_iot.dlserver.DLServer/Train",
            dlserver__pb2.TrainingRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
