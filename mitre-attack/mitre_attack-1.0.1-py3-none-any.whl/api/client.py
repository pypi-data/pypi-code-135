import mitre_attack.git
import collections
import json
import logging
from typing import Optional, Iterator, Dict
import mitre_attack.logging

import mitre_attack.pattern_matching
import mitre_attack.stix2
from mitre_attack.constants import GIT_REPO_URL, GIT_REPO_PATH, LOCAL_FILE_PATHS_BY_DOMAIN, ENTERPRISE, MOBILE, \
    ICS
from mitre_attack.types import get_len, STRS

logger = logging.getLogger(__name__)


class MitreAttack:
    def __init__(
            self,
            mitre_cti_git_repo_path: str = GIT_REPO_PATH,
            mitre_cti_git_repo_url: str = GIT_REPO_URL,
            include_enterprise: bool = True,
            include_mobile: bool = True,
            include_ics: bool = False):

        #: Allow the location of the mitre/cti repository to be customized.
        self.mitre_cti_git_repo_path = mitre_cti_git_repo_path
        self.mitre_cti_git_repo_url = mitre_cti_git_repo_url

        self.include_enterprise = include_enterprise
        self.include_mobile = include_mobile
        self.include_ics = include_ics

        if not any((self.include_enterprise, self.include_mobile, self.include_ics)):
            raise ValueError("Illegal configuration provided - cannot disable selection of all MITRE ATT&CK matrices")

    def _auto_update(self):
        mitre_attack.git.pull(path=self.mitre_cti_git_repo_path, url=self.mitre_cti_git_repo_url)

    def get_object(self, object_id: str) -> Optional[dict]:
        """
        Lookup objects.
        """
        self._auto_update()

        rows = tuple(self.iter_objects(object_ids=[object_id]))
        if rows:
            total = len(rows)
            if total > 1:
                logger.warning("Expected 1 match but found %d matches", total)
            return next(iter(rows))

    def iter_objects(
            self,
            object_ids: Optional[STRS] = None,
            object_types: Optional[STRS] = None,
            object_names: Optional[STRS] = None) -> Iterator[dict]:

        kwargs = locals()
        del kwargs['self']

        mitre_attack.logging.log_action(logger, 'Searching for objects', **kwargs)

        total = 0
        for row in self._iter_objects(object_ids=object_ids, object_types=object_types, object_names=object_names):
            yield row
            total += 1

        mitre_attack.logging.log_result(logger, 'Found {} matching objects'.format(total), **kwargs)

    def _iter_objects(
            self,
            object_ids: Optional[STRS] = None,
            object_types: Optional[STRS] = None,
            object_names: Optional[STRS] = None) -> Iterator[dict]:
        """
        Search for objects.
        """
        self._auto_update()

        rows = self.__iter_objects()

        if object_ids:
            object_ids = frozenset(object_ids)
            rows = filter(lambda row: row['id'] in object_ids, rows)

        if object_types:
            object_types = frozenset(object_types)
            rows = filter(lambda row: mitre_attack.stix2.get_stix_type_from_id(row['id']) in object_types, rows)

        if object_names:
            object_names = frozenset(object_names)
            rows = filter(lambda row: mitre_attack.pattern_matching.matches(row['name'], object_names), rows)

        yield from rows

    def __iter_objects(self) -> Iterator[dict]:
        for precondition, domain in [
            (self.include_enterprise, ENTERPRISE),
            (self.include_mobile, MOBILE),
            (self.include_ics, ICS),
        ]:
            if precondition:
                yield from self._iter_objects_by_domain(domain)

    def _iter_objects_by_domain(self, domain: str) -> Iterator[dict]:
        path = LOCAL_FILE_PATHS_BY_DOMAIN[domain]
        with open(path) as file:
            yield from json.load(file)['objects']

    def count_objects(
            self,
            object_ids: Optional[STRS] = None,
            object_types: Optional[STRS] = None,
            object_names: Optional[STRS] = None) -> int:
        """
        Count matching objects.
        """
        kwargs = locals()
        del kwargs['self']

        mitre_attack.logging.log_action(logger, 'Counting objects', **kwargs)

        rows = self.iter_objects(**kwargs)
        return sum(1 for _ in rows)

    def tally_objects_by_type(
            self,
            object_ids: Optional[STRS] = None,
            object_types: Optional[STRS] = None,
            object_names: Optional[STRS] = None) -> Dict[str, int]:

        seen = set()
        tally = collections.defaultdict(int)
        for row in self.iter_objects(object_ids=object_ids, object_types=object_types, object_names=object_names):

            #: Only count objects distributed across multiple matrix domains once.
            object_id = row['id']
            if object_id not in seen:
                seen.add(object_id)

                object_type = row['type']
                tally[object_type] += 1
        return dict(tally)

    def iter_relationships(
            self,
            relationship_ids: Optional[STRS] = None,
            relationship_types: Optional[STRS] = None,
            source_object_ids: Optional[STRS] = None,
            source_object_types: Optional[STRS] = None,
            target_object_ids: Optional[STRS] = None,
            target_object_types: Optional[STRS] = None) -> Iterator[dict]:
        """
        List relationships.
        """
        kwargs = locals()
        del kwargs['self']

        mitre_attack.logging.log_action(logger, "Searching for relationships", **kwargs)

        total = 0
        for relationship in self._iter_relationships(
            relationship_ids=relationship_ids,
            relationship_types=relationship_types,
            source_object_ids=source_object_ids,
            source_object_types=source_object_types,
            target_object_ids=target_object_ids,
            target_object_types=target_object_types,
        ):
            yield relationship
            total += 1

        mitre_attack.logging.log_action(
            logger, "Found {} {}".format(total, 'relationship' if total == 1 else 'relationships'), **kwargs)

    def _iter_relationships(
            self,
            relationship_ids: Optional[STRS] = None,
            relationship_types: Optional[STRS] = None,
            source_object_ids: Optional[STRS] = None,
            source_object_types: Optional[STRS] = None,
            target_object_ids: Optional[STRS] = None,
            target_object_types: Optional[STRS] = None) -> Iterator[dict]:

        for row in self.iter_objects(object_ids=relationship_ids, object_types=['relationship']):
            if relationship_ids and row['id'] not in relationship_ids:
                continue

            if relationship_types and row['relationship_type'] not in relationship_types:
                continue

            if source_object_ids and row['source_ref'] not in source_object_ids:
                continue

            if target_object_ids and row['target_ref'] not in target_object_ids:
                continue

            if source_object_types and mitre_attack.stix2.get_stix_type_from_id(
                    row['source_ref']) not in source_object_types:
                continue

            if target_object_types and mitre_attack.stix2.get_stix_type_from_id(
                    row['target_ref']) not in target_object_types:
                continue

            yield row

    def count_relationships(
            self,
            relationship_ids: Optional[STRS] = None,
            relationship_types: Optional[STRS] = None,
            source_object_ids: Optional[STRS] = None,
            source_object_types: Optional[STRS] = None,
            target_object_ids: Optional[STRS] = None,
            target_object_types: Optional[STRS] = None) -> int:
        """
        Count relationships.
        """
        kwargs = locals()
        del kwargs['self']

        mitre_attack.logging.log_action(logger, "Counting relationships", **kwargs)

        relationships = self.iter_relationships(
            relationship_ids=relationship_ids,
            relationship_types=relationship_types,
            source_object_ids=source_object_ids,
            source_object_types=source_object_types,
            target_object_ids=target_object_ids,
            target_object_types=target_object_types,
        )
        return get_len(relationships)

    def tally_relationships_by_type(
            self,
            relationship_ids: Optional[STRS] = None,
            relationship_types: Optional[STRS] = None,
            source_object_ids: Optional[STRS] = None,
            source_object_types: Optional[STRS] = None,
            target_object_ids: Optional[STRS] = None,
            target_object_types: Optional[STRS] = None) -> Dict[str, int]:
        """
        Tally relationships by type.
        """
        tally = collections.defaultdict(int)
        relationships = self.iter_relationships(
            relationship_ids=relationship_ids,
            relationship_types=relationship_types,
            source_object_ids=source_object_ids,
            source_object_types=source_object_types,
            target_object_ids=target_object_ids,
            target_object_types=target_object_types,
        )
        for row in relationships:
            source_object_type = mitre_attack.stix2.get_stix_type_from_id(row['source_ref'])
            target_object_type = mitre_attack.stix2.get_stix_type_from_id(row['target_ref'])
            relationship_type = '{} {} {}'.format(source_object_type, row['relationship_type'], target_object_type)
            tally[relationship_type] += 1
        return dict(tally)

    def get_relationship(self, relationship_id: str) -> Optional[dict]:
        """
        Lookup relationships.
        """
        return self.get_object(object_id=relationship_id)


class MitreAttackClassic(MitreAttack):
    def __init__(self):
        super(MitreAttackClassic, self).__init__(include_enterprise=True, include_mobile=True, include_ics=False)


class MitreAttackEnterprise(MitreAttack):
    def __init__(self):
        super(MitreAttackEnterprise, self).__init__(include_enterprise=True, include_mobile=False, include_ics=False)


class MitreAttackMobile(MitreAttack):
    def __init__(self):
        super(MitreAttackMobile, self).__init__(include_enterprise=False, include_mobile=True, include_ics=False)


class MitreAttackICS(MitreAttack):
    def __init__(self):
        super(MitreAttackICS, self).__init__(include_enterprise=False, include_mobile=False, include_ics=True)
