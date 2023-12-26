from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
import time

# draws a scatterplot such that each cluster's points are in different colors 
def draw_clustered_graph(k, X, clusters, centroids):
  colors = ['r', 'g', 'b', 'y', 'c', 'm']
  fig, ax = plt.subplots()
  for i in range(k):
    xpoints = []
    ypoints = []
    for j in range(len(X)):
      if clusters[j] == i:
        xpoints.append(X[j][0])
        ypoints.append(X[j][1])
    ax.scatter(xpoints, ypoints, s=7, c=colors[i])
  xpoints = []
  ypoints = []
  for c in centroids:
    xpoints.append(c[0])
    ypoints.append(c[1])
  ax.scatter(xpoints, ypoints, marker='H', s=200, c='#050505')
  plt.savefig("clustered_graph.png")
  plt.show()
  


#Here we get all the points for our algorithm to cluster.
points = []
data = pd.read_csv('customers.csv')

income = data.iloc[0:]['Annual Income']
spending = data.iloc[0:]['Spending Score']

for i in range(len(income)):
  points.append((income[i],spending[i]))


def euclidean(p1,p2):
  #We have implemented Euclidean Distance here!
  distance = math.sqrt(abs((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))
  return distance
  
def kmeans(k,points):
  centroids = []
  #Only add random centroids if the centroids list is empty.
  for i in range(k):
    centroids.append(((random.randint(0,140)), (random.randint(0,100))))
  #Now here we use the Euclidean function to calculate the distance from every point to the centroids.
  while True:
    #Here we make the list and dictionary
    clusters = []
    clustersDict = {}
    for point in points:
      euclideans = []
      for centroid in centroids:
        euclideans.append(euclidean(point,centroid))
      smallest = euclideans[0]
      for dist in euclideans:
        if dist < smallest:
          smallest = dist
      smallestIndex = euclideans.index(smallest)
      clusters.append(smallestIndex)
      clustersDict[point] = smallestIndex
    #print("Code Reached")
    #draw_clustered_graph(k,points,clusters,centroids)
  
    pointsClusters = []
    for i in range(k):
      pointsClusters.append([])
    for key in clustersDict:
      pointsClusters[clustersDict[key]].append(key)
  
    new_centroids = []
    for innerlist in pointsClusters:
      sumX,sumY = 0,0
      for point in innerlist:
        sumX += point[0]
        sumY += point[1]
      averageX = sumX/len(innerlist)
      averageY = sumY/len(innerlist)
      new_centroids.append((averageX,averageY))
  
    if new_centroids == centroids:
      print("[*] Final Result K-Means")
      draw_clustered_graph(k,points,clusters,centroids)
      break
    else:
      centroids = new_centroids



kmeans(5,points)


