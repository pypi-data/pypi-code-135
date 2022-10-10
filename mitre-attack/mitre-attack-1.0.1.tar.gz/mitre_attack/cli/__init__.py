from typing import Optional

import click
from click import Context

import mitre_attack.serialization
from mitre_attack.api.client import MitreAttack
from mitre_attack.cli.helpers import str_to_strs


@click.group()
@click.option('--enterprise/--no-enterprise', '-E', 'include_enterprise')
@click.option('--mobile/--no-mobile', '-M', 'include_mobile')
@click.option('--ics/--no-ics', '-I', 'include_ics')
@click.option('--all', '-A', 'include_all', is_flag=True)
@click.pass_context
def main(ctx: Context, include_enterprise: bool, include_mobile: bool, include_ics: bool, include_all: bool):
    if include_all or not any((include_enterprise, include_mobile, include_ics)):
        include_enterprise = include_mobile = include_ics = True

    client = MitreAttack(include_enterprise=include_enterprise, include_mobile=include_mobile, include_ics=include_ics)
    ctx.obj = client


@main.command()
@click.argument('object-id', required=True)
@click.pass_context
def get_object(ctx: Context, object_id: str):
    """
    Lookup objects.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    row = client.get_object(object_id)
    if row:
        print(mitre_attack.serialization.to_json(row))


@main.command()
@click.argument('object-ids', required=False)
@click.option('--object-types', '-T')
@click.option('--object-names', '-N')
@click.pass_context
def get_objects(
        ctx: Context,
        object_ids: Optional[str] = None,
        object_types: Optional[str] = None,
        object_names: Optional[str] = None):
    """
    Search for objects.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    rows = client.iter_objects(
        object_ids=str_to_strs(object_ids),
        object_types=str_to_strs(object_types),
        object_names=str_to_strs(object_names),
    )
    for row in rows:
        print(mitre_attack.serialization.to_json(row))


@main.command()
@click.argument('object-ids', required=False)
@click.option('--object-types', '-T')
@click.option('--object-names', '-N')
@click.pass_context
def count_objects(
        ctx: Context,
        object_ids: Optional[str] = None,
        object_types: Optional[str] = None,
        object_names: Optional[str] = None):
    """
    Count objects.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    total = client.count_objects(
        object_ids=str_to_strs(object_ids),
        object_types=str_to_strs(object_types),
        object_names=str_to_strs(object_names),
    )
    print(total)


@main.command()
@click.argument('relationship-id', required=True)
@click.pass_context
def get_relationship(ctx: Context, relationship_id: str):
    """
    Lookup relationships.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    row = client.get_relationship(relationship_id)
    if row:
        print(mitre_attack.serialization.to_json(row))


@main.command()
@click.argument('relationship-ids', required=False)
@click.option('--relationship-types')
@click.option('--source-object-ids')
@click.option('--source-object-types')
@click.option('--source-object-types')
@click.option('--target-object-ids')
@click.option('--target-object-types')
@click.pass_context
def get_relationships(
        ctx: Context,
        relationship_ids: Optional[str] = None,
        relationship_types: Optional[str] = None,
        source_object_ids: Optional[str] = None,
        source_object_types: Optional[str] = None,
        target_object_ids: Optional[str] = None,
        target_object_types: Optional[str] = None):
    """
    Search for relationships.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    rows = client.iter_relationships(
        relationship_ids=str_to_strs(relationship_ids),
        relationship_types=str_to_strs(relationship_types),
        source_object_ids=str_to_strs(source_object_ids),
        source_object_types=str_to_strs(source_object_types),
        target_object_ids=str_to_strs(target_object_ids),
        target_object_types=str_to_strs(target_object_types),
    )
    for row in rows:
        print(mitre_attack.serialization.to_json(row))


@main.command()
@click.argument('relationship-ids', required=False)
@click.option('--relationship-types')
@click.option('--source-object-ids')
@click.option('--source-object-types')
@click.option('--source-object-types')
@click.option('--target-object-ids')
@click.option('--target-object-types')
@click.pass_context
def count_relationships(
        ctx: Context,
        relationship_ids: Optional[str] = None,
        relationship_types: Optional[str] = None,
        source_object_ids: Optional[str] = None,
        source_object_types: Optional[str] = None,
        target_object_ids: Optional[str] = None,
        target_object_types: Optional[str] = None):
    """
    Count relationships.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    total = client.count_relationships(
        relationship_ids=str_to_strs(relationship_ids),
        relationship_types=str_to_strs(relationship_types),
        source_object_ids=str_to_strs(source_object_ids),
        source_object_types=str_to_strs(source_object_types),
        target_object_ids=str_to_strs(target_object_ids),
        target_object_types=str_to_strs(target_object_types),
    )
    print(total)


@main.command()
@click.argument('object-ids', required=False)
@click.option('--object-types', '-T')
@click.option('--object-names', '-N')
@click.pass_context
def tally_objects_by_type(
        ctx: Context,
        object_ids: Optional[str] = None,
        object_types: Optional[str] = None,
        object_names: Optional[str] = None):
    """
    Tally objects by type.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    tally = client.tally_objects_by_type(
        object_ids=str_to_strs(object_ids),
        object_types=str_to_strs(object_types),
        object_names=str_to_strs(object_names),
    )
    print(mitre_attack.serialization.to_json(tally))


@main.command()
@click.argument('relationship-ids', required=False)
@click.option('--relationship-types')
@click.option('--source-object-ids', '-s')
@click.option('--source-object-types', '-st')
@click.option('--target-object-ids', '-t')
@click.option('--target-object-types', '-tt')
@click.pass_context
def tally_relationships_by_type(
        ctx: Context,
        relationship_ids: Optional[str] = None,
        relationship_types: Optional[str] = None,
        source_object_ids: Optional[str] = None,
        source_object_types: Optional[str] = None,
        target_object_ids: Optional[str] = None,
        target_object_types: Optional[str] = None):
    """
    Tally relationships by type.
    """
    client = ctx.obj
    assert isinstance(client, MitreAttack)

    tally = client.tally_relationships_by_type(
        relationship_ids=str_to_strs(relationship_ids),
        relationship_types=str_to_strs(relationship_types),
        source_object_ids=str_to_strs(source_object_ids),
        source_object_types=str_to_strs(source_object_types),
        target_object_ids=str_to_strs(target_object_ids),
        target_object_types=str_to_strs(target_object_types),
    )
    print(mitre_attack.serialization.to_json(tally))
