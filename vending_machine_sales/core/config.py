from pathlib import Path


class Settings:
    BASE_DIR = Path(__file__).parent.parent
    BASE_CSV_DIR = (BASE_DIR / "csv").__str__()


settings = Settings()