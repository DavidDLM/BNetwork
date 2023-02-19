# https://pomegranate.readthedocs.io/en/latest/BayesianNetwork.html
# https://towardsdatascience.com/bbn-bayesian-belief-networks-how-to-build-them-effectively-in-python-6b7f93435bba

import Node

'''
Define the nodes of the Bayesian network: Identify the variables that will be modeled as nodes in the Bayesian network. Each node represents a random variable in the domain of interest.

Define the dependencies between nodes: Determine which nodes depend on which other nodes. This defines the structure of the Bayesian network.

Define the conditional probability distributions (CPDs) for each node: For each node in the network, define the conditional probability distribution given its parents in the network.

Implement inference algorithms: Given the structure and CPDs of the network, you can perform inference to compute posterior probabilities of unobserved variables.

'''


class Network(object):
    def __init__(this, network, cpd):
        this.network = network
        this.cpd = cpd
        this.returnNetwork()
    '''
    # Necessary functions: addProbability, inference, enumerate
        def addNode(this, name):
            newNode = Node(name)
            this.nodes.append(newNode)
    '''

    # BNetwork in a compact state
    def analyze(this):
        sortedNodes = None
        net = ""
        for node, values in this.network.items():
            if len(values) == 0:
                net += "P(" + node + ")"
            else:
                net += "P(" + node + "|"
                for parent in values:
                    net += parent
                net += ")"

        print("Analysis: ", net)
        return net

    # BNetwork format
    def format(this):
        nodes = this.cpd.keys()
        for nod in nodes:
            if nod in this.cpd[nod]["Parents"]:
                print("Circular dependencies")
                return False
            for parent in this.cpd[nod]["Parents"]:
                if parent[0] not in nodes:
                    print("Parent error")
                    return False
            if not isinstance(this.cpd[nod]["Probability"], list):
                print("Probability error")
        return True
    '''
        Bayesian enumeration algorithm is a probabilistic approach to solving combinatorial optimization problems. It is commonly used to find the optimal combination of variables that maximizes the objective function.

        The algorithm starts by defining a prior distribution over the space of possible solutions. This prior represents our initial belief about the probability of each solution being optimal. The algorithm then evaluates each possible solution, computes its likelihood based on the data and updates the posterior distribution using Bayes' rule.

        At each iteration, the algorithm selects the solution with the highest probability of being optimal, and generates new candidate solutions based on this solution. These new solutions are evaluated and added to the posterior distribution. The process is repeated until convergence or a stopping criterion is met.

    '''
    # Unfinished enumeration algorithm
    def enumeration(this):
        for node, values in this.cpd.items():
            totalProbability = 1
            if sum(values["Probability"]) != totalProbability:
                print("Probability error in network")

    # Implement inference algorithms
    '''
    # Implement inference algorithms
    def calculate_joint_probability(rain_value, sprinkler_value):
        return rain[rain_value] * sprinkler[sprinkler_value][rain_value]
        
    def calculate_marginal_probability(node, value):
        if not dependencies[node]:
            return cpds[node][value]
        else:
            parent_values = list(cpds[dependency][parent_value] for dependency in dependencies[node] for parent_value in [True, False])
            return cpds[node][value]['T']*parent_values[0] + cpds[node][value]['F']*parent_values[1]
    '''
    def jointProbability(dependencies, cpd, request):
        # Total probability should be 1
        total_probability = 1
        # For negated probabilities
        negated = '-'
        # Parent nodes from request
        parentNodes = dependencies[request[0]]
        # For value in the request
        for parent in parentNodes:
            parentNode = None
            for rq in request[1:]:
                if rq[0] == parent:
                    parentNode = rq[1]
            if not parentNode:
                return None
            parentNodeIndex = cpd[parent]['Parents'].index(
                (request[0], parentNode))
            total_probability *= cpd[parent]['Probability'][parentNodeIndex]
        return total_probability

    def marginalProbability(dependencies, cpd, request):
        return

    def returnNetwork(this):
        this.analyze()
        this.enumeration()
