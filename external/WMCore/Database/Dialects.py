

# sqlalchemy breaks this because they reorganized things. Fail.
# see: http://www.mail-archive.com/sqlalchemy@googlegroups.com/msg18392.html
#  -AMM 6/15/10

try:
    from sqlalchemy.databases.mysql import MySQLDialect
    from sqlalchemy.databases.sqlite import SQLiteDialect 
    from sqlalchemy.databases.oracle import OracleDialect
except:
    from sqlalchemy.dialects.mysql.base import MySQLDialect
    from sqlalchemy.dialects.sqlite.base import SQLiteDialect 
    from sqlalchemy.dialects.oracle.base import OracleDialect


__all__ = [MySQLDialect, SQLiteDialect, OracleDialect]