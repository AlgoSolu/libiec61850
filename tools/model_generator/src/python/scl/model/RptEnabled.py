#!/usr/bin/env python
""" generated source for module RptEnabled """
from __future__ import print_function
# package: com.libiec61850.scl.model
class RptEnabled(object):
    """ generated source for class RptEnabled """
    maxInstances = 1
    desc = None
    clientLNs = LinkedList()

    def __init__(self, rptEnabledNode):
        """ generated source for method __init__ """
        self.desc = ParserUtils.parseAttribute(rptEnabledNode, "desc")
        maxString = ParserUtils.parseAttribute(rptEnabledNode, "max")
        if maxString != None:
            self.maxInstances = int(maxString)
        clientLNNodes = ParserUtils.getChildNodesWithTag(rptEnabledNode, "ClientLN")
        for clientLNNode in clientLNNodes:
            clientLN = ClientLN(clientLNNode)
            self.clientLNs.add(clientLN)

    def getMaxInstances(self):
        """ generated source for method getMaxInstances """
        return self.maxInstances

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getClientLNs(self):
        """ generated source for method getClientLNs """
        return self.clientLNs

