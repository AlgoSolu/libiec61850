#!/usr/bin/env python
""" generated source for module OptionFields """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013, 2014 Michael Zillgith
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
class OptionFields(object):
    """ generated source for class OptionFields """
    # 
    #      * #define RPT_OPT_SEQ_NUM 1 #define RPT_OPT_TIME_STAMP 2 #define
    #      * RPT_OPT_REASON_FOR_INCLUSION 4 #define RPT_OPT_DATA_SET 8 #define
    #      * RPT_OPT_DATA_REFERENCE 16 #define RPT_OPT_BUFFER_OVERFLOW 32 #define
    #      * RPT_OPT_ENTRY_ID 64 #define RPT_OPT_CONF_REV 128
    #      
    seqNum = False
    timeStamp = False
    dataSet = False
    reasonCode = False
    dataRef = False
    entryID = False
    configRef = False
    bufOvfl = True

    # 
    #      * Get integer value for report options
    #      * 
    #      * @return
    #      
    def getIntValue(self):
        """ generated source for method getIntValue """
        intValue = 0
        if self.seqNum:
            intValue += 1
        if self.timeStamp:
            intValue += 2
        if self.reasonCode:
            intValue += 4
        if self.dataSet:
            intValue += 8
        if self.dataRef:
            intValue += 16
        if self.bufOvfl:
            intValue += 32
        if self.entryID:
            intValue += 64
        if self.configRef:
            intValue += 128
        return intValue

    def __init__(self, optFieldsNode):
        """ generated source for method __init__ """
        boolVal = None
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "seqNum")
        if boolVal != None:
            self.seqNum = boolVal
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "timeStamp")
        if boolVal != None:
            self.timeStamp = boolVal
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "dataSet")
        if boolVal != None:
            self.dataSet = boolVal
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "reasonCode")
        if boolVal != None:
            self.reasonCode = boolVal
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "dataRef")
        if boolVal != None:
            self.dataRef = boolVal
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "entryID")
        if boolVal != None:
            self.entryID = boolVal
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "configRef")
        if boolVal != None:
            self.configRef = boolVal
        boolVal = ParserUtils.parseBooleanAttribute(optFieldsNode, "bufOvfl")
        if boolVal != None:
            self.bufOvfl = boolVal

    def isSeqNum(self):
        """ generated source for method isSeqNum """
        return self.seqNum

    def isTimeStamp(self):
        """ generated source for method isTimeStamp """
        return self.timeStamp

    def isDataSet(self):
        """ generated source for method isDataSet """
        return self.dataSet

    def isReasonCode(self):
        """ generated source for method isReasonCode """
        return self.reasonCode

    def isDataRef(self):
        """ generated source for method isDataRef """
        return self.dataRef

    def isEntryID(self):
        """ generated source for method isEntryID """
        return self.entryID

    def isConfigRef(self):
        """ generated source for method isConfigRef """
        return self.configRef

    def isBufOvfl(self):
        """ generated source for method isBufOvfl """
        return self.bufOvfl

