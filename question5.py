import datetime
import locale
import processing_data

# Pour décoder les dates en français
locale.setlocale(locale.LC_TIME, "fr_FR")


def main():
    filename = str(processing_data.data.school_holidays())

    pipeline = processing_data.Pipeline()

    pipeline.add_step(
        processing_data.transformer.JSONReader(filename, 'Calendrier'))
    pipeline.add_step(
        processing_data.transformer.Date(
            dict(Debut="%Y-%m-%d",
                 Fin="%Y-%m-%d",
                 DateDebut="%A %d %B %Y",
                 DateFin="%A %d %B %Y")))
    pipeline.add_step(
        processing_data.transformer.Select(dict(Zone="Zone C")))
    pipeline.add_step(
        processing_data.transformer.Select(
            dict(Description="Vacances de la Toussaint")))
    pipeline.add_step(
        processing_data.transformer.Select(
            dict(annee_scolaire="2020-2021")))
    calendar = pipeline.run()
    # On prend la première ligne
    row = calendar.get_row(0)
    begin, end = row[-2], row[-1]
    print(begin, end)

    filename = str(processing_data.data.covid_new())

    pipeline.clear()

    pipeline.add_step(processing_data.transformer.CSVReader(filename))
    pipeline.add_step(processing_data.transformer.Date(dict(jour="%Y-%m-%d")))
    pipeline.add_step(
        processing_data.transformer.Windowing("jour", begin, end))
    pipeline.add_step(processing_data.transformer.Cast(dict(incid_hosp=int)))
    table = pipeline.run()
    print(sum(table.get_column("incid_hosp")))



if __name__ == "__main__":
    main()