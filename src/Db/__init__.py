try:
    from Db import Db
    from DbQuery import DbQuery
    from DbCursor import DbCursor
except Exception as err:
    from Db.Db import Db
    from Db.DbQuery import DbQuery
    from Db.DbCursor import DbCursor
