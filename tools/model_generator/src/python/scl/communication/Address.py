#!/usr/bin/env python
""" generated source for module Address """
from __future__ import print_function
# package: com.libiec61850.scl.communication
class Address(object):
    """ generated source for class Address """
    node = None
    addressParameters = LinkedList()

    def __init__(self, addressNode):
        """ generated source for method __init__ """
        self.node = addressNode
        pNodes = ParserUtils.getChildNodesWithTag(self.node, "P")
        for pNode in pNodes:
            self.addressParameters.add(P(pNode))

    def getAddressParameters(self):
        """ generated source for method getAddressParameters """
        return self.addressParameters

    def getAddressParameter(self, type_):
        """ generated source for method getAddressParameter """
        for p in addressParameters:
            if p.getType() == type_:
                return p
        return None

