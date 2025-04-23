library(NbClust)
data <- read.csv('data/preprocessed_vectors.csv')
nb <- NbClust(data, distance = "euclidean", min.nc = 2, max.nc = 10, method = "kmeans")
k_optimal <- nb$Best.nc[1]
write(k_optimal, file = "data/optimal_k.txt")
