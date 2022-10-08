'''
# `provider`

Refer to the Terraform Registory for docs: [`dnsimple`](https://www.terraform.io/docs/providers/dnsimple).
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


class DnsimpleProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-dnsimple.provider.DnsimpleProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/dnsimple dnsimple}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: builtins.str,
        token: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        prefetch: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sandbox: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_agent: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/dnsimple dnsimple} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account: The account for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#account DnsimpleProvider#account}
        :param token: The API v2 token for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#token DnsimpleProvider#token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#alias DnsimpleProvider#alias}
        :param prefetch: Flag to enable the prefetch of zone records. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#prefetch DnsimpleProvider#prefetch}
        :param sandbox: Flag to enable the sandbox API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#sandbox DnsimpleProvider#sandbox}
        :param user_agent: Custom string to append to the user agent used for sending HTTP requests to the API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#user_agent DnsimpleProvider#user_agent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsimpleProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DnsimpleProviderConfig(
            account=account,
            token=token,
            alias=alias,
            prefetch=prefetch,
            sandbox=sandbox,
            user_agent=user_agent,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetPrefetch")
    def reset_prefetch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefetch", []))

    @jsii.member(jsii_name="resetSandbox")
    def reset_sandbox(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSandbox", []))

    @jsii.member(jsii_name="resetUserAgent")
    def reset_user_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAgent", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountInput")
    def account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="prefetchInput")
    def prefetch_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "prefetchInput"))

    @builtins.property
    @jsii.member(jsii_name="sandboxInput")
    def sandbox_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sandboxInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="userAgentInput")
    def user_agent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @account.setter
    def account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsimpleProvider, "account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsimpleProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="prefetch")
    def prefetch(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "prefetch"))

    @prefetch.setter
    def prefetch(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsimpleProvider, "prefetch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefetch", value)

    @builtins.property
    @jsii.member(jsii_name="sandbox")
    def sandbox(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sandbox"))

    @sandbox.setter
    def sandbox(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsimpleProvider, "sandbox").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sandbox", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsimpleProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="userAgent")
    def user_agent(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAgent"))

    @user_agent.setter
    def user_agent(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsimpleProvider, "user_agent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAgent", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-dnsimple.provider.DnsimpleProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "token": "token",
        "alias": "alias",
        "prefetch": "prefetch",
        "sandbox": "sandbox",
        "user_agent": "userAgent",
    },
)
class DnsimpleProviderConfig:
    def __init__(
        self,
        *,
        account: builtins.str,
        token: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        prefetch: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sandbox: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_agent: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account: The account for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#account DnsimpleProvider#account}
        :param token: The API v2 token for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#token DnsimpleProvider#token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#alias DnsimpleProvider#alias}
        :param prefetch: Flag to enable the prefetch of zone records. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#prefetch DnsimpleProvider#prefetch}
        :param sandbox: Flag to enable the sandbox API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#sandbox DnsimpleProvider#sandbox}
        :param user_agent: Custom string to append to the user agent used for sending HTTP requests to the API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#user_agent DnsimpleProvider#user_agent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsimpleProviderConfig.__init__)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument prefetch", value=prefetch, expected_type=type_hints["prefetch"])
            check_type(argname="argument sandbox", value=sandbox, expected_type=type_hints["sandbox"])
            check_type(argname="argument user_agent", value=user_agent, expected_type=type_hints["user_agent"])
        self._values: typing.Dict[str, typing.Any] = {
            "account": account,
            "token": token,
        }
        if alias is not None:
            self._values["alias"] = alias
        if prefetch is not None:
            self._values["prefetch"] = prefetch
        if sandbox is not None:
            self._values["sandbox"] = sandbox
        if user_agent is not None:
            self._values["user_agent"] = user_agent

    @builtins.property
    def account(self) -> builtins.str:
        '''The account for API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#account DnsimpleProvider#account}
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token(self) -> builtins.str:
        '''The API v2 token for API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#token DnsimpleProvider#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#alias DnsimpleProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefetch(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to enable the prefetch of zone records.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#prefetch DnsimpleProvider#prefetch}
        '''
        result = self._values.get("prefetch")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sandbox(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to enable the sandbox API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#sandbox DnsimpleProvider#sandbox}
        '''
        result = self._values.get("sandbox")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def user_agent(self) -> typing.Optional[builtins.str]:
        '''Custom string to append to the user agent used for sending HTTP requests to the API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/dnsimple#user_agent DnsimpleProvider#user_agent}
        '''
        result = self._values.get("user_agent")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsimpleProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DnsimpleProvider",
    "DnsimpleProviderConfig",
]

publication.publish()
