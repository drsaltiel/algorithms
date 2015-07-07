'''
implementation of basic adjacency list directed graph object
'''


class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def add_neighbor(self, neighbor, weight=1):
        '''
        adds neighbor to vertex
        '''
        self.connections[neighbor] = weight

    def get_connections(self):
        '''
        returns vertexes connected to vertex
        '''
        return self.connections.keys()

    def id(self):
        '''
        returns id of vertex
        '''
        return self.id

    def weight(self, neighbor):
        '''
        returns weight between vertex and neighbor
        '''
        return self.connecttions[neighbor]


class Graph(object):
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        '''
        adds vertex to graph
        '''
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def find_vertex(self, n):
        '''
        returns vertex if in graph
        '''
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def add_edge(self, a, b, weight=1):
        '''
        adds directed edge from vertex a to vertez b
        '''
        if a not in self.vert_list:
            self.add_vertex(a)
        if b not in self.vert_list:
            self.add_vertex(b)
        self.vert_list[a].add_neighbor(self.vert_list[b], weight)

    def get_vertices(self):
        '''
        returns all vertices
        '''
        return self.vert_list.keys()
