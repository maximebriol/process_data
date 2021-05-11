import tempfile
import pathlib
import pandas
import processing_data


def print(table: processing_data.Table) -> pandas.DataFrame:
    with tempfile.TemporaryDirectory() as folder:
        path = pathlib.Path(folder).joinpath("dump.csv")
        with path.open("w") as stream:
            stream.write(table.to_csv())
        return pandas.read_csv(path, sep=";")


def 