from vending_machine_sales.pipeline.functions import (
    null_fields,
    replace_null_values,
)
from vending_machine_sales.pipeline.utils import numeric_format
from pandas import DataFrame


class MostSellPipeline:
    def __init__(self, df: DataFrame) -> None:
        self.df = df

    @staticmethod
    def __plot(
        df: DataFrame,
        n_plot: int,
        field: str,
        type_: str,
    ) -> None:
        df = df.head(n_plot)
        df.plot.pie(
            y=field,
            figsize=(18, 18),
            autopct=lambda x: numeric_format(type_, x, df[field].sum()),
            title="Most Sell Products",
        )
        return

    @staticmethod
    def __group_by(
        df: DataFrame, field: str, agg: str, rename: str = None
    ) -> DataFrame:
        group = (
            df[["Product", field]]
            .groupby(by=["Product"])
            .agg({field: agg})
            .rename(columns={field: rename})
        )

        group = group.sort_values(rename, ascending=False)
        return group

    def by_amount(self, n_plot: int = None) -> DataFrame | None:
        most_sell_amount = self.__group_by(self.df, "MQty", "count", "Amount")

        if n_plot:
            self.__plot(most_sell_amount, n_plot, "Amount", "percentage")
            return

        return most_sell_amount

    def by_income(self, n_plot: int = None) -> DataFrame | None:
        most_sell_income = self.__group_by(self.df, "MPrice", "sum", "Income")

        if n_plot:
            self.__plot(most_sell_income, n_plot, "Income", "money")
            return

        return most_sell_income


class BestPlacePipeline:
    def __init__(self, df: DataFrame) -> None:
        self.df = df

    @staticmethod
    def __plot(
        df: DataFrame,
        n_plot: int,
        field: str,
        type_: str,
    ) -> None:
        df = df.head(n_plot)
        df.plot.pie(
            y=field,
            figsize=(18, 18),
            autopct=lambda x: numeric_format(type_, x, df[field].sum()),
            title="Most Sell Products",
        )
        return

    @staticmethod
    def __group_by(
        df: DataFrame, field: str, agg: str, rename: str = None
    ) -> DataFrame:
        group = (
            df[["Product", field]]
            .groupby(by=["Product"])
            .agg({field: agg})
            .rename(columns={field: rename})
        )

