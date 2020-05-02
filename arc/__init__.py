from typing import List, Tuple, Union


class _Keycodes:
    """
    Returns multiple keycodes from
    a dictionary in one request.
    """
    def __init__(self) -> None:
        self.keys = {
            'enter':      13,
            'del':        127,
            'backspace':  8,
            'esc':        27,
            'c':          99,
            'x':          120,
            's':          115,
            '=':          61,
            '-':          45
        }

    def __getitem__(self, items: Union[str, Tuple]) -> List[int]:
        if isinstance(items, (int, str)):
            items = [items]

        return [self.keys[item] for item in items]


KEYS = _Keycodes()
