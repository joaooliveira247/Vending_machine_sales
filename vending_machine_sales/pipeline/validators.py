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
        return True
    return False


def load_csv(path: str) -> pd.DataFrame | None:
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"{path} not found.")

    if validate_df(df):
        return df
    raise Exception(
        "columns name not match with Vending Machine Sales default."
    )
