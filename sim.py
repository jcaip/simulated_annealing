import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


num_points = 100

def start():
    #set up enviorment and create points
    temp, coolingRate = 1000, 0.0002
    locs = np.random.randint(0, 200, size=(num_points,2))

    #create the starting path
    startingPath = np.insert(np.random.permutation(num_points-1) +1, 0, 0)
    currentPath = startingPath
    # array to keep track of the distances
    distance = []

    while(temp>1):
        neighbor = getNeighbors(currentPath)
        e_prime = computePath(locs, neighbor)
        e_current = computePath(locs, currentPath)

        probability = np.exp((e_current - e_prime) / temp)

        if e_prime < e_current:
            currentPath = neighbor
        elif probability > np.random.rand():
            currentPath = neighbor

        # print(currentPath)
        distance.append(computePath(locs, currentPath))

        temp *= 1-coolingRate;

    plt.subplot(211)
    plt.title("Distance v. # of Iterations")
    plt.plot(range(len(distance)), distance)

    plt.subplot(212)
    plot(locs, currentPath)

def plot(locs, path):
    plt.scatter(locs[:,0], locs[:,1])
    for j in path:
        i = path[j]
        k = path[(j+1) % len(path)]
        point = locs[i]
        point2= locs[k]
        plt.plot([point[0], point2[0]], [point[1], point2[1]])
    plt.title("END RESULT | Distance: " + str(computePath(locs, path)))
    plt.show()

def computePath(locs, path):
    dist = 0 
    for j in path:
        i = path[j]
        k = path[(j+1) % len(path)]
        point = locs[i]
        point2= locs[k]
        dist += (point[0]-point2[0])**2 + ( point[1]-point2[1])**2
    return dist

def getNeighbors(path_in):
    path = list(path_in)
    index1, index2 = np.random.choice(path, size=(2,1), replace=True)
    path[index1:index2] = reversed(path[index1:index2])
    return path

if __name__ == "__main__":
    start()
