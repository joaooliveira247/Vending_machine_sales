from vending_machine_sales.pipeline.functions import (
    null_fields,
    replace_null_values,
)
from vending_machine_sales.pipeline.utils import percent_format
from pandas import DataFrame


class MostSellPipeline:
    def __init__(self, df: DataFrame) -> None:
        self.df = df

    @staticmethod
    def __plot(df: DataFrame, n_plot: int) -> None:
        df = df.head(n_plot)
        df.plot.pie(
            y="Amount",
            figsize=(18, 18),
            autopct=lambda x: percent_format(x, df["Amount"].sum()),
            title="Most Sell Products",
        )
        return

    @staticmethod
    def __group_by(df: DataFrame, field: str, rename: str = None) -> DataFrame:
        group = (
            df[["Product", field]]
            .groupby(by=["Product"])
            .agg({field: "count"})
            .rename(columns={field: rename})
        )

        group = group.sort_values(rename, ascending=False)
        return group

    def by_amount(self, n_plot: int = None) -> DataFrame | None:
        most_sell_amount = self.__group_by(self.df, "MQty", "Amount")

        if n_plot:
            self.__plot(most_sell_amount, n_plot)
            return

        return most_sell_amount
