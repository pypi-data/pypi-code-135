# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUDomainFIPAclTemplateEntriesFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUDomainFIPAclTemplate(NURESTObject):
    """ Represents a DomainFIPAclTemplate in the VSD

        Notes:
            Defines the template for an Domain Floating IP ACL
    """

    __rest_name__ = "egressdomainfloatingipacltemplate"
    __resource_name__ = "egressdomainfloatingipacltemplates"

    
    ## Constants
    
    CONST_POLICY_STATE_DRAFT = "DRAFT"
    
    CONST_POLICY_STATE_LIVE = "LIVE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_PRIORITY_TYPE_NONE = "NONE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_PRIORITY_TYPE_TOP = "TOP"
    
    CONST_PRIORITY_TYPE_BOTTOM = "BOTTOM"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DomainFIPAclTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> domainfipacltemplate = NUDomainFIPAclTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'DomainFIPAclTemplate')
                >>> domainfipacltemplate = NUDomainFIPAclTemplate(data=my_dict)
        """

        super(NUDomainFIPAclTemplate, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._active = None
        self._default_allow_ip = None
        self._default_allow_non_ip = None
        self._description = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._entries = None
        self._policy_state = None
        self._creation_date = None
        self._priority = None
        self._priority_type = None
        self._associated_live_entity_id = None
        self._auto_generate_priority = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="active", remote_name="active", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_allow_ip", remote_name="defaultAllowIP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_allow_non_ip", remote_name="defaultAllowNonIP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="entries", remote_name="entries", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="policy_state", remote_name="policyState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DRAFT', u'LIVE'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority_type", remote_name="priorityType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BOTTOM', u'NONE', u'TOP'])
        self.expose_attribute(local_name="associated_live_entity_id", remote_name="associatedLiveEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auto_generate_priority", remote_name="autoGeneratePriority", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.domain_fip_acl_template_entries = NUDomainFIPAclTemplateEntriesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the entity

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the entity

                
        """
        self._name = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def active(self):
        """ Get active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        return self._active

    @active.setter
    def active(self, value):
        """ Set active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        self._active = value

    
    @property
    def default_allow_ip(self):
        """ Get default_allow_ip value.

            Notes:
                If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries

                
                This attribute is named `defaultAllowIP` in VSD API.
                
        """
        return self._default_allow_ip

    @default_allow_ip.setter
    def default_allow_ip(self, value):
        """ Set default_allow_ip value.

            Notes:
                If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries

                
                This attribute is named `defaultAllowIP` in VSD API.
                
        """
        self._default_allow_ip = value

    
    @property
    def default_allow_non_ip(self):
        """ Get default_allow_non_ip value.

            Notes:
                If enabled, non ip traffic will be dropped

                
                This attribute is named `defaultAllowNonIP` in VSD API.
                
        """
        return self._default_allow_non_ip

    @default_allow_non_ip.setter
    def default_allow_non_ip(self, value):
        """ Set default_allow_non_ip value.

            Notes:
                If enabled, non ip traffic will be dropped

                
                This attribute is named `defaultAllowNonIP` in VSD API.
                
        """
        self._default_allow_non_ip = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the entity

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the entity

                
        """
        self._description = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def entries(self):
        """ Get entries value.

            Notes:
                List of Egress Domain ACL entries associated with this ACL

                
        """
        return self._entries

    @entries.setter
    def entries(self, value):
        """ Set entries value.

            Notes:
                List of Egress Domain ACL entries associated with this ACL

                
        """
        self._entries = value

    
    @property
    def policy_state(self):
        """ Get policy_state value.

            Notes:
                State of the policy

                
                This attribute is named `policyState` in VSD API.
                
        """
        return self._policy_state

    @policy_state.setter
    def policy_state(self, value):
        """ Set policy_state value.

            Notes:
                State of the policy

                
                This attribute is named `policyState` in VSD API.
                
        """
        self._policy_state = value

    
    @property
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                The priority of the ACL entry that determines the order of entries

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                The priority of the ACL entry that determines the order of entries

                
        """
        self._priority = value

    
    @property
    def priority_type(self):
        """ Get priority_type value.

            Notes:
                None

                
                This attribute is named `priorityType` in VSD API.
                
        """
        return self._priority_type

    @priority_type.setter
    def priority_type(self, value):
        """ Set priority_type value.

            Notes:
                None

                
                This attribute is named `priorityType` in VSD API.
                
        """
        self._priority_type = value

    
    @property
    def associated_live_entity_id(self):
        """ Get associated_live_entity_id value.

            Notes:
                ID of the associated live entity

                
                This attribute is named `associatedLiveEntityID` in VSD API.
                
        """
        return self._associated_live_entity_id

    @associated_live_entity_id.setter
    def associated_live_entity_id(self, value):
        """ Set associated_live_entity_id value.

            Notes:
                ID of the associated live entity

                
                This attribute is named `associatedLiveEntityID` in VSD API.
                
        """
        self._associated_live_entity_id = value

    
    @property
    def auto_generate_priority(self):
        """ Get auto_generate_priority value.

            Notes:
                If enabled, entries priority will be randomly generated between allowed range.

                
                This attribute is named `autoGeneratePriority` in VSD API.
                
        """
        return self._auto_generate_priority

    @auto_generate_priority.setter
    def auto_generate_priority(self, value):
        """ Set auto_generate_priority value.

            Notes:
                If enabled, entries priority will be randomly generated between allowed range.

                
                This attribute is named `autoGeneratePriority` in VSD API.
                
        """
        self._auto_generate_priority = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    