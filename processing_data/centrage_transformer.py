class CentrageTransformer(AbstractTransformer):
    def centrage(self, table : Table):
            """Centrer les colonnes d'un tableau de valeurs
            
            Parameters
            --------
            table : list(list)
                tableau de valeurs dont les colonnes sont à centrer
            
            Returns
            ------
            list(list)
                retourne un tableau 
            ...
            
            """
    table.NormalisationTransformer.normalisation()
    for column in table.ncolumns():
            for i in range(O, len(column)):
                column[i] = column[i]/sqrt(column.VarianceEstimator())
    return table.ncolumns() 
        