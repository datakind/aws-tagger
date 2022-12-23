from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _name_to_arn
import botocore
from retrying import retry
import boto3

class SNSTopicTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.snstopic = _client('sns', role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "sns"
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)

        if self.verbose:
            print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._resourcegroup_create_tags(ResourceArn=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['FileSystemNotFound']:
                    print("SNS Topic Resource not found: %s" % resource_arn)
                else:
                    raise exception