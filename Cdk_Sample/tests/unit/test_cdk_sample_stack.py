import json
import pytest

from aws_cdk import core
from cdk_sample.cdk_sample_stack import CdkSampleStack


def get_template():
    app = core.App()
    CdkSampleStack(app, "cdk-sample")
    return json.dumps(app.synth().get_stack("cdk-sample").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
