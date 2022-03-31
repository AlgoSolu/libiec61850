#!/usr/bin/env python
""" generated source for module SMV """
from __future__ import print_function
# package: com.libiec61850.scl.communication
# 
#  *  Copyright 2015 Michael Zillgith
#  *
#  *  This file is part of libIEC61850.
#  *
#  *  libIEC61850 is free software: you can redistribute it and/or modify
#  *  it under the terms of the GNU General Public License as published by
#  *  the Free Software Foundation, either version 3 of the License, or
#  *  (at your option) any later version.
#  *
#  *  libIEC61850 is distributed in the hope that it will be useful,
#  *  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  *  GNU General Public License for more details.
#  *
#  *  You should have received a copy of the GNU General Public License
#  *  along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
#  *
#  *  See COPYING file for the complete license text.
#  
class SMV(object):
    """ generated source for class SMV """
    ldInst = None
    cbName = None
    address = None

    def __init__(self, gseNode):
        """ generated source for method __init__ """
        self.ldInst = ParserUtils.parseAttribute(gseNode, "ldInst")
        self.cbName = ParserUtils.parseAttribute(gseNode, "cbName")
        if (self.ldInst == None) or (self.cbName == None):
            raise SclParserException(gseNode, "SMV is missing required attribute")
        addressNode = ParserUtils.getChildNodeWithTag(gseNode, "Address")
        if addressNode == None:
            raise SclParserException(gseNode, "SMV is missing address definition!")
        self.address = PhyComAddress(addressNode)

    def getLdInst(self):
        """ generated source for method getLdInst """
        return self.ldInst

    def getCbName(self):
        """ generated source for method getCbName """
        return self.cbName

    def getAddress(self):
        """ generated source for method getAddress """
        return self.address

