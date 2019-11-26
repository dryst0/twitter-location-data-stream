#! /usr/bin/env python

from argparse import ArgumentParser

from cloud.aws.firehose import AWSFirehoseClient
from social.twitter.tweepy import TwitterClient


def main(twitter_api_consumer_key, twitter_api_consumer_key_secret, twitter_api_access_token, twitter_api_access_token_secret, aws_firehose_delivery_stream_name, aws_api_access_key, aws_api_secret_access_key, aws_api_region_name, logger_host='127.0.0.1', logger_port=24224):
    aws_firehose_client = AWSFirehoseClient(aws_api_access_key, aws_api_secret_access_key, aws_api_region_name, aws_firehose_delivery_stream_name)
    twitter_client = TwitterClient(aws_firehose_client, twitter_api_consumer_key, twitter_api_consumer_key_secret, twitter_api_access_token, twitter_api_access_token_secret)

    twitter_client.listen(location_bounding_box)


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-twitter_api_consumer_key', help='Twitter API Consumer Key', required=True, type=str)
    arg_parser.add_argument('-twitter_api_consumer_secret', help='Twitter API Consumer Secret', required=True, type=str)
    arg_parser.add_argument('-twitter_api_access_token', help='Twitter API Access Token', required=True, type=str)
    arg_parser.add_argument('-twitter_api_access_token_secret', help='Twitter API Access Token Secret', required=True, type=str)
    arg_parser.add_argument('-aws_api_access_key', help='AWS API Access Key', required=True, type=str)
    arg_parser.add_argument('-aws_api_secret_access_key', help='AWS API Secret Access Key', required=True, type=str)
    arg_parser.add_argument('-aws_api_region_name', help='AWS API Region Name', required=True, type=str)
    arg_parser.add_argument('-aws_firehose_delivery_stream_name', help='AWS Firehose Delivery Stream Name', required=True, type=str)
    arg_parser.add_argument('-twitter_stream_by_location', nargs='+', help='The location on which to listen for tweets in a form of bounding box. Format: <bottom_right_longitude> <bottom_right_latitude> <top_left_longitude> <top_left_latitude>', required=True, type=float)
    arg_parser.add_argument('--logger_host', default='127.0.0.1', help='Override default log aggregator host [127.0.0.1]', type=str)
    arg_parser.add_argument('--logger_port', default=24224, help='Override default log aggregator port [24224]', type=int)
    arg_parser.add_argument('--production', default=False, action='store_true', help='Production Mode')
    args = arg_parser.parse_args()

    production_mode = args.production
    logger_host = args.logger_host
    logger_port = args.logger_port
    location_bounding_box = args.twitter_stream_by_location
    twitter_api_consumer_key = args.twitter_api_consumer_key
    twitter_api_consumer_key_secret = args.twitter_api_consumer_secret
    twitter_api_access_token = args.twitter_api_access_token
    twitter_api_access_token_secret = args.twitter_api_access_token_secret
    aws_api_access_key = args.aws_api_access_key
    aws_api_secret_access_key = args.aws_api_secret_access_key
    aws_api_region_name = args.aws_api_region_name
    aws_firehose_delivery_stream_name = args.aws_firehose_delivery_stream_name

    main(twitter_api_consumer_key, twitter_api_consumer_key_secret, twitter_api_access_token, twitter_api_access_token_secret, aws_firehose_delivery_stream_name, aws_api_access_key, aws_api_secret_access_key, aws_api_region_name)
