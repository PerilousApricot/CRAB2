#!/usr/bin/env python
"""
__DbConfig__

a set of possible choices for the TaskAPITest.py usage

"""

__version__ = "$Id: DbConfig.py,v 1.1 2008/07/11 14:45:45 gcodispo Exp $"
__revision__ = "$Revision: 1.1 $"
__author__ = "Giuseppe.Codispoti@bo.infn.it"

def mySQLConfig() :
    return 'mysql', \
           {'dbName':'BossLiteDB',
            'host':'localhost',
            'user':'BossLiteUser',
            'passwd':'BossLitePass',
            'socketFileLocation':'$HOME/PRODAGENT_WORKDIR/mysqldata/mysql.sock',
            'portNr':'',
            'refreshPeriod' : 4*3600 ,
            'maxConnectionAttempts' : 5,
            'dbWaitingTime' : 10 
            }


def SQLiteConfig( dbPath=None ) :

    if dbPath is not None:
        return 'sqlite', { 'dbName' : 'BossLiteDB' }

    else :
        import os
        return 'sqlite', { 'dbName' : os.path.join(dbPath, 'BossLiteDB') }


def paConfig() :
    from ProdAgentDB.Config import defaultConfig
    return 'mysql', defaultConfig



dbType, dbConfig = mySQLConfig()

