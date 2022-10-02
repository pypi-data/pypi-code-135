"""Helper functions for XML Schema resources."""
import pkg_resources
import lxml.etree as etree


def assertValid(candidate, schema):
    schema_bytes = get_resource(schema)
    schema_doc = etree.fromstring(schema_bytes)
    candidate_doc = etree.fromstring(candidate)
    validator = etree.XMLSchema(schema_doc)
    validator.assertValid(candidate_doc)


def validate(candidate, schema):
    """Validates the document against the schema.

    Args:
        candidate (bytes): an xml document to be validated
        schema (string): the path of the schema file to use

    Returns:
        True/False
    """
    schema_bytes = get_resource(schema)
    schema_doc = etree.fromstring(schema_bytes)
    candidate_doc = etree.fromstring(candidate)
    validator = etree.XMLSchema(schema_doc)
    return validator.validate(candidate_doc)


def is_valid_for_version(document_bytes, version):
    assert isinstance(document_bytes, bytes)
    assert isinstance(version, str)
    version_map = {
            "3": "standard_invoice_v3.xsd",
            "4": "standard_invoice_v4.xsd",
            "5": "standard_invoice_v5.xsd",
            }
    document = etree.fromstring(document_bytes)
    schema_bytes = get_resource(version_map[version])
    schema_doc = etree.fromstring(schema_bytes)
    validator = etree.XMLSchema(schema_doc)
    return validator.validate(document)


def get_resource(path):
    """Gets the specified resource.

    The path being relative to the resources directory.

    Args:
        path (string): The ./resources/<path>

    Returns:
        bytes: Apparently.

    """
    resource_package = "bmb.schema"  # Could be any module/package name
    resource_path = '/'.join(("resources", path))
    resource = pkg_resources.resource_string(
        resource_package, resource_path)
    return resource


def get_each_invoice(invoices_xml):
    xpath = "//invoice"
    invoices_doc = etree.fromstring(invoices_xml)
    invoice_docs = invoices_doc.xpath(xpath)
    return [etree.tostring(invoice_doc) for invoice_doc in invoice_docs]


def get_document_version(document):
    assert isinstance(document, bytes)
    xpath = "/invoice/@version"
    doc = etree.fromstring(document)
    document_version = doc.xpath(xpath)
    return document_version[0]


def first(seq):
    return seq[0]


def maybe_first(seq):
    try:
        return seq[0]
    except IndexError:
        return None


def first_or_empty_string(seq):
    try:
        return seq[0]
    except IndexError:
        return ""


def doc(bytes_):
    return etree.fromstring(bytes_)


def bytes_(document):
    return etree.tostring(document)


def schema(document):
    return etree.XMLSchema(document)


def transform(transform_path, **kwargs):
    return etree.XSLT(doc(get_resource(transform_path)), **kwargs)


def xpath(document, path, namespace_dict):
    return document.xpath(path, namespaces=namespace_dict)


def validity(schema, candidate):
    try:
        schema.assertValid(candidate)
    except AssertionError:
        raise
    else:
        return True
