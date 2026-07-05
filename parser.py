"""
parser.py

Utility functions for detecting the programming language
of the submitted source code.
"""

import re


def detect_language(code: str) -> str:
    """
    Detect the programming language based on common syntax patterns.

    Supported:
    - Python
    - C++
    - Java
    - JavaScript
    - C
    - Go

    Parameters
    ----------
    code : str
        Source code submitted by the user.

    Returns
    -------
    str
        Detected programming language.
    """

    code = code.strip()

    if not code:
        return "Unknown"

    # ---------- Python ----------
    python_patterns = [
        r"^\s*def\s+\w+\(",
        r"^\s*class\s+\w+",
        r"import\s+\w+",
        r"from\s+\w+\s+import",
        r"print\s*\(",
    ]

    # ---------- C++ ----------
    cpp_patterns = [
        r"#include\s*<",
        r"using\s+namespace\s+std",
        r"std::",
        r"cout\s*<<",
        r"cin\s*>>",
    ]

    # ---------- C ----------
    c_patterns = [
        r"#include\s*<stdio\.h>",
        r"printf\s*\(",
        r"scanf\s*\(",
    ]

    # ---------- Java ----------
    java_patterns = [
        r"public\s+class",
        r"public\s+static\s+void\s+main",
        r"System\.out\.println",
    ]

    # ---------- JavaScript ----------
    js_patterns = [
        r"console\.log",
        r"\bfunction\b",
        r"\blet\b",
        r"\bconst\b",
        r"=>",
    ]

    # ---------- Go ----------
    go_patterns = [
        r"package\s+main",
        r"func\s+main",
        r"fmt\.Print",
    ]

    language_map = {
        "Python": python_patterns,
        "C++": cpp_patterns,
        "C": c_patterns,
        "Java": java_patterns,
        "JavaScript": js_patterns,
        "Go": go_patterns,
    }

    for language, patterns in language_map.items():
        for pattern in patterns:
            if re.search(pattern, code, re.MULTILINE):
                return language

    return "Unknown"