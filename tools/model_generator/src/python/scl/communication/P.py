#!/usr/bin/env python
""" generated source for module P """
from __future__ import print_function
# package: com.libiec61850.scl.communication
class P(object):
    """ generated source for class P """
    node = None
    type_ = None

    def __init__(self, pNode):
        """ generated source for method __init__ """
        self.node = pNode
        self.type_ = ParserUtils.parseAttribute(self.node, "type")
        if self.type_ == None:
            raise SclParserException(self.node, "type is missing in P element!")

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def getText(self):
        """ generated source for method getText """
        return self.node.getTextContent()

    def setText(self, text):
        """ generated source for method setText """
        self.node.setTextContent(text)

