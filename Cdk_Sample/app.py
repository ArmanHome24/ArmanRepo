#!/usr/bin/env python3

from aws_cdk import core

from cdk_sample.cdk_sample_stack import CdkSampleStack


app = core.App()
CdkSampleStack(app, "cdk-sample")

app.synth()
