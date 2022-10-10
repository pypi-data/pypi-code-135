import api.models as m
from api import call


def get_author_name(author_name_id: int) -> m.AuthorName:
    """
    Get an author name by author_name_id
    Returns None if the response is empty.

    :param author_name_id:
    :return:
    """
    response, success = call.get_author_name_from(author_name_id)
    return m.AuthorName(response) if success else None


def get_author(author_id: int) -> m.Author:
    """
    Get a single author from AntCat API using a single author id
    Returns None if the response is empty.

    :param author_id:
    :return:
    """
    response, success = call.get_author_from(author_id)
    return m.Author(response) if success else None


def get_citation(citation_id: int) -> m.Citation:
    """
    Gets a single citation from AntCat API using a single citation id.
    Returns None if the response is empty.

    :param citation_id:
    :return: Citation or None
    """
    response, success = call.get_citation_from(citation_id)
    return m.Citation(response) if success else None


def get_history_item(history_item_id: int) -> m.HistoryItem:
    """
    Gets a single history item from AntCat API using a single history_item_id
    Returns None if the response is empty.
    :param history_item_id:
    :return:
    """
    response, success = call.get_history_item_from(history_item_id)
    return m.HistoryItem(response) if success else None


def get_journal(journal_id: int) -> m.Journal:
    """
    Gets a single journal from AntCat API using a single journal_id
    Returns None if the response is empty.
    :param journal_id:
    :return:
    """
    response, success = call.get_journal_from(journal_id)
    return m.Journal(response) if success else None


def get_name(name_id: int) -> m.Name:
    """
    Gets a single name from AntCat API using a single name_id
    Returns None if the response is empty.
    :param name_id:
    :return:
    """
    response, success = call.get_name_from(name_id)
    return [m.Name(type_name, info) for type_name, info in response.json().items()][0] if success else None


def get_protonym(protonym_id: int) -> m.Protonym:
    """
    Gets a single protonym from AntCat API using a single protonym_id
    Returns None if the response is empty.
    :param protonym_id:
    :return:
    """
    response, success = call.get_protonym_from(protonym_id)
    return m.Protonym(response) if success else None


def get_publisher(publisher_id: int) -> m.Publisher:
    """
    Gets a single publisher from AntCat API using a single publisher_id
    Returns None if the response is empty.
    :param publisher_id:
    :return:
    """
    response, success = call.get_publisher_from(publisher_id)
    return m.Publisher(response) if success else None


def get_reference(reference_id: int) -> m.Reference:
    """
    Gets a single reference from AntCat API using a single reference_id
    Returns None if the response is empty.
    :param reference_id:
    :return:
    """
    response, success = call.get_reference_from(reference_id)
    return [m.Reference(type_name, info) for type_name, info in response.json().items()][0] if success else None


def get_reference_author_name(ref_author_name_id: int) -> m.ReferenceAuthorName:
    """
    Gets a single reference author name from AntCat API using a single ref_author_name_id
    Returns None if the response is empty.
    :param ref_author_name_id:
    :return:
    """
    response, success = call.get_reference_author_name_from(ref_author_name_id)
    return m.ReferenceAuthorName(response) if success else None


def get_reference_section(ref_section_id: int) -> m.ReferenceSection:
    """
    Gets a single reference section from AntCat API using a single ref_section_id
    Returns None if the response is empty.
    :param ref_section_id:
    :return:
    """
    response, success = call.get_reference_section_from(ref_section_id)
    return m.ReferenceSection(response) if success else None


def get_reference_document(ref_document_id: int) -> m.ReferenceDocument:
    """
    Gets a single reference document from AntCat API using a single ref_document_id
    Returns None if the response is empty.
    :param ref_document_id:
    :return:
    """
    response, success = call.get_reference_document_from(ref_document_id)
    return m.ReferenceDocument(response) if success else None


def search_taxa(taxa: str) -> list:
    """
    AntCat.org response contains the first ten (10) matching results.
    For a more refined search, include more in the name

    :param taxa:
    :return:
    """
    response, success = call.get_taxa_search_from(taxa)
    return [m.TaxaSearch(info) for info in response.json()] if success else []


def get_taxa(taxa_id: int) -> list:
    """

    :param taxa_id:
    :return:
    """
    response, success = call.get_taxa_from(taxa_id)
    return [m.Taxa(type_name, info) for type_name, info in response.json().items()][0] if success else []
