#!/usr/bin/env python3

"""
App
"""

import aws_cdk as cdk

from cdk.pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(app, "PipelineStack")

app.synth()
