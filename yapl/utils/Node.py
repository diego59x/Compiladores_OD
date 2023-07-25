class Node():
    def __init__(self, token):
        self.token = token

class IntNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "Integer"