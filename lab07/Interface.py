from abc import ABC, abstractmethod


class NodeInterface(ABC):
    @abstractmethod
    def __init__(self, num):
        self.num = num
        self.name = str(num)
        self.inDeg = 0
        self.outDeg = 0
        self.toThe = []
        self.fromThe = []
        self.canTo = []
        self.canFrom = []

        self.allHomie = [self]
        self.homieName = str(num)

        """ Temp instance """
        self.color = ""
        self.d = -1
        self.f = -1
        self.pi = None

    @abstractmethod
    def leadTo(self, other):
        pass

    @abstractmethod
    def unLeadTo(self, other):
        pass

    @abstractmethod
    def comeFrom(self, other):
        pass

    @abstractmethod
    def unComeFrom(self, other):
        pass

    @abstractmethod
    def noteCanTo(self, other):
        pass

    @abstractmethod
    def noteCantTo(self, other):
        pass

    @abstractmethod
    def noteCanFrom(self, other):
        pass

    @abstractmethod
    def noteCantFrom(self, other):
        pass

    @abstractmethod
    def buildHomie(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass

    @staticmethod
    @abstractmethod
    def assertNode(x):
        pass

    @staticmethod
    @abstractmethod
    def assertEmptyNode(node):
        pass


class GraphInterface(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.wMatrix = []
        self.minWeightMatrix = []
        self.piMatrix = []
        self.components = []
        self.edgeNum = 0
        self.nodeNum = 0
        self.compNum = 0

    @abstractmethod
    def addNode(self, num):
        pass

    @abstractmethod
    def addEdge(self, u, v, twoSide, weight):
        pass

    @abstractmethod
    def buildComponent(self):
        pass

    @abstractmethod
    def FWAllPair(self):
        pass

    @abstractmethod
    def __invert__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @staticmethod
    @abstractmethod
    def matrixToText(matrix, nodeList):
        pass
