import datetime
import processing_data
import processing_data.cartoplot


def main():
    filename = str(processing_data.data.covid_age())

    # Date du jour
    now = datetime.datetime(2021, 3, 3)

    pipeline = processing_data.Pipeline()

    pipeline.add_step(processing_data.transformer.CSVReader(filename))
    pipeline.add_step(processing_data.transformer.Date(dict(jour="%Y-%m-%d")))
    pipeline.add_step(
        processing_data.transformer.Windowing("jour",
                                              now - datetime.timedelta(days=7),
                                              now))
    pipeline.add_step(processing_data.transformer.Aggregation(["reg"],
                                                              "count"))

    table = pipeline.run()

    filename = str(processing_data.data.region())
    pipeline.add_step(
        processing_data.transformer.CSVReader(filename, delimiter=","))
    table = table.join(pipeline.run(), "reg")

    data = {}
    for k, v in zip(table.get_column("ncc"), table.get_column("hosp")):
        data[k] = v
    cp = processing_data.cartoplot.CartoPlot()
    fig = cp.plot_reg_map(data=data)
    fig.savefig('question2.jpg')

    print(table)


if __name__ == "__main__":
    main()