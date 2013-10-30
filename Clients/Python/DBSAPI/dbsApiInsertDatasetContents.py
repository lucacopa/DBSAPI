
import os, re, string, socket, xml.sax, xml.sax.handler
import base64
from xml.sax.saxutils import escape
from cStringIO import StringIO

from dbsException import DbsException
from dbsApiException import *

##import logging
import inspect

##from dbsLogger import **

from dbsUtil import *

def dbsApiImplInsertDatasetContents(self, xmlinput, ignore_parent = False):
    """

    This API call is used for inserting Dataset from XML dump generated by listDatasetContents
    The APIrepopulates (another) instance of DBS with same dataset as 
    produced by the listDatasetContents counterpart 

    params: 
        xmlinput : XML dump generated by listDatasetContents

    examples:

        Dump the contents of Block /this/block#1230-87698 for Dataset /PrimaryDS_01/procds-01/SIM
                  api.listDatasetContents("/PrimaryDS_01/procds-01/SIM", "/this/block#1230-87698") 
        
        Using a Dataset Object 
            primary = DbsPrimaryDataset (Name = "test_primary_anzar_001")
            proc = DbsProcessedDataset (
                            PrimaryDataset=primary,
                            Name="TestProcessedDS002",
                            PhysicsGroup="BPositive",
                            Status="VALID",
                            TierList=['SIM', 'RECO'],
                            AlgoList=[WhateverAlgoObject],
                            )
             xmldataset = api.listDatasetContents(proc, "/this/block#1230-87698")
             api.insertDatasetContents(xmldataset)

    May raise an DbsApiException.

    """
    funcInfo = inspect.getframeinfo(inspect.currentframe())
    ##logging.log(DBSDEBUG, "Api call invoked %s" % str(funcInfo[2]))

    #try:
    # Invoke Server.
    ignoreParent = "false"
    if ignore_parent:
	    ignoreParent = "true"
    data = self._server._call ({ 'api' : 'insertDatasetContents', 'xmlinput' : xmlinput, 'ignore_parent' : ignoreParent }, 'POST')
    ##logging.log(DBSDEBUG, data)

    return data
