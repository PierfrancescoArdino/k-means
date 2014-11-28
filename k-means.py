__author__ = 'pier'
"""
	Author: Ardino Pierfrancesco
	K-Means top down implementation
"""
import numpy as np
import matplotlib.pyplot as plt
import random


def distanza(element, centroide):  # funzione per calcolare la distanza euclidea
    """
    Calcola distanza euclidea tra due punti
    :param element:
    :param centroide:
    :return: distanza
    """
    return np.sqrt((element[0] - centroide[0]) ** 2 + (element[1] - centroide[1]) ** 2)


colors = ['b', 'g', 'r', 'm', 'k', 'c']
num = input("Insert number of element ")
k = input("Insert the number of cluster max 6 (too many cluster can make some problem with te centroids ")
k = int(k)
num = int(num)
# dataset di "esempi" creati con k diverse distribuzioni, non sono sicurissimo della esponenziale

dataset = [[np.random.uniform(-5, 5), np.random.uniform(-5, 5)] for item in range(num)]
random.shuffle(dataset)  # randomizzo gli esempi
# assegno tramite slicing gli esempi a dei cluster
cluster = [dataset[int((num / k) * i):int((num / k) * (i + 1))] for i in range(k)]
# calcolo i centroidi dei cluster
centroids = [[np.random.uniform(-5, 5), np.random.uniform(-5, 5)] for i in range(k)]
xpoints = []
ypoints = []
# suddivido i punti in due liste per cluster per poi disegnarli tramite un plot

for i in range(0, k):
    xpoints.append([])
    ypoints.append([])
    for j in cluster[i]:
        xpoints[i].append(j[0])
        ypoints[i].append(j[1])
    xpoints[i] = np.array(xpoints[i]).flatten()
    ypoints[i] = np.array(ypoints[i]).flatten()
# visualizzo gli esempi del cluster 1 con dei pallini rossi, cluster 2 con pallini ble e cluster 3 con pallini verdi,
# i centroidi hanno i colori dei rispettivi cluster ma vengono visualizzati tramite triangoli
for i in range(0, k):
    centroid = centroids[i]
    plt.plot(xpoints[i], ypoints[i], str(colors[i]) + 'o', centroid[0], centroid[1], str(colors[i]) + '^')
# plt.axis([-10, 10, -10.0, 10.0])
plt.show()
# ricalcolo il tutto per un massimo di 30 volte
for loops in range(0, 30):
    print(loops)
    cluster_new = [[] for i in range(0, k)]
    centroids_new = []
    # calcolo e controllo la distanza per ogni elemento dei cluster e lo riassegno al cluster più vicino
    for element in dataset:
        dist = []
        for i in range(0, k):
            if centroids[i] != []:
                dist.append(distanza(element, centroids[i]))
        cluster_new[dist.index(min(dist))].append(element)
    # ricalcolo i centroidi
    for i in range(0, k):
        if cluster_new[i] != []:
            centroids_new.append(np.mean(cluster_new[i], axis=0))
        else:
            centroids_new.append([])
    xpoints = [[] for i in range(0, k)]
    ypoints = [[] for i in range(0, k)]
    for i in range(0, k):
        for j in cluster_new[i]:
            xpoints[i].append(j[0])
            ypoints[i].append(j[1])
        xpoints[i] = np.array(xpoints[i])
        ypoints[i] = np.array(ypoints[i])
    d = 0
    for i in range(0, k):
        if centroids_new[i] != [] and centroids[i] != []:
            d += distanza(centroids_new[i], centroids[i])
    if d < 0.2:
        break
    centroids = centroids_new
    print(centroids)

    # se i centroidi sono gli stessi di prima mi fermo altrimenti vado avanti
    for i in range(0, k):
        if centroids_new[i] != [] and centroids[i] != []:
            centroid = centroids_new[i]
            plt.plot(xpoints[i], ypoints[i], str(colors[i]) + 'o', centroid[0], centroid[1], str(colors[i]) + '^')
            # plt.axis([-10, 10, -10.0, 10.0])
    plt.show()
