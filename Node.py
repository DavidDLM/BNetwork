# https://pomegranate.readthedocs.io/en/latest/BayesianNetwork.html
# https://towardsdatascience.com/bbn-bayesian-belief-networks-how-to-build-them-effectively-in-python-6b7f93435bba

class Node:
    node = None
    parentNodes = []

    def __init__(this, node):
        this.node = node  # name of the node

    def parentNodes(this):
        parentNodes = []
        for n in parentNodes:
            parentNodes.append(n.node)
        return ''.join(parentNodes)

    def __repr__(this):
        return this.name

    # With parent nodes
    def __str__(this):
        nod = this.node
        if this.parentNodes:
            nod += '|'
            for n in this.parentNodes:
                nod += n.node
        return nod
