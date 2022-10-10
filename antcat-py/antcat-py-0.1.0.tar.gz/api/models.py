from api import helper
from api import call


class AuthorName:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        """

        """
        Example Response        
        {
        "author_name":
            {
                "id": 170693,
                "name": "Anonymous",
                "created_at": "2010-11-17T02:42:35.000Z",
                "updated_at": "2010-11-22T01:29:15.000Z",
                "author_id": 1
            }
        }
        """
        self.meta = helper.parse('author_name', response)
        self.author_name_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.author_id = self.meta['author_id']
        self.name = self.meta['name']


class Author:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        """

        """
        Example Response
        {
            "author":
            {
                "id": 1,
                "created_at": "2010-11-22T01:29:15.000Z",
                "updated_at": "2010-11-22T01:29:15.000Z"
            }
        }

        """
        self.meta = helper.parse('author', response)
        self.author_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']


class Citation:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        """

        """
        Example Response
        {
        "citation": {
            "id": 154418,
            "reference_id": 128551,
            "pages": "270",
            "created_at": "2012-09-12T02:17:08.000Z",
            "updated_at": "2018-08-01T23:01:37.000Z"
            }
        }
        """
        self.meta = helper.parse(call.CITATION_KEY, response)
        self.citation_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.reference_id = self.meta['reference_id']
        self.pages = self.meta['pages']

    def __str__(self):
        return f'{self.citation_id} {self.pages}'


class HistoryItem:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        :return:
        """
        """
        Example Response
        {
            "history_item": {
            "id": 239426,
            "taxt": "Formicidae as family: {ref 126798}: 124 [Formicariae]; {ref 126849}: 147 [Formicarides]; 
                {ref 129018}: 356 [first spelling as {tax 429011}]; {ref 125734}: 331; {ref 129811}: 217; 
                {ref 129098}: 171; {ref 127561}: 877; {ref 124947}: 1 [Formicariae]; 
                {ref 127185}: 275 [{tax 429350}]; {ref 128683}: 52; {ref 128685}: 1; 
                {ref 127189}: 21; {ref 127193}: 6; {ref 125819}: 6 [Formicaria]; 
                {ref 124987}: 307 [{tax 429149}]; {ref 124988}: 19 [Formicariae]; {ref 124002}: 1; 
                {ref 125089}: 1; {ref 128175}: 5 [Formicarii]; {ref 122766}: 1; 
                {ref 128184}: 91 [Formicariae or {tax 429011}]; {ref 122385}: 384; all subsequent authors",
            "created_at": "2012-09-12T02:17:04.000Z",
            "updated_at": "2020-05-28T19:48:23.000Z",
            "position": 2,
            "protonym_id": 154879
            }
        }
        :param response:
        :return:
        """
        self.meta = helper.parse(call.HISTORY_ITEM_KEY, response)
        self.history_item_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.taxt = self.meta['taxt']
        self.position = self.meta['position']
        self.protonym_id = self.meta['protonym_id']


class Journal:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        :return:
        """
        """
        Example Response
        {
            "journal": {
              "id": 19346,
              "name": "Esakia",
              "created_at": "2010-11-27T03:41:25.000Z",
              "updated_at": "2010-11-27T03:41:25.000Z"
            }
        }
        :param response:
        :return:
        """
        self.meta = helper.parse(call.JOURNAL_KEY, response)
        self.journal_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.name = self.meta['name']


class Name:

    def __init__(self, type_name: str, info: dict):
        """
        Initialize from AntCat.org API Response
        :param type_name:
        :param info:
        :return:
        """
        """
        Example Response
        {
            "family_name": {
                "id": 134042,
                "name": "Formicariae",
                "epithet": "Formicariae",
                "created_at": "2012-09-12T02:17:04.000Z",
                "updated_at": "2020-09-12T02:11:33.000Z",
                "gender": null
            }
        }
        :param response:
        :return:
        """
        # self.meta = helper.parse(call.JOURNAL_KEY, response)
        # self.type =
        self.type_name = type_name.replace('_name', '')

        self.name_id = info['id']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']
        self.epithet = info['epithet']
        self.gender = info['gender']
        self.name = info['name']


class Protonym:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        :return:
        """
        """
        Example Response
        {
            "protonym": {
                "id": 154742,
                "created_at": "2012-09-12T02:17:08.000Z",
                "updated_at": "2020-05-20T07:49:26.000Z",
                "authorship_id": 154418,
                "fossil": true,
                "sic": false,
                "locality": null,
                "name_id": 134089,
                "primary_type_information_taxt": null,
                "secondary_type_information_taxt": null,
                "type_notes_taxt": null,
                "bioregion": null,
                "forms": null,
                "notes_taxt": "[as member of family Braconidae]",
                "ichnotaxon": false
            }
        }
        """
        self.meta = helper.parse(call.PROTONYMS_KEY, response)
        self.protonym_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.authorship_id = self.meta['authorship_id']
        self.fossil = self.meta['fossil']
        self.sic = self.meta['sic']
        self.locality = self.meta['locality']
        self.name_id = self.meta['name_id']
        self.primary_type_information_taxt = self.meta['primary_type_information_taxt']
        self.secondary_type_information_taxt = self.meta['secondary_type_information_taxt']
        self.type_notes_taxt = self.meta['type_notes_taxt']
        self.bioregion = self.meta['bioregion']
        self.forms = self.meta['forms']
        self.notes_taxt = self.meta['notes_taxt']
        self.ichnotaxon = self.meta['ichnotaxon']


class Publisher:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        :return:
        """
        """
        Example Response
        {
            "publisher": {
                "id": 4551,
                "name": "University of the Ryukyus",
                "created_at": "2010-11-27T03:41:26.000Z",
                "updated_at": "2018-09-13T19:11:38.000Z",
                "place": "Naha, Okinawa"
            }
        }        
        """
        self.meta = helper.parse(call.PUBLISHERS_KEY, response)
        self.publisher_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.name = self.meta['name']
        self.place = self.meta['place']


class ReferenceAuthorName:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        :return:
        """
        """
        Example Response
        {
            "reference_author_name": {
                "id": 177008,
                "author_name_id": 190005,
                "reference_id": 122097,
                "created_at": "2010-11-27T03:41:25.000Z",
                "updated_at": "2010-11-27T03:41:25.000Z",
                "position": 3
            }
        }
        """
        self.meta = helper.parse(call.REFERENCE_AUTHOR_NAMES_KEY, response)
        self.reference_author_name_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.position = self.meta['position']


class ReferenceDocument:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        :return:
        """
        """
        Example Response
        {
            "reference_document": {
                "id": 4,
                "url": null,
                "file_file_name": "6846.pdf",
                "created_at": "2010-12-15T01:56:42.000Z",
                "updated_at": "2021-04-18T15:31:10.000Z",
                "reference_id": 122123
            }
        }        
        """
        self.meta = helper.parse(call.REFERENCE_DOCUMENTS_KEY, response)
        self.reference_document_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.url = self.meta['url']
        self.file_file_name = self.meta['file_file_name']
        self.reference_id = self.meta['reference_id']


class ReferenceSection:

    def __init__(self, response):
        """
        Initialize from AntCat.org API Response
        :param response:
        :return:
        """
        """
        Example Response
        {
            "reference_section": {
                "id": 2091,
                "taxon_id": 429011,
                "position": 1,
                "title_taxt": "FAMILY FORMICIDAE REFERENCES, WORLD",
                    "references_taxt": "{ref 128094}: 1 ({tax 429011}); {ref 127213}: 394 ({tax 429011}); 
                    {ref 124002}: 1 ({tax 429011}); {ref 124696}: 3 ({tax 429481}); 
                    {ref 124702}: 2 ({tax 430052}); {ref 124711}: 2 ({tax 429071}); {ref 124749}: 3, 
                    {ref 124756}: 95 and {ref 124769}: 207 ({tax 429529}); {ref 124775}: 2 ({tax 429149}); 
                    {ref 128601}: 1 ({tax 429060} and {tax 429071}); {ref 122860}: 7 ({tax 429011})",
                "created_at": "2012-09-12T02:17:04.000Z",
                "updated_at": "2012-09-12T02:55:46.000Z",
                "subtitle_taxt": "WORLD CATALOGUES"
            }
        }   
            
        """
        self.meta = helper.parse(call.REFERENCE_SECTIONS_KEY, response)
        self.reference_document_id = self.meta['id']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']
        self.taxon_id = self.meta['taxon_id']
        self.position = self.meta['position']
        self.title_taxt = self.meta['title_taxt']
        self.references_taxt = self.meta['references_taxt']
        self.subtitle_taxt = self.meta['subtitle_taxt']


class Reference:

    def __init__(self, type_reference: str, info: dict):
        """
        Initialize from AntCat.org API Response
        :param type_reference:
        :param info:
        :return:
        """
        """
        Example Response
        {
            "article_reference": {
                "id": 122098,
                "year": 1991,
                "date": "19910731",
                "created_at": "2010-11-27T03:41:25.000Z",
                "updated_at": "2018-08-03T19:35:52.000Z",
                "publisher_id": null,
                "journal_id": 19346,
                "series_volume_issue": "31",
                "pagination": "1-115",
                "author_names_string_cache": "Abe, M.; Smith, D. R.",
                "editor_notes": "And *Myrmecium* (misspelling).",
                "public_notes": "Page 53: *Myrmicium*.",
                "taxonomic_notes": null,
                "title": "The genus-group names of Symphyta (Hymenoptera) and their type species",
                "nesting_reference_id": null,
                "author_names_suffix": null,
                "review_state": "reviewed",
                "doi": null,
                "bolton_key": "Abe Smith 1991",
                "online_early": false,
                "stated_year": null,
                "year_suffix": null
            }
        },
        {
            "book_reference": {
                "id": 122099,
                "year": 1974,
                "date": null,
                "created_at": "2010-11-27T03:41:26.000Z",
                "updated_at": "2020-10-03T19:45:58.000Z",
                "publisher_id": 4551,
                "journal_id": null,
                "series_volume_issue": null,
                "pagination": "278 pp.",
                "author_names_string_cache": "Ikehara, S.",
                "editor_notes": null,
                "public_notes": null,
                "taxonomic_notes": null,
                "title": "Ecological studies of nature conservation of the Ryukyu Islands (1). 
                    Report for the fiscal year of 1973. [In Japanese.]",
                "nesting_reference_id": null,
                "author_names_suffix": "(ed.)",
                "review_state": "reviewed",
                "doi": null,
                "bolton_key": null,
                "online_early": false,
                "stated_year": null,
                "year_suffix": null
            }
        }
        """
        self.type_reference = type_reference.replace('_reference', '')
        self.reference_document_id = info['id']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']


class TaxaSearch:

    def __init__(self, info: dict):
        """
        Initialize from AntCat.org API Response
        :param info:
        :return:
        """
        """
        Example Response
        [
            {
                "id": 429784,
                "name": "Pogonomyrmex"
            },
            {
                "id": 445214,
                "name": "Pogonomyrmex abdominalis"
            }
        ]
        
        """
        self.taxa_id = info['id']
        self.name = info['name']

    def __str__(self):
        return f"{self.taxa_id} {self.name}"

class Taxa:

    def __init__(self, type_name: str, info: dict):
        """
        Initialize from AntCat.org API Response
        :param type_name:
        :param info:
        :return:
        """
        """
        Example Response
        {
            "family": {
                "id": 429011,
                "created_at": "2012-09-12T02:17:04.000Z",
                "updated_at": "2019-05-15T23:50:13.000Z",
                "status": "valid",
                "subfamily_id": null,
                "tribe_id": null,
                "genus_id": null,
                "homonym_replaced_by_id": null,
                "incertae_sedis_in": null,
                "species_id": null,
                "protonym_id": 154879,
                "subgenus_id": null,
                "name_id": 134043,
                "name_cache": "Formicidae",
                "unresolved_homonym": false,
                "current_taxon_id": null,
                "family_id": null,
                "hol_id": null,
                "collective_group_name": false,
                "original_combination": false,
                "subspecies_id": null,
                "author_citation": "Latreille, 1809",
                "name_html_cache": "Formicidae"
            }
        }
        """
        self.type_name = type_name
        self.taxa_id = info['id']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']
        self.status = info['status']
        self.subfamily_id = info['subfamily_id']
        self.tribe_id = info['tribe_id']
        self.genus_id = info['genus_id']
        self.homonym_replaced_by_id = info['homonym_replaced_by_id']
        self.incertae_sedis_in = info['incertae_sedis_in']
        self.species_id = info['species_id']
        self.protonym_id = info['protonym_id']
        self.subgenus_id = info['subgenus_id']
        self.name_id = info['name_id']
        self.name_cache = info['name_cache']
        self.unresolved_homonym = info['unresolved_homonym']
        self.current_taxon_id = info['current_taxon_id']
        self.family_id = info['family_id']
        self.hol_id = info['hol_id']
        self.collective_group_name = info['collective_group_name']
        self.original_combination = info['original_combination']
        self.subspecies_id = info['original_combination']
        self.author_citation = info['author_citation']
        self.name_html_cache = info['name_html_cache']

    def __str__(self):
        return f"{self.type_name.capitalize()}: {self.name_cache}"
