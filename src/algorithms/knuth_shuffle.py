from random import randint


"""
At iteration i, pick integer r between 0 and i inclusive uniformly at random, then
swap the entries at positions i and r. Result will be a uniformly random permutation.
"""
def knuth_shuffle(array):
    for idx in range(len(array)):
        random_idx = randint(0, idx)
        array[idx], array[random_idx] = array[random_idx], array[idx]
    return array
