# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "735a0a8a6fd62c9a0010573c318cd3e8552ac07a7e6839c5ca0d332d8d9279c1"


from pathlib import Path

from ecoscope_workflows_core.testing import TestCase, run_cli_test_case


def test_cli(
    entrypoint: str,
    execution_mode: str,
    mock_io: bool,
    case: TestCase,
    tmp_path: Path,
):
    run_cli_test_case(entrypoint, execution_mode, mock_io, case, tmp_path)
