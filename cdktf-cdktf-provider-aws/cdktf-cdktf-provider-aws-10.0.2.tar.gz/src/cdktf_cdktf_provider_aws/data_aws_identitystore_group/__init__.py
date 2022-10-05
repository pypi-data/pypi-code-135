'''
# `data_aws_identitystore_group`

Refer to the Terraform Registory for docs: [`data_aws_identitystore_group`](https://www.terraform.io/docs/providers/aws/d/identitystore_group).
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


class DataAwsIdentitystoreGroup(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group aws_identitystore_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsIdentitystoreGroupFilter", typing.Dict[str, typing.Any]]]],
        identity_store_id: builtins.str,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group aws_identitystore_group} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#filter DataAwsIdentitystoreGroup#filter}
        :param identity_store_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#identity_store_id DataAwsIdentitystoreGroup#identity_store_id}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#group_id DataAwsIdentitystoreGroup#group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsIdentitystoreGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsIdentitystoreGroupConfig(
            filter=filter,
            identity_store_id=identity_store_id,
            group_id=group_id,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsIdentitystoreGroupFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsIdentitystoreGroup.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsIdentitystoreGroupFilterList":
        return typing.cast("DataAwsIdentitystoreGroupFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsIdentitystoreGroupFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsIdentitystoreGroupFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="identityStoreIdInput")
    def identity_store_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityStoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroup, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroup, "identity_store_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filter": "filter",
        "identity_store_id": "identityStoreId",
        "group_id": "groupId",
        "id": "id",
    },
)
class DataAwsIdentitystoreGroupConfig(cdktf.TerraformMetaArguments):
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
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsIdentitystoreGroupFilter", typing.Dict[str, typing.Any]]]],
        identity_store_id: builtins.str,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#filter DataAwsIdentitystoreGroup#filter}
        :param identity_store_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#identity_store_id DataAwsIdentitystoreGroup#identity_store_id}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#group_id DataAwsIdentitystoreGroup#group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsIdentitystoreGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
            "identity_store_id": identity_store_id,
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
        if group_id is not None:
            self._values["group_id"] = group_id
        if id is not None:
            self._values["id"] = id

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
    def filter(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["DataAwsIdentitystoreGroupFilter"]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#filter DataAwsIdentitystoreGroup#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["DataAwsIdentitystoreGroupFilter"]], result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#identity_store_id DataAwsIdentitystoreGroup#identity_store_id}.'''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#group_id DataAwsIdentitystoreGroup#group_id}.'''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupFilter",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_path": "attributePath",
        "attribute_value": "attributeValue",
    },
)
class DataAwsIdentitystoreGroupFilter:
    def __init__(
        self,
        *,
        attribute_path: builtins.str,
        attribute_value: builtins.str,
    ) -> None:
        '''
        :param attribute_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsIdentitystoreGroupFilter.__init__)
            check_type(argname="argument attribute_path", value=attribute_path, expected_type=type_hints["attribute_path"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "attribute_path": attribute_path,
            "attribute_value": attribute_value,
        }

    @builtins.property
    def attribute_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.'''
        result = self._values.get("attribute_path")
        assert result is not None, "Required property 'attribute_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.'''
        result = self._values.get("attribute_value")
        assert result is not None, "Required property 'attribute_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsIdentitystoreGroupFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupFilterList",
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
            type_hints = typing.get_type_hints(DataAwsIdentitystoreGroupFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsIdentitystoreGroupFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsIdentitystoreGroupFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsIdentitystoreGroupFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroupFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroupFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroupFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsIdentitystoreGroupFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsIdentitystoreGroupFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsIdentitystoreGroupFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroupFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsIdentitystoreGroupFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupFilterOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsIdentitystoreGroupFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="attributePathInput")
    def attribute_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributePathInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="attributePath")
    def attribute_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributePath"))

    @attribute_path.setter
    def attribute_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroupFilterOutputReference, "attribute_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributePath", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroupFilterOutputReference, "attribute_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsIdentitystoreGroupFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsIdentitystoreGroupFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsIdentitystoreGroupFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsIdentitystoreGroupFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsIdentitystoreGroup",
    "DataAwsIdentitystoreGroupConfig",
    "DataAwsIdentitystoreGroupFilter",
    "DataAwsIdentitystoreGroupFilterList",
    "DataAwsIdentitystoreGroupFilterOutputReference",
]

publication.publish()
