
from fluent import sender as logger
from fluent.event import Event as log_event

from tweepy import StreamListener

class TweetListener(StreamListener):

    def __init__(self, aws_firehose_client, logger_host='127.0.0.1', logger_port=24224):
        super().__init__()
        self._aws_firehose_client = aws_firehose_client
        self.logger_host = logger_host
        self.logger_port = logger_port

    def on_data(self, data):
        try:
            response = self._aws_firehose_client.stream_record(data)
        except Exception as e:
            raise Exception(f"Problem pushing to Amazon Web Service Kinesis Firehose: {e}")

        # TODO: Log response

    def on_error(self, status):
        # TODO: Log error
        print(f"Twitter Filter Status Code: {status}")
