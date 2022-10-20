# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hpo_pb2 as hpo__pb2


class HpoServiceStub(object):
    """The hpo service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NumberExperiments = channel.unary_unary(
                '/helloworld.HpoService/NumberExperiments',
                request_serializer=hpo__pb2.NumberExperimentsParams.SerializeToString,
                response_deserializer=hpo__pb2.NumberExperimentsReply.FromString,
                )
        self.ExperimentsList = channel.unary_unary(
                '/helloworld.HpoService/ExperimentsList',
                request_serializer=hpo__pb2.ExperimentsListParams.SerializeToString,
                response_deserializer=hpo__pb2.ExperimentsListReply.FromString,
                )
        self.NewExperiment = channel.unary_unary(
                '/helloworld.HpoService/NewExperiment',
                request_serializer=hpo__pb2.ExperimentDetails.SerializeToString,
                response_deserializer=hpo__pb2.NewExperimentsReply.FromString,
                )
        self.DeleteExperiment = channel.unary_unary(
                '/helloworld.HpoService/DeleteExperiment',
                request_serializer=hpo__pb2.ExperimentNameParams.SerializeToString,
                response_deserializer=hpo__pb2.ExperimentEmptyReply.FromString,
                )
        self.GetExperimentDetails = channel.unary_unary(
                '/helloworld.HpoService/GetExperimentDetails',
                request_serializer=hpo__pb2.ExperimentNameParams.SerializeToString,
                response_deserializer=hpo__pb2.ExperimentDetails.FromString,
                )
        self.GetTrialConfig = channel.unary_unary(
                '/helloworld.HpoService/GetTrialConfig',
                request_serializer=hpo__pb2.ExperimentTrial.SerializeToString,
                response_deserializer=hpo__pb2.TrialConfig.FromString,
                )
        self.UpdateTrialResult = channel.unary_unary(
                '/helloworld.HpoService/UpdateTrialResult',
                request_serializer=hpo__pb2.ExperimentTrialResult.SerializeToString,
                response_deserializer=hpo__pb2.ExperimentEmptyReply.FromString,
                )
        self.GenerateNextConfig = channel.unary_unary(
                '/helloworld.HpoService/GenerateNextConfig',
                request_serializer=hpo__pb2.ExperimentNameParams.SerializeToString,
                response_deserializer=hpo__pb2.NewExperimentsReply.FromString,
                )
        self.GetRecommendedConfig = channel.unary_unary(
                '/helloworld.HpoService/GetRecommendedConfig',
                request_serializer=hpo__pb2.ExperimentNameParams.SerializeToString,
                response_deserializer=hpo__pb2.RecommendedConfigReply.FromString,
                )


class HpoServiceServicer(object):
    """The hpo service definition.
    """

    def NumberExperiments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExperimentsList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewExperiment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteExperiment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExperimentDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrialConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTrialResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateNextConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecommendedConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HpoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NumberExperiments': grpc.unary_unary_rpc_method_handler(
                    servicer.NumberExperiments,
                    request_deserializer=hpo__pb2.NumberExperimentsParams.FromString,
                    response_serializer=hpo__pb2.NumberExperimentsReply.SerializeToString,
            ),
            'ExperimentsList': grpc.unary_unary_rpc_method_handler(
                    servicer.ExperimentsList,
                    request_deserializer=hpo__pb2.ExperimentsListParams.FromString,
                    response_serializer=hpo__pb2.ExperimentsListReply.SerializeToString,
            ),
            'NewExperiment': grpc.unary_unary_rpc_method_handler(
                    servicer.NewExperiment,
                    request_deserializer=hpo__pb2.ExperimentDetails.FromString,
                    response_serializer=hpo__pb2.NewExperimentsReply.SerializeToString,
            ),
            'DeleteExperiment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteExperiment,
                    request_deserializer=hpo__pb2.ExperimentNameParams.FromString,
                    response_serializer=hpo__pb2.ExperimentEmptyReply.SerializeToString,
            ),
            'GetExperimentDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExperimentDetails,
                    request_deserializer=hpo__pb2.ExperimentNameParams.FromString,
                    response_serializer=hpo__pb2.ExperimentDetails.SerializeToString,
            ),
            'GetTrialConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrialConfig,
                    request_deserializer=hpo__pb2.ExperimentTrial.FromString,
                    response_serializer=hpo__pb2.TrialConfig.SerializeToString,
            ),
            'UpdateTrialResult': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTrialResult,
                    request_deserializer=hpo__pb2.ExperimentTrialResult.FromString,
                    response_serializer=hpo__pb2.ExperimentEmptyReply.SerializeToString,
            ),
            'GenerateNextConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateNextConfig,
                    request_deserializer=hpo__pb2.ExperimentNameParams.FromString,
                    response_serializer=hpo__pb2.NewExperimentsReply.SerializeToString,
            ),
            'GetRecommendedConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecommendedConfig,
                    request_deserializer=hpo__pb2.ExperimentNameParams.FromString,
                    response_serializer=hpo__pb2.RecommendedConfigReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.HpoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HpoService(object):
    """The hpo service definition.
    """

    @staticmethod
    def NumberExperiments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/NumberExperiments',
            hpo__pb2.NumberExperimentsParams.SerializeToString,
            hpo__pb2.NumberExperimentsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExperimentsList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/ExperimentsList',
            hpo__pb2.ExperimentsListParams.SerializeToString,
            hpo__pb2.ExperimentsListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NewExperiment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/NewExperiment',
            hpo__pb2.ExperimentDetails.SerializeToString,
            hpo__pb2.NewExperimentsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteExperiment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/DeleteExperiment',
            hpo__pb2.ExperimentNameParams.SerializeToString,
            hpo__pb2.ExperimentEmptyReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExperimentDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/GetExperimentDetails',
            hpo__pb2.ExperimentNameParams.SerializeToString,
            hpo__pb2.ExperimentDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrialConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/GetTrialConfig',
            hpo__pb2.ExperimentTrial.SerializeToString,
            hpo__pb2.TrialConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTrialResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/UpdateTrialResult',
            hpo__pb2.ExperimentTrialResult.SerializeToString,
            hpo__pb2.ExperimentEmptyReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateNextConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/GenerateNextConfig',
            hpo__pb2.ExperimentNameParams.SerializeToString,
            hpo__pb2.NewExperimentsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecommendedConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HpoService/GetRecommendedConfig',
            hpo__pb2.ExperimentNameParams.SerializeToString,
            hpo__pb2.RecommendedConfigReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
