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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUForwardingPathListEntry(NURESTObject):
    """ Represents a ForwardingPathListEntry in the VSD

        Notes:
            Forwarding path list entry to be associated with forwarding path list for l4 based policy to PAT / IKE to underlay.
    """

    __rest_name__ = "forwardingpathlistentry"
    __resource_name__ = "forwardingpathlistentries"

    
    ## Constants
    
    CONST_FORWARDING_ACTION_IKE = "IKE"
    
    CONST_FORWARDING_ACTION_UNDERLAY_ROUTE = "UNDERLAY_ROUTE"
    
    CONST_FORWARDING_ACTION_UNDERLAY_PAT = "UNDERLAY_PAT"
    
    CONST_FC_OVERRIDE_NONE = "NONE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_UPLINK_PREFERENCE_PRIMARY = "PRIMARY"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_UPLINK_PREFERENCE_SECONDARY = "SECONDARY"
    
    CONST_FC_OVERRIDE_H = "H"
    
    CONST_FC_OVERRIDE_F = "F"
    
    CONST_FC_OVERRIDE_G = "G"
    
    CONST_FC_OVERRIDE_D = "D"
    
    CONST_FC_OVERRIDE_E = "E"
    
    CONST_FC_OVERRIDE_B = "B"
    
    CONST_FC_OVERRIDE_C = "C"
    
    CONST_FC_OVERRIDE_A = "A"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ForwardingPathListEntry instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> forwardingpathlistentry = NUForwardingPathListEntry(id=u'xxxx-xxx-xxx-xxx', name=u'ForwardingPathListEntry')
                >>> forwardingpathlistentry = NUForwardingPathListEntry(data=my_dict)
        """

        super(NUForwardingPathListEntry, self).__init__()

        # Read/Write Attributes
        
        self._fc_override = None
        self._last_updated_by = None
        self._entity_scope = None
        self._forwarding_action = None
        self._uplink_preference = None
        self._priority = None
        self._external_id = None
        
        self.expose_attribute(local_name="fc_override", remote_name="FCOverride", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="forwarding_action", remote_name="forwardingAction", attribute_type=str, is_required=True, is_unique=False, choices=[u'IKE', u'UNDERLAY_PAT', u'UNDERLAY_ROUTE'])
        self.expose_attribute(local_name="uplink_preference", remote_name="uplinkPreference", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'SECONDARY'])
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def fc_override(self):
        """ Get fc_override value.

            Notes:
                Value of the Service Class to be overridden in the packet when the match conditions are satisfied.

                
                This attribute is named `FCOverride` in VSD API.
                
        """
        return self._fc_override

    @fc_override.setter
    def fc_override(self, value):
        """ Set fc_override value.

            Notes:
                Value of the Service Class to be overridden in the packet when the match conditions are satisfied.

                
                This attribute is named `FCOverride` in VSD API.
                
        """
        self._fc_override = value

    
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
    def forwarding_action(self):
        """ Get forwarding_action value.

            Notes:
                Type of forwarding action associated with this entry.

                
                This attribute is named `forwardingAction` in VSD API.
                
        """
        return self._forwarding_action

    @forwarding_action.setter
    def forwarding_action(self, value):
        """ Set forwarding_action value.

            Notes:
                Type of forwarding action associated with this entry.

                
                This attribute is named `forwardingAction` in VSD API.
                
        """
        self._forwarding_action = value

    
    @property
    def uplink_preference(self):
        """ Get uplink_preference value.

            Notes:
                Type of forwarding uplink preference associated with this entry. In case of forwardingAction "IKE", uplinkPreference must not be set.

                
                This attribute is named `uplinkPreference` in VSD API.
                
        """
        return self._uplink_preference

    @uplink_preference.setter
    def uplink_preference(self, value):
        """ Set uplink_preference value.

            Notes:
                Type of forwarding uplink preference associated with this entry. In case of forwardingAction "IKE", uplinkPreference must not be set.

                
                This attribute is named `uplinkPreference` in VSD API.
                
        """
        self._uplink_preference = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                Autogenerated priority of a Forwarding Path List Entry for a given Forwarding Path List.

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                Autogenerated priority of a Forwarding Path List Entry for a given Forwarding Path List.

                
        """
        self._priority = value

    
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

    

    