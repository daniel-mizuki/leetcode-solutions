#!/usr/bin/env python3

"""
App
"""

import aws_cdk

from cdk.pipeline_stack import PipelineStack

app = aws_cdk.App()
PipelineStack(app, "PipelineStack")

app.synth()
