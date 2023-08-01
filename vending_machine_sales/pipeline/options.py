from dataclasses import dataclass
from enum import Enum
from numpy import sum, size


class Aggregator(Enum):
    count = size
    sum = sum


@dataclass
class GroupOptions:
    fields: list[str]
    group_field: list[str]
    agg_field: str
    agg: Aggregator
    rename: str



@dataclass
class PlotOptions:
    ...
