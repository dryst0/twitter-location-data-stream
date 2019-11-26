from abc import ABC, abstractmethod


class AWSClient(ABC):

    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_region_name, logger_host='127.0.0.1', logger_port=24224):
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key
        self._aws_region_name = aws_region_name
        self._logger_host = logger_host
        self._logger_port = logger_port
        self._client = None

    @abstractmethod
    def _get_client(self):
        pass
    