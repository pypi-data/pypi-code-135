'''
# `aws_sagemaker_domain`

Refer to the Terraform Registory for docs: [`aws_sagemaker_domain`](https://www.terraform.io/docs/providers/aws/r/sagemaker_domain).
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


class SagemakerDomain(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain aws_sagemaker_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        auth_mode: builtins.str,
        default_user_settings: typing.Union["SagemakerDomainDefaultUserSettings", typing.Dict[str, typing.Any]],
        domain_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_network_access_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        retention_policy: typing.Optional[typing.Union["SagemakerDomainRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain aws_sagemaker_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auth_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#auth_mode SagemakerDomain#auth_mode}.
        :param default_user_settings: default_user_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_user_settings SagemakerDomain#default_user_settings}
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#domain_name SagemakerDomain#domain_name}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#subnet_ids SagemakerDomain#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#vpc_id SagemakerDomain#vpc_id}.
        :param app_network_access_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#app_network_access_type SagemakerDomain#app_network_access_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#id SagemakerDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#kms_key_id SagemakerDomain#kms_key_id}.
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#retention_policy SagemakerDomain#retention_policy}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tags SagemakerDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tags_all SagemakerDomain#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerDomainConfig(
            auth_mode=auth_mode,
            default_user_settings=default_user_settings,
            domain_name=domain_name,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            app_network_access_type=app_network_access_type,
            id=id,
            kms_key_id=kms_key_id,
            retention_policy=retention_policy,
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

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDefaultUserSettings")
    def put_default_user_settings(
        self,
        *,
        execution_role: builtins.str,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings", typing.Dict[str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings", typing.Dict[str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        sharing_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSharingSettings", typing.Dict[str, typing.Any]]] = None,
        tensor_board_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#execution_role SagemakerDomain#execution_role}.
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#security_groups SagemakerDomain#security_groups}.
        :param sharing_settings: sharing_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sharing_settings SagemakerDomain#sharing_settings}
        :param tensor_board_app_settings: tensor_board_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tensor_board_app_settings SagemakerDomain#tensor_board_app_settings}
        '''
        value = SagemakerDomainDefaultUserSettings(
            execution_role=execution_role,
            jupyter_server_app_settings=jupyter_server_app_settings,
            kernel_gateway_app_settings=kernel_gateway_app_settings,
            security_groups=security_groups,
            sharing_settings=sharing_settings,
            tensor_board_app_settings=tensor_board_app_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultUserSettings", [value]))

    @jsii.member(jsii_name="putRetentionPolicy")
    def put_retention_policy(
        self,
        *,
        home_efs_file_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param home_efs_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#home_efs_file_system SagemakerDomain#home_efs_file_system}.
        '''
        value = SagemakerDomainRetentionPolicy(
            home_efs_file_system=home_efs_file_system
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionPolicy", [value]))

    @jsii.member(jsii_name="resetAppNetworkAccessType")
    def reset_app_network_access_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppNetworkAccessType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetRetentionPolicy")
    def reset_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicy", []))

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
    @jsii.member(jsii_name="defaultUserSettings")
    def default_user_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsOutputReference", jsii.get(self, "defaultUserSettings"))

    @builtins.property
    @jsii.member(jsii_name="homeEfsFileSystemId")
    def home_efs_file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeEfsFileSystemId"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(self) -> "SagemakerDomainRetentionPolicyOutputReference":
        return typing.cast("SagemakerDomainRetentionPolicyOutputReference", jsii.get(self, "retentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="singleSignOnManagedApplicationInstanceId")
    def single_sign_on_managed_application_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleSignOnManagedApplicationInstanceId"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="appNetworkAccessTypeInput")
    def app_network_access_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appNetworkAccessTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authModeInput")
    def auth_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authModeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultUserSettingsInput")
    def default_user_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettings"], jsii.get(self, "defaultUserSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyInput")
    def retention_policy_input(
        self,
    ) -> typing.Optional["SagemakerDomainRetentionPolicy"]:
        return typing.cast(typing.Optional["SagemakerDomainRetentionPolicy"], jsii.get(self, "retentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

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
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appNetworkAccessType")
    def app_network_access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appNetworkAccessType"))

    @app_network_access_type.setter
    def app_network_access_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "app_network_access_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appNetworkAccessType", value)

    @builtins.property
    @jsii.member(jsii_name="authMode")
    def auth_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMode"))

    @auth_mode.setter
    def auth_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "auth_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMode", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomain, "vpc_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auth_mode": "authMode",
        "default_user_settings": "defaultUserSettings",
        "domain_name": "domainName",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "app_network_access_type": "appNetworkAccessType",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "retention_policy": "retentionPolicy",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerDomainConfig(cdktf.TerraformMetaArguments):
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
        auth_mode: builtins.str,
        default_user_settings: typing.Union["SagemakerDomainDefaultUserSettings", typing.Dict[str, typing.Any]],
        domain_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_network_access_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        retention_policy: typing.Optional[typing.Union["SagemakerDomainRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
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
        :param auth_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#auth_mode SagemakerDomain#auth_mode}.
        :param default_user_settings: default_user_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_user_settings SagemakerDomain#default_user_settings}
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#domain_name SagemakerDomain#domain_name}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#subnet_ids SagemakerDomain#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#vpc_id SagemakerDomain#vpc_id}.
        :param app_network_access_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#app_network_access_type SagemakerDomain#app_network_access_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#id SagemakerDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#kms_key_id SagemakerDomain#kms_key_id}.
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#retention_policy SagemakerDomain#retention_policy}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tags SagemakerDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tags_all SagemakerDomain#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_user_settings, dict):
            default_user_settings = SagemakerDomainDefaultUserSettings(**default_user_settings)
        if isinstance(retention_policy, dict):
            retention_policy = SagemakerDomainRetentionPolicy(**retention_policy)
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auth_mode", value=auth_mode, expected_type=type_hints["auth_mode"])
            check_type(argname="argument default_user_settings", value=default_user_settings, expected_type=type_hints["default_user_settings"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument app_network_access_type", value=app_network_access_type, expected_type=type_hints["app_network_access_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "auth_mode": auth_mode,
            "default_user_settings": default_user_settings,
            "domain_name": domain_name,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
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
        if app_network_access_type is not None:
            self._values["app_network_access_type"] = app_network_access_type
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy
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
    def auth_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#auth_mode SagemakerDomain#auth_mode}.'''
        result = self._values.get("auth_mode")
        assert result is not None, "Required property 'auth_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_user_settings(self) -> "SagemakerDomainDefaultUserSettings":
        '''default_user_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_user_settings SagemakerDomain#default_user_settings}
        '''
        result = self._values.get("default_user_settings")
        assert result is not None, "Required property 'default_user_settings' is missing"
        return typing.cast("SagemakerDomainDefaultUserSettings", result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#domain_name SagemakerDomain#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#subnet_ids SagemakerDomain#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#vpc_id SagemakerDomain#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_network_access_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#app_network_access_type SagemakerDomain#app_network_access_type}.'''
        result = self._values.get("app_network_access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#id SagemakerDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#kms_key_id SagemakerDomain#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_policy(self) -> typing.Optional["SagemakerDomainRetentionPolicy"]:
        '''retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#retention_policy SagemakerDomain#retention_policy}
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional["SagemakerDomainRetentionPolicy"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tags SagemakerDomain#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tags_all SagemakerDomain#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettings",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role": "executionRole",
        "jupyter_server_app_settings": "jupyterServerAppSettings",
        "kernel_gateway_app_settings": "kernelGatewayAppSettings",
        "security_groups": "securityGroups",
        "sharing_settings": "sharingSettings",
        "tensor_board_app_settings": "tensorBoardAppSettings",
    },
)
class SagemakerDomainDefaultUserSettings:
    def __init__(
        self,
        *,
        execution_role: builtins.str,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings", typing.Dict[str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings", typing.Dict[str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        sharing_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSharingSettings", typing.Dict[str, typing.Any]]] = None,
        tensor_board_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#execution_role SagemakerDomain#execution_role}.
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#security_groups SagemakerDomain#security_groups}.
        :param sharing_settings: sharing_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sharing_settings SagemakerDomain#sharing_settings}
        :param tensor_board_app_settings: tensor_board_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tensor_board_app_settings SagemakerDomain#tensor_board_app_settings}
        '''
        if isinstance(jupyter_server_app_settings, dict):
            jupyter_server_app_settings = SagemakerDomainDefaultUserSettingsJupyterServerAppSettings(**jupyter_server_app_settings)
        if isinstance(kernel_gateway_app_settings, dict):
            kernel_gateway_app_settings = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings(**kernel_gateway_app_settings)
        if isinstance(sharing_settings, dict):
            sharing_settings = SagemakerDomainDefaultUserSettingsSharingSettings(**sharing_settings)
        if isinstance(tensor_board_app_settings, dict):
            tensor_board_app_settings = SagemakerDomainDefaultUserSettingsTensorBoardAppSettings(**tensor_board_app_settings)
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettings.__init__)
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument jupyter_server_app_settings", value=jupyter_server_app_settings, expected_type=type_hints["jupyter_server_app_settings"])
            check_type(argname="argument kernel_gateway_app_settings", value=kernel_gateway_app_settings, expected_type=type_hints["kernel_gateway_app_settings"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument sharing_settings", value=sharing_settings, expected_type=type_hints["sharing_settings"])
            check_type(argname="argument tensor_board_app_settings", value=tensor_board_app_settings, expected_type=type_hints["tensor_board_app_settings"])
        self._values: typing.Dict[str, typing.Any] = {
            "execution_role": execution_role,
        }
        if jupyter_server_app_settings is not None:
            self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
        if kernel_gateway_app_settings is not None:
            self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if sharing_settings is not None:
            self._values["sharing_settings"] = sharing_settings
        if tensor_board_app_settings is not None:
            self._values["tensor_board_app_settings"] = tensor_board_app_settings

    @builtins.property
    def execution_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#execution_role SagemakerDomain#execution_role}.'''
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def jupyter_server_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings"]:
        '''jupyter_server_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        '''
        result = self._values.get("jupyter_server_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings"], result)

    @builtins.property
    def kernel_gateway_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings"]:
        '''kernel_gateway_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        '''
        result = self._values.get("kernel_gateway_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings"], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#security_groups SagemakerDomain#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sharing_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"]:
        '''sharing_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sharing_settings SagemakerDomain#sharing_settings}
        '''
        result = self._values.get("sharing_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"], result)

    @builtins.property
    def tensor_board_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"]:
        '''tensor_board_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#tensor_board_app_settings SagemakerDomain#tensor_board_app_settings}
        '''
        result = self._values.get("tensor_board_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "default_resource_spec": "defaultResourceSpec",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterServerAppSettings:
    def __init__(
        self,
        *,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec", typing.Dict[str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsJupyterServerAppSettings.__init__)
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterServerAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec.__init__)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, "lifecycle_config_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, "sagemaker_image_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, "sagemaker_image_version_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference, "lifecycle_config_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings:
    def __init__(
        self,
        *,
        custom_image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage", typing.Dict[str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec", typing.Dict[str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings.__init__)
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#image_name SagemakerDomain#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage.__init__)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#image_name SagemakerDomain#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference, "app_image_config_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference, "image_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference, "image_version_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec.__init__)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, "lifecycle_config_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, "sagemaker_image_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, "sagemaker_image_version_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference.put_custom_image)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList:
        return typing.cast(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference, "lifecycle_config_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerDomainDefaultUserSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putJupyterServerAppSettings")
    def put_jupyter_server_app_settings(
        self,
        *,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec, typing.Dict[str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterServerAppSettings(
            default_resource_spec=default_resource_spec,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putJupyterServerAppSettings", [value]))

    @jsii.member(jsii_name="putKernelGatewayAppSettings")
    def put_kernel_gateway_app_settings(
        self,
        *,
        custom_image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec, typing.Dict[str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings(
            custom_image=custom_image,
            default_resource_spec=default_resource_spec,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putKernelGatewayAppSettings", [value]))

    @jsii.member(jsii_name="putSharingSettings")
    def put_sharing_settings(
        self,
        *,
        notebook_output_option: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
        s3_output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notebook_output_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#notebook_output_option SagemakerDomain#notebook_output_option}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#s3_output_path SagemakerDomain#s3_output_path}.
        '''
        value = SagemakerDomainDefaultUserSettingsSharingSettings(
            notebook_output_option=notebook_output_option,
            s3_kms_key_id=s3_kms_key_id,
            s3_output_path=s3_output_path,
        )

        return typing.cast(None, jsii.invoke(self, "putSharingSettings", [value]))

    @jsii.member(jsii_name="putTensorBoardAppSettings")
    def put_tensor_board_app_settings(
        self,
        *,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        value = SagemakerDomainDefaultUserSettingsTensorBoardAppSettings(
            default_resource_spec=default_resource_spec
        )

        return typing.cast(None, jsii.invoke(self, "putTensorBoardAppSettings", [value]))

    @jsii.member(jsii_name="resetJupyterServerAppSettings")
    def reset_jupyter_server_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJupyterServerAppSettings", []))

    @jsii.member(jsii_name="resetKernelGatewayAppSettings")
    def reset_kernel_gateway_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernelGatewayAppSettings", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSharingSettings")
    def reset_sharing_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharingSettings", []))

    @jsii.member(jsii_name="resetTensorBoardAppSettings")
    def reset_tensor_board_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTensorBoardAppSettings", []))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference, jsii.get(self, "jupyterServerAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference, jsii.get(self, "kernelGatewayAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="sharingSettings")
    def sharing_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference", jsii.get(self, "sharingSettings"))

    @builtins.property
    @jsii.member(jsii_name="tensorBoardAppSettings")
    def tensor_board_app_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference", jsii.get(self, "tensorBoardAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleInput")
    def execution_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettingsInput")
    def jupyter_server_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings], jsii.get(self, "jupyterServerAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettingsInput")
    def kernel_gateway_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings], jsii.get(self, "kernelGatewayAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="sharingSettingsInput")
    def sharing_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"], jsii.get(self, "sharingSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="tensorBoardAppSettingsInput")
    def tensor_board_app_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"], jsii.get(self, "tensorBoardAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsOutputReference, "execution_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsOutputReference, "security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerDomainDefaultUserSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSharingSettings",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_output_option": "notebookOutputOption",
        "s3_kms_key_id": "s3KmsKeyId",
        "s3_output_path": "s3OutputPath",
    },
)
class SagemakerDomainDefaultUserSettingsSharingSettings:
    def __init__(
        self,
        *,
        notebook_output_option: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
        s3_output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notebook_output_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#notebook_output_option SagemakerDomain#notebook_output_option}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#s3_output_path SagemakerDomain#s3_output_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsSharingSettings.__init__)
            check_type(argname="argument notebook_output_option", value=notebook_output_option, expected_type=type_hints["notebook_output_option"])
            check_type(argname="argument s3_kms_key_id", value=s3_kms_key_id, expected_type=type_hints["s3_kms_key_id"])
            check_type(argname="argument s3_output_path", value=s3_output_path, expected_type=type_hints["s3_output_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if notebook_output_option is not None:
            self._values["notebook_output_option"] = notebook_output_option
        if s3_kms_key_id is not None:
            self._values["s3_kms_key_id"] = s3_kms_key_id
        if s3_output_path is not None:
            self._values["s3_output_path"] = s3_output_path

    @builtins.property
    def notebook_output_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#notebook_output_option SagemakerDomain#notebook_output_option}.'''
        result = self._values.get("notebook_output_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.'''
        result = self._values.get("s3_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_output_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#s3_output_path SagemakerDomain#s3_output_path}.'''
        result = self._values.get("s3_output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsSharingSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNotebookOutputOption")
    def reset_notebook_output_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebookOutputOption", []))

    @jsii.member(jsii_name="resetS3KmsKeyId")
    def reset_s3_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KmsKeyId", []))

    @jsii.member(jsii_name="resetS3OutputPath")
    def reset_s3_output_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3OutputPath", []))

    @builtins.property
    @jsii.member(jsii_name="notebookOutputOptionInput")
    def notebook_output_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookOutputOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyIdInput")
    def s3_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputPathInput")
    def s3_output_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3OutputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="notebookOutputOption")
    def notebook_output_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notebookOutputOption"))

    @notebook_output_option.setter
    def notebook_output_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference, "notebook_output_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebookOutputOption", value)

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyId")
    def s3_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KmsKeyId"))

    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference, "s3_kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="s3OutputPath")
    def s3_output_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3OutputPath"))

    @s3_output_path.setter
    def s3_output_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference, "s3_output_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3OutputPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsSharingSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsSharingSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsSharingSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettings",
    jsii_struct_bases=[],
    name_mapping={"default_resource_spec": "defaultResourceSpec"},
)
class SagemakerDomainDefaultUserSettingsTensorBoardAppSettings:
    def __init__(
        self,
        *,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsTensorBoardAppSettings.__init__)
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsTensorBoardAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec.__init__)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, "lifecycle_config_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, "sagemaker_image_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, "sagemaker_image_version_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"home_efs_file_system": "homeEfsFileSystem"},
)
class SagemakerDomainRetentionPolicy:
    def __init__(
        self,
        *,
        home_efs_file_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param home_efs_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#home_efs_file_system SagemakerDomain#home_efs_file_system}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SagemakerDomainRetentionPolicy.__init__)
            check_type(argname="argument home_efs_file_system", value=home_efs_file_system, expected_type=type_hints["home_efs_file_system"])
        self._values: typing.Dict[str, typing.Any] = {}
        if home_efs_file_system is not None:
            self._values["home_efs_file_system"] = home_efs_file_system

    @builtins.property
    def home_efs_file_system(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_domain#home_efs_file_system SagemakerDomain#home_efs_file_system}.'''
        result = self._values.get("home_efs_file_system")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerDomain.SagemakerDomainRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(SagemakerDomainRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHomeEfsFileSystem")
    def reset_home_efs_file_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeEfsFileSystem", []))

    @builtins.property
    @jsii.member(jsii_name="homeEfsFileSystemInput")
    def home_efs_file_system_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeEfsFileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="homeEfsFileSystem")
    def home_efs_file_system(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeEfsFileSystem"))

    @home_efs_file_system.setter
    def home_efs_file_system(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainRetentionPolicyOutputReference, "home_efs_file_system").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeEfsFileSystem", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerDomainRetentionPolicy]:
        return typing.cast(typing.Optional[SagemakerDomainRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SagemakerDomainRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerDomain",
    "SagemakerDomainConfig",
    "SagemakerDomainDefaultUserSettings",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettings",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsSharingSettings",
    "SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettings",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference",
    "SagemakerDomainRetentionPolicy",
    "SagemakerDomainRetentionPolicyOutputReference",
]

publication.publish()
