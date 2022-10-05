'''
# `aws_wafv2_rule_group`

Refer to the Terraform Registory for docs: [`aws_wafv2_rule_group`](https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group).
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


class Wafv2RuleGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group aws_wafv2_rule_group}.'''

    def __init__(
        self,
        scope_: constructs.Construct,
        id_: builtins.str,
        *,
        capacity: jsii.Number,
        name: builtins.str,
        scope: builtins.str,
        visibility_config: typing.Union["Wafv2RuleGroupVisibilityConfig", typing.Dict[str, typing.Any]],
        custom_response_body: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupCustomResponseBody", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRule", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group aws_wafv2_rule_group} Resource.

        :param scope_: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#capacity Wafv2RuleGroup#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#scope Wafv2RuleGroup#scope}.
        :param visibility_config: visibility_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#visibility_config Wafv2RuleGroup#visibility_config}
        :param custom_response_body: custom_response_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response_body Wafv2RuleGroup#custom_response_body}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#description Wafv2RuleGroup#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#id Wafv2RuleGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#rule Wafv2RuleGroup#rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#tags Wafv2RuleGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#tags_all Wafv2RuleGroup#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroup.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Wafv2RuleGroupConfig(
            capacity=capacity,
            name=name,
            scope=scope,
            visibility_config=visibility_config,
            custom_response_body=custom_response_body,
            description=description,
            id=id,
            rule=rule,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope_, id_, config])

    @jsii.member(jsii_name="putCustomResponseBody")
    def put_custom_response_body(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupCustomResponseBody", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroup.put_custom_response_body)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomResponseBody", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroup.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putVisibilityConfig")
    def put_visibility_config(
        self,
        *,
        cloudwatch_metrics_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        metric_name: builtins.str,
        sampled_requests_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param cloudwatch_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cloudwatch_metrics_enabled Wafv2RuleGroup#cloudwatch_metrics_enabled}.
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#metric_name Wafv2RuleGroup#metric_name}.
        :param sampled_requests_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sampled_requests_enabled Wafv2RuleGroup#sampled_requests_enabled}.
        '''
        value = Wafv2RuleGroupVisibilityConfig(
            cloudwatch_metrics_enabled=cloudwatch_metrics_enabled,
            metric_name=metric_name,
            sampled_requests_enabled=sampled_requests_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putVisibilityConfig", [value]))

    @jsii.member(jsii_name="resetCustomResponseBody")
    def reset_custom_response_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomResponseBody", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="customResponseBody")
    def custom_response_body(self) -> "Wafv2RuleGroupCustomResponseBodyList":
        return typing.cast("Wafv2RuleGroupCustomResponseBodyList", jsii.get(self, "customResponseBody"))

    @builtins.property
    @jsii.member(jsii_name="lockToken")
    def lock_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lockToken"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "Wafv2RuleGroupRuleList":
        return typing.cast("Wafv2RuleGroupRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="visibilityConfig")
    def visibility_config(self) -> "Wafv2RuleGroupVisibilityConfigOutputReference":
        return typing.cast("Wafv2RuleGroupVisibilityConfigOutputReference", jsii.get(self, "visibilityConfig"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="customResponseBodyInput")
    def custom_response_body_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupCustomResponseBody"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupCustomResponseBody"]]], jsii.get(self, "customResponseBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityConfigInput")
    def visibility_config_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupVisibilityConfig"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupVisibilityConfig"], jsii.get(self, "visibilityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroup, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroup, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroup, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroup, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "capacity": "capacity",
        "name": "name",
        "scope": "scope",
        "visibility_config": "visibilityConfig",
        "custom_response_body": "customResponseBody",
        "description": "description",
        "id": "id",
        "rule": "rule",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class Wafv2RuleGroupConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        capacity: jsii.Number,
        name: builtins.str,
        scope: builtins.str,
        visibility_config: typing.Union["Wafv2RuleGroupVisibilityConfig", typing.Dict[str, typing.Any]],
        custom_response_body: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupCustomResponseBody", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRule", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#capacity Wafv2RuleGroup#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#scope Wafv2RuleGroup#scope}.
        :param visibility_config: visibility_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#visibility_config Wafv2RuleGroup#visibility_config}
        :param custom_response_body: custom_response_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response_body Wafv2RuleGroup#custom_response_body}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#description Wafv2RuleGroup#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#id Wafv2RuleGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#rule Wafv2RuleGroup#rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#tags Wafv2RuleGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#tags_all Wafv2RuleGroup#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(visibility_config, dict):
            visibility_config = Wafv2RuleGroupVisibilityConfig(**visibility_config)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument visibility_config", value=visibility_config, expected_type=type_hints["visibility_config"])
            check_type(argname="argument custom_response_body", value=custom_response_body, expected_type=type_hints["custom_response_body"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "name": name,
            "scope": scope,
            "visibility_config": visibility_config,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if custom_response_body is not None:
            self._values["custom_response_body"] = custom_response_body
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if rule is not None:
            self._values["rule"] = rule
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#capacity Wafv2RuleGroup#capacity}.'''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#scope Wafv2RuleGroup#scope}.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def visibility_config(self) -> "Wafv2RuleGroupVisibilityConfig":
        '''visibility_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#visibility_config Wafv2RuleGroup#visibility_config}
        '''
        result = self._values.get("visibility_config")
        assert result is not None, "Required property 'visibility_config' is missing"
        return typing.cast("Wafv2RuleGroupVisibilityConfig", result)

    @builtins.property
    def custom_response_body(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupCustomResponseBody"]]]:
        '''custom_response_body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response_body Wafv2RuleGroup#custom_response_body}
        '''
        result = self._values.get("custom_response_body")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupCustomResponseBody"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#description Wafv2RuleGroup#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#id Wafv2RuleGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#rule Wafv2RuleGroup#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRule"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#tags Wafv2RuleGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#tags_all Wafv2RuleGroup#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupCustomResponseBody",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "content_type": "contentType", "key": "key"},
)
class Wafv2RuleGroupCustomResponseBody:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        key: builtins.str,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#content Wafv2RuleGroup#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#content_type Wafv2RuleGroup#content_type}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#key Wafv2RuleGroup#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupCustomResponseBody.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
            "key": key,
        }

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#content Wafv2RuleGroup#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#content_type Wafv2RuleGroup#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#key Wafv2RuleGroup#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupCustomResponseBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupCustomResponseBodyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupCustomResponseBodyList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupCustomResponseBodyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupCustomResponseBodyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupCustomResponseBodyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupCustomResponseBodyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupCustomResponseBody]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupCustomResponseBody]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupCustomResponseBody]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupCustomResponseBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupCustomResponseBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupCustomResponseBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupCustomResponseBody, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupCustomResponseBody, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupCustomResponseBody, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupCustomResponseBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "name": "name",
        "priority": "priority",
        "statement": "statement",
        "visibility_config": "visibilityConfig",
        "rule_label": "ruleLabel",
    },
)
class Wafv2RuleGroupRule:
    def __init__(
        self,
        *,
        action: typing.Union["Wafv2RuleGroupRuleAction", typing.Dict[str, typing.Any]],
        name: builtins.str,
        priority: jsii.Number,
        statement: typing.Union["Wafv2RuleGroupRuleStatement", typing.Dict[str, typing.Any]],
        visibility_config: typing.Union["Wafv2RuleGroupRuleVisibilityConfig", typing.Dict[str, typing.Any]],
        rule_label: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleRuleLabel", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#action Wafv2RuleGroup#action}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.
        :param statement: statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        :param visibility_config: visibility_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#visibility_config Wafv2RuleGroup#visibility_config}
        :param rule_label: rule_label block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#rule_label Wafv2RuleGroup#rule_label}
        '''
        if isinstance(action, dict):
            action = Wafv2RuleGroupRuleAction(**action)
        if isinstance(statement, dict):
            statement = Wafv2RuleGroupRuleStatement(**statement)
        if isinstance(visibility_config, dict):
            visibility_config = Wafv2RuleGroupRuleVisibilityConfig(**visibility_config)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
            check_type(argname="argument visibility_config", value=visibility_config, expected_type=type_hints["visibility_config"])
            check_type(argname="argument rule_label", value=rule_label, expected_type=type_hints["rule_label"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
            "priority": priority,
            "statement": statement,
            "visibility_config": visibility_config,
        }
        if rule_label is not None:
            self._values["rule_label"] = rule_label

    @builtins.property
    def action(self) -> "Wafv2RuleGroupRuleAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#action Wafv2RuleGroup#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("Wafv2RuleGroupRuleAction", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def statement(self) -> "Wafv2RuleGroupRuleStatement":
        '''statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        result = self._values.get("statement")
        assert result is not None, "Required property 'statement' is missing"
        return typing.cast("Wafv2RuleGroupRuleStatement", result)

    @builtins.property
    def visibility_config(self) -> "Wafv2RuleGroupRuleVisibilityConfig":
        '''visibility_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#visibility_config Wafv2RuleGroup#visibility_config}
        '''
        result = self._values.get("visibility_config")
        assert result is not None, "Required property 'visibility_config' is missing"
        return typing.cast("Wafv2RuleGroupRuleVisibilityConfig", result)

    @builtins.property
    def rule_label(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleRuleLabel"]]]:
        '''rule_label block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#rule_label Wafv2RuleGroup#rule_label}
        '''
        result = self._values.get("rule_label")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleRuleLabel"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleAction",
    jsii_struct_bases=[],
    name_mapping={"allow": "allow", "block": "block", "count": "count"},
)
class Wafv2RuleGroupRuleAction:
    def __init__(
        self,
        *,
        allow: typing.Optional[typing.Union["Wafv2RuleGroupRuleActionAllow", typing.Dict[str, typing.Any]]] = None,
        block: typing.Optional[typing.Union["Wafv2RuleGroupRuleActionBlock", typing.Dict[str, typing.Any]]] = None,
        count: typing.Optional[typing.Union["Wafv2RuleGroupRuleActionCount", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#allow Wafv2RuleGroup#allow}
        :param block: block block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#block Wafv2RuleGroup#block}
        :param count: count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#count Wafv2RuleGroup#count}
        '''
        if isinstance(allow, dict):
            allow = Wafv2RuleGroupRuleActionAllow(**allow)
        if isinstance(block, dict):
            block = Wafv2RuleGroupRuleActionBlock(**block)
        if isinstance(count, dict):
            count = Wafv2RuleGroupRuleActionCount(**count)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleAction.__init__)
            check_type(argname="argument allow", value=allow, expected_type=type_hints["allow"])
            check_type(argname="argument block", value=block, expected_type=type_hints["block"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow is not None:
            self._values["allow"] = allow
        if block is not None:
            self._values["block"] = block
        if count is not None:
            self._values["count"] = count

    @builtins.property
    def allow(self) -> typing.Optional["Wafv2RuleGroupRuleActionAllow"]:
        '''allow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#allow Wafv2RuleGroup#allow}
        '''
        result = self._values.get("allow")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleActionAllow"], result)

    @builtins.property
    def block(self) -> typing.Optional["Wafv2RuleGroupRuleActionBlock"]:
        '''block block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#block Wafv2RuleGroup#block}
        '''
        result = self._values.get("block")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleActionBlock"], result)

    @builtins.property
    def count(self) -> typing.Optional["Wafv2RuleGroupRuleActionCount"]:
        '''count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#count Wafv2RuleGroup#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleActionCount"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionAllow",
    jsii_struct_bases=[],
    name_mapping={"custom_request_handling": "customRequestHandling"},
)
class Wafv2RuleGroupRuleActionAllow:
    def __init__(
        self,
        *,
        custom_request_handling: typing.Optional[typing.Union["Wafv2RuleGroupRuleActionAllowCustomRequestHandling", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_request_handling: custom_request_handling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_request_handling Wafv2RuleGroup#custom_request_handling}
        '''
        if isinstance(custom_request_handling, dict):
            custom_request_handling = Wafv2RuleGroupRuleActionAllowCustomRequestHandling(**custom_request_handling)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllow.__init__)
            check_type(argname="argument custom_request_handling", value=custom_request_handling, expected_type=type_hints["custom_request_handling"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_request_handling is not None:
            self._values["custom_request_handling"] = custom_request_handling

    @builtins.property
    def custom_request_handling(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleActionAllowCustomRequestHandling"]:
        '''custom_request_handling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_request_handling Wafv2RuleGroup#custom_request_handling}
        '''
        result = self._values.get("custom_request_handling")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleActionAllowCustomRequestHandling"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionAllow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionAllowCustomRequestHandling",
    jsii_struct_bases=[],
    name_mapping={"insert_header": "insertHeader"},
)
class Wafv2RuleGroupRuleActionAllowCustomRequestHandling:
    def __init__(
        self,
        *,
        insert_header: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param insert_header: insert_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#insert_header Wafv2RuleGroup#insert_header}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowCustomRequestHandling.__init__)
            check_type(argname="argument insert_header", value=insert_header, expected_type=type_hints["insert_header"])
        self._values: typing.Dict[str, typing.Any] = {
            "insert_header": insert_header,
        }

    @builtins.property
    def insert_header(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader"]]:
        '''insert_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#insert_header Wafv2RuleGroup#insert_header}
        '''
        result = self._values.get("insert_header")
        assert result is not None, "Required property 'insert_header' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionAllowCustomRequestHandling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#value Wafv2RuleGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#value Wafv2RuleGroup#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInsertHeader")
    def put_insert_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference.put_insert_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInsertHeader", [value]))

    @builtins.property
    @jsii.member(jsii_name="insertHeader")
    def insert_header(
        self,
    ) -> Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList:
        return typing.cast(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList, jsii.get(self, "insertHeader"))

    @builtins.property
    @jsii.member(jsii_name="insertHeaderInput")
    def insert_header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader]]], jsii.get(self, "insertHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleActionAllowCustomRequestHandling]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionAllowCustomRequestHandling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleActionAllowCustomRequestHandling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionAllowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionAllowOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionAllowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomRequestHandling")
    def put_custom_request_handling(
        self,
        *,
        insert_header: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param insert_header: insert_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#insert_header Wafv2RuleGroup#insert_header}
        '''
        value = Wafv2RuleGroupRuleActionAllowCustomRequestHandling(
            insert_header=insert_header
        )

        return typing.cast(None, jsii.invoke(self, "putCustomRequestHandling", [value]))

    @jsii.member(jsii_name="resetCustomRequestHandling")
    def reset_custom_request_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRequestHandling", []))

    @builtins.property
    @jsii.member(jsii_name="customRequestHandling")
    def custom_request_handling(
        self,
    ) -> Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference:
        return typing.cast(Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference, jsii.get(self, "customRequestHandling"))

    @builtins.property
    @jsii.member(jsii_name="customRequestHandlingInput")
    def custom_request_handling_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleActionAllowCustomRequestHandling]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionAllowCustomRequestHandling], jsii.get(self, "customRequestHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupRuleActionAllow]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionAllow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleActionAllow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionAllowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionBlock",
    jsii_struct_bases=[],
    name_mapping={"custom_response": "customResponse"},
)
class Wafv2RuleGroupRuleActionBlock:
    def __init__(
        self,
        *,
        custom_response: typing.Optional[typing.Union["Wafv2RuleGroupRuleActionBlockCustomResponse", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_response: custom_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response Wafv2RuleGroup#custom_response}
        '''
        if isinstance(custom_response, dict):
            custom_response = Wafv2RuleGroupRuleActionBlockCustomResponse(**custom_response)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlock.__init__)
            check_type(argname="argument custom_response", value=custom_response, expected_type=type_hints["custom_response"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_response is not None:
            self._values["custom_response"] = custom_response

    @builtins.property
    def custom_response(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleActionBlockCustomResponse"]:
        '''custom_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response Wafv2RuleGroup#custom_response}
        '''
        result = self._values.get("custom_response")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleActionBlockCustomResponse"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionBlock(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionBlockCustomResponse",
    jsii_struct_bases=[],
    name_mapping={
        "response_code": "responseCode",
        "custom_response_body_key": "customResponseBodyKey",
        "response_header": "responseHeader",
    },
)
class Wafv2RuleGroupRuleActionBlockCustomResponse:
    def __init__(
        self,
        *,
        response_code: jsii.Number,
        custom_response_body_key: typing.Optional[builtins.str] = None,
        response_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param response_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#response_code Wafv2RuleGroup#response_code}.
        :param custom_response_body_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response_body_key Wafv2RuleGroup#custom_response_body_key}.
        :param response_header: response_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#response_header Wafv2RuleGroup#response_header}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockCustomResponse.__init__)
            check_type(argname="argument response_code", value=response_code, expected_type=type_hints["response_code"])
            check_type(argname="argument custom_response_body_key", value=custom_response_body_key, expected_type=type_hints["custom_response_body_key"])
            check_type(argname="argument response_header", value=response_header, expected_type=type_hints["response_header"])
        self._values: typing.Dict[str, typing.Any] = {
            "response_code": response_code,
        }
        if custom_response_body_key is not None:
            self._values["custom_response_body_key"] = custom_response_body_key
        if response_header is not None:
            self._values["response_header"] = response_header

    @builtins.property
    def response_code(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#response_code Wafv2RuleGroup#response_code}.'''
        result = self._values.get("response_code")
        assert result is not None, "Required property 'response_code' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def custom_response_body_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response_body_key Wafv2RuleGroup#custom_response_body_key}.'''
        result = self._values.get("custom_response_body_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader"]]]:
        '''response_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#response_header Wafv2RuleGroup#response_header}
        '''
        result = self._values.get("response_header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionBlockCustomResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putResponseHeader")
    def put_response_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference.put_response_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeader", [value]))

    @jsii.member(jsii_name="resetCustomResponseBodyKey")
    def reset_custom_response_body_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomResponseBodyKey", []))

    @jsii.member(jsii_name="resetResponseHeader")
    def reset_response_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeader", []))

    @builtins.property
    @jsii.member(jsii_name="responseHeader")
    def response_header(
        self,
    ) -> "Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList":
        return typing.cast("Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList", jsii.get(self, "responseHeader"))

    @builtins.property
    @jsii.member(jsii_name="customResponseBodyKeyInput")
    def custom_response_body_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customResponseBodyKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCodeInput")
    def response_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "responseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeaderInput")
    def response_header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader"]]], jsii.get(self, "responseHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="customResponseBodyKey")
    def custom_response_body_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customResponseBodyKey"))

    @custom_response_body_key.setter
    def custom_response_body_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference, "custom_response_body_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customResponseBodyKey", value)

    @builtins.property
    @jsii.member(jsii_name="responseCode")
    def response_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "responseCode"))

    @response_code.setter
    def response_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference, "response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleActionBlockCustomResponse]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionBlockCustomResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleActionBlockCustomResponse],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#value Wafv2RuleGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#value Wafv2RuleGroup#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionBlockOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionBlockOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionBlockOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomResponse")
    def put_custom_response(
        self,
        *,
        response_code: jsii.Number,
        custom_response_body_key: typing.Optional[builtins.str] = None,
        response_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param response_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#response_code Wafv2RuleGroup#response_code}.
        :param custom_response_body_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response_body_key Wafv2RuleGroup#custom_response_body_key}.
        :param response_header: response_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#response_header Wafv2RuleGroup#response_header}
        '''
        value = Wafv2RuleGroupRuleActionBlockCustomResponse(
            response_code=response_code,
            custom_response_body_key=custom_response_body_key,
            response_header=response_header,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomResponse", [value]))

    @jsii.member(jsii_name="resetCustomResponse")
    def reset_custom_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomResponse", []))

    @builtins.property
    @jsii.member(jsii_name="customResponse")
    def custom_response(
        self,
    ) -> Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference:
        return typing.cast(Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference, jsii.get(self, "customResponse"))

    @builtins.property
    @jsii.member(jsii_name="customResponseInput")
    def custom_response_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleActionBlockCustomResponse]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionBlockCustomResponse], jsii.get(self, "customResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupRuleActionBlock]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionBlock], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleActionBlock],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionBlockOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionCount",
    jsii_struct_bases=[],
    name_mapping={"custom_request_handling": "customRequestHandling"},
)
class Wafv2RuleGroupRuleActionCount:
    def __init__(
        self,
        *,
        custom_request_handling: typing.Optional[typing.Union["Wafv2RuleGroupRuleActionCountCustomRequestHandling", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_request_handling: custom_request_handling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_request_handling Wafv2RuleGroup#custom_request_handling}
        '''
        if isinstance(custom_request_handling, dict):
            custom_request_handling = Wafv2RuleGroupRuleActionCountCustomRequestHandling(**custom_request_handling)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCount.__init__)
            check_type(argname="argument custom_request_handling", value=custom_request_handling, expected_type=type_hints["custom_request_handling"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_request_handling is not None:
            self._values["custom_request_handling"] = custom_request_handling

    @builtins.property
    def custom_request_handling(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleActionCountCustomRequestHandling"]:
        '''custom_request_handling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_request_handling Wafv2RuleGroup#custom_request_handling}
        '''
        result = self._values.get("custom_request_handling")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleActionCountCustomRequestHandling"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionCountCustomRequestHandling",
    jsii_struct_bases=[],
    name_mapping={"insert_header": "insertHeader"},
)
class Wafv2RuleGroupRuleActionCountCustomRequestHandling:
    def __init__(
        self,
        *,
        insert_header: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param insert_header: insert_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#insert_header Wafv2RuleGroup#insert_header}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountCustomRequestHandling.__init__)
            check_type(argname="argument insert_header", value=insert_header, expected_type=type_hints["insert_header"])
        self._values: typing.Dict[str, typing.Any] = {
            "insert_header": insert_header,
        }

    @builtins.property
    def insert_header(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader"]]:
        '''insert_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#insert_header Wafv2RuleGroup#insert_header}
        '''
        result = self._values.get("insert_header")
        assert result is not None, "Required property 'insert_header' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionCountCustomRequestHandling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#value Wafv2RuleGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#value Wafv2RuleGroup#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInsertHeader")
    def put_insert_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference.put_insert_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInsertHeader", [value]))

    @builtins.property
    @jsii.member(jsii_name="insertHeader")
    def insert_header(
        self,
    ) -> Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList:
        return typing.cast(Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList, jsii.get(self, "insertHeader"))

    @builtins.property
    @jsii.member(jsii_name="insertHeaderInput")
    def insert_header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader]]], jsii.get(self, "insertHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleActionCountCustomRequestHandling]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionCountCustomRequestHandling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleActionCountCustomRequestHandling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionCountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionCountOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionCountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomRequestHandling")
    def put_custom_request_handling(
        self,
        *,
        insert_header: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param insert_header: insert_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#insert_header Wafv2RuleGroup#insert_header}
        '''
        value = Wafv2RuleGroupRuleActionCountCustomRequestHandling(
            insert_header=insert_header
        )

        return typing.cast(None, jsii.invoke(self, "putCustomRequestHandling", [value]))

    @jsii.member(jsii_name="resetCustomRequestHandling")
    def reset_custom_request_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRequestHandling", []))

    @builtins.property
    @jsii.member(jsii_name="customRequestHandling")
    def custom_request_handling(
        self,
    ) -> Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference:
        return typing.cast(Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference, jsii.get(self, "customRequestHandling"))

    @builtins.property
    @jsii.member(jsii_name="customRequestHandlingInput")
    def custom_request_handling_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleActionCountCustomRequestHandling]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionCountCustomRequestHandling], jsii.get(self, "customRequestHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupRuleActionCount]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleActionCount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionCountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleActionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllow")
    def put_allow(
        self,
        *,
        custom_request_handling: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionAllowCustomRequestHandling, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_request_handling: custom_request_handling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_request_handling Wafv2RuleGroup#custom_request_handling}
        '''
        value = Wafv2RuleGroupRuleActionAllow(
            custom_request_handling=custom_request_handling
        )

        return typing.cast(None, jsii.invoke(self, "putAllow", [value]))

    @jsii.member(jsii_name="putBlock")
    def put_block(
        self,
        *,
        custom_response: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionBlockCustomResponse, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_response: custom_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_response Wafv2RuleGroup#custom_response}
        '''
        value = Wafv2RuleGroupRuleActionBlock(custom_response=custom_response)

        return typing.cast(None, jsii.invoke(self, "putBlock", [value]))

    @jsii.member(jsii_name="putCount")
    def put_count(
        self,
        *,
        custom_request_handling: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionCountCustomRequestHandling, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_request_handling: custom_request_handling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#custom_request_handling Wafv2RuleGroup#custom_request_handling}
        '''
        value = Wafv2RuleGroupRuleActionCount(
            custom_request_handling=custom_request_handling
        )

        return typing.cast(None, jsii.invoke(self, "putCount", [value]))

    @jsii.member(jsii_name="resetAllow")
    def reset_allow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllow", []))

    @jsii.member(jsii_name="resetBlock")
    def reset_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlock", []))

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @builtins.property
    @jsii.member(jsii_name="allow")
    def allow(self) -> Wafv2RuleGroupRuleActionAllowOutputReference:
        return typing.cast(Wafv2RuleGroupRuleActionAllowOutputReference, jsii.get(self, "allow"))

    @builtins.property
    @jsii.member(jsii_name="block")
    def block(self) -> Wafv2RuleGroupRuleActionBlockOutputReference:
        return typing.cast(Wafv2RuleGroupRuleActionBlockOutputReference, jsii.get(self, "block"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> Wafv2RuleGroupRuleActionCountOutputReference:
        return typing.cast(Wafv2RuleGroupRuleActionCountOutputReference, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="allowInput")
    def allow_input(self) -> typing.Optional[Wafv2RuleGroupRuleActionAllow]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionAllow], jsii.get(self, "allowInput"))

    @builtins.property
    @jsii.member(jsii_name="blockInput")
    def block_input(self) -> typing.Optional[Wafv2RuleGroupRuleActionBlock]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionBlock], jsii.get(self, "blockInput"))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[Wafv2RuleGroupRuleActionCount]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleActionCount], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupRuleAction]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[Wafv2RuleGroupRuleAction]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "Wafv2RuleGroupRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        allow: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionAllow, typing.Dict[str, typing.Any]]] = None,
        block: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionBlock, typing.Dict[str, typing.Any]]] = None,
        count: typing.Optional[typing.Union[Wafv2RuleGroupRuleActionCount, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#allow Wafv2RuleGroup#allow}
        :param block: block block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#block Wafv2RuleGroup#block}
        :param count: count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#count Wafv2RuleGroup#count}
        '''
        value = Wafv2RuleGroupRuleAction(allow=allow, block=block, count=count)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putRuleLabel")
    def put_rule_label(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleRuleLabel", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleOutputReference.put_rule_label)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRuleLabel", [value]))

    @jsii.member(jsii_name="putStatement")
    def put_statement(
        self,
        *,
        and_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementAndStatement", typing.Dict[str, typing.Any]]] = None,
        byte_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatement", typing.Dict[str, typing.Any]]] = None,
        geo_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementGeoMatchStatement", typing.Dict[str, typing.Any]]] = None,
        ip_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementIpSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        label_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementLabelMatchStatement", typing.Dict[str, typing.Any]]] = None,
        not_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementNotStatement", typing.Dict[str, typing.Any]]] = None,
        or_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementOrStatement", typing.Dict[str, typing.Any]]] = None,
        regex_pattern_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        size_constraint_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatement", typing.Dict[str, typing.Any]]] = None,
        sqli_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatement", typing.Dict[str, typing.Any]]] = None,
        xss_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatement", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_statement: and_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#and_statement Wafv2RuleGroup#and_statement}
        :param byte_match_statement: byte_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#byte_match_statement Wafv2RuleGroup#byte_match_statement}
        :param geo_match_statement: geo_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#geo_match_statement Wafv2RuleGroup#geo_match_statement}
        :param ip_set_reference_statement: ip_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_reference_statement Wafv2RuleGroup#ip_set_reference_statement}
        :param label_match_statement: label_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#label_match_statement Wafv2RuleGroup#label_match_statement}
        :param not_statement: not_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#not_statement Wafv2RuleGroup#not_statement}
        :param or_statement: or_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#or_statement Wafv2RuleGroup#or_statement}
        :param regex_pattern_set_reference_statement: regex_pattern_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#regex_pattern_set_reference_statement Wafv2RuleGroup#regex_pattern_set_reference_statement}
        :param size_constraint_statement: size_constraint_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size_constraint_statement Wafv2RuleGroup#size_constraint_statement}
        :param sqli_match_statement: sqli_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sqli_match_statement Wafv2RuleGroup#sqli_match_statement}
        :param xss_match_statement: xss_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#xss_match_statement Wafv2RuleGroup#xss_match_statement}
        '''
        value = Wafv2RuleGroupRuleStatement(
            and_statement=and_statement,
            byte_match_statement=byte_match_statement,
            geo_match_statement=geo_match_statement,
            ip_set_reference_statement=ip_set_reference_statement,
            label_match_statement=label_match_statement,
            not_statement=not_statement,
            or_statement=or_statement,
            regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
            size_constraint_statement=size_constraint_statement,
            sqli_match_statement=sqli_match_statement,
            xss_match_statement=xss_match_statement,
        )

        return typing.cast(None, jsii.invoke(self, "putStatement", [value]))

    @jsii.member(jsii_name="putVisibilityConfig")
    def put_visibility_config(
        self,
        *,
        cloudwatch_metrics_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        metric_name: builtins.str,
        sampled_requests_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param cloudwatch_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cloudwatch_metrics_enabled Wafv2RuleGroup#cloudwatch_metrics_enabled}.
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#metric_name Wafv2RuleGroup#metric_name}.
        :param sampled_requests_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sampled_requests_enabled Wafv2RuleGroup#sampled_requests_enabled}.
        '''
        value = Wafv2RuleGroupRuleVisibilityConfig(
            cloudwatch_metrics_enabled=cloudwatch_metrics_enabled,
            metric_name=metric_name,
            sampled_requests_enabled=sampled_requests_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putVisibilityConfig", [value]))

    @jsii.member(jsii_name="resetRuleLabel")
    def reset_rule_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleLabel", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> Wafv2RuleGroupRuleActionOutputReference:
        return typing.cast(Wafv2RuleGroupRuleActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="ruleLabel")
    def rule_label(self) -> "Wafv2RuleGroupRuleRuleLabelList":
        return typing.cast("Wafv2RuleGroupRuleRuleLabelList", jsii.get(self, "ruleLabel"))

    @builtins.property
    @jsii.member(jsii_name="statement")
    def statement(self) -> "Wafv2RuleGroupRuleStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementOutputReference", jsii.get(self, "statement"))

    @builtins.property
    @jsii.member(jsii_name="visibilityConfig")
    def visibility_config(self) -> "Wafv2RuleGroupRuleVisibilityConfigOutputReference":
        return typing.cast("Wafv2RuleGroupRuleVisibilityConfigOutputReference", jsii.get(self, "visibilityConfig"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[Wafv2RuleGroupRuleAction]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleLabelInput")
    def rule_label_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleRuleLabel"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleRuleLabel"]]], jsii.get(self, "ruleLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="statementInput")
    def statement_input(self) -> typing.Optional["Wafv2RuleGroupRuleStatement"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatement"], jsii.get(self, "statementInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityConfigInput")
    def visibility_config_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleVisibilityConfig"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleVisibilityConfig"], jsii.get(self, "visibilityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleRuleLabel",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleRuleLabel:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleRuleLabel.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleRuleLabel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleRuleLabelList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleRuleLabelList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleRuleLabelList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "Wafv2RuleGroupRuleRuleLabelOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleRuleLabelList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleRuleLabelOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleRuleLabelList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleRuleLabelList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleRuleLabelList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleRuleLabel]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleRuleLabel]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleRuleLabel]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleRuleLabelList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleRuleLabelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleRuleLabelOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleRuleLabelOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleRuleLabelOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleRuleLabel, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleRuleLabel, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleRuleLabel, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleRuleLabelOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatement",
    jsii_struct_bases=[],
    name_mapping={
        "and_statement": "andStatement",
        "byte_match_statement": "byteMatchStatement",
        "geo_match_statement": "geoMatchStatement",
        "ip_set_reference_statement": "ipSetReferenceStatement",
        "label_match_statement": "labelMatchStatement",
        "not_statement": "notStatement",
        "or_statement": "orStatement",
        "regex_pattern_set_reference_statement": "regexPatternSetReferenceStatement",
        "size_constraint_statement": "sizeConstraintStatement",
        "sqli_match_statement": "sqliMatchStatement",
        "xss_match_statement": "xssMatchStatement",
    },
)
class Wafv2RuleGroupRuleStatement:
    def __init__(
        self,
        *,
        and_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementAndStatement", typing.Dict[str, typing.Any]]] = None,
        byte_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatement", typing.Dict[str, typing.Any]]] = None,
        geo_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementGeoMatchStatement", typing.Dict[str, typing.Any]]] = None,
        ip_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementIpSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        label_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementLabelMatchStatement", typing.Dict[str, typing.Any]]] = None,
        not_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementNotStatement", typing.Dict[str, typing.Any]]] = None,
        or_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementOrStatement", typing.Dict[str, typing.Any]]] = None,
        regex_pattern_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        size_constraint_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatement", typing.Dict[str, typing.Any]]] = None,
        sqli_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatement", typing.Dict[str, typing.Any]]] = None,
        xss_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatement", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_statement: and_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#and_statement Wafv2RuleGroup#and_statement}
        :param byte_match_statement: byte_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#byte_match_statement Wafv2RuleGroup#byte_match_statement}
        :param geo_match_statement: geo_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#geo_match_statement Wafv2RuleGroup#geo_match_statement}
        :param ip_set_reference_statement: ip_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_reference_statement Wafv2RuleGroup#ip_set_reference_statement}
        :param label_match_statement: label_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#label_match_statement Wafv2RuleGroup#label_match_statement}
        :param not_statement: not_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#not_statement Wafv2RuleGroup#not_statement}
        :param or_statement: or_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#or_statement Wafv2RuleGroup#or_statement}
        :param regex_pattern_set_reference_statement: regex_pattern_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#regex_pattern_set_reference_statement Wafv2RuleGroup#regex_pattern_set_reference_statement}
        :param size_constraint_statement: size_constraint_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size_constraint_statement Wafv2RuleGroup#size_constraint_statement}
        :param sqli_match_statement: sqli_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sqli_match_statement Wafv2RuleGroup#sqli_match_statement}
        :param xss_match_statement: xss_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#xss_match_statement Wafv2RuleGroup#xss_match_statement}
        '''
        if isinstance(and_statement, dict):
            and_statement = Wafv2RuleGroupRuleStatementAndStatement(**and_statement)
        if isinstance(byte_match_statement, dict):
            byte_match_statement = Wafv2RuleGroupRuleStatementByteMatchStatement(**byte_match_statement)
        if isinstance(geo_match_statement, dict):
            geo_match_statement = Wafv2RuleGroupRuleStatementGeoMatchStatement(**geo_match_statement)
        if isinstance(ip_set_reference_statement, dict):
            ip_set_reference_statement = Wafv2RuleGroupRuleStatementIpSetReferenceStatement(**ip_set_reference_statement)
        if isinstance(label_match_statement, dict):
            label_match_statement = Wafv2RuleGroupRuleStatementLabelMatchStatement(**label_match_statement)
        if isinstance(not_statement, dict):
            not_statement = Wafv2RuleGroupRuleStatementNotStatement(**not_statement)
        if isinstance(or_statement, dict):
            or_statement = Wafv2RuleGroupRuleStatementOrStatement(**or_statement)
        if isinstance(regex_pattern_set_reference_statement, dict):
            regex_pattern_set_reference_statement = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement(**regex_pattern_set_reference_statement)
        if isinstance(size_constraint_statement, dict):
            size_constraint_statement = Wafv2RuleGroupRuleStatementSizeConstraintStatement(**size_constraint_statement)
        if isinstance(sqli_match_statement, dict):
            sqli_match_statement = Wafv2RuleGroupRuleStatementSqliMatchStatement(**sqli_match_statement)
        if isinstance(xss_match_statement, dict):
            xss_match_statement = Wafv2RuleGroupRuleStatementXssMatchStatement(**xss_match_statement)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatement.__init__)
            check_type(argname="argument and_statement", value=and_statement, expected_type=type_hints["and_statement"])
            check_type(argname="argument byte_match_statement", value=byte_match_statement, expected_type=type_hints["byte_match_statement"])
            check_type(argname="argument geo_match_statement", value=geo_match_statement, expected_type=type_hints["geo_match_statement"])
            check_type(argname="argument ip_set_reference_statement", value=ip_set_reference_statement, expected_type=type_hints["ip_set_reference_statement"])
            check_type(argname="argument label_match_statement", value=label_match_statement, expected_type=type_hints["label_match_statement"])
            check_type(argname="argument not_statement", value=not_statement, expected_type=type_hints["not_statement"])
            check_type(argname="argument or_statement", value=or_statement, expected_type=type_hints["or_statement"])
            check_type(argname="argument regex_pattern_set_reference_statement", value=regex_pattern_set_reference_statement, expected_type=type_hints["regex_pattern_set_reference_statement"])
            check_type(argname="argument size_constraint_statement", value=size_constraint_statement, expected_type=type_hints["size_constraint_statement"])
            check_type(argname="argument sqli_match_statement", value=sqli_match_statement, expected_type=type_hints["sqli_match_statement"])
            check_type(argname="argument xss_match_statement", value=xss_match_statement, expected_type=type_hints["xss_match_statement"])
        self._values: typing.Dict[str, typing.Any] = {}
        if and_statement is not None:
            self._values["and_statement"] = and_statement
        if byte_match_statement is not None:
            self._values["byte_match_statement"] = byte_match_statement
        if geo_match_statement is not None:
            self._values["geo_match_statement"] = geo_match_statement
        if ip_set_reference_statement is not None:
            self._values["ip_set_reference_statement"] = ip_set_reference_statement
        if label_match_statement is not None:
            self._values["label_match_statement"] = label_match_statement
        if not_statement is not None:
            self._values["not_statement"] = not_statement
        if or_statement is not None:
            self._values["or_statement"] = or_statement
        if regex_pattern_set_reference_statement is not None:
            self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
        if size_constraint_statement is not None:
            self._values["size_constraint_statement"] = size_constraint_statement
        if sqli_match_statement is not None:
            self._values["sqli_match_statement"] = sqli_match_statement
        if xss_match_statement is not None:
            self._values["xss_match_statement"] = xss_match_statement

    @builtins.property
    def and_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementAndStatement"]:
        '''and_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#and_statement Wafv2RuleGroup#and_statement}
        '''
        result = self._values.get("and_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementAndStatement"], result)

    @builtins.property
    def byte_match_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatement"]:
        '''byte_match_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#byte_match_statement Wafv2RuleGroup#byte_match_statement}
        '''
        result = self._values.get("byte_match_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatement"], result)

    @builtins.property
    def geo_match_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementGeoMatchStatement"]:
        '''geo_match_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#geo_match_statement Wafv2RuleGroup#geo_match_statement}
        '''
        result = self._values.get("geo_match_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementGeoMatchStatement"], result)

    @builtins.property
    def ip_set_reference_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementIpSetReferenceStatement"]:
        '''ip_set_reference_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_reference_statement Wafv2RuleGroup#ip_set_reference_statement}
        '''
        result = self._values.get("ip_set_reference_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementIpSetReferenceStatement"], result)

    @builtins.property
    def label_match_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementLabelMatchStatement"]:
        '''label_match_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#label_match_statement Wafv2RuleGroup#label_match_statement}
        '''
        result = self._values.get("label_match_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementLabelMatchStatement"], result)

    @builtins.property
    def not_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementNotStatement"]:
        '''not_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#not_statement Wafv2RuleGroup#not_statement}
        '''
        result = self._values.get("not_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementNotStatement"], result)

    @builtins.property
    def or_statement(self) -> typing.Optional["Wafv2RuleGroupRuleStatementOrStatement"]:
        '''or_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#or_statement Wafv2RuleGroup#or_statement}
        '''
        result = self._values.get("or_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementOrStatement"], result)

    @builtins.property
    def regex_pattern_set_reference_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement"]:
        '''regex_pattern_set_reference_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#regex_pattern_set_reference_statement Wafv2RuleGroup#regex_pattern_set_reference_statement}
        '''
        result = self._values.get("regex_pattern_set_reference_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement"], result)

    @builtins.property
    def size_constraint_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatement"]:
        '''size_constraint_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size_constraint_statement Wafv2RuleGroup#size_constraint_statement}
        '''
        result = self._values.get("size_constraint_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatement"], result)

    @builtins.property
    def sqli_match_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatement"]:
        '''sqli_match_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sqli_match_statement Wafv2RuleGroup#sqli_match_statement}
        '''
        result = self._values.get("sqli_match_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatement"], result)

    @builtins.property
    def xss_match_statement(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatement"]:
        '''xss_match_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#xss_match_statement Wafv2RuleGroup#xss_match_statement}
        '''
        result = self._values.get("xss_match_statement")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatement"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementAndStatement",
    jsii_struct_bases=[],
    name_mapping={"statement": "statement"},
)
class Wafv2RuleGroupRuleStatementAndStatement:
    def __init__(
        self,
        *,
        statement: typing.Union[Wafv2RuleGroupRuleStatement, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param statement: statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        if isinstance(statement, dict):
            statement = Wafv2RuleGroupRuleStatement(**statement)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementAndStatement.__init__)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        self._values: typing.Dict[str, typing.Any] = {
            "statement": statement,
        }

    @builtins.property
    def statement(self) -> Wafv2RuleGroupRuleStatement:
        '''statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        result = self._values.get("statement")
        assert result is not None, "Required property 'statement' is missing"
        return typing.cast(Wafv2RuleGroupRuleStatement, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementAndStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementAndStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementAndStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementAndStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStatement")
    def put_statement(
        self,
        *,
        and_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementAndStatement, typing.Dict[str, typing.Any]]] = None,
        byte_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatement", typing.Dict[str, typing.Any]]] = None,
        geo_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementGeoMatchStatement", typing.Dict[str, typing.Any]]] = None,
        ip_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementIpSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        label_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementLabelMatchStatement", typing.Dict[str, typing.Any]]] = None,
        not_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementNotStatement", typing.Dict[str, typing.Any]]] = None,
        or_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementOrStatement", typing.Dict[str, typing.Any]]] = None,
        regex_pattern_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        size_constraint_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatement", typing.Dict[str, typing.Any]]] = None,
        sqli_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatement", typing.Dict[str, typing.Any]]] = None,
        xss_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatement", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_statement: and_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#and_statement Wafv2RuleGroup#and_statement}
        :param byte_match_statement: byte_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#byte_match_statement Wafv2RuleGroup#byte_match_statement}
        :param geo_match_statement: geo_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#geo_match_statement Wafv2RuleGroup#geo_match_statement}
        :param ip_set_reference_statement: ip_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_reference_statement Wafv2RuleGroup#ip_set_reference_statement}
        :param label_match_statement: label_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#label_match_statement Wafv2RuleGroup#label_match_statement}
        :param not_statement: not_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#not_statement Wafv2RuleGroup#not_statement}
        :param or_statement: or_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#or_statement Wafv2RuleGroup#or_statement}
        :param regex_pattern_set_reference_statement: regex_pattern_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#regex_pattern_set_reference_statement Wafv2RuleGroup#regex_pattern_set_reference_statement}
        :param size_constraint_statement: size_constraint_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size_constraint_statement Wafv2RuleGroup#size_constraint_statement}
        :param sqli_match_statement: sqli_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sqli_match_statement Wafv2RuleGroup#sqli_match_statement}
        :param xss_match_statement: xss_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#xss_match_statement Wafv2RuleGroup#xss_match_statement}
        '''
        value = Wafv2RuleGroupRuleStatement(
            and_statement=and_statement,
            byte_match_statement=byte_match_statement,
            geo_match_statement=geo_match_statement,
            ip_set_reference_statement=ip_set_reference_statement,
            label_match_statement=label_match_statement,
            not_statement=not_statement,
            or_statement=or_statement,
            regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
            size_constraint_statement=size_constraint_statement,
            sqli_match_statement=sqli_match_statement,
            xss_match_statement=xss_match_statement,
        )

        return typing.cast(None, jsii.invoke(self, "putStatement", [value]))

    @builtins.property
    @jsii.member(jsii_name="statement")
    def statement(self) -> "Wafv2RuleGroupRuleStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementOutputReference", jsii.get(self, "statement"))

    @builtins.property
    @jsii.member(jsii_name="statementInput")
    def statement_input(self) -> typing.Optional[Wafv2RuleGroupRuleStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatement], jsii.get(self, "statementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementAndStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementAndStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementAndStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementAndStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatement",
    jsii_struct_bases=[],
    name_mapping={
        "positional_constraint": "positionalConstraint",
        "search_string": "searchString",
        "text_transformation": "textTransformation",
        "field_to_match": "fieldToMatch",
    },
)
class Wafv2RuleGroupRuleStatementByteMatchStatement:
    def __init__(
        self,
        *,
        positional_constraint: builtins.str,
        search_string: builtins.str,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param positional_constraint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#positional_constraint Wafv2RuleGroup#positional_constraint}.
        :param search_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#search_string Wafv2RuleGroup#search_string}.
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        if isinstance(field_to_match, dict):
            field_to_match = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch(**field_to_match)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatement.__init__)
            check_type(argname="argument positional_constraint", value=positional_constraint, expected_type=type_hints["positional_constraint"])
            check_type(argname="argument search_string", value=search_string, expected_type=type_hints["search_string"])
            check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "positional_constraint": positional_constraint,
            "search_string": search_string,
            "text_transformation": text_transformation,
        }
        if field_to_match is not None:
            self._values["field_to_match"] = field_to_match

    @builtins.property
    def positional_constraint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#positional_constraint Wafv2RuleGroup#positional_constraint}.'''
        result = self._values.get("positional_constraint")
        assert result is not None, "Required property 'positional_constraint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def search_string(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#search_string Wafv2RuleGroup#search_string}.'''
        result = self._values.get("search_string")
        assert result is not None, "Required property 'search_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_transformation(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation"]]:
        '''text_transformation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        '''
        result = self._values.get("text_transformation")
        assert result is not None, "Required property 'text_transformation' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation"]], result)

    @builtins.property
    def field_to_match(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch"]:
        '''field_to_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        result = self._values.get("field_to_match")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch",
    jsii_struct_bases=[],
    name_mapping={
        "all_query_arguments": "allQueryArguments",
        "body": "body",
        "cookies": "cookies",
        "json_body": "jsonBody",
        "method": "method",
        "query_string": "queryString",
        "single_header": "singleHeader",
        "single_query_argument": "singleQueryArgument",
        "uri_path": "uriPath",
    },
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch:
    def __init__(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody", typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies", typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody", typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString", typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader", typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument", typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        if isinstance(all_query_arguments, dict):
            all_query_arguments = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments(**all_query_arguments)
        if isinstance(body, dict):
            body = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody(**body)
        if isinstance(cookies, dict):
            cookies = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies(**cookies)
        if isinstance(json_body, dict):
            json_body = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody(**json_body)
        if isinstance(method, dict):
            method = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod(**method)
        if isinstance(query_string, dict):
            query_string = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString(**query_string)
        if isinstance(single_header, dict):
            single_header = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader(**single_header)
        if isinstance(single_query_argument, dict):
            single_query_argument = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument(**single_query_argument)
        if isinstance(uri_path, dict):
            uri_path = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath(**uri_path)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch.__init__)
            check_type(argname="argument all_query_arguments", value=all_query_arguments, expected_type=type_hints["all_query_arguments"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
            check_type(argname="argument json_body", value=json_body, expected_type=type_hints["json_body"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
            check_type(argname="argument single_query_argument", value=single_query_argument, expected_type=type_hints["single_query_argument"])
            check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all_query_arguments is not None:
            self._values["all_query_arguments"] = all_query_arguments
        if body is not None:
            self._values["body"] = body
        if cookies is not None:
            self._values["cookies"] = cookies
        if json_body is not None:
            self._values["json_body"] = json_body
        if method is not None:
            self._values["method"] = method
        if query_string is not None:
            self._values["query_string"] = query_string
        if single_header is not None:
            self._values["single_header"] = single_header
        if single_query_argument is not None:
            self._values["single_query_argument"] = single_query_argument
        if uri_path is not None:
            self._values["uri_path"] = uri_path

    @builtins.property
    def all_query_arguments(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments"]:
        '''all_query_arguments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        '''
        result = self._values.get("all_query_arguments")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments"], result)

    @builtins.property
    def body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody"]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody"], result)

    @builtins.property
    def cookies(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies"]:
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        '''
        result = self._values.get("cookies")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies"], result)

    @builtins.property
    def json_body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody"]:
        '''json_body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        '''
        result = self._values.get("json_body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody"], result)

    @builtins.property
    def method(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod"]:
        '''method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString"]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString"], result)

    @builtins.property
    def single_header(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader"]:
        '''single_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        '''
        result = self._values.get("single_header")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader"], result)

    @builtins.property
    def single_query_argument(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument"]:
        '''single_query_argument block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        '''
        result = self._values.get("single_query_argument")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument"], result)

    @builtins.property
    def uri_path(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath"]:
        '''uri_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        result = self._values.get("uri_path")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArgumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArgumentsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArgumentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArgumentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies:
    def __init__(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern", typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
            "oversize_handling": oversize_handling,
        }

    @builtins.property
    def match_pattern(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern"]]:
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern"]], result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oversize_handling(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        assert result is not None, "Required property 'oversize_handling' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "excluded_cookies": "excludedCookies",
        "included_cookies": "includedCookies",
    },
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        excluded_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
        included_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param excluded_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.
        :param included_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument excluded_cookies", value=excluded_cookies, expected_type=type_hints["excluded_cookies"])
            check_type(argname="argument included_cookies", value=included_cookies, expected_type=type_hints["included_cookies"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if excluded_cookies is not None:
            self._values["excluded_cookies"] = excluded_cookies
        if included_cookies is not None:
            self._values["included_cookies"] = included_cookies

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll"], result)

    @builtins.property
    def excluded_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.'''
        result = self._values.get("excluded_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def included_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.'''
        result = self._values.get("included_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetExcludedCookies")
    def reset_excluded_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedCookies", []))

    @jsii.member(jsii_name="resetIncludedCookies")
    def reset_included_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedCookies", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookiesInput")
    def excluded_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="includedCookiesInput")
    def included_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookies")
    def excluded_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedCookies"))

    @excluded_cookies.setter
    def excluded_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "excluded_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="includedCookies")
    def included_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedCookies"))

    @included_cookies.setter
    def included_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "included_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference.put_match_pattern)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "invalid_fallback_behavior": "invalidFallbackBehavior",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody:
    def __init__(
        self,
        *,
        match_pattern: typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern", typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if isinstance(match_pattern, dict):
            match_pattern = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(**match_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument invalid_fallback_behavior", value=invalid_fallback_behavior, expected_type=type_hints["invalid_fallback_behavior"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
        }
        if invalid_fallback_behavior is not None:
            self._values["invalid_fallback_behavior"] = invalid_fallback_behavior
        if oversize_handling is not None:
            self._values["oversize_handling"] = oversize_handling

    @builtins.property
    def match_pattern(
        self,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern":
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern", result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invalid_fallback_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.'''
        result = self._values.get("invalid_fallback_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oversize_handling(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "included_paths": "includedPaths"},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument included_paths", value=included_paths, expected_type=type_hints["included_paths"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if included_paths is not None:
            self._values["included_paths"] = included_paths

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll"], result)

    @builtins.property
    def included_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.'''
        result = self._values.get("included_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetIncludedPaths")
    def reset_included_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedPaths", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPathsInput")
    def included_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPaths")
    def included_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedPaths"))

    @included_paths.setter
    def included_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, "included_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedPaths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        *,
        all: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll, typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(
            all=all, included_paths=included_paths
        )

        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @jsii.member(jsii_name="resetInvalidFallbackBehavior")
    def reset_invalid_fallback_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvalidFallbackBehavior", []))

    @jsii.member(jsii_name="resetOversizeHandling")
    def reset_oversize_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOversizeHandling", []))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehaviorInput")
    def invalid_fallback_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invalidFallbackBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invalidFallbackBehavior"))

    @invalid_fallback_behavior.setter
    def invalid_fallback_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference, "invalid_fallback_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invalidFallbackBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethodOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllQueryArguments")
    def put_all_query_arguments(self) -> None:
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments()

        return typing.cast(None, jsii.invoke(self, "putAllQueryArguments", [value]))

    @jsii.member(jsii_name="putBody")
    def put_body(self) -> None:
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody()

        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies(
            match_pattern=match_pattern,
            match_scope=match_scope,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="putJsonBody")
    def put_json_body(
        self,
        *,
        match_pattern: typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern, typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody(
            match_pattern=match_pattern,
            match_scope=match_scope,
            invalid_fallback_behavior=invalid_fallback_behavior,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putJsonBody", [value]))

    @jsii.member(jsii_name="putMethod")
    def put_method(self) -> None:
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod()

        return typing.cast(None, jsii.invoke(self, "putMethod", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(self) -> None:
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString()

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSingleHeader")
    def put_single_header(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleHeader", [value]))

    @jsii.member(jsii_name="putSingleQueryArgument")
    def put_single_query_argument(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleQueryArgument", [value]))

    @jsii.member(jsii_name="putUriPath")
    def put_uri_path(self) -> None:
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath()

        return typing.cast(None, jsii.invoke(self, "putUriPath", [value]))

    @jsii.member(jsii_name="resetAllQueryArguments")
    def reset_all_query_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllQueryArguments", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCookies")
    def reset_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookies", []))

    @jsii.member(jsii_name="resetJsonBody")
    def reset_json_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonBody", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSingleHeader")
    def reset_single_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleHeader", []))

    @jsii.member(jsii_name="resetSingleQueryArgument")
    def reset_single_query_argument(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleQueryArgument", []))

    @jsii.member(jsii_name="resetUriPath")
    def reset_uri_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUriPath", []))

    @builtins.property
    @jsii.member(jsii_name="allQueryArguments")
    def all_query_arguments(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArgumentsOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArgumentsOutputReference, jsii.get(self, "allQueryArguments"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBodyOutputReference, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="jsonBody")
    def json_body(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference, jsii.get(self, "jsonBody"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethodOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethodOutputReference, jsii.get(self, "method"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryStringOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="singleHeader")
    def single_header(
        self,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference", jsii.get(self, "singleHeader"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgument")
    def single_query_argument(
        self,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference", jsii.get(self, "singleQueryArgument"))

    @builtins.property
    @jsii.member(jsii_name="uriPath")
    def uri_path(
        self,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPathOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPathOutputReference", jsii.get(self, "uriPath"))

    @builtins.property
    @jsii.member(jsii_name="allQueryArgumentsInput")
    def all_query_arguments_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments], jsii.get(self, "allQueryArgumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonBodyInput")
    def json_body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody], jsii.get(self, "jsonBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="singleHeaderInput")
    def single_header_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader"], jsii.get(self, "singleHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgumentInput")
    def single_query_argument_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument"], jsii.get(self, "singleQueryArgumentInput"))

    @builtins.property
    @jsii.member(jsii_name="uriPathInput")
    def uri_path_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath"], jsii.get(self, "uriPathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPathOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFieldToMatch")
    def put_field_to_match(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments, typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody, typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies, typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody, typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod, typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString, typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader, typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument, typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        value = Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch(
            all_query_arguments=all_query_arguments,
            body=body,
            cookies=cookies,
            json_body=json_body,
            method=method,
            query_string=query_string,
            single_header=single_header,
            single_query_argument=single_query_argument,
            uri_path=uri_path,
        )

        return typing.cast(None, jsii.invoke(self, "putFieldToMatch", [value]))

    @jsii.member(jsii_name="putTextTransformation")
    def put_text_transformation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference.put_text_transformation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTextTransformation", [value]))

    @jsii.member(jsii_name="resetFieldToMatch")
    def reset_field_to_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldToMatch", []))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatch")
    def field_to_match(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchOutputReference, jsii.get(self, "fieldToMatch"))

    @builtins.property
    @jsii.member(jsii_name="textTransformation")
    def text_transformation(
        self,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList":
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList", jsii.get(self, "textTransformation"))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatchInput")
    def field_to_match_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch], jsii.get(self, "fieldToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="positionalConstraintInput")
    def positional_constraint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "positionalConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="searchStringInput")
    def search_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchStringInput"))

    @builtins.property
    @jsii.member(jsii_name="textTransformationInput")
    def text_transformation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation"]]], jsii.get(self, "textTransformationInput"))

    @builtins.property
    @jsii.member(jsii_name="positionalConstraint")
    def positional_constraint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "positionalConstraint"))

    @positional_constraint.setter
    def positional_constraint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference, "positional_constraint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "positionalConstraint", value)

    @builtins.property
    @jsii.member(jsii_name="searchString")
    def search_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "searchString"))

    @search_string.setter
    def search_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference, "search_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchString", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation",
    jsii_struct_bases=[],
    name_mapping={"priority": "priority", "type": "type"},
)
class Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation:
    def __init__(self, *, priority: jsii.Number, type: builtins.str) -> None:
        '''
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation.__init__)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "type": type,
        }

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementGeoMatchStatement",
    jsii_struct_bases=[],
    name_mapping={
        "country_codes": "countryCodes",
        "forwarded_ip_config": "forwardedIpConfig",
    },
)
class Wafv2RuleGroupRuleStatementGeoMatchStatement:
    def __init__(
        self,
        *,
        country_codes: typing.Sequence[builtins.str],
        forwarded_ip_config: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param country_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#country_codes Wafv2RuleGroup#country_codes}.
        :param forwarded_ip_config: forwarded_ip_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#forwarded_ip_config Wafv2RuleGroup#forwarded_ip_config}
        '''
        if isinstance(forwarded_ip_config, dict):
            forwarded_ip_config = Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig(**forwarded_ip_config)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementGeoMatchStatement.__init__)
            check_type(argname="argument country_codes", value=country_codes, expected_type=type_hints["country_codes"])
            check_type(argname="argument forwarded_ip_config", value=forwarded_ip_config, expected_type=type_hints["forwarded_ip_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "country_codes": country_codes,
        }
        if forwarded_ip_config is not None:
            self._values["forwarded_ip_config"] = forwarded_ip_config

    @builtins.property
    def country_codes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#country_codes Wafv2RuleGroup#country_codes}.'''
        result = self._values.get("country_codes")
        assert result is not None, "Required property 'country_codes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def forwarded_ip_config(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig"]:
        '''forwarded_ip_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#forwarded_ip_config Wafv2RuleGroup#forwarded_ip_config}
        '''
        result = self._values.get("forwarded_ip_config")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementGeoMatchStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig",
    jsii_struct_bases=[],
    name_mapping={
        "fallback_behavior": "fallbackBehavior",
        "header_name": "headerName",
    },
)
class Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig:
    def __init__(
        self,
        *,
        fallback_behavior: builtins.str,
        header_name: builtins.str,
    ) -> None:
        '''
        :param fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#fallback_behavior Wafv2RuleGroup#fallback_behavior}.
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#header_name Wafv2RuleGroup#header_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig.__init__)
            check_type(argname="argument fallback_behavior", value=fallback_behavior, expected_type=type_hints["fallback_behavior"])
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "fallback_behavior": fallback_behavior,
            "header_name": header_name,
        }

    @builtins.property
    def fallback_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#fallback_behavior Wafv2RuleGroup#fallback_behavior}.'''
        result = self._values.get("fallback_behavior")
        assert result is not None, "Required property 'fallback_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#header_name Wafv2RuleGroup#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fallbackBehaviorInput")
    def fallback_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fallbackBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fallbackBehavior")
    def fallback_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fallbackBehavior"))

    @fallback_behavior.setter
    def fallback_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference, "fallback_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putForwardedIpConfig")
    def put_forwarded_ip_config(
        self,
        *,
        fallback_behavior: builtins.str,
        header_name: builtins.str,
    ) -> None:
        '''
        :param fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#fallback_behavior Wafv2RuleGroup#fallback_behavior}.
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#header_name Wafv2RuleGroup#header_name}.
        '''
        value = Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig(
            fallback_behavior=fallback_behavior, header_name=header_name
        )

        return typing.cast(None, jsii.invoke(self, "putForwardedIpConfig", [value]))

    @jsii.member(jsii_name="resetForwardedIpConfig")
    def reset_forwarded_ip_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardedIpConfig", []))

    @builtins.property
    @jsii.member(jsii_name="forwardedIpConfig")
    def forwarded_ip_config(
        self,
    ) -> Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference, jsii.get(self, "forwardedIpConfig"))

    @builtins.property
    @jsii.member(jsii_name="countryCodesInput")
    def country_codes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "countryCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardedIpConfigInput")
    def forwarded_ip_config_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig], jsii.get(self, "forwardedIpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodes")
    def country_codes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "countryCodes"))

    @country_codes.setter
    def country_codes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference, "country_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCodes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementIpSetReferenceStatement",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "ip_set_forwarded_ip_config": "ipSetForwardedIpConfig",
    },
)
class Wafv2RuleGroupRuleStatementIpSetReferenceStatement:
    def __init__(
        self,
        *,
        arn: builtins.str,
        ip_set_forwarded_ip_config: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#arn Wafv2RuleGroup#arn}.
        :param ip_set_forwarded_ip_config: ip_set_forwarded_ip_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_forwarded_ip_config Wafv2RuleGroup#ip_set_forwarded_ip_config}
        '''
        if isinstance(ip_set_forwarded_ip_config, dict):
            ip_set_forwarded_ip_config = Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig(**ip_set_forwarded_ip_config)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementIpSetReferenceStatement.__init__)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument ip_set_forwarded_ip_config", value=ip_set_forwarded_ip_config, expected_type=type_hints["ip_set_forwarded_ip_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
        }
        if ip_set_forwarded_ip_config is not None:
            self._values["ip_set_forwarded_ip_config"] = ip_set_forwarded_ip_config

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#arn Wafv2RuleGroup#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_set_forwarded_ip_config(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig"]:
        '''ip_set_forwarded_ip_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_forwarded_ip_config Wafv2RuleGroup#ip_set_forwarded_ip_config}
        '''
        result = self._values.get("ip_set_forwarded_ip_config")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementIpSetReferenceStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig",
    jsii_struct_bases=[],
    name_mapping={
        "fallback_behavior": "fallbackBehavior",
        "header_name": "headerName",
        "position": "position",
    },
)
class Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig:
    def __init__(
        self,
        *,
        fallback_behavior: builtins.str,
        header_name: builtins.str,
        position: builtins.str,
    ) -> None:
        '''
        :param fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#fallback_behavior Wafv2RuleGroup#fallback_behavior}.
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#header_name Wafv2RuleGroup#header_name}.
        :param position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#position Wafv2RuleGroup#position}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig.__init__)
            check_type(argname="argument fallback_behavior", value=fallback_behavior, expected_type=type_hints["fallback_behavior"])
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
        self._values: typing.Dict[str, typing.Any] = {
            "fallback_behavior": fallback_behavior,
            "header_name": header_name,
            "position": position,
        }

    @builtins.property
    def fallback_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#fallback_behavior Wafv2RuleGroup#fallback_behavior}.'''
        result = self._values.get("fallback_behavior")
        assert result is not None, "Required property 'fallback_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#header_name Wafv2RuleGroup#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def position(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#position Wafv2RuleGroup#position}.'''
        result = self._values.get("position")
        assert result is not None, "Required property 'position' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fallbackBehaviorInput")
    def fallback_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fallbackBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "positionInput"))

    @builtins.property
    @jsii.member(jsii_name="fallbackBehavior")
    def fallback_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fallbackBehavior"))

    @fallback_behavior.setter
    def fallback_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference, "fallback_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "position"))

    @position.setter
    def position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference, "position").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIpSetForwardedIpConfig")
    def put_ip_set_forwarded_ip_config(
        self,
        *,
        fallback_behavior: builtins.str,
        header_name: builtins.str,
        position: builtins.str,
    ) -> None:
        '''
        :param fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#fallback_behavior Wafv2RuleGroup#fallback_behavior}.
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#header_name Wafv2RuleGroup#header_name}.
        :param position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#position Wafv2RuleGroup#position}.
        '''
        value = Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig(
            fallback_behavior=fallback_behavior,
            header_name=header_name,
            position=position,
        )

        return typing.cast(None, jsii.invoke(self, "putIpSetForwardedIpConfig", [value]))

    @jsii.member(jsii_name="resetIpSetForwardedIpConfig")
    def reset_ip_set_forwarded_ip_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpSetForwardedIpConfig", []))

    @builtins.property
    @jsii.member(jsii_name="ipSetForwardedIpConfig")
    def ip_set_forwarded_ip_config(
        self,
    ) -> Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference, jsii.get(self, "ipSetForwardedIpConfig"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="ipSetForwardedIpConfigInput")
    def ip_set_forwarded_ip_config_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig], jsii.get(self, "ipSetForwardedIpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference, "arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementLabelMatchStatement",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "scope": "scope"},
)
class Wafv2RuleGroupRuleStatementLabelMatchStatement:
    def __init__(self, *, key: builtins.str, scope: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#key Wafv2RuleGroup#key}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#scope Wafv2RuleGroup#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementLabelMatchStatement.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "scope": scope,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#key Wafv2RuleGroup#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#scope Wafv2RuleGroup#scope}.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementLabelMatchStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementLabelMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementLabelMatchStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementLabelMatchStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementNotStatement",
    jsii_struct_bases=[],
    name_mapping={"statement": "statement"},
)
class Wafv2RuleGroupRuleStatementNotStatement:
    def __init__(
        self,
        *,
        statement: typing.Union[Wafv2RuleGroupRuleStatement, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param statement: statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        if isinstance(statement, dict):
            statement = Wafv2RuleGroupRuleStatement(**statement)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementNotStatement.__init__)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        self._values: typing.Dict[str, typing.Any] = {
            "statement": statement,
        }

    @builtins.property
    def statement(self) -> Wafv2RuleGroupRuleStatement:
        '''statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        result = self._values.get("statement")
        assert result is not None, "Required property 'statement' is missing"
        return typing.cast(Wafv2RuleGroupRuleStatement, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementNotStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementNotStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementNotStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementNotStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStatement")
    def put_statement(
        self,
        *,
        and_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementAndStatement, typing.Dict[str, typing.Any]]] = None,
        byte_match_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatement, typing.Dict[str, typing.Any]]] = None,
        geo_match_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementGeoMatchStatement, typing.Dict[str, typing.Any]]] = None,
        ip_set_reference_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementIpSetReferenceStatement, typing.Dict[str, typing.Any]]] = None,
        label_match_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementLabelMatchStatement, typing.Dict[str, typing.Any]]] = None,
        not_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementNotStatement, typing.Dict[str, typing.Any]]] = None,
        or_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementOrStatement", typing.Dict[str, typing.Any]]] = None,
        regex_pattern_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        size_constraint_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatement", typing.Dict[str, typing.Any]]] = None,
        sqli_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatement", typing.Dict[str, typing.Any]]] = None,
        xss_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatement", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_statement: and_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#and_statement Wafv2RuleGroup#and_statement}
        :param byte_match_statement: byte_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#byte_match_statement Wafv2RuleGroup#byte_match_statement}
        :param geo_match_statement: geo_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#geo_match_statement Wafv2RuleGroup#geo_match_statement}
        :param ip_set_reference_statement: ip_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_reference_statement Wafv2RuleGroup#ip_set_reference_statement}
        :param label_match_statement: label_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#label_match_statement Wafv2RuleGroup#label_match_statement}
        :param not_statement: not_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#not_statement Wafv2RuleGroup#not_statement}
        :param or_statement: or_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#or_statement Wafv2RuleGroup#or_statement}
        :param regex_pattern_set_reference_statement: regex_pattern_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#regex_pattern_set_reference_statement Wafv2RuleGroup#regex_pattern_set_reference_statement}
        :param size_constraint_statement: size_constraint_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size_constraint_statement Wafv2RuleGroup#size_constraint_statement}
        :param sqli_match_statement: sqli_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sqli_match_statement Wafv2RuleGroup#sqli_match_statement}
        :param xss_match_statement: xss_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#xss_match_statement Wafv2RuleGroup#xss_match_statement}
        '''
        value = Wafv2RuleGroupRuleStatement(
            and_statement=and_statement,
            byte_match_statement=byte_match_statement,
            geo_match_statement=geo_match_statement,
            ip_set_reference_statement=ip_set_reference_statement,
            label_match_statement=label_match_statement,
            not_statement=not_statement,
            or_statement=or_statement,
            regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
            size_constraint_statement=size_constraint_statement,
            sqli_match_statement=sqli_match_statement,
            xss_match_statement=xss_match_statement,
        )

        return typing.cast(None, jsii.invoke(self, "putStatement", [value]))

    @builtins.property
    @jsii.member(jsii_name="statement")
    def statement(self) -> "Wafv2RuleGroupRuleStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementOutputReference", jsii.get(self, "statement"))

    @builtins.property
    @jsii.member(jsii_name="statementInput")
    def statement_input(self) -> typing.Optional[Wafv2RuleGroupRuleStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatement], jsii.get(self, "statementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementNotStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementNotStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementNotStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementNotStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementOrStatement",
    jsii_struct_bases=[],
    name_mapping={"statement": "statement"},
)
class Wafv2RuleGroupRuleStatementOrStatement:
    def __init__(
        self,
        *,
        statement: typing.Union[Wafv2RuleGroupRuleStatement, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param statement: statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        if isinstance(statement, dict):
            statement = Wafv2RuleGroupRuleStatement(**statement)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementOrStatement.__init__)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        self._values: typing.Dict[str, typing.Any] = {
            "statement": statement,
        }

    @builtins.property
    def statement(self) -> Wafv2RuleGroupRuleStatement:
        '''statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        result = self._values.get("statement")
        assert result is not None, "Required property 'statement' is missing"
        return typing.cast(Wafv2RuleGroupRuleStatement, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementOrStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementOrStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementOrStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementOrStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStatement")
    def put_statement(
        self,
        *,
        and_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementAndStatement, typing.Dict[str, typing.Any]]] = None,
        byte_match_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatement, typing.Dict[str, typing.Any]]] = None,
        geo_match_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementGeoMatchStatement, typing.Dict[str, typing.Any]]] = None,
        ip_set_reference_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementIpSetReferenceStatement, typing.Dict[str, typing.Any]]] = None,
        label_match_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementLabelMatchStatement, typing.Dict[str, typing.Any]]] = None,
        not_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementNotStatement, typing.Dict[str, typing.Any]]] = None,
        or_statement: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementOrStatement, typing.Dict[str, typing.Any]]] = None,
        regex_pattern_set_reference_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement", typing.Dict[str, typing.Any]]] = None,
        size_constraint_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatement", typing.Dict[str, typing.Any]]] = None,
        sqli_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatement", typing.Dict[str, typing.Any]]] = None,
        xss_match_statement: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatement", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_statement: and_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#and_statement Wafv2RuleGroup#and_statement}
        :param byte_match_statement: byte_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#byte_match_statement Wafv2RuleGroup#byte_match_statement}
        :param geo_match_statement: geo_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#geo_match_statement Wafv2RuleGroup#geo_match_statement}
        :param ip_set_reference_statement: ip_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_reference_statement Wafv2RuleGroup#ip_set_reference_statement}
        :param label_match_statement: label_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#label_match_statement Wafv2RuleGroup#label_match_statement}
        :param not_statement: not_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#not_statement Wafv2RuleGroup#not_statement}
        :param or_statement: or_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#or_statement Wafv2RuleGroup#or_statement}
        :param regex_pattern_set_reference_statement: regex_pattern_set_reference_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#regex_pattern_set_reference_statement Wafv2RuleGroup#regex_pattern_set_reference_statement}
        :param size_constraint_statement: size_constraint_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size_constraint_statement Wafv2RuleGroup#size_constraint_statement}
        :param sqli_match_statement: sqli_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sqli_match_statement Wafv2RuleGroup#sqli_match_statement}
        :param xss_match_statement: xss_match_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#xss_match_statement Wafv2RuleGroup#xss_match_statement}
        '''
        value = Wafv2RuleGroupRuleStatement(
            and_statement=and_statement,
            byte_match_statement=byte_match_statement,
            geo_match_statement=geo_match_statement,
            ip_set_reference_statement=ip_set_reference_statement,
            label_match_statement=label_match_statement,
            not_statement=not_statement,
            or_statement=or_statement,
            regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
            size_constraint_statement=size_constraint_statement,
            sqli_match_statement=sqli_match_statement,
            xss_match_statement=xss_match_statement,
        )

        return typing.cast(None, jsii.invoke(self, "putStatement", [value]))

    @builtins.property
    @jsii.member(jsii_name="statement")
    def statement(self) -> "Wafv2RuleGroupRuleStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementOutputReference", jsii.get(self, "statement"))

    @builtins.property
    @jsii.member(jsii_name="statementInput")
    def statement_input(self) -> typing.Optional[Wafv2RuleGroupRuleStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatement], jsii.get(self, "statementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupRuleStatementOrStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementOrStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementOrStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementOrStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAndStatement")
    def put_and_statement(
        self,
        *,
        statement: typing.Union[Wafv2RuleGroupRuleStatement, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param statement: statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        value = Wafv2RuleGroupRuleStatementAndStatement(statement=statement)

        return typing.cast(None, jsii.invoke(self, "putAndStatement", [value]))

    @jsii.member(jsii_name="putByteMatchStatement")
    def put_byte_match_statement(
        self,
        *,
        positional_constraint: builtins.str,
        search_string: builtins.str,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation, typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param positional_constraint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#positional_constraint Wafv2RuleGroup#positional_constraint}.
        :param search_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#search_string Wafv2RuleGroup#search_string}.
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        value = Wafv2RuleGroupRuleStatementByteMatchStatement(
            positional_constraint=positional_constraint,
            search_string=search_string,
            text_transformation=text_transformation,
            field_to_match=field_to_match,
        )

        return typing.cast(None, jsii.invoke(self, "putByteMatchStatement", [value]))

    @jsii.member(jsii_name="putGeoMatchStatement")
    def put_geo_match_statement(
        self,
        *,
        country_codes: typing.Sequence[builtins.str],
        forwarded_ip_config: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param country_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#country_codes Wafv2RuleGroup#country_codes}.
        :param forwarded_ip_config: forwarded_ip_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#forwarded_ip_config Wafv2RuleGroup#forwarded_ip_config}
        '''
        value = Wafv2RuleGroupRuleStatementGeoMatchStatement(
            country_codes=country_codes, forwarded_ip_config=forwarded_ip_config
        )

        return typing.cast(None, jsii.invoke(self, "putGeoMatchStatement", [value]))

    @jsii.member(jsii_name="putIpSetReferenceStatement")
    def put_ip_set_reference_statement(
        self,
        *,
        arn: builtins.str,
        ip_set_forwarded_ip_config: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#arn Wafv2RuleGroup#arn}.
        :param ip_set_forwarded_ip_config: ip_set_forwarded_ip_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#ip_set_forwarded_ip_config Wafv2RuleGroup#ip_set_forwarded_ip_config}
        '''
        value = Wafv2RuleGroupRuleStatementIpSetReferenceStatement(
            arn=arn, ip_set_forwarded_ip_config=ip_set_forwarded_ip_config
        )

        return typing.cast(None, jsii.invoke(self, "putIpSetReferenceStatement", [value]))

    @jsii.member(jsii_name="putLabelMatchStatement")
    def put_label_match_statement(
        self,
        *,
        key: builtins.str,
        scope: builtins.str,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#key Wafv2RuleGroup#key}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#scope Wafv2RuleGroup#scope}.
        '''
        value = Wafv2RuleGroupRuleStatementLabelMatchStatement(key=key, scope=scope)

        return typing.cast(None, jsii.invoke(self, "putLabelMatchStatement", [value]))

    @jsii.member(jsii_name="putNotStatement")
    def put_not_statement(
        self,
        *,
        statement: typing.Union[Wafv2RuleGroupRuleStatement, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param statement: statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        value = Wafv2RuleGroupRuleStatementNotStatement(statement=statement)

        return typing.cast(None, jsii.invoke(self, "putNotStatement", [value]))

    @jsii.member(jsii_name="putOrStatement")
    def put_or_statement(
        self,
        *,
        statement: typing.Union[Wafv2RuleGroupRuleStatement, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param statement: statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#statement Wafv2RuleGroup#statement}
        '''
        value = Wafv2RuleGroupRuleStatementOrStatement(statement=statement)

        return typing.cast(None, jsii.invoke(self, "putOrStatement", [value]))

    @jsii.member(jsii_name="putRegexPatternSetReferenceStatement")
    def put_regex_pattern_set_reference_statement(
        self,
        *,
        arn: builtins.str,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#arn Wafv2RuleGroup#arn}.
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement(
            arn=arn,
            text_transformation=text_transformation,
            field_to_match=field_to_match,
        )

        return typing.cast(None, jsii.invoke(self, "putRegexPatternSetReferenceStatement", [value]))

    @jsii.member(jsii_name="putSizeConstraintStatement")
    def put_size_constraint_statement(
        self,
        *,
        comparison_operator: builtins.str,
        size: jsii.Number,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param comparison_operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#comparison_operator Wafv2RuleGroup#comparison_operator}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size Wafv2RuleGroup#size}.
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatement(
            comparison_operator=comparison_operator,
            size=size,
            text_transformation=text_transformation,
            field_to_match=field_to_match,
        )

        return typing.cast(None, jsii.invoke(self, "putSizeConstraintStatement", [value]))

    @jsii.member(jsii_name="putSqliMatchStatement")
    def put_sqli_match_statement(
        self,
        *,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        value = Wafv2RuleGroupRuleStatementSqliMatchStatement(
            text_transformation=text_transformation, field_to_match=field_to_match
        )

        return typing.cast(None, jsii.invoke(self, "putSqliMatchStatement", [value]))

    @jsii.member(jsii_name="putXssMatchStatement")
    def put_xss_match_statement(
        self,
        *,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        value = Wafv2RuleGroupRuleStatementXssMatchStatement(
            text_transformation=text_transformation, field_to_match=field_to_match
        )

        return typing.cast(None, jsii.invoke(self, "putXssMatchStatement", [value]))

    @jsii.member(jsii_name="resetAndStatement")
    def reset_and_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAndStatement", []))

    @jsii.member(jsii_name="resetByteMatchStatement")
    def reset_byte_match_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetByteMatchStatement", []))

    @jsii.member(jsii_name="resetGeoMatchStatement")
    def reset_geo_match_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoMatchStatement", []))

    @jsii.member(jsii_name="resetIpSetReferenceStatement")
    def reset_ip_set_reference_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpSetReferenceStatement", []))

    @jsii.member(jsii_name="resetLabelMatchStatement")
    def reset_label_match_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelMatchStatement", []))

    @jsii.member(jsii_name="resetNotStatement")
    def reset_not_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotStatement", []))

    @jsii.member(jsii_name="resetOrStatement")
    def reset_or_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrStatement", []))

    @jsii.member(jsii_name="resetRegexPatternSetReferenceStatement")
    def reset_regex_pattern_set_reference_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexPatternSetReferenceStatement", []))

    @jsii.member(jsii_name="resetSizeConstraintStatement")
    def reset_size_constraint_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeConstraintStatement", []))

    @jsii.member(jsii_name="resetSqliMatchStatement")
    def reset_sqli_match_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqliMatchStatement", []))

    @jsii.member(jsii_name="resetXssMatchStatement")
    def reset_xss_match_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXssMatchStatement", []))

    @builtins.property
    @jsii.member(jsii_name="andStatement")
    def and_statement(self) -> Wafv2RuleGroupRuleStatementAndStatementOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementAndStatementOutputReference, jsii.get(self, "andStatement"))

    @builtins.property
    @jsii.member(jsii_name="byteMatchStatement")
    def byte_match_statement(
        self,
    ) -> Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference, jsii.get(self, "byteMatchStatement"))

    @builtins.property
    @jsii.member(jsii_name="geoMatchStatement")
    def geo_match_statement(
        self,
    ) -> Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference, jsii.get(self, "geoMatchStatement"))

    @builtins.property
    @jsii.member(jsii_name="ipSetReferenceStatement")
    def ip_set_reference_statement(
        self,
    ) -> Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference, jsii.get(self, "ipSetReferenceStatement"))

    @builtins.property
    @jsii.member(jsii_name="labelMatchStatement")
    def label_match_statement(
        self,
    ) -> Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference, jsii.get(self, "labelMatchStatement"))

    @builtins.property
    @jsii.member(jsii_name="notStatement")
    def not_statement(self) -> Wafv2RuleGroupRuleStatementNotStatementOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementNotStatementOutputReference, jsii.get(self, "notStatement"))

    @builtins.property
    @jsii.member(jsii_name="orStatement")
    def or_statement(self) -> Wafv2RuleGroupRuleStatementOrStatementOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementOrStatementOutputReference, jsii.get(self, "orStatement"))

    @builtins.property
    @jsii.member(jsii_name="regexPatternSetReferenceStatement")
    def regex_pattern_set_reference_statement(
        self,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference", jsii.get(self, "regexPatternSetReferenceStatement"))

    @builtins.property
    @jsii.member(jsii_name="sizeConstraintStatement")
    def size_constraint_statement(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference", jsii.get(self, "sizeConstraintStatement"))

    @builtins.property
    @jsii.member(jsii_name="sqliMatchStatement")
    def sqli_match_statement(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference", jsii.get(self, "sqliMatchStatement"))

    @builtins.property
    @jsii.member(jsii_name="xssMatchStatement")
    def xss_match_statement(
        self,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference", jsii.get(self, "xssMatchStatement"))

    @builtins.property
    @jsii.member(jsii_name="andStatementInput")
    def and_statement_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementAndStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementAndStatement], jsii.get(self, "andStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="byteMatchStatementInput")
    def byte_match_statement_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementByteMatchStatement], jsii.get(self, "byteMatchStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="geoMatchStatementInput")
    def geo_match_statement_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementGeoMatchStatement], jsii.get(self, "geoMatchStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="ipSetReferenceStatementInput")
    def ip_set_reference_statement_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementIpSetReferenceStatement], jsii.get(self, "ipSetReferenceStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="labelMatchStatementInput")
    def label_match_statement_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementLabelMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementLabelMatchStatement], jsii.get(self, "labelMatchStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="notStatementInput")
    def not_statement_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementNotStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementNotStatement], jsii.get(self, "notStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="orStatementInput")
    def or_statement_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementOrStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementOrStatement], jsii.get(self, "orStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="regexPatternSetReferenceStatementInput")
    def regex_pattern_set_reference_statement_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement"], jsii.get(self, "regexPatternSetReferenceStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeConstraintStatementInput")
    def size_constraint_statement_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatement"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatement"], jsii.get(self, "sizeConstraintStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="sqliMatchStatementInput")
    def sqli_match_statement_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatement"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatement"], jsii.get(self, "sqliMatchStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="xssMatchStatementInput")
    def xss_match_statement_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatement"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatement"], jsii.get(self, "xssMatchStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupRuleStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "text_transformation": "textTransformation",
        "field_to_match": "fieldToMatch",
    },
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement:
    def __init__(
        self,
        *,
        arn: builtins.str,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#arn Wafv2RuleGroup#arn}.
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        if isinstance(field_to_match, dict):
            field_to_match = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch(**field_to_match)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement.__init__)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "text_transformation": text_transformation,
        }
        if field_to_match is not None:
            self._values["field_to_match"] = field_to_match

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#arn Wafv2RuleGroup#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_transformation(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation"]]:
        '''text_transformation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        '''
        result = self._values.get("text_transformation")
        assert result is not None, "Required property 'text_transformation' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation"]], result)

    @builtins.property
    def field_to_match(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch"]:
        '''field_to_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        result = self._values.get("field_to_match")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch",
    jsii_struct_bases=[],
    name_mapping={
        "all_query_arguments": "allQueryArguments",
        "body": "body",
        "cookies": "cookies",
        "json_body": "jsonBody",
        "method": "method",
        "query_string": "queryString",
        "single_header": "singleHeader",
        "single_query_argument": "singleQueryArgument",
        "uri_path": "uriPath",
    },
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch:
    def __init__(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody", typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies", typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody", typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString", typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader", typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument", typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        if isinstance(all_query_arguments, dict):
            all_query_arguments = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments(**all_query_arguments)
        if isinstance(body, dict):
            body = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody(**body)
        if isinstance(cookies, dict):
            cookies = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies(**cookies)
        if isinstance(json_body, dict):
            json_body = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(**json_body)
        if isinstance(method, dict):
            method = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod(**method)
        if isinstance(query_string, dict):
            query_string = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString(**query_string)
        if isinstance(single_header, dict):
            single_header = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(**single_header)
        if isinstance(single_query_argument, dict):
            single_query_argument = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(**single_query_argument)
        if isinstance(uri_path, dict):
            uri_path = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath(**uri_path)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch.__init__)
            check_type(argname="argument all_query_arguments", value=all_query_arguments, expected_type=type_hints["all_query_arguments"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
            check_type(argname="argument json_body", value=json_body, expected_type=type_hints["json_body"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
            check_type(argname="argument single_query_argument", value=single_query_argument, expected_type=type_hints["single_query_argument"])
            check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all_query_arguments is not None:
            self._values["all_query_arguments"] = all_query_arguments
        if body is not None:
            self._values["body"] = body
        if cookies is not None:
            self._values["cookies"] = cookies
        if json_body is not None:
            self._values["json_body"] = json_body
        if method is not None:
            self._values["method"] = method
        if query_string is not None:
            self._values["query_string"] = query_string
        if single_header is not None:
            self._values["single_header"] = single_header
        if single_query_argument is not None:
            self._values["single_query_argument"] = single_query_argument
        if uri_path is not None:
            self._values["uri_path"] = uri_path

    @builtins.property
    def all_query_arguments(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments"]:
        '''all_query_arguments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        '''
        result = self._values.get("all_query_arguments")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments"], result)

    @builtins.property
    def body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody"]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody"], result)

    @builtins.property
    def cookies(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies"]:
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        '''
        result = self._values.get("cookies")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies"], result)

    @builtins.property
    def json_body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody"]:
        '''json_body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        '''
        result = self._values.get("json_body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody"], result)

    @builtins.property
    def method(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod"]:
        '''method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString"]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString"], result)

    @builtins.property
    def single_header(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader"]:
        '''single_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        '''
        result = self._values.get("single_header")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader"], result)

    @builtins.property
    def single_query_argument(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument"]:
        '''single_query_argument block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        '''
        result = self._values.get("single_query_argument")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument"], result)

    @builtins.property
    def uri_path(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath"]:
        '''uri_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        result = self._values.get("uri_path")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArgumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArgumentsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArgumentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArgumentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies:
    def __init__(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern", typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
            "oversize_handling": oversize_handling,
        }

    @builtins.property
    def match_pattern(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern"]]:
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern"]], result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oversize_handling(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        assert result is not None, "Required property 'oversize_handling' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "excluded_cookies": "excludedCookies",
        "included_cookies": "includedCookies",
    },
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        excluded_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
        included_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param excluded_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.
        :param included_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument excluded_cookies", value=excluded_cookies, expected_type=type_hints["excluded_cookies"])
            check_type(argname="argument included_cookies", value=included_cookies, expected_type=type_hints["included_cookies"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if excluded_cookies is not None:
            self._values["excluded_cookies"] = excluded_cookies
        if included_cookies is not None:
            self._values["included_cookies"] = included_cookies

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll"], result)

    @builtins.property
    def excluded_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.'''
        result = self._values.get("excluded_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def included_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.'''
        result = self._values.get("included_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetExcludedCookies")
    def reset_excluded_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedCookies", []))

    @jsii.member(jsii_name="resetIncludedCookies")
    def reset_included_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedCookies", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookiesInput")
    def excluded_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="includedCookiesInput")
    def included_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookies")
    def excluded_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedCookies"))

    @excluded_cookies.setter
    def excluded_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference, "excluded_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="includedCookies")
    def included_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedCookies"))

    @included_cookies.setter
    def included_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference, "included_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference.put_match_pattern)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "invalid_fallback_behavior": "invalidFallbackBehavior",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody:
    def __init__(
        self,
        *,
        match_pattern: typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern", typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if isinstance(match_pattern, dict):
            match_pattern = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(**match_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument invalid_fallback_behavior", value=invalid_fallback_behavior, expected_type=type_hints["invalid_fallback_behavior"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
        }
        if invalid_fallback_behavior is not None:
            self._values["invalid_fallback_behavior"] = invalid_fallback_behavior
        if oversize_handling is not None:
            self._values["oversize_handling"] = oversize_handling

    @builtins.property
    def match_pattern(
        self,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern":
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern", result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invalid_fallback_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.'''
        result = self._values.get("invalid_fallback_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oversize_handling(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "included_paths": "includedPaths"},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument included_paths", value=included_paths, expected_type=type_hints["included_paths"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if included_paths is not None:
            self._values["included_paths"] = included_paths

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll"], result)

    @builtins.property
    def included_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.'''
        result = self._values.get("included_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetIncludedPaths")
    def reset_included_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedPaths", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPathsInput")
    def included_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPaths")
    def included_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedPaths"))

    @included_paths.setter
    def included_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference, "included_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedPaths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        *,
        all: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll, typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(
            all=all, included_paths=included_paths
        )

        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @jsii.member(jsii_name="resetInvalidFallbackBehavior")
    def reset_invalid_fallback_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvalidFallbackBehavior", []))

    @jsii.member(jsii_name="resetOversizeHandling")
    def reset_oversize_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOversizeHandling", []))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehaviorInput")
    def invalid_fallback_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invalidFallbackBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invalidFallbackBehavior"))

    @invalid_fallback_behavior.setter
    def invalid_fallback_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference, "invalid_fallback_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invalidFallbackBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethodOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllQueryArguments")
    def put_all_query_arguments(self) -> None:
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments()

        return typing.cast(None, jsii.invoke(self, "putAllQueryArguments", [value]))

    @jsii.member(jsii_name="putBody")
    def put_body(self) -> None:
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody()

        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies(
            match_pattern=match_pattern,
            match_scope=match_scope,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="putJsonBody")
    def put_json_body(
        self,
        *,
        match_pattern: typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern, typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(
            match_pattern=match_pattern,
            match_scope=match_scope,
            invalid_fallback_behavior=invalid_fallback_behavior,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putJsonBody", [value]))

    @jsii.member(jsii_name="putMethod")
    def put_method(self) -> None:
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod()

        return typing.cast(None, jsii.invoke(self, "putMethod", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(self) -> None:
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString()

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSingleHeader")
    def put_single_header(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleHeader", [value]))

    @jsii.member(jsii_name="putSingleQueryArgument")
    def put_single_query_argument(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleQueryArgument", [value]))

    @jsii.member(jsii_name="putUriPath")
    def put_uri_path(self) -> None:
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath()

        return typing.cast(None, jsii.invoke(self, "putUriPath", [value]))

    @jsii.member(jsii_name="resetAllQueryArguments")
    def reset_all_query_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllQueryArguments", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCookies")
    def reset_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookies", []))

    @jsii.member(jsii_name="resetJsonBody")
    def reset_json_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonBody", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSingleHeader")
    def reset_single_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleHeader", []))

    @jsii.member(jsii_name="resetSingleQueryArgument")
    def reset_single_query_argument(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleQueryArgument", []))

    @jsii.member(jsii_name="resetUriPath")
    def reset_uri_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUriPath", []))

    @builtins.property
    @jsii.member(jsii_name="allQueryArguments")
    def all_query_arguments(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArgumentsOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArgumentsOutputReference, jsii.get(self, "allQueryArguments"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBodyOutputReference, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="jsonBody")
    def json_body(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference, jsii.get(self, "jsonBody"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethodOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethodOutputReference, jsii.get(self, "method"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryStringOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="singleHeader")
    def single_header(
        self,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference", jsii.get(self, "singleHeader"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgument")
    def single_query_argument(
        self,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference", jsii.get(self, "singleQueryArgument"))

    @builtins.property
    @jsii.member(jsii_name="uriPath")
    def uri_path(
        self,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPathOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPathOutputReference", jsii.get(self, "uriPath"))

    @builtins.property
    @jsii.member(jsii_name="allQueryArgumentsInput")
    def all_query_arguments_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments], jsii.get(self, "allQueryArgumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonBodyInput")
    def json_body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody], jsii.get(self, "jsonBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="singleHeaderInput")
    def single_header_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader"], jsii.get(self, "singleHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgumentInput")
    def single_query_argument_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument"], jsii.get(self, "singleQueryArgumentInput"))

    @builtins.property
    @jsii.member(jsii_name="uriPathInput")
    def uri_path_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath"], jsii.get(self, "uriPathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPathOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFieldToMatch")
    def put_field_to_match(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments, typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody, typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies, typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody, typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod, typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString, typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader, typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument, typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        value = Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch(
            all_query_arguments=all_query_arguments,
            body=body,
            cookies=cookies,
            json_body=json_body,
            method=method,
            query_string=query_string,
            single_header=single_header,
            single_query_argument=single_query_argument,
            uri_path=uri_path,
        )

        return typing.cast(None, jsii.invoke(self, "putFieldToMatch", [value]))

    @jsii.member(jsii_name="putTextTransformation")
    def put_text_transformation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference.put_text_transformation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTextTransformation", [value]))

    @jsii.member(jsii_name="resetFieldToMatch")
    def reset_field_to_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldToMatch", []))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatch")
    def field_to_match(
        self,
    ) -> Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchOutputReference, jsii.get(self, "fieldToMatch"))

    @builtins.property
    @jsii.member(jsii_name="textTransformation")
    def text_transformation(
        self,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList":
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList", jsii.get(self, "textTransformation"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatchInput")
    def field_to_match_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch], jsii.get(self, "fieldToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="textTransformationInput")
    def text_transformation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation"]]], jsii.get(self, "textTransformationInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference, "arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation",
    jsii_struct_bases=[],
    name_mapping={"priority": "priority", "type": "type"},
)
class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation:
    def __init__(self, *, priority: jsii.Number, type: builtins.str) -> None:
        '''
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation.__init__)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "type": type,
        }

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatement",
    jsii_struct_bases=[],
    name_mapping={
        "comparison_operator": "comparisonOperator",
        "size": "size",
        "text_transformation": "textTransformation",
        "field_to_match": "fieldToMatch",
    },
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatement:
    def __init__(
        self,
        *,
        comparison_operator: builtins.str,
        size: jsii.Number,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param comparison_operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#comparison_operator Wafv2RuleGroup#comparison_operator}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size Wafv2RuleGroup#size}.
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        if isinstance(field_to_match, dict):
            field_to_match = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch(**field_to_match)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatement.__init__)
            check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "comparison_operator": comparison_operator,
            "size": size,
            "text_transformation": text_transformation,
        }
        if field_to_match is not None:
            self._values["field_to_match"] = field_to_match

    @builtins.property
    def comparison_operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#comparison_operator Wafv2RuleGroup#comparison_operator}.'''
        result = self._values.get("comparison_operator")
        assert result is not None, "Required property 'comparison_operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#size Wafv2RuleGroup#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def text_transformation(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation"]]:
        '''text_transformation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        '''
        result = self._values.get("text_transformation")
        assert result is not None, "Required property 'text_transformation' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation"]], result)

    @builtins.property
    def field_to_match(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch"]:
        '''field_to_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        result = self._values.get("field_to_match")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch",
    jsii_struct_bases=[],
    name_mapping={
        "all_query_arguments": "allQueryArguments",
        "body": "body",
        "cookies": "cookies",
        "json_body": "jsonBody",
        "method": "method",
        "query_string": "queryString",
        "single_header": "singleHeader",
        "single_query_argument": "singleQueryArgument",
        "uri_path": "uriPath",
    },
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch:
    def __init__(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody", typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies", typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody", typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString", typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader", typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument", typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        if isinstance(all_query_arguments, dict):
            all_query_arguments = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments(**all_query_arguments)
        if isinstance(body, dict):
            body = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody(**body)
        if isinstance(cookies, dict):
            cookies = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies(**cookies)
        if isinstance(json_body, dict):
            json_body = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody(**json_body)
        if isinstance(method, dict):
            method = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod(**method)
        if isinstance(query_string, dict):
            query_string = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString(**query_string)
        if isinstance(single_header, dict):
            single_header = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader(**single_header)
        if isinstance(single_query_argument, dict):
            single_query_argument = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(**single_query_argument)
        if isinstance(uri_path, dict):
            uri_path = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath(**uri_path)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch.__init__)
            check_type(argname="argument all_query_arguments", value=all_query_arguments, expected_type=type_hints["all_query_arguments"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
            check_type(argname="argument json_body", value=json_body, expected_type=type_hints["json_body"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
            check_type(argname="argument single_query_argument", value=single_query_argument, expected_type=type_hints["single_query_argument"])
            check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all_query_arguments is not None:
            self._values["all_query_arguments"] = all_query_arguments
        if body is not None:
            self._values["body"] = body
        if cookies is not None:
            self._values["cookies"] = cookies
        if json_body is not None:
            self._values["json_body"] = json_body
        if method is not None:
            self._values["method"] = method
        if query_string is not None:
            self._values["query_string"] = query_string
        if single_header is not None:
            self._values["single_header"] = single_header
        if single_query_argument is not None:
            self._values["single_query_argument"] = single_query_argument
        if uri_path is not None:
            self._values["uri_path"] = uri_path

    @builtins.property
    def all_query_arguments(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments"]:
        '''all_query_arguments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        '''
        result = self._values.get("all_query_arguments")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments"], result)

    @builtins.property
    def body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody"]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody"], result)

    @builtins.property
    def cookies(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies"]:
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        '''
        result = self._values.get("cookies")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies"], result)

    @builtins.property
    def json_body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody"]:
        '''json_body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        '''
        result = self._values.get("json_body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody"], result)

    @builtins.property
    def method(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod"]:
        '''method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString"]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString"], result)

    @builtins.property
    def single_header(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader"]:
        '''single_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        '''
        result = self._values.get("single_header")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader"], result)

    @builtins.property
    def single_query_argument(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument"]:
        '''single_query_argument block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        '''
        result = self._values.get("single_query_argument")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument"], result)

    @builtins.property
    def uri_path(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath"]:
        '''uri_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        result = self._values.get("uri_path")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArgumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArgumentsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArgumentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArgumentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies:
    def __init__(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern", typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
            "oversize_handling": oversize_handling,
        }

    @builtins.property
    def match_pattern(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern"]]:
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern"]], result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oversize_handling(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        assert result is not None, "Required property 'oversize_handling' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "excluded_cookies": "excludedCookies",
        "included_cookies": "includedCookies",
    },
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        excluded_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
        included_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param excluded_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.
        :param included_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument excluded_cookies", value=excluded_cookies, expected_type=type_hints["excluded_cookies"])
            check_type(argname="argument included_cookies", value=included_cookies, expected_type=type_hints["included_cookies"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if excluded_cookies is not None:
            self._values["excluded_cookies"] = excluded_cookies
        if included_cookies is not None:
            self._values["included_cookies"] = included_cookies

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll"], result)

    @builtins.property
    def excluded_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.'''
        result = self._values.get("excluded_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def included_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.'''
        result = self._values.get("included_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetExcludedCookies")
    def reset_excluded_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedCookies", []))

    @jsii.member(jsii_name="resetIncludedCookies")
    def reset_included_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedCookies", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookiesInput")
    def excluded_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="includedCookiesInput")
    def included_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookies")
    def excluded_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedCookies"))

    @excluded_cookies.setter
    def excluded_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference, "excluded_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="includedCookies")
    def included_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedCookies"))

    @included_cookies.setter
    def included_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference, "included_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference.put_match_pattern)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "invalid_fallback_behavior": "invalidFallbackBehavior",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody:
    def __init__(
        self,
        *,
        match_pattern: typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern", typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if isinstance(match_pattern, dict):
            match_pattern = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(**match_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument invalid_fallback_behavior", value=invalid_fallback_behavior, expected_type=type_hints["invalid_fallback_behavior"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
        }
        if invalid_fallback_behavior is not None:
            self._values["invalid_fallback_behavior"] = invalid_fallback_behavior
        if oversize_handling is not None:
            self._values["oversize_handling"] = oversize_handling

    @builtins.property
    def match_pattern(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern":
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern", result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invalid_fallback_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.'''
        result = self._values.get("invalid_fallback_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oversize_handling(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "included_paths": "includedPaths"},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument included_paths", value=included_paths, expected_type=type_hints["included_paths"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if included_paths is not None:
            self._values["included_paths"] = included_paths

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll"], result)

    @builtins.property
    def included_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.'''
        result = self._values.get("included_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetIncludedPaths")
    def reset_included_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedPaths", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPathsInput")
    def included_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPaths")
    def included_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedPaths"))

    @included_paths.setter
    def included_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference, "included_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedPaths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        *,
        all: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll, typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(
            all=all, included_paths=included_paths
        )

        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @jsii.member(jsii_name="resetInvalidFallbackBehavior")
    def reset_invalid_fallback_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvalidFallbackBehavior", []))

    @jsii.member(jsii_name="resetOversizeHandling")
    def reset_oversize_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOversizeHandling", []))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehaviorInput")
    def invalid_fallback_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invalidFallbackBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invalidFallbackBehavior"))

    @invalid_fallback_behavior.setter
    def invalid_fallback_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference, "invalid_fallback_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invalidFallbackBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethodOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllQueryArguments")
    def put_all_query_arguments(self) -> None:
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments()

        return typing.cast(None, jsii.invoke(self, "putAllQueryArguments", [value]))

    @jsii.member(jsii_name="putBody")
    def put_body(self) -> None:
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody()

        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies(
            match_pattern=match_pattern,
            match_scope=match_scope,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="putJsonBody")
    def put_json_body(
        self,
        *,
        match_pattern: typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern, typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody(
            match_pattern=match_pattern,
            match_scope=match_scope,
            invalid_fallback_behavior=invalid_fallback_behavior,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putJsonBody", [value]))

    @jsii.member(jsii_name="putMethod")
    def put_method(self) -> None:
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod()

        return typing.cast(None, jsii.invoke(self, "putMethod", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(self) -> None:
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString()

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSingleHeader")
    def put_single_header(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleHeader", [value]))

    @jsii.member(jsii_name="putSingleQueryArgument")
    def put_single_query_argument(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleQueryArgument", [value]))

    @jsii.member(jsii_name="putUriPath")
    def put_uri_path(self) -> None:
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath()

        return typing.cast(None, jsii.invoke(self, "putUriPath", [value]))

    @jsii.member(jsii_name="resetAllQueryArguments")
    def reset_all_query_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllQueryArguments", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCookies")
    def reset_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookies", []))

    @jsii.member(jsii_name="resetJsonBody")
    def reset_json_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonBody", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSingleHeader")
    def reset_single_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleHeader", []))

    @jsii.member(jsii_name="resetSingleQueryArgument")
    def reset_single_query_argument(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleQueryArgument", []))

    @jsii.member(jsii_name="resetUriPath")
    def reset_uri_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUriPath", []))

    @builtins.property
    @jsii.member(jsii_name="allQueryArguments")
    def all_query_arguments(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArgumentsOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArgumentsOutputReference, jsii.get(self, "allQueryArguments"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBodyOutputReference, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="jsonBody")
    def json_body(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference, jsii.get(self, "jsonBody"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethodOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethodOutputReference, jsii.get(self, "method"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryStringOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="singleHeader")
    def single_header(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference", jsii.get(self, "singleHeader"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgument")
    def single_query_argument(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference", jsii.get(self, "singleQueryArgument"))

    @builtins.property
    @jsii.member(jsii_name="uriPath")
    def uri_path(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPathOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPathOutputReference", jsii.get(self, "uriPath"))

    @builtins.property
    @jsii.member(jsii_name="allQueryArgumentsInput")
    def all_query_arguments_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments], jsii.get(self, "allQueryArgumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonBodyInput")
    def json_body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody], jsii.get(self, "jsonBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="singleHeaderInput")
    def single_header_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader"], jsii.get(self, "singleHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgumentInput")
    def single_query_argument_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument"], jsii.get(self, "singleQueryArgumentInput"))

    @builtins.property
    @jsii.member(jsii_name="uriPathInput")
    def uri_path_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath"], jsii.get(self, "uriPathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPathOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFieldToMatch")
    def put_field_to_match(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments, typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody, typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies, typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody, typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod, typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString, typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader, typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument, typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        value = Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch(
            all_query_arguments=all_query_arguments,
            body=body,
            cookies=cookies,
            json_body=json_body,
            method=method,
            query_string=query_string,
            single_header=single_header,
            single_query_argument=single_query_argument,
            uri_path=uri_path,
        )

        return typing.cast(None, jsii.invoke(self, "putFieldToMatch", [value]))

    @jsii.member(jsii_name="putTextTransformation")
    def put_text_transformation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference.put_text_transformation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTextTransformation", [value]))

    @jsii.member(jsii_name="resetFieldToMatch")
    def reset_field_to_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldToMatch", []))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatch")
    def field_to_match(
        self,
    ) -> Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchOutputReference, jsii.get(self, "fieldToMatch"))

    @builtins.property
    @jsii.member(jsii_name="textTransformation")
    def text_transformation(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList":
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList", jsii.get(self, "textTransformation"))

    @builtins.property
    @jsii.member(jsii_name="comparisonOperatorInput")
    def comparison_operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparisonOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatchInput")
    def field_to_match_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch], jsii.get(self, "fieldToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="textTransformationInput")
    def text_transformation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation"]]], jsii.get(self, "textTransformationInput"))

    @builtins.property
    @jsii.member(jsii_name="comparisonOperator")
    def comparison_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparisonOperator"))

    @comparison_operator.setter
    def comparison_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference, "comparison_operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparisonOperator", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSizeConstraintStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation",
    jsii_struct_bases=[],
    name_mapping={"priority": "priority", "type": "type"},
)
class Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation:
    def __init__(self, *, priority: jsii.Number, type: builtins.str) -> None:
        '''
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation.__init__)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "type": type,
        }

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatement",
    jsii_struct_bases=[],
    name_mapping={
        "text_transformation": "textTransformation",
        "field_to_match": "fieldToMatch",
    },
)
class Wafv2RuleGroupRuleStatementSqliMatchStatement:
    def __init__(
        self,
        *,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        if isinstance(field_to_match, dict):
            field_to_match = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch(**field_to_match)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatement.__init__)
            check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "text_transformation": text_transformation,
        }
        if field_to_match is not None:
            self._values["field_to_match"] = field_to_match

    @builtins.property
    def text_transformation(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation"]]:
        '''text_transformation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        '''
        result = self._values.get("text_transformation")
        assert result is not None, "Required property 'text_transformation' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation"]], result)

    @builtins.property
    def field_to_match(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch"]:
        '''field_to_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        result = self._values.get("field_to_match")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch",
    jsii_struct_bases=[],
    name_mapping={
        "all_query_arguments": "allQueryArguments",
        "body": "body",
        "cookies": "cookies",
        "json_body": "jsonBody",
        "method": "method",
        "query_string": "queryString",
        "single_header": "singleHeader",
        "single_query_argument": "singleQueryArgument",
        "uri_path": "uriPath",
    },
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch:
    def __init__(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody", typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies", typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody", typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString", typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader", typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument", typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        if isinstance(all_query_arguments, dict):
            all_query_arguments = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments(**all_query_arguments)
        if isinstance(body, dict):
            body = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody(**body)
        if isinstance(cookies, dict):
            cookies = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies(**cookies)
        if isinstance(json_body, dict):
            json_body = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody(**json_body)
        if isinstance(method, dict):
            method = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod(**method)
        if isinstance(query_string, dict):
            query_string = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString(**query_string)
        if isinstance(single_header, dict):
            single_header = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader(**single_header)
        if isinstance(single_query_argument, dict):
            single_query_argument = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument(**single_query_argument)
        if isinstance(uri_path, dict):
            uri_path = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath(**uri_path)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch.__init__)
            check_type(argname="argument all_query_arguments", value=all_query_arguments, expected_type=type_hints["all_query_arguments"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
            check_type(argname="argument json_body", value=json_body, expected_type=type_hints["json_body"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
            check_type(argname="argument single_query_argument", value=single_query_argument, expected_type=type_hints["single_query_argument"])
            check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all_query_arguments is not None:
            self._values["all_query_arguments"] = all_query_arguments
        if body is not None:
            self._values["body"] = body
        if cookies is not None:
            self._values["cookies"] = cookies
        if json_body is not None:
            self._values["json_body"] = json_body
        if method is not None:
            self._values["method"] = method
        if query_string is not None:
            self._values["query_string"] = query_string
        if single_header is not None:
            self._values["single_header"] = single_header
        if single_query_argument is not None:
            self._values["single_query_argument"] = single_query_argument
        if uri_path is not None:
            self._values["uri_path"] = uri_path

    @builtins.property
    def all_query_arguments(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments"]:
        '''all_query_arguments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        '''
        result = self._values.get("all_query_arguments")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments"], result)

    @builtins.property
    def body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody"]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody"], result)

    @builtins.property
    def cookies(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies"]:
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        '''
        result = self._values.get("cookies")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies"], result)

    @builtins.property
    def json_body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody"]:
        '''json_body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        '''
        result = self._values.get("json_body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody"], result)

    @builtins.property
    def method(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod"]:
        '''method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString"]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString"], result)

    @builtins.property
    def single_header(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader"]:
        '''single_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        '''
        result = self._values.get("single_header")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader"], result)

    @builtins.property
    def single_query_argument(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument"]:
        '''single_query_argument block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        '''
        result = self._values.get("single_query_argument")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument"], result)

    @builtins.property
    def uri_path(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath"]:
        '''uri_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        result = self._values.get("uri_path")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArgumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArgumentsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArgumentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArgumentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies:
    def __init__(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern", typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
            "oversize_handling": oversize_handling,
        }

    @builtins.property
    def match_pattern(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern"]]:
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern"]], result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oversize_handling(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        assert result is not None, "Required property 'oversize_handling' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "excluded_cookies": "excludedCookies",
        "included_cookies": "includedCookies",
    },
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        excluded_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
        included_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param excluded_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.
        :param included_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument excluded_cookies", value=excluded_cookies, expected_type=type_hints["excluded_cookies"])
            check_type(argname="argument included_cookies", value=included_cookies, expected_type=type_hints["included_cookies"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if excluded_cookies is not None:
            self._values["excluded_cookies"] = excluded_cookies
        if included_cookies is not None:
            self._values["included_cookies"] = included_cookies

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll"], result)

    @builtins.property
    def excluded_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.'''
        result = self._values.get("excluded_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def included_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.'''
        result = self._values.get("included_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetExcludedCookies")
    def reset_excluded_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedCookies", []))

    @jsii.member(jsii_name="resetIncludedCookies")
    def reset_included_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedCookies", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookiesInput")
    def excluded_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="includedCookiesInput")
    def included_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookies")
    def excluded_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedCookies"))

    @excluded_cookies.setter
    def excluded_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "excluded_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="includedCookies")
    def included_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedCookies"))

    @included_cookies.setter
    def included_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "included_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference.put_match_pattern)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "invalid_fallback_behavior": "invalidFallbackBehavior",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody:
    def __init__(
        self,
        *,
        match_pattern: typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern", typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if isinstance(match_pattern, dict):
            match_pattern = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(**match_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument invalid_fallback_behavior", value=invalid_fallback_behavior, expected_type=type_hints["invalid_fallback_behavior"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
        }
        if invalid_fallback_behavior is not None:
            self._values["invalid_fallback_behavior"] = invalid_fallback_behavior
        if oversize_handling is not None:
            self._values["oversize_handling"] = oversize_handling

    @builtins.property
    def match_pattern(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern":
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern", result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invalid_fallback_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.'''
        result = self._values.get("invalid_fallback_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oversize_handling(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "included_paths": "includedPaths"},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument included_paths", value=included_paths, expected_type=type_hints["included_paths"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if included_paths is not None:
            self._values["included_paths"] = included_paths

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll"], result)

    @builtins.property
    def included_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.'''
        result = self._values.get("included_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetIncludedPaths")
    def reset_included_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedPaths", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPathsInput")
    def included_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPaths")
    def included_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedPaths"))

    @included_paths.setter
    def included_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, "included_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedPaths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        *,
        all: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll, typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(
            all=all, included_paths=included_paths
        )

        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @jsii.member(jsii_name="resetInvalidFallbackBehavior")
    def reset_invalid_fallback_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvalidFallbackBehavior", []))

    @jsii.member(jsii_name="resetOversizeHandling")
    def reset_oversize_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOversizeHandling", []))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehaviorInput")
    def invalid_fallback_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invalidFallbackBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invalidFallbackBehavior"))

    @invalid_fallback_behavior.setter
    def invalid_fallback_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference, "invalid_fallback_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invalidFallbackBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethodOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllQueryArguments")
    def put_all_query_arguments(self) -> None:
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments()

        return typing.cast(None, jsii.invoke(self, "putAllQueryArguments", [value]))

    @jsii.member(jsii_name="putBody")
    def put_body(self) -> None:
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody()

        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies(
            match_pattern=match_pattern,
            match_scope=match_scope,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="putJsonBody")
    def put_json_body(
        self,
        *,
        match_pattern: typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern, typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody(
            match_pattern=match_pattern,
            match_scope=match_scope,
            invalid_fallback_behavior=invalid_fallback_behavior,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putJsonBody", [value]))

    @jsii.member(jsii_name="putMethod")
    def put_method(self) -> None:
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod()

        return typing.cast(None, jsii.invoke(self, "putMethod", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(self) -> None:
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString()

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSingleHeader")
    def put_single_header(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleHeader", [value]))

    @jsii.member(jsii_name="putSingleQueryArgument")
    def put_single_query_argument(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleQueryArgument", [value]))

    @jsii.member(jsii_name="putUriPath")
    def put_uri_path(self) -> None:
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath()

        return typing.cast(None, jsii.invoke(self, "putUriPath", [value]))

    @jsii.member(jsii_name="resetAllQueryArguments")
    def reset_all_query_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllQueryArguments", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCookies")
    def reset_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookies", []))

    @jsii.member(jsii_name="resetJsonBody")
    def reset_json_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonBody", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSingleHeader")
    def reset_single_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleHeader", []))

    @jsii.member(jsii_name="resetSingleQueryArgument")
    def reset_single_query_argument(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleQueryArgument", []))

    @jsii.member(jsii_name="resetUriPath")
    def reset_uri_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUriPath", []))

    @builtins.property
    @jsii.member(jsii_name="allQueryArguments")
    def all_query_arguments(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArgumentsOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArgumentsOutputReference, jsii.get(self, "allQueryArguments"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBodyOutputReference, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="jsonBody")
    def json_body(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference, jsii.get(self, "jsonBody"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethodOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethodOutputReference, jsii.get(self, "method"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryStringOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="singleHeader")
    def single_header(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference", jsii.get(self, "singleHeader"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgument")
    def single_query_argument(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference", jsii.get(self, "singleQueryArgument"))

    @builtins.property
    @jsii.member(jsii_name="uriPath")
    def uri_path(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPathOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPathOutputReference", jsii.get(self, "uriPath"))

    @builtins.property
    @jsii.member(jsii_name="allQueryArgumentsInput")
    def all_query_arguments_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments], jsii.get(self, "allQueryArgumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonBodyInput")
    def json_body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody], jsii.get(self, "jsonBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="singleHeaderInput")
    def single_header_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader"], jsii.get(self, "singleHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgumentInput")
    def single_query_argument_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument"], jsii.get(self, "singleQueryArgumentInput"))

    @builtins.property
    @jsii.member(jsii_name="uriPathInput")
    def uri_path_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath"], jsii.get(self, "uriPathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPathOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFieldToMatch")
    def put_field_to_match(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments, typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody, typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies, typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody, typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod, typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString, typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader, typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument, typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        value = Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch(
            all_query_arguments=all_query_arguments,
            body=body,
            cookies=cookies,
            json_body=json_body,
            method=method,
            query_string=query_string,
            single_header=single_header,
            single_query_argument=single_query_argument,
            uri_path=uri_path,
        )

        return typing.cast(None, jsii.invoke(self, "putFieldToMatch", [value]))

    @jsii.member(jsii_name="putTextTransformation")
    def put_text_transformation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference.put_text_transformation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTextTransformation", [value]))

    @jsii.member(jsii_name="resetFieldToMatch")
    def reset_field_to_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldToMatch", []))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatch")
    def field_to_match(
        self,
    ) -> Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchOutputReference, jsii.get(self, "fieldToMatch"))

    @builtins.property
    @jsii.member(jsii_name="textTransformation")
    def text_transformation(
        self,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList":
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList", jsii.get(self, "textTransformation"))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatchInput")
    def field_to_match_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch], jsii.get(self, "fieldToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="textTransformationInput")
    def text_transformation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation"]]], jsii.get(self, "textTransformationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementSqliMatchStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation",
    jsii_struct_bases=[],
    name_mapping={"priority": "priority", "type": "type"},
)
class Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation:
    def __init__(self, *, priority: jsii.Number, type: builtins.str) -> None:
        '''
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation.__init__)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "type": type,
        }

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatement",
    jsii_struct_bases=[],
    name_mapping={
        "text_transformation": "textTransformation",
        "field_to_match": "fieldToMatch",
    },
)
class Wafv2RuleGroupRuleStatementXssMatchStatement:
    def __init__(
        self,
        *,
        text_transformation: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
        field_to_match: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text_transformation: text_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        if isinstance(field_to_match, dict):
            field_to_match = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch(**field_to_match)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatement.__init__)
            check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "text_transformation": text_transformation,
        }
        if field_to_match is not None:
            self._values["field_to_match"] = field_to_match

    @builtins.property
    def text_transformation(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation"]]:
        '''text_transformation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#text_transformation Wafv2RuleGroup#text_transformation}
        '''
        result = self._values.get("text_transformation")
        assert result is not None, "Required property 'text_transformation' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation"]], result)

    @builtins.property
    def field_to_match(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch"]:
        '''field_to_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#field_to_match Wafv2RuleGroup#field_to_match}
        '''
        result = self._values.get("field_to_match")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch",
    jsii_struct_bases=[],
    name_mapping={
        "all_query_arguments": "allQueryArguments",
        "body": "body",
        "cookies": "cookies",
        "json_body": "jsonBody",
        "method": "method",
        "query_string": "queryString",
        "single_header": "singleHeader",
        "single_query_argument": "singleQueryArgument",
        "uri_path": "uriPath",
    },
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch:
    def __init__(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody", typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies", typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody", typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString", typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader", typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument", typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        if isinstance(all_query_arguments, dict):
            all_query_arguments = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments(**all_query_arguments)
        if isinstance(body, dict):
            body = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody(**body)
        if isinstance(cookies, dict):
            cookies = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies(**cookies)
        if isinstance(json_body, dict):
            json_body = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody(**json_body)
        if isinstance(method, dict):
            method = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod(**method)
        if isinstance(query_string, dict):
            query_string = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString(**query_string)
        if isinstance(single_header, dict):
            single_header = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader(**single_header)
        if isinstance(single_query_argument, dict):
            single_query_argument = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument(**single_query_argument)
        if isinstance(uri_path, dict):
            uri_path = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath(**uri_path)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch.__init__)
            check_type(argname="argument all_query_arguments", value=all_query_arguments, expected_type=type_hints["all_query_arguments"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
            check_type(argname="argument json_body", value=json_body, expected_type=type_hints["json_body"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
            check_type(argname="argument single_query_argument", value=single_query_argument, expected_type=type_hints["single_query_argument"])
            check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all_query_arguments is not None:
            self._values["all_query_arguments"] = all_query_arguments
        if body is not None:
            self._values["body"] = body
        if cookies is not None:
            self._values["cookies"] = cookies
        if json_body is not None:
            self._values["json_body"] = json_body
        if method is not None:
            self._values["method"] = method
        if query_string is not None:
            self._values["query_string"] = query_string
        if single_header is not None:
            self._values["single_header"] = single_header
        if single_query_argument is not None:
            self._values["single_query_argument"] = single_query_argument
        if uri_path is not None:
            self._values["uri_path"] = uri_path

    @builtins.property
    def all_query_arguments(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments"]:
        '''all_query_arguments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        '''
        result = self._values.get("all_query_arguments")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments"], result)

    @builtins.property
    def body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody"]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody"], result)

    @builtins.property
    def cookies(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies"]:
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        '''
        result = self._values.get("cookies")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies"], result)

    @builtins.property
    def json_body(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody"]:
        '''json_body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        '''
        result = self._values.get("json_body")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody"], result)

    @builtins.property
    def method(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod"]:
        '''method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString"]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString"], result)

    @builtins.property
    def single_header(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader"]:
        '''single_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        '''
        result = self._values.get("single_header")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader"], result)

    @builtins.property
    def single_query_argument(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument"]:
        '''single_query_argument block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        '''
        result = self._values.get("single_query_argument")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument"], result)

    @builtins.property
    def uri_path(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath"]:
        '''uri_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        result = self._values.get("uri_path")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArgumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArgumentsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArgumentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArgumentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies:
    def __init__(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern", typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
            "oversize_handling": oversize_handling,
        }

    @builtins.property
    def match_pattern(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern"]]:
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern"]], result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oversize_handling(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        assert result is not None, "Required property 'oversize_handling' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "excluded_cookies": "excludedCookies",
        "included_cookies": "includedCookies",
    },
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        excluded_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
        included_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param excluded_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.
        :param included_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument excluded_cookies", value=excluded_cookies, expected_type=type_hints["excluded_cookies"])
            check_type(argname="argument included_cookies", value=included_cookies, expected_type=type_hints["included_cookies"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if excluded_cookies is not None:
            self._values["excluded_cookies"] = excluded_cookies
        if included_cookies is not None:
            self._values["included_cookies"] = included_cookies

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll"], result)

    @builtins.property
    def excluded_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#excluded_cookies Wafv2RuleGroup#excluded_cookies}.'''
        result = self._values.get("excluded_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def included_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_cookies Wafv2RuleGroup#included_cookies}.'''
        result = self._values.get("included_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetExcludedCookies")
    def reset_excluded_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedCookies", []))

    @jsii.member(jsii_name="resetIncludedCookies")
    def reset_included_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedCookies", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookiesInput")
    def excluded_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="includedCookiesInput")
    def included_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedCookies")
    def excluded_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedCookies"))

    @excluded_cookies.setter
    def excluded_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "excluded_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="includedCookies")
    def included_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedCookies"))

    @included_cookies.setter
    def included_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "included_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference.put_match_pattern)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern]]], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody",
    jsii_struct_bases=[],
    name_mapping={
        "match_pattern": "matchPattern",
        "match_scope": "matchScope",
        "invalid_fallback_behavior": "invalidFallbackBehavior",
        "oversize_handling": "oversizeHandling",
    },
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody:
    def __init__(
        self,
        *,
        match_pattern: typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern", typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        if isinstance(match_pattern, dict):
            match_pattern = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(**match_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody.__init__)
            check_type(argname="argument match_pattern", value=match_pattern, expected_type=type_hints["match_pattern"])
            check_type(argname="argument match_scope", value=match_scope, expected_type=type_hints["match_scope"])
            check_type(argname="argument invalid_fallback_behavior", value=invalid_fallback_behavior, expected_type=type_hints["invalid_fallback_behavior"])
            check_type(argname="argument oversize_handling", value=oversize_handling, expected_type=type_hints["oversize_handling"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_pattern": match_pattern,
            "match_scope": match_scope,
        }
        if invalid_fallback_behavior is not None:
            self._values["invalid_fallback_behavior"] = invalid_fallback_behavior
        if oversize_handling is not None:
            self._values["oversize_handling"] = oversize_handling

    @builtins.property
    def match_pattern(
        self,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern":
        '''match_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        '''
        result = self._values.get("match_pattern")
        assert result is not None, "Required property 'match_pattern' is missing"
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern", result)

    @builtins.property
    def match_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.'''
        result = self._values.get("match_scope")
        assert result is not None, "Required property 'match_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invalid_fallback_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.'''
        result = self._values.get("invalid_fallback_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oversize_handling(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.'''
        result = self._values.get("oversize_handling")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "included_paths": "includedPaths"},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll", typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        if isinstance(all, dict):
            all = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll(**all)
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument included_paths", value=included_paths, expected_type=type_hints["included_paths"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if included_paths is not None:
            self._values["included_paths"] = included_paths

    @builtins.property
    def all(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll"], result)

    @builtins.property
    def included_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.'''
        result = self._values.get("included_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAll")
    def put_all(self) -> None:
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll()

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetIncludedPaths")
    def reset_included_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedPaths", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPathsInput")
    def included_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPaths")
    def included_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedPaths"))

    @included_paths.setter
    def included_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, "included_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedPaths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchPattern")
    def put_match_pattern(
        self,
        *,
        all: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll, typing.Dict[str, typing.Any]]] = None,
        included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all Wafv2RuleGroup#all}
        :param included_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#included_paths Wafv2RuleGroup#included_paths}.
        '''
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(
            all=all, included_paths=included_paths
        )

        return typing.cast(None, jsii.invoke(self, "putMatchPattern", [value]))

    @jsii.member(jsii_name="resetInvalidFallbackBehavior")
    def reset_invalid_fallback_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvalidFallbackBehavior", []))

    @jsii.member(jsii_name="resetOversizeHandling")
    def reset_oversize_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOversizeHandling", []))

    @builtins.property
    @jsii.member(jsii_name="matchPattern")
    def match_pattern(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference, jsii.get(self, "matchPattern"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehaviorInput")
    def invalid_fallback_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invalidFallbackBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPatternInput")
    def match_pattern_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern], jsii.get(self, "matchPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="matchScopeInput")
    def match_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="oversizeHandlingInput")
    def oversize_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oversizeHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invalidFallbackBehavior"))

    @invalid_fallback_behavior.setter
    def invalid_fallback_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference, "invalid_fallback_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invalidFallbackBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="matchScope")
    def match_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchScope"))

    @match_scope.setter
    def match_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference, "match_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchScope", value)

    @builtins.property
    @jsii.member(jsii_name="oversizeHandling")
    def oversize_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oversizeHandling"))

    @oversize_handling.setter
    def oversize_handling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference, "oversize_handling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oversizeHandling", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethodOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllQueryArguments")
    def put_all_query_arguments(self) -> None:
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments()

        return typing.cast(None, jsii.invoke(self, "putAllQueryArguments", [value]))

    @jsii.member(jsii_name="putBody")
    def put_body(self) -> None:
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody()

        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        match_pattern: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern, typing.Dict[str, typing.Any]]]],
        match_scope: builtins.str,
        oversize_handling: builtins.str,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies(
            match_pattern=match_pattern,
            match_scope=match_scope,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="putJsonBody")
    def put_json_body(
        self,
        *,
        match_pattern: typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern, typing.Dict[str, typing.Any]],
        match_scope: builtins.str,
        invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        oversize_handling: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_pattern: match_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_pattern Wafv2RuleGroup#match_pattern}
        :param match_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#match_scope Wafv2RuleGroup#match_scope}.
        :param invalid_fallback_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#invalid_fallback_behavior Wafv2RuleGroup#invalid_fallback_behavior}.
        :param oversize_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#oversize_handling Wafv2RuleGroup#oversize_handling}.
        '''
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody(
            match_pattern=match_pattern,
            match_scope=match_scope,
            invalid_fallback_behavior=invalid_fallback_behavior,
            oversize_handling=oversize_handling,
        )

        return typing.cast(None, jsii.invoke(self, "putJsonBody", [value]))

    @jsii.member(jsii_name="putMethod")
    def put_method(self) -> None:
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod()

        return typing.cast(None, jsii.invoke(self, "putMethod", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(self) -> None:
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString()

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSingleHeader")
    def put_single_header(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleHeader", [value]))

    @jsii.member(jsii_name="putSingleQueryArgument")
    def put_single_query_argument(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleQueryArgument", [value]))

    @jsii.member(jsii_name="putUriPath")
    def put_uri_path(self) -> None:
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath()

        return typing.cast(None, jsii.invoke(self, "putUriPath", [value]))

    @jsii.member(jsii_name="resetAllQueryArguments")
    def reset_all_query_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllQueryArguments", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCookies")
    def reset_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookies", []))

    @jsii.member(jsii_name="resetJsonBody")
    def reset_json_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonBody", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSingleHeader")
    def reset_single_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleHeader", []))

    @jsii.member(jsii_name="resetSingleQueryArgument")
    def reset_single_query_argument(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleQueryArgument", []))

    @jsii.member(jsii_name="resetUriPath")
    def reset_uri_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUriPath", []))

    @builtins.property
    @jsii.member(jsii_name="allQueryArguments")
    def all_query_arguments(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArgumentsOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArgumentsOutputReference, jsii.get(self, "allQueryArguments"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBodyOutputReference, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="jsonBody")
    def json_body(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference, jsii.get(self, "jsonBody"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethodOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethodOutputReference, jsii.get(self, "method"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryStringOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="singleHeader")
    def single_header(
        self,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference", jsii.get(self, "singleHeader"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgument")
    def single_query_argument(
        self,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference", jsii.get(self, "singleQueryArgument"))

    @builtins.property
    @jsii.member(jsii_name="uriPath")
    def uri_path(
        self,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPathOutputReference":
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPathOutputReference", jsii.get(self, "uriPath"))

    @builtins.property
    @jsii.member(jsii_name="allQueryArgumentsInput")
    def all_query_arguments_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments], jsii.get(self, "allQueryArgumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonBodyInput")
    def json_body_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody], jsii.get(self, "jsonBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="singleHeaderInput")
    def single_header_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader"], jsii.get(self, "singleHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgumentInput")
    def single_query_argument_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument"], jsii.get(self, "singleQueryArgumentInput"))

    @builtins.property
    @jsii.member(jsii_name="uriPathInput")
    def uri_path_input(
        self,
    ) -> typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath"]:
        return typing.cast(typing.Optional["Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath"], jsii.get(self, "uriPathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#name Wafv2RuleGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPathOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFieldToMatch")
    def put_field_to_match(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments, typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody, typing.Dict[str, typing.Any]]] = None,
        cookies: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies, typing.Dict[str, typing.Any]]] = None,
        json_body: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody, typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod, typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString, typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader, typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument, typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#all_query_arguments Wafv2RuleGroup#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#body Wafv2RuleGroup#body}
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cookies Wafv2RuleGroup#cookies}
        :param json_body: json_body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#json_body Wafv2RuleGroup#json_body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#method Wafv2RuleGroup#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#query_string Wafv2RuleGroup#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_header Wafv2RuleGroup#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#single_query_argument Wafv2RuleGroup#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#uri_path Wafv2RuleGroup#uri_path}
        '''
        value = Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch(
            all_query_arguments=all_query_arguments,
            body=body,
            cookies=cookies,
            json_body=json_body,
            method=method,
            query_string=query_string,
            single_header=single_header,
            single_query_argument=single_query_argument,
            uri_path=uri_path,
        )

        return typing.cast(None, jsii.invoke(self, "putFieldToMatch", [value]))

    @jsii.member(jsii_name="putTextTransformation")
    def put_text_transformation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference.put_text_transformation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTextTransformation", [value]))

    @jsii.member(jsii_name="resetFieldToMatch")
    def reset_field_to_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldToMatch", []))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatch")
    def field_to_match(
        self,
    ) -> Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchOutputReference:
        return typing.cast(Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchOutputReference, jsii.get(self, "fieldToMatch"))

    @builtins.property
    @jsii.member(jsii_name="textTransformation")
    def text_transformation(
        self,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList":
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList", jsii.get(self, "textTransformation"))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatchInput")
    def field_to_match_input(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch], jsii.get(self, "fieldToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="textTransformationInput")
    def text_transformation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation"]]], jsii.get(self, "textTransformationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatement]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleStatementXssMatchStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation",
    jsii_struct_bases=[],
    name_mapping={"priority": "priority", "type": "type"},
)
class Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation:
    def __init__(self, *, priority: jsii.Number, type: builtins.str) -> None:
        '''
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation.__init__)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "type": type,
        }

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#priority Wafv2RuleGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#type Wafv2RuleGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleVisibilityConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_metrics_enabled": "cloudwatchMetricsEnabled",
        "metric_name": "metricName",
        "sampled_requests_enabled": "sampledRequestsEnabled",
    },
)
class Wafv2RuleGroupRuleVisibilityConfig:
    def __init__(
        self,
        *,
        cloudwatch_metrics_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        metric_name: builtins.str,
        sampled_requests_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param cloudwatch_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cloudwatch_metrics_enabled Wafv2RuleGroup#cloudwatch_metrics_enabled}.
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#metric_name Wafv2RuleGroup#metric_name}.
        :param sampled_requests_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sampled_requests_enabled Wafv2RuleGroup#sampled_requests_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleVisibilityConfig.__init__)
            check_type(argname="argument cloudwatch_metrics_enabled", value=cloudwatch_metrics_enabled, expected_type=type_hints["cloudwatch_metrics_enabled"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument sampled_requests_enabled", value=sampled_requests_enabled, expected_type=type_hints["sampled_requests_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloudwatch_metrics_enabled": cloudwatch_metrics_enabled,
            "metric_name": metric_name,
            "sampled_requests_enabled": sampled_requests_enabled,
        }

    @builtins.property
    def cloudwatch_metrics_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cloudwatch_metrics_enabled Wafv2RuleGroup#cloudwatch_metrics_enabled}.'''
        result = self._values.get("cloudwatch_metrics_enabled")
        assert result is not None, "Required property 'cloudwatch_metrics_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#metric_name Wafv2RuleGroup#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sampled_requests_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sampled_requests_enabled Wafv2RuleGroup#sampled_requests_enabled}.'''
        result = self._values.get("sampled_requests_enabled")
        assert result is not None, "Required property 'sampled_requests_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupRuleVisibilityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupRuleVisibilityConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupRuleVisibilityConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupRuleVisibilityConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetricsEnabledInput")
    def cloudwatch_metrics_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cloudwatchMetricsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sampledRequestsEnabledInput")
    def sampled_requests_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sampledRequestsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetricsEnabled")
    def cloudwatch_metrics_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cloudwatchMetricsEnabled"))

    @cloudwatch_metrics_enabled.setter
    def cloudwatch_metrics_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleVisibilityConfigOutputReference, "cloudwatch_metrics_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchMetricsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleVisibilityConfigOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="sampledRequestsEnabled")
    def sampled_requests_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sampledRequestsEnabled"))

    @sampled_requests_enabled.setter
    def sampled_requests_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleVisibilityConfigOutputReference, "sampled_requests_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampledRequestsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupRuleVisibilityConfig]:
        return typing.cast(typing.Optional[Wafv2RuleGroupRuleVisibilityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupRuleVisibilityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupRuleVisibilityConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupVisibilityConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_metrics_enabled": "cloudwatchMetricsEnabled",
        "metric_name": "metricName",
        "sampled_requests_enabled": "sampledRequestsEnabled",
    },
)
class Wafv2RuleGroupVisibilityConfig:
    def __init__(
        self,
        *,
        cloudwatch_metrics_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        metric_name: builtins.str,
        sampled_requests_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param cloudwatch_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cloudwatch_metrics_enabled Wafv2RuleGroup#cloudwatch_metrics_enabled}.
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#metric_name Wafv2RuleGroup#metric_name}.
        :param sampled_requests_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sampled_requests_enabled Wafv2RuleGroup#sampled_requests_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupVisibilityConfig.__init__)
            check_type(argname="argument cloudwatch_metrics_enabled", value=cloudwatch_metrics_enabled, expected_type=type_hints["cloudwatch_metrics_enabled"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument sampled_requests_enabled", value=sampled_requests_enabled, expected_type=type_hints["sampled_requests_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloudwatch_metrics_enabled": cloudwatch_metrics_enabled,
            "metric_name": metric_name,
            "sampled_requests_enabled": sampled_requests_enabled,
        }

    @builtins.property
    def cloudwatch_metrics_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#cloudwatch_metrics_enabled Wafv2RuleGroup#cloudwatch_metrics_enabled}.'''
        result = self._values.get("cloudwatch_metrics_enabled")
        assert result is not None, "Required property 'cloudwatch_metrics_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#metric_name Wafv2RuleGroup#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sampled_requests_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_rule_group#sampled_requests_enabled Wafv2RuleGroup#sampled_requests_enabled}.'''
        result = self._values.get("sampled_requests_enabled")
        assert result is not None, "Required property 'sampled_requests_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2RuleGroupVisibilityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2RuleGroupVisibilityConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2RuleGroup.Wafv2RuleGroupVisibilityConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Wafv2RuleGroupVisibilityConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetricsEnabledInput")
    def cloudwatch_metrics_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cloudwatchMetricsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sampledRequestsEnabledInput")
    def sampled_requests_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sampledRequestsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetricsEnabled")
    def cloudwatch_metrics_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cloudwatchMetricsEnabled"))

    @cloudwatch_metrics_enabled.setter
    def cloudwatch_metrics_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupVisibilityConfigOutputReference, "cloudwatch_metrics_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchMetricsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupVisibilityConfigOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="sampledRequestsEnabled")
    def sampled_requests_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sampledRequestsEnabled"))

    @sampled_requests_enabled.setter
    def sampled_requests_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupVisibilityConfigOutputReference, "sampled_requests_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampledRequestsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Wafv2RuleGroupVisibilityConfig]:
        return typing.cast(typing.Optional[Wafv2RuleGroupVisibilityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2RuleGroupVisibilityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Wafv2RuleGroupVisibilityConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Wafv2RuleGroup",
    "Wafv2RuleGroupConfig",
    "Wafv2RuleGroupCustomResponseBody",
    "Wafv2RuleGroupCustomResponseBodyList",
    "Wafv2RuleGroupCustomResponseBodyOutputReference",
    "Wafv2RuleGroupRule",
    "Wafv2RuleGroupRuleAction",
    "Wafv2RuleGroupRuleActionAllow",
    "Wafv2RuleGroupRuleActionAllowCustomRequestHandling",
    "Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader",
    "Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderList",
    "Wafv2RuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderOutputReference",
    "Wafv2RuleGroupRuleActionAllowCustomRequestHandlingOutputReference",
    "Wafv2RuleGroupRuleActionAllowOutputReference",
    "Wafv2RuleGroupRuleActionBlock",
    "Wafv2RuleGroupRuleActionBlockCustomResponse",
    "Wafv2RuleGroupRuleActionBlockCustomResponseOutputReference",
    "Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeader",
    "Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderList",
    "Wafv2RuleGroupRuleActionBlockCustomResponseResponseHeaderOutputReference",
    "Wafv2RuleGroupRuleActionBlockOutputReference",
    "Wafv2RuleGroupRuleActionCount",
    "Wafv2RuleGroupRuleActionCountCustomRequestHandling",
    "Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeader",
    "Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderList",
    "Wafv2RuleGroupRuleActionCountCustomRequestHandlingInsertHeaderOutputReference",
    "Wafv2RuleGroupRuleActionCountCustomRequestHandlingOutputReference",
    "Wafv2RuleGroupRuleActionCountOutputReference",
    "Wafv2RuleGroupRuleActionOutputReference",
    "Wafv2RuleGroupRuleList",
    "Wafv2RuleGroupRuleOutputReference",
    "Wafv2RuleGroupRuleRuleLabel",
    "Wafv2RuleGroupRuleRuleLabelList",
    "Wafv2RuleGroupRuleRuleLabelOutputReference",
    "Wafv2RuleGroupRuleStatement",
    "Wafv2RuleGroupRuleStatementAndStatement",
    "Wafv2RuleGroupRuleStatementAndStatementOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatement",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatch",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArgumentsOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBody",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchBodyOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternList",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchMethodOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryStringOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeaderOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgumentOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath",
    "Wafv2RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPathOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementOutputReference",
    "Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformation",
    "Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationList",
    "Wafv2RuleGroupRuleStatementByteMatchStatementTextTransformationOutputReference",
    "Wafv2RuleGroupRuleStatementGeoMatchStatement",
    "Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig",
    "Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfigOutputReference",
    "Wafv2RuleGroupRuleStatementGeoMatchStatementOutputReference",
    "Wafv2RuleGroupRuleStatementIpSetReferenceStatement",
    "Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig",
    "Wafv2RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfigOutputReference",
    "Wafv2RuleGroupRuleStatementIpSetReferenceStatementOutputReference",
    "Wafv2RuleGroupRuleStatementLabelMatchStatement",
    "Wafv2RuleGroupRuleStatementLabelMatchStatementOutputReference",
    "Wafv2RuleGroupRuleStatementNotStatement",
    "Wafv2RuleGroupRuleStatementNotStatementOutputReference",
    "Wafv2RuleGroupRuleStatementOrStatement",
    "Wafv2RuleGroupRuleStatementOrStatementOutputReference",
    "Wafv2RuleGroupRuleStatementOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatement",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArgumentsOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBodyOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternList",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethodOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryStringOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPathOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementOutputReference",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationList",
    "Wafv2RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformationOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatement",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatch",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArgumentsOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBodyOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternList",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethodOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryStringOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeaderOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPathOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementOutputReference",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformation",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationList",
    "Wafv2RuleGroupRuleStatementSizeConstraintStatementTextTransformationOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatement",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatch",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArgumentsOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchBodyOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternList",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethodOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryStringOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeaderOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgumentOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPathOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementOutputReference",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformation",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationList",
    "Wafv2RuleGroupRuleStatementSqliMatchStatementTextTransformationOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatement",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatch",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArgumentsOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBody",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchBodyOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternList",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAllOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchMethodOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryStringOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeaderOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgumentOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath",
    "Wafv2RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPathOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementOutputReference",
    "Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformation",
    "Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationList",
    "Wafv2RuleGroupRuleStatementXssMatchStatementTextTransformationOutputReference",
    "Wafv2RuleGroupRuleVisibilityConfig",
    "Wafv2RuleGroupRuleVisibilityConfigOutputReference",
    "Wafv2RuleGroupVisibilityConfig",
    "Wafv2RuleGroupVisibilityConfigOutputReference",
]

publication.publish()
