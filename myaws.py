from typing import List

import boto3
import click


DEFAULT_INSTANCE_IDS = ["i-0d4c1285df95ed943"]


@click.group()
def cli():
    pass


@cli.command()
@click.argument("instance_ids", nargs=-1)
@click.option(
    "--region",
    default="us-west-2",
    help="AWS region",
)
@click.option(
    "--ssh_host_name",
    default="ec",
    help="if not null, will create a host in ~/.ssh/config",
)
def up(instance_ids: List[str], region: str, ssh_host_name: str):
    if len(instance_ids) == 0:
        instance_ids = DEFAULT_INSTANCE_IDS
    ec2 = boto3.resource("ec2", region_name=region)
    instances = ec2.instances.filter(InstanceIds=instance_ids)
    instances.start()
    # TODO: wait until instance has an IP and update ~/.ssh/config
