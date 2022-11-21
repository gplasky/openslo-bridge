import click
import sys
from pathlib import Path

@click.group('cli', invoke_without_command=True)
@click.option('--version', '-v', is_flag=True, help="Show openslo-bridge version")
@click.option('--file', '-f', required=False, default='openslo.yaml', type=click.Path(), help='YAML file to convert')
@click.option('--create', '-c', is_flag=True, help='Create SLO for converted OpenSLO object')
@click.pass_context
def cli(ctx, version, file, create):

    """Converts OpenSLO specs to Google Cloud Service Monitoring SLOs"""

    if version:
        v = '0.1' #TODO
        print(f'openslo-bridge {v}')
        sys.exit(0)

    readOpenSloFile()
    createServiceMonitoringSLO()

def readOpenSloFile():
    print('Read file!')

def createServiceMonitoringSLO():
    print('Create SLO!')

if __name__ == '__main__':
    cli()
