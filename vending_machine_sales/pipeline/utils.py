from enum import Enum

class TypeFormat(Enum):
    monetary = None,
    amount = None

def numeric_format(type_: TypeFormat, x: float, total: int | float) -> str:
    match type_:
        case TypeFormat.amount:
            return "{:.2f} %\n{} units".format(x, round(total * (x / 100)))
        case TypeFormat.monetary:
            return "{:.2f} %\nUSD: {:.2f}".format(x, total * (x / 100))
