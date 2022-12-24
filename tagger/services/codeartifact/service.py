from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class codeartifactTagger(object):
    def __init__(self, dryrun, verbose, servicetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.servicetype = servicetype
        self.codeartifact = _client('codeartifact', role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "codeartifact"
        if self.servicetype == 'CodeArtifactDomain':
            resource_arn = "domain/"+resource_arn

        if self.servicetype == 'CodeArtifactRepository':
            resource_arn = "repository/"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        if self.verbose:
            print("tagging %s with %s" % (", ".join(file_system_id), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._codeartifact_create_tags(resourceArn=file_system_id, tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _codeartifact_create_tags(self, **kwargs):
        return self.codeartifact.tag_resource(**kwargs)