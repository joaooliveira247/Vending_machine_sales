def percent_format(x: float, total: int | float) -> str:
    return "{:.2f} %\n{}".format(x, round(total * (x / 100)))
