import Network as nw
'''
# Define the nodes of the Bayesian network
rain = {'T': 0.6, 'F': 0.4}
sprinkler = {'T': {True: 0.1, False: 0.9}, 'F': {True: 0.5, False: 0.5}}

'''

# Define the dependencies between nodes
dependencies = {
    'Rain': ['Clouds', 'Sprinkler'],
    'Clouds': [],
    'Sprinkler': ['GrassWet'],
    'GrassWet': []
}

# Define the CPDs for each node
cpds = {
    'Rain': {'Probability': [0.1, 0.9], 'Parents': []},
    'Clouds': {'Probability': [0.8, 0.2], 'Parents': [('Rain', 0), ('Rain', 1)]},
    'Sprinkler': {'Probability': [0.7, 0.3], 'Parents': [('Rain', 0), ('Rain', 1)]},
    'GrassWet': {'Probability': [0.6, 0.4], 'Parents': [('Sprinkler', 0), ('Sprinkler', 1)]}
}
# Call object class
nw.Network(dependencies, cpds)
# New request
request = ('Sprinkler', ('GrassWet', 1))
nw.Network.jointProbability(dependencies, cpds, request)
