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

        source = pipelines.CodePipelineSource.git_hub(
            "daniel-mizuki/leetcode-solutions",
            "main",
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
