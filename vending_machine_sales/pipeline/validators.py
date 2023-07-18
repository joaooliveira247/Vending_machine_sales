import pandas as pd

def validate_df(df: pd.DataFrame) -> pd.DataFrame | None:
    columns = [
        "Status",
        "Device ID",
        "Location",
        "Machine",
        "Product",
        "Category",
        "Transaction",
        "TransDate",
        "Type",
        "RCoil",
        "RPrice",
        "RQty",
        "MCoil",
        "MPrice",
        "MQty",
        "LineTotal",
        "TransTotal",
        "Prcd Date",
    ]
    if all([df_column in columns for df_column in list(df.columns)]):
        return df
    raise Exception(f"Check if headers are set correctly.\nLike: \n{columns}")