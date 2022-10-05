'''
# `aws_elasticache_global_replication_group`

Refer to the Terraform Registory for docs: [`aws_elasticache_global_replication_group`](https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group).
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


class ElasticacheGlobalReplicationGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticacheGlobalReplicationGroup.ElasticacheGlobalReplicationGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group aws_elasticache_global_replication_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        global_replication_group_id_suffix: builtins.str,
        primary_replication_group_id: builtins.str,
        engine_version: typing.Optional[builtins.str] = None,
        global_replication_group_description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group aws_elasticache_global_replication_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param global_replication_group_id_suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#global_replication_group_id_suffix ElasticacheGlobalReplicationGroup#global_replication_group_id_suffix}.
        :param primary_replication_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#primary_replication_group_id ElasticacheGlobalReplicationGroup#primary_replication_group_id}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#engine_version ElasticacheGlobalReplicationGroup#engine_version}.
        :param global_replication_group_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#global_replication_group_description ElasticacheGlobalReplicationGroup#global_replication_group_description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#id ElasticacheGlobalReplicationGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#parameter_group_name ElasticacheGlobalReplicationGroup#parameter_group_name}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticacheGlobalReplicationGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElasticacheGlobalReplicationGroupConfig(
            global_replication_group_id_suffix=global_replication_group_id_suffix,
            primary_replication_group_id=primary_replication_group_id,
            engine_version=engine_version,
            global_replication_group_description=global_replication_group_description,
            id=id,
            parameter_group_name=parameter_group_name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

    @jsii.member(jsii_name="resetGlobalReplicationGroupDescription")
    def reset_global_replication_group_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalReplicationGroupDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameterGroupName")
    def reset_parameter_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameterGroupName", []))

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
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "atRestEncryptionEnabled"))

    @builtins.property
    @jsii.member(jsii_name="authTokenEnabled")
    def auth_token_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "authTokenEnabled"))

    @builtins.property
    @jsii.member(jsii_name="cacheNodeType")
    def cache_node_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheNodeType"))

    @builtins.property
    @jsii.member(jsii_name="clusterEnabled")
    def cluster_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "clusterEnabled"))

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionActual")
    def engine_version_actual(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersionActual"))

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupId")
    def global_replication_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalReplicationGroupId"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "transitEncryptionEnabled"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionInput")
    def engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupDescriptionInput")
    def global_replication_group_description_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupIdSuffixInput")
    def global_replication_group_id_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupIdSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterGroupNameInput")
    def parameter_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryReplicationGroupIdInput")
    def primary_replication_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryReplicationGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticacheGlobalReplicationGroup, "engine_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalReplicationGroupDescription"))

    @global_replication_group_description.setter
    def global_replication_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticacheGlobalReplicationGroup, "global_replication_group_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalReplicationGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalReplicationGroupIdSuffix"))

    @global_replication_group_id_suffix.setter
    def global_replication_group_id_suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticacheGlobalReplicationGroup, "global_replication_group_id_suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalReplicationGroupIdSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticacheGlobalReplicationGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticacheGlobalReplicationGroup, "parameter_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="primaryReplicationGroupId")
    def primary_replication_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryReplicationGroupId"))

    @primary_replication_group_id.setter
    def primary_replication_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticacheGlobalReplicationGroup, "primary_replication_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryReplicationGroupId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticacheGlobalReplicationGroup.ElasticacheGlobalReplicationGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "global_replication_group_id_suffix": "globalReplicationGroupIdSuffix",
        "primary_replication_group_id": "primaryReplicationGroupId",
        "engine_version": "engineVersion",
        "global_replication_group_description": "globalReplicationGroupDescription",
        "id": "id",
        "parameter_group_name": "parameterGroupName",
    },
)
class ElasticacheGlobalReplicationGroupConfig(cdktf.TerraformMetaArguments):
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
        global_replication_group_id_suffix: builtins.str,
        primary_replication_group_id: builtins.str,
        engine_version: typing.Optional[builtins.str] = None,
        global_replication_group_description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param global_replication_group_id_suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#global_replication_group_id_suffix ElasticacheGlobalReplicationGroup#global_replication_group_id_suffix}.
        :param primary_replication_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#primary_replication_group_id ElasticacheGlobalReplicationGroup#primary_replication_group_id}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#engine_version ElasticacheGlobalReplicationGroup#engine_version}.
        :param global_replication_group_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#global_replication_group_description ElasticacheGlobalReplicationGroup#global_replication_group_description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#id ElasticacheGlobalReplicationGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#parameter_group_name ElasticacheGlobalReplicationGroup#parameter_group_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticacheGlobalReplicationGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument global_replication_group_id_suffix", value=global_replication_group_id_suffix, expected_type=type_hints["global_replication_group_id_suffix"])
            check_type(argname="argument primary_replication_group_id", value=primary_replication_group_id, expected_type=type_hints["primary_replication_group_id"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument global_replication_group_description", value=global_replication_group_description, expected_type=type_hints["global_replication_group_description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "global_replication_group_id_suffix": global_replication_group_id_suffix,
            "primary_replication_group_id": primary_replication_group_id,
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
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if global_replication_group_description is not None:
            self._values["global_replication_group_description"] = global_replication_group_description
        if id is not None:
            self._values["id"] = id
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name

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
    def global_replication_group_id_suffix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#global_replication_group_id_suffix ElasticacheGlobalReplicationGroup#global_replication_group_id_suffix}.'''
        result = self._values.get("global_replication_group_id_suffix")
        assert result is not None, "Required property 'global_replication_group_id_suffix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary_replication_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#primary_replication_group_id ElasticacheGlobalReplicationGroup#primary_replication_group_id}.'''
        result = self._values.get("primary_replication_group_id")
        assert result is not None, "Required property 'primary_replication_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#engine_version ElasticacheGlobalReplicationGroup#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_replication_group_description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#global_replication_group_description ElasticacheGlobalReplicationGroup#global_replication_group_description}.'''
        result = self._values.get("global_replication_group_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#id ElasticacheGlobalReplicationGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_global_replication_group#parameter_group_name ElasticacheGlobalReplicationGroup#parameter_group_name}.'''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticacheGlobalReplicationGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ElasticacheGlobalReplicationGroup",
    "ElasticacheGlobalReplicationGroupConfig",
]

publication.publish()
