from jira import JIRA, Issue
from dataclasses import dataclass

from datetime import date


@dataclass
class CustomFieldMapping:
    epic_name: str
    epic_link: str
    target_end: str
    target_start: str


class JiraLoader:
    def __init__(self, jira: JIRA, custom_field_mapping: CustomFieldMapping, follow_children: bool = True):
        self.jira = jira
        self.follow_children = follow_children
        self.custom_field_mapping = custom_field_mapping

        self._issues = {}
        self._gather_queue = {}
        self._queue_evaluating = False

        self.swimlane_map = {}

        self.start_date = None
        self.end_date = None

    def append_issues_search(self, jql: str):
        issues = self.jira.search_issues(jql)
        self._eval_push_queue(issues)
        self._start_queue_eval()

    def append_issue(self, issue: Issue):
        self._eval_push_queue(issue)
        self._start_queue_eval()

    @property
    def _eval_queue_has_items(self):
        return len(self._gather_queue) > 0

    def _start_queue_eval(self):
        if not self._queue_evaluating:
            self._eval_gather_queue()

    def _eval_push_queue(self, issue):
        if isinstance(issue, (list, set)):
            for issue in issue:
                self._eval_push_queue(issue)
        else:
            if issue.key not in self._issues and issue.key not in self._gather_queue:
                self._gather_queue[issue.key] = issue

    def _eval_pop_queue(self):
        if self._eval_queue_has_items:
            next_key = next(iter(self._gather_queue.keys()))
            return self._gather_queue.pop(next_key)

    def _eval_gather_queue(self):
        self._queue_evaluating = True
        issue = self._eval_pop_queue()

        while issue:
            self._issues[issue.key] = issue

            if issue.fields.issuetype.name == "Epic":
                epic_name = getattr(issue.fields, self.custom_field_mapping.epic_name)
                self.append_issues_search(f'"Epic Link" = "{epic_name}"')

            if issue.fields.issuetype.name in ["Task", "Sub-Task"]:
                self.append_issues_search(f'Parent = "{issue.key}"')

            issue = self._eval_pop_queue()
        self._queue_evaluating = False

    def update_start_end(self, new_date):
        new_date = date.fromisoformat(new_date)

        if not self.start_date or self.start_date > new_date:
            self.start_date = new_date
        if not self.end_date or self.end_date < new_date:
            self.end_date = new_date

    def export_svgdiagram_gantt(self, assign_swimlane, extract_name):
        for issue in self._issues.values():
            swimlane_name = assign_swimlane(issue)

            if not swimlane_name:
                continue

            item_name = extract_name(issue)

            target_start = getattr(issue.fields, self.custom_field_mapping.target_start)
            target_end = getattr(issue.fields, self.custom_field_mapping.target_end)

            swimlane = self.swimlane_map.get(swimlane_name, {"name": swimlane_name})

            if issue.fields.duedate:
                self.update_start_end(issue.fields.duedate)
                milestones = swimlane.get("milestones", [])
                milestones.append({
                    "due_date": issue.fields.duedate,
                    "name": item_name
                })
                swimlane["milestones"] = milestones

            if target_start and target_end:
                self.update_start_end(target_start)
                self.update_start_end(target_end)
                tasks = swimlane.get("tasks", [])
                tasks.append({
                    "start_date": target_start,
                    "end_date": target_end,
                    "name": item_name
                })
                swimlane["tasks"] = tasks

            self.swimlane_map[swimlane_name] = swimlane

        return {
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "swimlanes": list(self.swimlane_map.values()),
        }
