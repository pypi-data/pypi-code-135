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


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUOverlayMirrorDestinationTemplate(NURESTObject):
    """ Represents a OverlayMirrorDestinationTemplate in the VSD

        Notes:
            Overlay mirror destinations are pointed to by advanced forwarding policies as the destination for redirected traffic. Targets can be of two types, L3 or virtual wire. For L3 targets a virtual IP should be provided as it allows the system to track among which of the end-points belonging to the overlay mirror destination is the active one. For this type of redirect the packet's destination MAC address is changed to match that of the Virtual IP. For virtual-wire redirection targets, the packets are untouched and forwarded directly to the end-point.
    """

    __rest_name__ = "overlaymirrordestinationtemplate"
    __resource_name__ = "overlaymirrordestinationtemplates"

    
    ## Constants
    
    CONST_DESTINATION_TYPE_REDIRECTION_TARGET = "REDIRECTION_TARGET"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_DESTINATION_TYPE_OVERLAY_MIRROR_DESTINATION = "OVERLAY_MIRROR_DESTINATION"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_END_POINT_TYPE_NONE = "NONE"
    
    CONST_TRIGGER_TYPE_NONE = "NONE"
    
    CONST_END_POINT_TYPE_VIRTUAL_WIRE = "VIRTUAL_WIRE"
    
    CONST_TRIGGER_TYPE_GARP = "GARP"
    
    

    def __init__(self, **kwargs):
        """ Initializes a OverlayMirrorDestinationTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> overlaymirrordestinationtemplate = NUOverlayMirrorDestinationTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'OverlayMirrorDestinationTemplate')
                >>> overlaymirrordestinationtemplate = NUOverlayMirrorDestinationTemplate(data=my_dict)
        """

        super(NUOverlayMirrorDestinationTemplate, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._redundancy_enabled = None
        self._description = None
        self._destination_type = None
        self._embedded_metadata = None
        self._end_point_type = None
        self._entity_scope = None
        self._creation_date = None
        self._trigger_type = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_enabled", remote_name="redundancyEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_type", remote_name="destinationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'OVERLAY_MIRROR_DESTINATION', u'REDIRECTION_TARGET'])
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_point_type", remote_name="endPointType", attribute_type=str, is_required=True, is_unique=False, choices=[u'NONE', u'VIRTUAL_WIRE'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="trigger_type", remote_name="triggerType", attribute_type=str, is_required=False, is_unique=False, choices=[u'GARP', u'NONE'])
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of this overlay mirror destination template

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of this overlay mirror destination template

                
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
    def redundancy_enabled(self):
        """ Get redundancy_enabled value.

            Notes:
                Allow/Disallow redundant appliances and VIP

                
                This attribute is named `redundancyEnabled` in VSD API.
                
        """
        return self._redundancy_enabled

    @redundancy_enabled.setter
    def redundancy_enabled(self, value):
        """ Set redundancy_enabled value.

            Notes:
                Allow/Disallow redundant appliances and VIP

                
                This attribute is named `redundancyEnabled` in VSD API.
                
        """
        self._redundancy_enabled = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of this overlay mirror destination template

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of this overlay mirror destination template

                
        """
        self._description = value

    
    @property
    def destination_type(self):
        """ Get destination_type value.

            Notes:
                Determines the type of destination : redirection target or overlay mirror destination

                
                This attribute is named `destinationType` in VSD API.
                
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, value):
        """ Set destination_type value.

            Notes:
                Determines the type of destination : redirection target or overlay mirror destination

                
                This attribute is named `destinationType` in VSD API.
                
        """
        self._destination_type = value

    
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
    def end_point_type(self):
        """ Get end_point_type value.

            Notes:
                VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a overlay mirror destination. Possible value is VIRTUAL_WIRE.

                
                This attribute is named `endPointType` in VSD API.
                
        """
        return self._end_point_type

    @end_point_type.setter
    def end_point_type(self, value):
        """ Set end_point_type value.

            Notes:
                VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a overlay mirror destination. Possible value is VIRTUAL_WIRE.

                
                This attribute is named `endPointType` in VSD API.
                
        """
        self._end_point_type = value

    
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
    def trigger_type(self):
        """ Get trigger_type value.

            Notes:
                Trigger type, could be NONE/GARP - THIS IS READONLY

                
                This attribute is named `triggerType` in VSD API.
                
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, value):
        """ Set trigger_type value.

            Notes:
                Trigger type, could be NONE/GARP - THIS IS READONLY

                
                This attribute is named `triggerType` in VSD API.
                
        """
        self._trigger_type = value

    
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

    

    