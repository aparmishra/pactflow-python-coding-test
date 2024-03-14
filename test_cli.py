from click.testing import CliRunner

from pypacter_cli import cli


def test_cli_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "PyPacter" in result.output


def test_cli_version() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "PyPacter" in result.output


def test_cli_detect_language() -> None:
    runner = CliRunner()

    # Test with a file path
    result_file_path = runner.invoke(cli, ["detect-language", "path/to/your/code/file"])
    assert result_file_path.exit_code == 0
    assert "Detected language" in result_file_path.output

    # Test with standard input
    result_stdin = runner.invoke(cli, ["detect-language"], input="your code snippet")
    assert result_stdin.exit_code == 0
    assert "Detected language" in result_stdin.output