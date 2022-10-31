"""Implementation for store program data"""

import json
from pathlib import Path
from typing import Any, Callable


class State:
    """Implementation for store program state"""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def kwargs(self):
        return vars(self)

    @kwargs.setter
    def kwargs(self, value):
        raise AttributeError("You're trying to modify private member")

    @staticmethod
    def from_cfg(file: Path = Path("assets/state.cfg")):
        with open(file, "r") as f:
            return State(**json.load(f))

    def save(self, file: Path = Path("assets/state.cfg")):
        with open(file, "w") as f:
            json.dump(self.kwargs, f)

    def __str__(self) -> str:
        return str(self.kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)
