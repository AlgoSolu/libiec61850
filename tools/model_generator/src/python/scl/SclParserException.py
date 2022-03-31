#!/usr/bin/env python
""" generated source for module SclParserException """
from __future__ import print_function
# package: com.libiec61850.scl
# 
#  *  SclParserException.java
#  *
#  *  Copyright 2013 Michael Zillgith
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
class SclParserException(Exception):
    """ generated source for class SclParserException """
    node = None

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(SclParserException, self).__init__()

    @__init__.register(object, str)
    def __init___0(self, message):
        """ generated source for method __init___0 """
        super(SclParserException, self).__init__(message)

    @__init__.register(object, Node, str)
    def __init___1(self, node, message):
        """ generated source for method __init___1 """
        super(SclParserException, self).__init__(message)
        self.node = node

    def getMessage(self):
        """ generated source for method getMessage """
        message = None
        if self.node != None:
            message = self.node.getNodeName() + " starting at line " + self.node.getUserData("START_LINE_NUMBER_ATTR") + " column " + self.node.getUserData("START_COLUMN_NUMBER_ATTR") + ": " + super(SclParserException, self).getMessage()
        else:
            message = super(SclParserException, self).getMessage()
        return message

    serialVersionUID = 6243253854159814835

