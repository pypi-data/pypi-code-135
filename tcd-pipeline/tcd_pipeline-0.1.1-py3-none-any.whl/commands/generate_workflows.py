"""
Command generate-workflow
"""
import click
from tcd_pipeline import pipeline as pipeline_tool


@click.command(help="Generate workflows from pipelines")
@click.option("--pipelines",
  default=".",
  type=click.Path(),
  show_default=True,
  help="Path to pipeline file or directory contains *-pipelines.yaml"
  )
@click.option("--output", "-o",
  help="Output workflows file. [Default: stdout]",
  type=click.Path()
  )
def generate_workflows(pipelines, output):
    """Generate workflows from pipelines"""
    if output == "" or output == "stdout":
        output = None

    try:
        pipeline_tool.generate_workflows(
          pipeline_path=pipelines,
          output=output
        )
    except Exception as err:
        print(err)
