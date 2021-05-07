
class NormalisationTransformer(AbstractTransformer) :
    def normalisation(self, table : Table):
            """Normaliser les colonnes d'un tableau de valeurs
            
            Parameters
            --------
            table : list(list)
                tableau de valeurs dont les colonnes sont à normaliser
            
            Returns
            ------
            list(list)
                retourne un tableau 
            ...
            
            """
    for column in table.ncolumns() : 
            for i in range(0, len(column)):
                column[i] = column[i]-column.MeanEstimator.mean()
    return table.ncolumns() #on retourne pas column ?