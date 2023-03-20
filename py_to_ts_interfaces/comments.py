from typing import List, Tuple

from py_to_ts_interfaces.type_converting import python_to_typescript_type
from py_to_ts_interfaces.utils import to_camel_case


class CommentDefinition:
    """Represent a python/typescript comment."""
    comment: str
    consecutive: bool

    def __init__(self, definition: List[str]):
        self.consecutive = True
        self.comment = definition[0]

    def get_typescript(self) -> str:
        """Return the comment in typescript syntax (including indentation)."""
        typescript_string = self.comment.replace("#", "//", 1)
        print(typescript_string)
        return typescript_string
