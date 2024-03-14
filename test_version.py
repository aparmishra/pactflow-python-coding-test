from pypacter_api import __version__
from pygments import *


def test_version() -> None:
    assert len(__version__.split(".")) >= 3

def detect_language(code_snippet):
    """
    Detects the most likely programming language for a given code snippet.Parameters it will take:
    - code_snippet (str): The input code snippet.
    Returns:
    - str: The detected programming language.
    """
    from pygments.lexers import guess_lexer

    try:
        lexer = guess_lexer(code_snippet)
        language = lexer.name
        return language
    except Exception as e:
        # Handle exceptions or errors
        return f"Error: {e}"

# You might need to install the 'pygments' library:
# pip install pygments