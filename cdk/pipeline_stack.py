"""
Pipeline Stack
"""

from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
)


class PipelineStack(Stack):
    """
    Pipeline Stack
    """

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source = pipelines.CodePipelineSource.git_hub(
            "daniel-mizuki/leetcode-solutions",
            "main",
        )

        pipelines.CodePipeline(
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
