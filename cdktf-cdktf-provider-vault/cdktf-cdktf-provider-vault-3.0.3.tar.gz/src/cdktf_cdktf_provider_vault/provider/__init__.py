'''
# `provider`

Refer to the Terraform Registory for docs: [`vault`](https://www.terraform.io/docs/providers/vault).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class VaultProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.provider.VaultProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault vault}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        address: builtins.str,
        add_address_to_env: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        auth_login: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VaultProviderAuthLogin", typing.Dict[str, typing.Any]]]]] = None,
        ca_cert_dir: typing.Optional[builtins.str] = None,
        ca_cert_file: typing.Optional[builtins.str] = None,
        client_auth: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VaultProviderClientAuth", typing.Dict[str, typing.Any]]]]] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VaultProviderHeaders", typing.Dict[str, typing.Any]]]]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        max_retries_ccc: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        skip_child_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_tls_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        token_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault vault} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address: URL of the root of the target Vault server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#address VaultProvider#address}
        :param add_address_to_env: If true, adds the value of the ``address`` argument to the Terraform process environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#add_address_to_env VaultProvider#add_address_to_env}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#alias VaultProvider#alias}
        :param auth_login: auth_login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#auth_login VaultProvider#auth_login}
        :param ca_cert_dir: Path to directory containing CA certificate files to validate the server's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#ca_cert_dir VaultProvider#ca_cert_dir}
        :param ca_cert_file: Path to a CA certificate file to validate the server's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#ca_cert_file VaultProvider#ca_cert_file}
        :param client_auth: client_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#client_auth VaultProvider#client_auth}
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#headers VaultProvider#headers}
        :param max_lease_ttl_seconds: Maximum TTL for secret leases requested by this provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_lease_ttl_seconds VaultProvider#max_lease_ttl_seconds}
        :param max_retries: Maximum number of retries when a 5xx error code is encountered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_retries VaultProvider#max_retries}
        :param max_retries_ccc: Maximum number of retries for Client Controlled Consistency related operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_retries_ccc VaultProvider#max_retries_ccc}
        :param namespace: The namespace to use. Available only for Vault Enterprise. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#namespace VaultProvider#namespace}
        :param skip_child_token: Set this to true to prevent the creation of ephemeral child token used by this provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#skip_child_token VaultProvider#skip_child_token}
        :param skip_tls_verify: Set this to true only if the target Vault server is an insecure development instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#skip_tls_verify VaultProvider#skip_tls_verify}
        :param tls_server_name: Name to use as the SNI host when connecting via TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#tls_server_name VaultProvider#tls_server_name}
        :param token: Token to use to authenticate to Vault. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#token VaultProvider#token}
        :param token_name: Token name to use for creating the Vault child token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#token_name VaultProvider#token_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VaultProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = VaultProviderConfig(
            address=address,
            add_address_to_env=add_address_to_env,
            alias=alias,
            auth_login=auth_login,
            ca_cert_dir=ca_cert_dir,
            ca_cert_file=ca_cert_file,
            client_auth=client_auth,
            headers=headers,
            max_lease_ttl_seconds=max_lease_ttl_seconds,
            max_retries=max_retries,
            max_retries_ccc=max_retries_ccc,
            namespace=namespace,
            skip_child_token=skip_child_token,
            skip_tls_verify=skip_tls_verify,
            tls_server_name=tls_server_name,
            token=token,
            token_name=token_name,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAddAddressToEnv")
    def reset_add_address_to_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddAddressToEnv", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAuthLogin")
    def reset_auth_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthLogin", []))

    @jsii.member(jsii_name="resetCaCertDir")
    def reset_ca_cert_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCertDir", []))

    @jsii.member(jsii_name="resetCaCertFile")
    def reset_ca_cert_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCertFile", []))

    @jsii.member(jsii_name="resetClientAuth")
    def reset_client_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAuth", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetMaxLeaseTtlSeconds")
    def reset_max_lease_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLeaseTtlSeconds", []))

    @jsii.member(jsii_name="resetMaxRetries")
    def reset_max_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetries", []))

    @jsii.member(jsii_name="resetMaxRetriesCcc")
    def reset_max_retries_ccc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetriesCcc", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetSkipChildToken")
    def reset_skip_child_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipChildToken", []))

    @jsii.member(jsii_name="resetSkipTlsVerify")
    def reset_skip_tls_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipTlsVerify", []))

    @jsii.member(jsii_name="resetTlsServerName")
    def reset_tls_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsServerName", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetTokenName")
    def reset_token_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenName", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="addAddressToEnvInput")
    def add_address_to_env_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addAddressToEnvInput"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authLoginInput")
    def auth_login_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderAuthLogin"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderAuthLogin"]]], jsii.get(self, "authLoginInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertDirInput")
    def ca_cert_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertDirInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertFileInput")
    def ca_cert_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertFileInput"))

    @builtins.property
    @jsii.member(jsii_name="clientAuthInput")
    def client_auth_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderClientAuth"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderClientAuth"]]], jsii.get(self, "clientAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderHeaders"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderHeaders"]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlSecondsInput")
    def max_lease_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLeaseTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesCccInput")
    def max_retries_ccc_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesCccInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="skipChildTokenInput")
    def skip_child_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipChildTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="skipTlsVerifyInput")
    def skip_tls_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipTlsVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsServerNameInput")
    def tls_server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsServerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNameInput")
    def token_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenNameInput"))

    @builtins.property
    @jsii.member(jsii_name="addAddressToEnv")
    def add_address_to_env(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addAddressToEnv"))

    @add_address_to_env.setter
    def add_address_to_env(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "add_address_to_env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addAddressToEnv", value)

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "address"))

    @address.setter
    def address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="authLogin")
    def auth_login(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderAuthLogin"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderAuthLogin"]]], jsii.get(self, "authLogin"))

    @auth_login.setter
    def auth_login(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderAuthLogin"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "auth_login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authLogin", value)

    @builtins.property
    @jsii.member(jsii_name="caCertDir")
    def ca_cert_dir(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertDir"))

    @ca_cert_dir.setter
    def ca_cert_dir(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "ca_cert_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertDir", value)

    @builtins.property
    @jsii.member(jsii_name="caCertFile")
    def ca_cert_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertFile"))

    @ca_cert_file.setter
    def ca_cert_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "ca_cert_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertFile", value)

    @builtins.property
    @jsii.member(jsii_name="clientAuth")
    def client_auth(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderClientAuth"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderClientAuth"]]], jsii.get(self, "clientAuth"))

    @client_auth.setter
    def client_auth(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderClientAuth"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "client_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAuth", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderHeaders"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderHeaders"]]], jsii.get(self, "headers"))

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderHeaders"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlSeconds")
    def max_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLeaseTtlSeconds"))

    @max_lease_ttl_seconds.setter
    def max_lease_ttl_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "max_lease_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLeaseTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "max_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetriesCcc")
    def max_retries_ccc(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesCcc"))

    @max_retries_ccc.setter
    def max_retries_ccc(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "max_retries_ccc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetriesCcc", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="skipChildToken")
    def skip_child_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipChildToken"))

    @skip_child_token.setter
    def skip_child_token(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "skip_child_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipChildToken", value)

    @builtins.property
    @jsii.member(jsii_name="skipTlsVerify")
    def skip_tls_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipTlsVerify"))

    @skip_tls_verify.setter
    def skip_tls_verify(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "skip_tls_verify").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipTlsVerify", value)

    @builtins.property
    @jsii.member(jsii_name="tlsServerName")
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsServerName"))

    @tls_server_name.setter
    def tls_server_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "tls_server_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsServerName", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="tokenName")
    def token_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenName"))

    @token_name.setter
    def token_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VaultProvider, "token_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.provider.VaultProviderAuthLogin",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "method": "method",
        "namespace": "namespace",
        "parameters": "parameters",
    },
)
class VaultProviderAuthLogin:
    def __init__(
        self,
        *,
        path: builtins.str,
        method: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#path VaultProvider#path}.
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#method VaultProvider#method}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#namespace VaultProvider#namespace}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#parameters VaultProvider#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VaultProviderAuthLogin.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if method is not None:
            self._values["method"] = method
        if namespace is not None:
            self._values["namespace"] = namespace
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#path VaultProvider#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#method VaultProvider#method}.'''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#namespace VaultProvider#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#parameters VaultProvider#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultProviderAuthLogin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.provider.VaultProviderClientAuth",
    jsii_struct_bases=[],
    name_mapping={"cert_file": "certFile", "key_file": "keyFile"},
)
class VaultProviderClientAuth:
    def __init__(
        self,
        *,
        cert_file: typing.Optional[builtins.str] = None,
        key_file: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cert_file: Path to a file containing the client certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#cert_file VaultProvider#cert_file}
        :param key_file: Path to a file containing the private key that the certificate was issued for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#key_file VaultProvider#key_file}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VaultProviderClientAuth.__init__)
            check_type(argname="argument cert_file", value=cert_file, expected_type=type_hints["cert_file"])
            check_type(argname="argument key_file", value=key_file, expected_type=type_hints["key_file"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cert_file is not None:
            self._values["cert_file"] = cert_file
        if key_file is not None:
            self._values["key_file"] = key_file

    @builtins.property
    def cert_file(self) -> typing.Optional[builtins.str]:
        '''Path to a file containing the client certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#cert_file VaultProvider#cert_file}
        '''
        result = self._values.get("cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_file(self) -> typing.Optional[builtins.str]:
        '''Path to a file containing the private key that the certificate was issued for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#key_file VaultProvider#key_file}
        '''
        result = self._values.get("key_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultProviderClientAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.provider.VaultProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "add_address_to_env": "addAddressToEnv",
        "alias": "alias",
        "auth_login": "authLogin",
        "ca_cert_dir": "caCertDir",
        "ca_cert_file": "caCertFile",
        "client_auth": "clientAuth",
        "headers": "headers",
        "max_lease_ttl_seconds": "maxLeaseTtlSeconds",
        "max_retries": "maxRetries",
        "max_retries_ccc": "maxRetriesCcc",
        "namespace": "namespace",
        "skip_child_token": "skipChildToken",
        "skip_tls_verify": "skipTlsVerify",
        "tls_server_name": "tlsServerName",
        "token": "token",
        "token_name": "tokenName",
    },
)
class VaultProviderConfig:
    def __init__(
        self,
        *,
        address: builtins.str,
        add_address_to_env: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        auth_login: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VaultProviderAuthLogin, typing.Dict[str, typing.Any]]]]] = None,
        ca_cert_dir: typing.Optional[builtins.str] = None,
        ca_cert_file: typing.Optional[builtins.str] = None,
        client_auth: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VaultProviderClientAuth, typing.Dict[str, typing.Any]]]]] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VaultProviderHeaders", typing.Dict[str, typing.Any]]]]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        max_retries_ccc: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        skip_child_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_tls_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        token_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address: URL of the root of the target Vault server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#address VaultProvider#address}
        :param add_address_to_env: If true, adds the value of the ``address`` argument to the Terraform process environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#add_address_to_env VaultProvider#add_address_to_env}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#alias VaultProvider#alias}
        :param auth_login: auth_login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#auth_login VaultProvider#auth_login}
        :param ca_cert_dir: Path to directory containing CA certificate files to validate the server's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#ca_cert_dir VaultProvider#ca_cert_dir}
        :param ca_cert_file: Path to a CA certificate file to validate the server's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#ca_cert_file VaultProvider#ca_cert_file}
        :param client_auth: client_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#client_auth VaultProvider#client_auth}
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#headers VaultProvider#headers}
        :param max_lease_ttl_seconds: Maximum TTL for secret leases requested by this provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_lease_ttl_seconds VaultProvider#max_lease_ttl_seconds}
        :param max_retries: Maximum number of retries when a 5xx error code is encountered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_retries VaultProvider#max_retries}
        :param max_retries_ccc: Maximum number of retries for Client Controlled Consistency related operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_retries_ccc VaultProvider#max_retries_ccc}
        :param namespace: The namespace to use. Available only for Vault Enterprise. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#namespace VaultProvider#namespace}
        :param skip_child_token: Set this to true to prevent the creation of ephemeral child token used by this provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#skip_child_token VaultProvider#skip_child_token}
        :param skip_tls_verify: Set this to true only if the target Vault server is an insecure development instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#skip_tls_verify VaultProvider#skip_tls_verify}
        :param tls_server_name: Name to use as the SNI host when connecting via TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#tls_server_name VaultProvider#tls_server_name}
        :param token: Token to use to authenticate to Vault. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#token VaultProvider#token}
        :param token_name: Token name to use for creating the Vault child token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#token_name VaultProvider#token_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VaultProviderConfig.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument add_address_to_env", value=add_address_to_env, expected_type=type_hints["add_address_to_env"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument auth_login", value=auth_login, expected_type=type_hints["auth_login"])
            check_type(argname="argument ca_cert_dir", value=ca_cert_dir, expected_type=type_hints["ca_cert_dir"])
            check_type(argname="argument ca_cert_file", value=ca_cert_file, expected_type=type_hints["ca_cert_file"])
            check_type(argname="argument client_auth", value=client_auth, expected_type=type_hints["client_auth"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument max_lease_ttl_seconds", value=max_lease_ttl_seconds, expected_type=type_hints["max_lease_ttl_seconds"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument max_retries_ccc", value=max_retries_ccc, expected_type=type_hints["max_retries_ccc"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument skip_child_token", value=skip_child_token, expected_type=type_hints["skip_child_token"])
            check_type(argname="argument skip_tls_verify", value=skip_tls_verify, expected_type=type_hints["skip_tls_verify"])
            check_type(argname="argument tls_server_name", value=tls_server_name, expected_type=type_hints["tls_server_name"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument token_name", value=token_name, expected_type=type_hints["token_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
        }
        if add_address_to_env is not None:
            self._values["add_address_to_env"] = add_address_to_env
        if alias is not None:
            self._values["alias"] = alias
        if auth_login is not None:
            self._values["auth_login"] = auth_login
        if ca_cert_dir is not None:
            self._values["ca_cert_dir"] = ca_cert_dir
        if ca_cert_file is not None:
            self._values["ca_cert_file"] = ca_cert_file
        if client_auth is not None:
            self._values["client_auth"] = client_auth
        if headers is not None:
            self._values["headers"] = headers
        if max_lease_ttl_seconds is not None:
            self._values["max_lease_ttl_seconds"] = max_lease_ttl_seconds
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if max_retries_ccc is not None:
            self._values["max_retries_ccc"] = max_retries_ccc
        if namespace is not None:
            self._values["namespace"] = namespace
        if skip_child_token is not None:
            self._values["skip_child_token"] = skip_child_token
        if skip_tls_verify is not None:
            self._values["skip_tls_verify"] = skip_tls_verify
        if tls_server_name is not None:
            self._values["tls_server_name"] = tls_server_name
        if token is not None:
            self._values["token"] = token
        if token_name is not None:
            self._values["token_name"] = token_name

    @builtins.property
    def address(self) -> builtins.str:
        '''URL of the root of the target Vault server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#address VaultProvider#address}
        '''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_address_to_env(self) -> typing.Optional[builtins.str]:
        '''If true, adds the value of the ``address`` argument to the Terraform process environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#add_address_to_env VaultProvider#add_address_to_env}
        '''
        result = self._values.get("add_address_to_env")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#alias VaultProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_login(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VaultProviderAuthLogin]]]:
        '''auth_login block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#auth_login VaultProvider#auth_login}
        '''
        result = self._values.get("auth_login")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VaultProviderAuthLogin]]], result)

    @builtins.property
    def ca_cert_dir(self) -> typing.Optional[builtins.str]:
        '''Path to directory containing CA certificate files to validate the server's certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#ca_cert_dir VaultProvider#ca_cert_dir}
        '''
        result = self._values.get("ca_cert_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_cert_file(self) -> typing.Optional[builtins.str]:
        '''Path to a CA certificate file to validate the server's certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#ca_cert_file VaultProvider#ca_cert_file}
        '''
        result = self._values.get("ca_cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_auth(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VaultProviderClientAuth]]]:
        '''client_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#client_auth VaultProvider#client_auth}
        '''
        result = self._values.get("client_auth")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VaultProviderClientAuth]]], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#headers VaultProvider#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VaultProviderHeaders"]]], result)

    @builtins.property
    def max_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum TTL for secret leases requested by this provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_lease_ttl_seconds VaultProvider#max_lease_ttl_seconds}
        '''
        result = self._values.get("max_lease_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of retries when a 5xx error code is encountered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_retries VaultProvider#max_retries}
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries_ccc(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of retries for Client Controlled Consistency related operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#max_retries_ccc VaultProvider#max_retries_ccc}
        '''
        result = self._values.get("max_retries_ccc")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace to use. Available only for Vault Enterprise.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#namespace VaultProvider#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_child_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set this to true to prevent the creation of ephemeral child token used by this provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#skip_child_token VaultProvider#skip_child_token}
        '''
        result = self._values.get("skip_child_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def skip_tls_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set this to true only if the target Vault server is an insecure development instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#skip_tls_verify VaultProvider#skip_tls_verify}
        '''
        result = self._values.get("skip_tls_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        '''Name to use as the SNI host when connecting via TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#tls_server_name VaultProvider#tls_server_name}
        '''
        result = self._values.get("tls_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Token to use to authenticate to Vault.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#token VaultProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_name(self) -> typing.Optional[builtins.str]:
        '''Token name to use for creating the Vault child token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#token_name VaultProvider#token_name}
        '''
        result = self._values.get("token_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.provider.VaultProviderHeaders",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class VaultProviderHeaders:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: The header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#name VaultProvider#name}
        :param value: The header value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#value VaultProvider#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VaultProviderHeaders.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#name VaultProvider#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The header value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault#value VaultProvider#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultProviderHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VaultProvider",
    "VaultProviderAuthLogin",
    "VaultProviderClientAuth",
    "VaultProviderConfig",
    "VaultProviderHeaders",
]

publication.publish()
