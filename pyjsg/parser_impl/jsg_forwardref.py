from typing import Set, List

_forward_template = """
{}_f_ = ForwardRef['{}']"""


class JSGForwardRef:
    def __init__(self, ref: str):
        self._ref = ref

    def as_python(self) -> str:
        # return _forward_template.format(self._ref, self.label)
        return ""

    def dependencies(self) -> Set[str]:
        # Forwards don't show dependencies
        return set(self.dependency_list())

    def dependency_list(self) -> List[str]:
        return []

    @property
    def label(self) -> str:
        return '"{}"'.format(self._ref)
