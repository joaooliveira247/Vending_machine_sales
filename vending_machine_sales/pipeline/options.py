from dataclasses import dataclass
from enum import Enum
from numpy import sum, size


class Aggregator(Enum):
    count = size
    sum = sum


@dataclass
class GroupOptions:
    ...


@dataclass
class PlotOptions:
    ...
