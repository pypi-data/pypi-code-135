# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import re
import unittest
from click.testing import CliRunner
from pytermor.util.string_filter import SGR_REGEXP

from es7s.cli import entrypoint


class TestCliGroups(unittest.TestCase):
    def test_entrypoint(self):
        expected_commands = [
            "demo",
            "manage",
            "exec",
            "monitor",
        ]
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s)

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertRegex(result.stdout, re.compile(r"^Usage: es7s"), "Missing usage")

        for expected_command in expected_commands:
            self.assertRegex(
                result.stdout, re.compile(r"^\s+" + expected_command, flags=re.MULTILINE), "Missing command"
            )

    def test_demo_group(self):
        expected_commands = [
            "format-numerics",
        ]
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["demo"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertRegex(result.stdout, re.compile(r"^Usage: es7s demo"), "Missing usage")

        for expected_command in expected_commands:
            self.assertRegex(
                result.stdout, re.compile(r"^\s+" + expected_command, flags=re.MULTILINE), "Missing command"
            )

    def test_manage_group(self):
        expected_commands = [
            "config",
            "install",
        ]
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["manage"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertRegex(result.stdout, re.compile(r"^Usage: es7s manage"), "Missing usage")

        for expected_command in expected_commands:
            self.assertRegex(
                result.stdout, re.compile(r"^\s+" + expected_command, flags=re.MULTILINE), "Missing command"
            )

    def test_exec_group(self):
        expected_commands = [
            "list-dir",
        ]
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["exec"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertRegex(result.stdout, re.compile(r"^Usage: es7s exec"))

        for expected_command in expected_commands:
            self.assertRegex(result.stdout, re.compile(r"^\s+" + expected_command, flags=re.MULTILINE))


class TestCliCommands(unittest.TestCase):
    def test_demo_format_numerics(self):
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["demo", "format-numerics"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertRegex(result.output, re.compile(r"Input:", flags=re.MULTILINE), "Missing input header")
        self.assertRegex(result.output, re.compile(r"Output:", flags=re.MULTILINE), "Missing output header")


class TestCliCommonOptions(unittest.TestCase):
    def test_color_option_enables_sgrs(self):
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["demo", "format-numerics", "--color"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertRegex(result.stdout, SGR_REGEXP, "No SGRs found")

    def test_no_color_option_disables_sgrs(self):
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["demo", "format-numerics", "--no-color"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertNotRegex(result.stdout, SGR_REGEXP, "SGRs found")

    def test_color_option_enables_sgrs_in_help(self):
        self.skipTest("todo")
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["--help", "--color"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertRegex(result.stdout, SGR_REGEXP, "No SGRs found")

    def test_no_color_option_disables_sgrs_in_help(self):
        self.skipTest("todo")
        # noinspection PyTypeChecker
        result = CliRunner().invoke(entrypoint.es7s, ["--help", "--no-color"])

        self.assertEqual(result.exit_code, 0, "Exit code > 0")
        self.assertNotRegex(result.stdout, SGR_REGEXP, "SGRs found")

    def test_stderr_is_empty_with_quiet_flag(self):
        self.skipTest("unimplementable by now")
        # noinspection PyTypeChecker
        result = CliRunner(mix_stderr=False).invoke(entrypoint.es7s, ["run", "non-existing-cmd", "-q"])

        self.assertGreater(result.exit_code, 0, "Exit code should be >0")
        self.assertEqual(len(result.stderr), 0, "stderr should be empty")

    def test_stderr_transmits_error_by_default(self):
        self.skipTest("unimplementable by now")
        # noinspection PyTypeChecker
        result = CliRunner(mix_stderr=False).invoke(entrypoint.es7s, ["run", "non-existing-cmd"])

        self.assertGreater(result.exit_code, 0, "Exit code should be >0")
        self.assertGreater(len(result.stderr), 0, "stderr should be filled")
