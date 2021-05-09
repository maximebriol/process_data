from ..k_meansestimator import K_meansEstimator
from ..table import Table

def test_distance_euclidienne():
    liste=[[1,2],[2,5]]
    table=Table(["A","B","C"])
    table.append_row([100,100,100])
    table.append_row([2,2,2])
    table.append_row([2,4,1])
    table.append_row([1,0,1])

    k_means = K_meansEstimator()
    assert k_means.centre_classe(liste) == [1.5,3.5]
    assert k_means.K_means(2, table) == [[[2, 2, 2], [2, 4, 1], [1, 0, 1]], [[100, 100, 100]]]