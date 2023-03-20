import re
from typing import List

class FromStatement:
    """Represent a python dataclass/typescript interface."""
    package: str
    modules: List[str]
    consecutive: bool

    SKIP_MODULES = None

    @staticmethod
    def set_skip_modules(skip_modules: List[str]):
        FromStatement.SKIP_MODULES = skip_modules

    def __init__(self, definition: List[str]):
        self.consecutive = True
        statement = definition[0]

        # Extract the package name.
        tokens = re.search("from (.*) import (.*)", statement)
        self.package = tokens.groups(0)[0]
        #print('package', self.package)
        self.modules = tokens.groups(0)[1].strip("()").split(",")
        #print('modules', self.modules)

    def get_typescript(self) -> str:
        """Return the import statement in typescript syntax."""
        if self.package in FromStatement.SKIP_MODULES:
            return ""

        typescript_string = "import {{ {0} }} from \'{1}\'\n".format(
            ', '.join(self.modules),
            self.package.replace('.', '/')
        )
        return typescript_string
