from vending_machine_sales.pipeline.utils import percent_format
from pandas import DataFrame, Series
from typing import Any


def null_fields(df: DataFrame) -> list[tuple[str, int]]:
    try:
        null_fields_count: Series = df.isnull().sum()
    except Exception:
        raise Exception("DataFrame don't loaded")

    null_fields = list(zip(null_fields_count.index, null_fields_count))

    return dict(
        [null_field for null_field in null_fields if null_field[1] > 0]
    )


def replace_null_values(df: DataFrame, replace: dict[str, Any]) -> DataFrame:
    for k, v in replace.items():
        try:
            df[k] = df[k].fillna(v)
        except Exception:
            raise KeyError(f"field {k} not found.")
    return df


def most_selling(df: DataFrame, n_plot: int = None) -> DataFrame | None:
    most_sell = (
        df[["Product", "Category", "MPrice", "MQty"]]
        .groupby(by=["Product", "MPrice"])
        .agg({"MQty": "count", "MPrice": "sum"})
        .rename(columns={"MQty": "Amount", "MPrice": "Sum"})
    )

    most_sell = (
        most_sell.groupby("Product")
        .sum()
        .sort_values("Amount", ascending=False)
    )

    if n_plot:
        n_most_sell = most_sell.head(n_plot)
        n_most_sell.plot.pie(
            y="Amount",
            figsize=(18, 18),
            autopct=lambda x: percent_format(x, n_most_sell["Amount"].sum()),
            title="Most Sell Products",
        )
        return

    return most_sell
