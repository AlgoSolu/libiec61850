#!/usr/bin/env python
""" generated source for module FunctionalConstraintData """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013 Michael Zillgith
#  *
#  *	This file is part of libIEC61850.
#  *
#  *	libIEC61850 is free software: you can redistribute it and/or modify
#  *	it under the terms of the GNU General Public License as published by
#  *	the Free Software Foundation, either version 3 of the License, or
#  *	(at your option) any later version.
#  *
#  *	libIEC61850 is distributed in the hope that it will be useful,
#  *	but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  *	GNU General Public License for more details.
#  *
#  *	You should have received a copy of the GNU General Public License
#  *	along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
#  *
#  *	See COPYING file for the complete license text.
#  
class FunctionalConstraintData(object):
    """ generated source for class FunctionalConstraintData """
    ldInstance = None
    prefix = None
    lnClass = None
    lnInstance = None
    doName = None
    daName = None
    fc = None
    ix = None

    #  array index 
    def __init__(self, fcdaNode):
        """ generated source for method __init__ """
        self.ldInstance = ParserUtils.parseAttribute(fcdaNode, "ldInst")
        self.prefix = ParserUtils.parseAttribute(fcdaNode, "prefix")
        self.lnClass = ParserUtils.parseAttribute(fcdaNode, "lnClass")
        self.lnInstance = ParserUtils.parseAttribute(fcdaNode, "lnInst")
        self.doName = ParserUtils.parseAttribute(fcdaNode, "doName")
        self.daName = ParserUtils.parseAttribute(fcdaNode, "daName")
        fc = ParserUtils.parseAttribute(fcdaNode, "fc")
        if fc != None:
            self.fc = FunctionalConstraint.createFromString(fc)
        index = ParserUtils.parseAttribute(fcdaNode, "ix")
        if index != None:
            self.ix = int(index)

    def getLdInstance(self):
        """ generated source for method getLdInstance """
        return self.ldInstance

    def getLnClass(self):
        """ generated source for method getLnClass """
        return self.lnClass

    def getLnInstance(self):
        """ generated source for method getLnInstance """
        return self.lnInstance

    def getDoName(self):
        """ generated source for method getDoName """
        return self.doName

    def getDaName(self):
        """ generated source for method getDaName """
        return self.daName

    def getFc(self):
        """ generated source for method getFc """
        return self.fc

    def getIx(self):
        """ generated source for method getIx """
        return self.ix

    def getPrefix(self):
        """ generated source for method getPrefix """
        return self.prefix

    def __str__(self):
        """ generated source for method toString """
        string = ""
        if self.ldInstance != None:
            string = self.ldInstance + "/"
        if self.lnClass != None:
            if self.prefix != None:
                string += self.prefix
            string += self.lnClass
            if self.lnInstance == None:
                string += "."
        if self.lnInstance != None:
            string += self.lnInstance + "."
        if self.doName != None:
            string += self.doName
        if self.daName != None:
            string += "." + self.daName
        return string

