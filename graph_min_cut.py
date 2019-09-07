import random
import copy
"""
Implementation of Random Contraction Algorithm

"""

#Returns vertex count of an adjacency list.
def v_count(adj_lst):
    return sum([1 for x in adj_lst if x])

#Contract two node together with given nodes.
def contraction(adj_lst, u, v):
    min_u = min(u,v)
    max_v = max(u,v)
    edges_u = adj_lst[min_u]
    edges_v = adj_lst[max_v]
    new_edges = edges_u + edges_v
    while min_u in new_edges: new_edges.remove(min_u)
    while max_v in new_edges: new_edges.remove(max_v)
    adj_lst[min_u] = new_edges
    adj_lst[max_v] = []
    for i in adj_lst:
        for j in range(len(i)):
            if i[j] == min_u or i[j] == max_v:
                i[j] = min_u
    return None

#Returns the list of remaining nodes
def remaining_indexes(adj_lst):
    return [x for x in range(len(adj_lst)) if adj_lst[x]]

#Apply One Minimum Cut algorithm.
def min_cut(lst):
    adj_lst = copy.deepcopy(lst)
    while v_count(adj_lst) >2:
        rem_index = remaining_indexes(adj_lst)
        u = random.choice(rem_index)
        v = random.choice(adj_lst[u])
        contraction(adj_lst, u, v)
    print(adj_lst)
    return len(adj_lst[1])

#Applies multiple Minimum Cut Algorithm.
def multiple_min_cut(adj_lst):
    minimum = 9999999
    for _ in range(500):
        returned_val = min_cut(adj_lst)
        if returned_val < minimum:
            minimum = returned_val
    return minimum

