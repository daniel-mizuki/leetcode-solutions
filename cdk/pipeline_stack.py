"""
Pipeline Stack
"""

from constructs import Construct
from aws_cdk import (
    pipelines,
    Stack,
)


class PipelineStack(Stack):
    """
    Pipeline Stack
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = pipelines.CodePipelineSource.connection(
            "daniel-mizuki/leetcode-solutions",
            "main",
            connection_arn=(
                "arn:aws:codestar-connections:us-west-1"
                ":211125549495:connection"
                "/bf8949cf-df8a-4bd8-86fa-b00da059fd43"
            ),
        )

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=source,
                commands=[
                    "npm install -g aws-cdk",
                    "pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )
