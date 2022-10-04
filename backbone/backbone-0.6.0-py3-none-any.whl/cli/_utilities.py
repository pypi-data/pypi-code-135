import functools
import gc
import typing
import uuid
from pathlib import Path

import typer
from nacl import encoding, hash
from nacl.pwhash import argon2id
from zxcvbn import zxcvbn

from backbone import sync as backbone
from backbone.cli import Context, _config
from backbone.common import models, service

# Define the configuration file location
BACKBONE_ROOT: Path = Path(typer.get_app_dir("backbone"))
BACKBONE_CONFIG: Path = BACKBONE_ROOT / "config.json"


def local_secret():
    """A local secret used for on-disk sensitive file encryption"""
    node = uuid.getnode().to_bytes(8, "big")
    salt = hash.sha256(b"backbone:local", encoder=encoding.RawEncoder)
    salt = hash.sha256(salt, encoder=encoding.RawEncoder)

    return argon2id.kdf(
        size=32,
        password=node,
        salt=salt[:16],
        memlimit=argon2id.MEMLIMIT_INTERACTIVE,
        opslimit=argon2id.OPSLIMIT_INTERACTIVE,
    )


def config_to_backbone(configuration: typing.Optional[_config.LocalConfiguration]) -> backbone.Client:
    if not configuration:
        typer.echo("Not authenticated. Have you tried `backbone authenticate`?")
        raise typer.Exit()

    return backbone.from_derived_secrets(
        user_name=configuration.user_name,
        secret_key=configuration.secret_key,
        private_key=configuration.private_key,
        signing_key=configuration.signing_key,
    )


def read_configuration() -> typing.Optional[_config.LocalConfiguration]:
    try:
        with BACKBONE_CONFIG.open("rb") as configuration_file:
            encrypted_configuration: _config.EncryptedLocalConfiguration = _config.EncryptedLocalConfiguration.decode(
                configuration_file.read()
            )
            configuration: _config.LocalConfiguration = encrypted_configuration.decrypt(key=local_secret())
            gc.collect()
            return configuration
    except FileNotFoundError:
        return None
    except models.CryptographyError:
        return None


def write_configuration(configuration: _config.LocalConfiguration) -> None:
    if not BACKBONE_ROOT.is_dir():
        BACKBONE_ROOT.mkdir(parents=True)

    with open(BACKBONE_CONFIG, "wb") as config_file:
        encrypted_configuration: _config.EncryptedLocalConfiguration = _config.EncryptedLocalConfiguration.encrypt(
            key=local_secret(), encrypted=configuration, plain=None
        )
        config_file.write(encrypted_configuration.encode())


def clear_configuration() -> None:
    BACKBONE_CONFIG.unlink(missing_ok=True)


def request_master_secret(context: typer.Context, associated_data: typing.List[str] = None, setup: bool = False) -> str:
    ctx: Context = context.obj
    secret = typer.prompt(f"Enter your master key", hide_input=True, confirmation_prompt=setup)

    if setup:
        with ctx.fmt.begin("Assessing password strength"):
            evaluation = zxcvbn(secret, user_inputs=associated_data)

            if int(evaluation["crack_times_seconds"]["offline_fast_hashing_1e10_per_second"]) < 10 * 365 * 24 * 3600:
                ctx.fmt.failure(
                    "Your password is too weak and could be cracked by a motivated attacker in"
                    f" {evaluation['crack_times_display']['offline_fast_hashing_1e10_per_second']}.\nBackbone mandates"
                    " a 10-year minimum for enhanced security."
                )

                if evaluation["feedback"]["suggestions"]:
                    ctx.fmt.info("Please consider the following suggestions to pick a better password:")

                    for suggestion in evaluation["feedback"]["suggestions"]:
                        ctx.fmt.raw(f"- {suggestion}")
                else:
                    ctx.fmt.info("Please choose a stronger password and try again.")

                raise typer.Exit()
            else:
                ctx.fmt.success(
                    "Password strength assessed: estimated lifetime of"
                    f" {evaluation['crack_times_display']['offline_slow_hashing_1e4_per_second']}."
                )

    return secret


def expect_workspace(f):
    @functools.wraps(f)
    def wrapper(context: typer.Context, *args, **kwargs):
        backbone_context: Context = context.obj
        if not backbone_context.workspace_name:
            raise typer.BadParameter("Workspace is not defined")
        return f(context, *args, **kwargs)

    return wrapper


def expect_client(f):
    @functools.wraps(f)
    def wrapper(context: typer.Context, *args, **kwargs):
        backbone_context: Context = context.obj
        if not backbone_context.client:
            raise ValueError("Not authenticated. Have you tried `backbone user login`?")
        return f(context, *args, **kwargs)

    return wrapper


def list_workspace_users(workspace_client):
    grants = workspace_client.list_grants()
    results = []

    for grant in grants:
        recipient_type, recipient_identity = grant.plain.recipient

        if recipient_type != "user":
            continue

        results.append(recipient_identity)

    return results


def find_workspace_user(workspace_client, user_name):
    grant: models.SharedWorkspaceGrant = workspace_client.fetch_grant(user_name)
    _recipient_type, recipient = grant.plain.recipient
    return recipient


def match_workspace_users(workspace_client, user_names):
    user_names = set(user_names)
    result = {}

    for user in list_workspace_users(workspace_client):
        if user.name not in user_names:
            continue

        result[user.name] = user

    return result


def handle_exceptions(f):
    @functools.wraps(f)
    def wrapper(context: typer.Context, *args, **kwargs):
        ctx: Context = context.obj
        try:
            return f(context, *args, **kwargs)
        except typer.Exit:
            pass
        except service.Error as e:
            ctx.fmt.failure(e.message)
            raise typer.Exit()
        except Exception as e:
            ctx.fmt.failure(str(e))
            raise typer.Exit()

    return wrapper
