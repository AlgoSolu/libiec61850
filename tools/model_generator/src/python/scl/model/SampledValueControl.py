#!/usr/bin/env python
""" generated source for module SampledValueControl """
from __future__ import print_function
# package: com.libiec61850.scl.model
class SampledValueControl(object):
    """ generated source for class SampledValueControl """
    name = None
    desc = None
    datSet = None
    confRev = 1
    smvID = None
    smpRate = int()
    nofASDU = int()
    multicast = False
    smvOpts = None

    def __init__(self, smvControlNode):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(smvControlNode, "name")
        self.desc = ParserUtils.parseAttribute(smvControlNode, "desc")
        self.datSet = ParserUtils.parseAttribute(smvControlNode, "datSet")
        confRevString = ParserUtils.parseAttribute(smvControlNode, "confRev")
        if confRevString != None:
            self.confRev = int(confRevString)
        self.smvID = ParserUtils.parseAttribute(smvControlNode, "smvID")
        multicast = ParserUtils.parseBooleanAttribute(smvControlNode, "multicast")
        if multicast != None:
            self.multicast = multicast
        smpRateString = ParserUtils.parseAttribute(smvControlNode, "smpRate")
        if smpRateString != None:
            self.smpRate = int(smpRateString)
        nofASDUString = ParserUtils.parseAttribute(smvControlNode, "nofASDU")
        if nofASDUString != None:
            self.nofASDU = int(nofASDUString)
        smvOptsNode = ParserUtils.getChildNodeWithTag(smvControlNode, "SmvOpts")
        self.smvOpts = SmvOpts(smvOptsNode)

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getDatSet(self):
        """ generated source for method getDatSet """
        return self.datSet

    def getConfRev(self):
        """ generated source for method getConfRev """
        return self.confRev

    def getSmvID(self):
        """ generated source for method getSmvID """
        return self.smvID

    def getSmpRate(self):
        """ generated source for method getSmpRate """
        return self.smpRate

    def getNofASDI(self):
        """ generated source for method getNofASDI """
        return self.nofASDU

    def isMulticast(self):
        """ generated source for method isMulticast """
        return self.multicast

    def getSmvOpts(self):
        """ generated source for method getSmvOpts """
        return self.smvOpts

