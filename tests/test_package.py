import re

import ci_triage_agent


def test_version_is_semver() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+", ci_triage_agent.__version__)
