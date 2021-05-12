from typing import Any, List
import copy
import random

from ..table import Table
from .abc import AbstractEstimator
from .mean import Mean


def euclidean_distance(p1: List[Any], p2: List[Any]) -> float:
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
    >>>euclidian_distance([1,2],[2,0])
    2,236
    """
    sum = 0
    for ix in range(len(p1)):
        #On calcule la distance euclidienne au carré
        sum += (p1[ix] - p2[ix])**2
        #On récupère la distance euclidienne.
    return sum**0.5


def center_class(samples: List[List[Any]]) -> List[Any]:
    """Calcul du centre de la classe

    Calcul du centre de la classe composé d'individus à n observations

    Parameters
    ---------
    samples:list(list)
        liste d'individus qui contiennent chacun n observations

    Returns
    --------
    list
        retourne la liste des moyennes de chaque observation

    Examples
    --------
    >>>center_class([[1,2],[2,5]])
    [1.5,3.5]
    """
    # Nombre de variables des individus
    n = len(samples[1])
    center = []
    for ix in range(n):
        center.append(Mean.calculate([item[ix] for item in samples]))
        #On  calcule les centres de toutes les classes.
    return center


class KMeans(AbstractEstimator):
    """Algorithme de clustering des K-means"""
    def fit(self, table: Table) -> Table:
        raise NotImplementedError()

    @staticmethod
    def calculate(nb_clusters, table: Table) -> List[List[Any]]:
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
            Une liste de liste, de taille nb_clusters où dans chaque élément on
            retrouve les observations les plus proches par rapport à la distance
            euclidienne

        Examples
        ---------
        table=[[100,100,100],[2,2,2],[2,4,1],[1,0,1]]
        >>>k_means(2,table)
        [[[2, 2, 2], [2, 4, 1], [1, 0, 1]], [[100, 100, 100]]]
        """
        columns = table.column_names()
        # C'est la taille des colonnes, donc le nb d'individus
        n = table.nrows()
        center_classes = []
        for ix in range(nb_clusters):
            values = [random.randint(0, 100) for _ in range(n)]
            # Il y a nb_clusters centres de classes, qui est de meme taille
            # d'une observation
            center_classes.append(values)
        # Liste de listes d'observations d'une même classe
        cluster = []
        # 15 est mis au hasard, jsp qd définir le cran d'arrêt
        for _ in range(15):
            end_cluster = copy.deepcopy(cluster)
            cluster = [[] for _ in range(nb_clusters)]
            distances = [0.0 for _ in range(nb_clusters)]
            for name in columns:
                for ix in range(nb_clusters):
                    # distance euclidienne entre l'individu de la ligne ix et le
                    # ieme des centres
                    distances[ix] = euclidean_distance(table.get_column(name),
                                                       center_classes[ix])
                # la place de la plus petite distance entre la ligne et le
                # centre
                min_value = distances.index(min(distances))
                cluster[min_value].append(table.get_column(name))
                # on recalcule le centre de la classe
                center_classes[min_value] = center_class(
                    [center_classes[min_value],
                     table.get_column(name)])
            if cluster == end_cluster:
                break
        return cluster
