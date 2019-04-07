class EncodedNode:
    def __init__(self):
        self.subnodes = []
        self.metadata = []
        self.finished = False
        self.started = False
        self.num_meta = None
        self.value = None

    def __repr__(self):
        return f'metadata: {self.metadata} value: {self.value}'

    def process(self, e):
        if self.started == False:
            self.started = True
            self.num_subnodes = e
        elif self.num_meta == None:
            self.num_meta = e
        else:
            if not self.subnodes:
                self.subnodes = [EncodedNode() for i in range(self.num_subnodes)]
            for node in self.subnodes:
                if node.finished:
                    pass
                else:
                    node.process(e)
                    return
            if len(self.metadata) == self.num_meta:
                self.finished = True
            else:
                self.metadata.append(e)
                if len(self.metadata) == self.num_meta:
                    self.finished = True

    def start_node(self, num_nodes, num_meta):
        pass

    def add_metadata(self):
        pass


def process(tree):
    decoded_tree = EncodedNode()
    [decoded_tree.process(e) for e in tree]

    return decoded_tree


tree = open('input-8.txt').readline().split()
tree = [int(e) for e in tree]

# tree = [2, 2, 0, 1, 2, 0, 1, 3, 4, 5]

decoded_tree = process(tree)


def add_values(graph):
    # all_metadata = []
    visited, stack = set(), [graph]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            # all_metadata += vertex.metadata
            if not vertex.subnodes:
                vertex.value = sum(vertex.metadata)
                visited.add(vertex)
            else:
                for i in vertex.metadata:
                    try:
                        if vertex.subnodes[i - 1].value != None:
                            if vertex.value == None:
                                vertex.value = vertex.subnodes[i - 1].value
                            else:
                                vertex.value += vertex.subnodes[i - 1].value
                            visited.add(vertex)
                        else:
                            stack.append(vertex)
                            break
                    except IndexError:
                        pass
            for child in vertex.subnodes:
                if child not in visited:
                    stack.append(child)
    return graph


graph = add_values(decoded_tree)

print(graph)
