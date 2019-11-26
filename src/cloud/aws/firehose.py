
from boto3 import client as aws_api_client
from fluent import sender as logger
from fluent.event import Event as log_event

from .base import AWSClient

class AWSFirehoseClient(AWSClient):
    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_region_name, delivery_stream_name, logger_host='127.0.0.1', logger_port=24224):
        super().__init__(aws_access_key_id, aws_secret_access_key, aws_region_name, logger_host=logger_host, logger_port=logger_port)
        self._delivery_stream_name = delivery_stream_name
        self._client = self._get_client()

    def _get_client(self):
        return aws_api_client('firehose',
                              aws_access_key_id=self._aws_access_key_id,
                              aws_secret_access_key=self._aws_secret_access_key,
                              region_name=self._aws_region_name)

    def stream_record(self, record):
        response = {}
        try:
            response = self._client.put_record(DeliveryStreamName=self._delivery_stream_name,
                                                            Record=dict(Data=record))
        except Exception as e:
            raise Exception({e})

        return response
