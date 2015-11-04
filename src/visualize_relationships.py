__author__ = 'arkanath'

import operator
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import sys
import networkx as nx
import json
from nltk import word_tokenize
from nltk import pos_tag
import gzip
import math
import seaborn as sns
sns.set(color_codes=True)
sns.set(rc={"figure.figsize": (8, 4)}); np.random.seed(0)
hashtag_file_index = {}

def visualize(filename):
    total_done = 0
    last_done = 0
    top_characters = ['maximus', 'commodus', 'lucilla', 'proximo', 'marcus', 'juba', 'hagen', 'gracchus', 'cicero', 'lucius']
    G=nx.Graph()
    for c in top_characters:
        G.add_node(c)
    json_edges = {}
    with open(filename, 'rb+') as f:
        json_edges = json.load(f)

    threshold = 0.4
    for l in json_edges:
        if l not in top_characters:
            # print l, "not there, giddy up"
            continue
        for val in json_edges[l]:
            pers = val[0]
            if pers not in top_characters:
                continue
            weight = val[1]
            if weight<threshold:
                break
            G.add_edge(l, pers, weight=weight)
    pos=nx.circular_layout(G) # positions for all nodes
    e1=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > threshold and d['weight'] <= 0.7)]
    e2=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > 0.7 and d['weight'] <= 1.2)]
    e3=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > 1.2 and d['weight'] <= 1.5)]
    e4=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > 1.5)]
    nx.draw_networkx_nodes(G,pos,node_size=5)
    for (u,v,d) in G.edges(data=True):
        nx.draw_networkx_edges(G,pos,edgelist=[(u,v)], width=1+d['weight'], alpha = min(d['weight'],2.0)/2.0, edge_color='#2196F3')
    # nx.draw_networkx_edges(G,pos,edgelist=e1,width=0.5,alpha=0.3)
    # nx.draw_networkx_edges(G,pos,edgelist=e2,width=0.7,alpha=0.5)
    # nx.draw_networkx_edges(G,pos,edgelist=e3,width=1,alpha=1)
    # nx.draw_networkx_edges(G,pos,edgelist=e4,width=2,alpha=1, edge_color='#2196F3')
    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
    plt.axis('off')
    plt.show()
    # print json_data['iphone']
    # print "found", find_similarity(json_data['ipad'],json_data['iphone'])
    # for i in range(len(good_hashtags)):
    #     t=t+1
    #     print "doind", t
    #     j1 = json_data[good_hashtags[i]]
    #     for j in range(i+1,len(good_hashtags)):
    #         j2 = json_data[good_hashtags[j]]
    #         x = find_similarity(j1,j2)
    #         if x<1000000:
    #             continue
    #         if x not in edge_weights_lists:
    #             edge_weights_lists[x] = []
    #         edge_weights_lists[x].append((good_hashtags[i],good_hashtags[j]))
    #         edge_weights.append(x)
    #         G.add_edge(good_hashtags[i],good_hashtags[j],weight=x)
    # edge_weights = sorted(edge_weights)
    # edge_weights = list(reversed(edge_weights))
    # print len(edge_weights), edge_weights[0], edge_weights[1]
    # # edge_weights_lists = list(reversed(sorted(edge_weights_lists.items(), key=operator.itemgetter(0))))
    # # print edge_weights_lists[edge_weights[0]]
    # # plt.hist(edge_weights)
    # # plt.savefig("May_ipadgames_edgeweights_dot_cut_off.ps")
    # # plt.show()
    # # with open("weight_distribution_may_ipadgames.json","w+") as f:
    # #     json.dump(edge_weights_lists,f)
    # print t
    # pos=nx.circular_layout(G) # positions for all nodes
    # e1=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > 1000000 and d['weight'] <= 1500000)]
    # e2=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > 1500000 and d['weight'] <= 2500000)]
    # e3=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > 2500000 and d['weight'] <= 4000000)]
    # e4=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] > 4000000)]
    # # nodes
    # nx.draw_networkx_nodes(G,pos,node_size=5)
    # #
    # # # edges
    # nx.draw_networkx_edges(G,pos,edgelist=e1,width=0.5,alpha=0.3)
    # nx.draw_networkx_edges(G,pos,edgelist=e2,width=0.7,alpha=0.5)
    # nx.draw_networkx_edges(G,pos,edgelist=e3,width=1,alpha=1)
    # nx.draw_networkx_edges(G,pos,edgelist=e4,width=2,alpha=1, edge_color='r')
    # # nx.draw_networkx_edges(G,pos,edgelist=esmall,
    # #                     width=1,alpha=0.5,edge_color='b',style='dashed')
    # #
    # # # labels
    # nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
    # #
    # plt.axis('off')
    # # plt.savefig("Mat_ipadgames_graph_dot.ps") # save as png
    # plt.show() # display

visualize('file.json')