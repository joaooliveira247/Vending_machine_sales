def numeric_format(type_: str, x: float, total: int | float) -> str:
    match type_:
        case "percentage":
            return "{:.2f} %\n{} units".format(x, round(total * (x / 100)))
        case "money":
            return "{:.2f} %\nUSD: {:.2f}".format(x, total * (x / 100))
