from .abc import AbstractEstimator
from .mean_estimator import MeanEstimator
from .table import Table
from random import randint
from typing import Any, List


class K_meansEstimator(AbstractEstimator):
    """Algorithme de clustering des K-means"""
    def distance_eucli(self, p1: List[Any], p2: List[Any]) -> float:
        """Calcul de la distance euclidienne

        Calcul de la distance euclidienne entre deux points p1 et p2 de taille n

        Parameters
        ----------
        p1 : list
            premier point représenté comme une liste de coordonées
        p2 : list
            deuxième point représenté comme une liste de coordonées

        Returns
        --------
        float
            retourne la distance euclidienne entre les 2 points de dimension n
        
        Examples
        --------
        >>>distance_eucli([1,2],[2,0])
        2,236
        """
        n = len(p1)
        s = 0
        for i in range(n):
            s += (p1[i] - p2[i])**2
        return s**0.5

    def fit(self, p1: List[Any], p2: List[Any]):
        return self.distance_eucli(p1, p2)

    def centre_classe(self, liste_individus: List[Any]):
        """Calcul du centre de la classe

        Calcul du centre de la classe composé d'individus à n observations

        Parameters
        ---------
        liste_individus:list(list)
            liste d'individus qui contiennent chacun n observations
        
        Returns
        --------
        list 
            retourne la liste des moyennes de chaque observation
        
        Examples
        --------
        >>>centre_classe([[1,2],[2,5]])
        [1.5,3.5]
        """
        n = len(liste_individus[1])  #nb de variables des individus
        nb_ind = len(liste_individus)
        centre = []
        for i in range(n):
            liste = []
            for j in range(nb_ind):
                liste.append(liste_individus[j][i])
            centre.append(MeanEstimator.mean(liste))
        return centre  #c'est une liste composé des moyennes de chaque composantes

    def K_means(self, nb_clusters, table: Table):
        """Algorithme de clustering du K-means

        A partir d'un tableau de valeurs, regroupe des observations en classes
        
        Parameters
        ----------
        nb_clusters:float
            nombre de clusters souhaité par l'utilisateur
        table:list(list)
            tableau de valeur, on souhaiter classer les observations en colonnes
        
        Returns
        ---------
        list(list)
            retourne une liste de liste, de taille nb_clusters où dans chaque élément on retrouve les observations les plus proches par rapport à la distance euclidienne
        
        Examples
        ---------
        table=[[100,100,100],[2,2,2],[2,4,1],[1,0,1]]
        >>>K_means(2,table)
        [[[2, 2, 2], [2, 4, 1], [1, 0, 1]], [[100, 100, 100]]]
        """
        columns = table.column_names()
        n = table.nrows(
        )  #c'est la taille des colonnes, donc le nb d'individus
        centres_classes = []
        for j in range(nb_clusters):
            liste = [randint(0, 100) for i in range(n)]
            centres_classes.append(
                liste
            )  # il y a nb_clusters centres de classes, qui est de meme taille d'une observation
        cluster = [[] for i in range(nb_clusters)
                   ]  #liste de listes d'observations d'une même classe
        cluster_fin = [[0] for i in range(nb_clusters)]
        s = 0
        while cluster != cluster_fin or s > 15:  #15 est mis au hasard, jsp qd définir le cran d'arrêt
            cluster_fin = cluster
            liste_distance = []
            for l in range(nb_clusters+1):
                liste_distance.append([])
            for name in columns:
                for j in range(nb_clusters):
                    liste_distance[j] = K_meansEstimator.distance_eucli(
                        self, table.get_column(name), centres_classes[j]
                    )  #distance eucli entre l'individu de la ligne j et le ieme des centres
                mini = liste_distance.index(
                    min(liste_distance)
                )  #la place de la plus petite distance entre la ligne et le centre
                cluster[mini].append(table.get_column(name))
                centres_classes[mini] = K_meansEstimator.centre_classe(
                    self, [centres_classes[mini],
                           table.get_column(name)
                           ])  #on recalcule le centre de la classe
            return cluster
        s = s + 1
        return cluster