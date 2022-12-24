
def checkresource(resourcetype):
    # Define resource list by service+resource
    resourcelist = [
        'amazonmqBroker',
        'amazonmqConfiguration',
        'AppstreamFleet',
        'AppstreamImageBulder',
        'AppstreamImageStack',
        'BraketQuantumTask',
        'CertificateManagerCertificate',
        'Cloud9Environment',
        'CloudFrontStreamingDistribution',
        'CloudFrontDistribution',
        'CloudTrailTrail',
        'CloudWatchAlarm',
        'CodeArtifactDomain',
        'CodeArtifactRepository',
        'CodeBuildProject',
        'CodeCommitRepository',
        'CodeGuruReviewerRepositoryAssociation',
        'CodePipelinePipeline',
        'CodePipelineWebhook',
        'CognitoIdentityPool',
        'CognitoUserPool',
        'ComprehendDocumentClassifier',
        'ComprehendEntityRecognizer',
        'ConfigConfigRule',
        'DataBrewJob',
        'DataBrewProject',
        'DataBrewRecipe',
        'DataBrewSchedule',
        'DataExchangeDataSet',
        'DataPipelinePipeline',
        'DynamoDBTable',
        'Ec2CustomerGateway',
        'Ec2DHCPOptions',
        'Ec2Image',
        'Ec2InternetGateway',
        'Ec2NetworkInterface',
        'Ec2ReservedInstance',
        'Ec2NatGateway',
        'Ec2NetworkAcl',
        'Ec2RouteTable',
        'Ec2EIP',
        'Ec2SecurityGroup',
        'Ec2Subnet',
        'Ec2Instance',
        'Ec2Snapshot',
        'Ec2SpotInstanceRequest',
        'Ec2VPC',
        'Ec2VPNConnection',
        'Ec2VPNGateway',
        'Ec2Volume',
        'ECSCluster',
        'ECSTaskDefinition',
        'EFSFileSystem',
        'EKSCluster',
        'EMRCluster',
        'EMRContainersVirtualCluster',
        'ElasticCacheElasticCache',
        'ElasticCacheSnapshot',
        'ElasticBeanstalkApplication',
        'ElasticInferenceElasticInferenceAccelerator',
        'ElasticLoadBalancingLoadBalancer',
        'ElasticLoadBalancingV2LoadBalancer',
        'ElasticLoadBalancingV2TargetGroup',
        'EventsRule',
        'FSxFileSystem',
        'ForecastDataset',
        'ForecastDatasetGroup',
        'ForecastForecast',
        'ForecastForecastExportJob',
        'ForecastPredictor',
        'ForecastPredictorBacktestExportJob',
        'FraudDetectorDetector',
        'FraudDetectorEntityType',
        'FraudDetectorEventType',
        'FraudDetectorExternalModel',
        'FraudDetectorLabel',
        'FraudDetectorModel',
        'FraudDetectorOutcome',
        'FraudDetectorVariable',
        'GlacierVault',
        'GlueCrawler',
        'GlueJob',
        'GlueTrigger',
        'GreengrassConnectorDefinition',
        'GreengrassCoreDefinition',
        'GreengrassDeviceDefinition',
        'GreengrassFunctionDefinition',
        'GreengrassGroup',
        'GreengrassLoggerDefinition',
        'GreengrassResourceDefinition',
        'GreengrassSubscriptionDefinition',
        'IAMInstanceProfile',
        'IAMManagedPolicy',
        'IAMOpenIDConnectProvider',
        'IAMSAMLProvider',
        'IAMServerCertificate',
        'IotAnalyticsDataset',
        'IoTEventsDetectorModel',
        'IoTEventsInput',
        'KMSKey',
        'KafkaCluster',
        'KinesisStream',
        'KinesisAnalyticsApplication',
        'MacieClassificationJob',
        'MacieCustomDataIdentifier',
        'MacieFindingsFilter',
        'MacieMember',
        'OpenSearchServiceDomain',
        'OrganizationsAccount',
        'OrganizationsRoot',
        'QLDBLedger',
        'RAMResourceShare',
        'RDSDBCluster',
        'RDSDBClusterParameterGroup',
        'RDSDBClusterSnapshot',
        'RDSDBInstance',
        'RDSDBParameterGroup',
        'RDSDBSecurityGroup',
        'RDSDBSnapshot',
        'RDSDBSubnetGroup',
        'RDSEventSubscription',
        'RDSOptionGroup',
        'RDSReservedDBInstance',
        'RedshiftCluster',
        'RedshiftClusterSubnetGroup',
        'RedshiftHSMClientCertificate',
        'ResourceGroupsGroup',
        'RoboMakerRobotApplication',
        'RoboMakerSimulationApplication',
        'RoboMakerSimuationJob',
        'Route53Domain',
        'Route53HealthCheck',
        'Route53ResolverResolverEndpoint',
        'Route53ResolverResolverRule',
        'SESConfigurationSet',
        'SESContactList',
        'SESDedicatedIpPool',
        'SESIdentity',
        'SNSTopic',
        'SQSQueue',
        'SSMParameter',
        'StepFunctionsActivity',
        'StepFunctionsStateMachine',
        'StorageGatewayGateway',
        'WorkspacesWorkspace',
    ]
    if resourcetype in resourcelist:
        return True
    else:
        return False