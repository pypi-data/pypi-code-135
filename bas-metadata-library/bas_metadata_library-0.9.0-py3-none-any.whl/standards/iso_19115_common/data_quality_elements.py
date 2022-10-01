from typing import Dict

from lxml.etree import SubElement  # nosec - see 'lxml` package (bandit)' section in README

from bas_metadata_library.standards.iso_19115_common import MetadataRecordElement
from bas_metadata_library.standards.iso_19115_common.base_elements import ScopeCode


class DataQuality(MetadataRecordElement):
    def make_config(self) -> dict:
        _ = {}

        lineage = Lineage(
            record=self.record,
            attributes=self.attributes,
            xpath=f"{self.xpath}/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage",
        )
        _lineage = lineage.make_config()
        if bool(_lineage):
            _["lineage"] = _lineage

        return _

    def make_element(self):
        data_quality_wrapper = SubElement(self.record, f"{{{self.ns.gmd}}}dataQualityInfo")
        data_quality_element = SubElement(data_quality_wrapper, f"{{{self.ns.gmd}}}DQ_DataQuality")

        scope = Scope(record=self.record, attributes=self.attributes, parent_element=data_quality_element)
        scope.make_element()

        lineage = Lineage(
            record=self.record,
            attributes=self.attributes,
            parent_element=data_quality_element,
            element_attributes=self.attributes["identification"],
        )
        lineage.make_element()


class Scope(MetadataRecordElement):
    def make_element(self):
        scope_wrapper = SubElement(self.parent_element, f"{{{self.ns.gmd}}}scope")
        scope_element = SubElement(scope_wrapper, f"{{{self.ns.gmd}}}DQ_Scope")

        scope_code = ScopeCode(record=self.record, attributes=self.attributes, parent_element=scope_element)
        scope_code.make_element()


class Lineage(MetadataRecordElement):
    def make_config(self) -> Dict[str, str]:
        _ = {}

        # note: this should be refactored to have a dedicated Statement and Source element when lineage sources are
        # added properly [#73]
        lineage_value = self.record.xpath(
            f"{self.xpath}/gmd:LI_Lineage/gmd:statement/gco:CharacterString/text()", namespaces=self.ns.nsmap()
        )
        if len(lineage_value) == 1:
            _["statement"] = lineage_value[0]

        return _

    def make_element(self):
        if "lineage" in self.element_attributes:
            lineage_container = SubElement(self.parent_element, f"{{{self.ns.gmd}}}lineage")
            lineage_wrapper = SubElement(lineage_container, f"{{{self.ns.gmd}}}LI_Lineage")

            # note: this should be refactored to have a dedicated Statement and Source element when lineage sources are
            # added properly [#73]
            lineage_element = SubElement(lineage_wrapper, f"{{{self.ns.gmd}}}statement")
            lineage_value = SubElement(lineage_element, f"{{{self.ns.gco}}}CharacterString")
            lineage_value.text = self.element_attributes["lineage"]["statement"]
