from dataclasses import dataclass
from enum import Enum
from numpy import sum, size
from vending_machine_sales.pipeline.utils import TypeFormat


class Aggregator(Enum):
    count = size
    sum = sum


class PlotGrafic(Enum):
    pie = "pie"
    line = "line"


@dataclass
class GroupOptions:
    fields: list[str]
    group_fields: list[str]
    agg_field: str
    agg: Aggregator
    rename: str


@dataclass
class PlotOptions:
    kind: PlotGrafic
    n_plot: int
    field: str
    type_: TypeFormat
    title: str
