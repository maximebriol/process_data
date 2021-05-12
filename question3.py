import datetime
import processing_data
import processing_data.cartoplot


def plot(table: processing_data.Table, filename: str):
    data = {}
    for k, v in zip(table.get_column("dep"), table.get_column("incid_hosp")):
        data[k] = v
    cp = processing_data.cartoplot.CartoPlot()
    fig = cp.plot_dep_map(data=data, x_lim=(-6, 10), y_lim=(41, 52))
    fig.show()
    fig.savefig(filename)

def main():
    filename = str(processing_data.data.covid_new())

    # Date du jour
    now = datetime.datetime(2021, 3, 3)

    pipeline = processing_data.Pipeline()

    pipeline.add_step(processing_data.transformer.CSVReader(filename))
    pipeline.add_step(processing_data.transformer.Date(dict(jour="%Y-%m-%d")))
    pipeline.add_step(
        processing_data.transformer.Windowing("jour",
                                              now - datetime.timedelta(days=7),
                                              now))
    pipeline.add_step(processing_data.transformer.Cast(dict(incid_hosp=int)))
    table = pipeline.run()
    print(
        processing_data.estimatator.Mean.calculate(
            table.get_column("incid_hosp")))
    plot(table, "question3_current_week.png")

    pipeline.add_step(processing_data.transformer.CSVReader(filename))
    pipeline.add_step(processing_data.transformer.Date(dict(jour="%Y-%m-%d")))
    pipeline.add_step(
        processing_data.transformer.Windowing(
            "jour", now - datetime.timedelta(days=14),
            now - datetime.timedelta(days=7)))
    pipeline.add_step(processing_data.transformer.Cast(dict(incid_hosp=int)))
    table = pipeline.run()
    print(
        processing_data.estimatator.Mean.calculate(
            table.get_column("incid_hosp")))
    plot(table, "question3_previous_week.png")


if __name__ == "__main__":
    main()