import datetime
import processing_data


def main():
    filename = str(processing_data.data.covid_incid_reg())
    pipeline = processing_data.Pipeline()

    pipeline.add_step(processing_data.transformer.CSVReader(filename))
    table = pipeline.run()

    print(table.nrows())


if __name__ == "__main__":
    main()