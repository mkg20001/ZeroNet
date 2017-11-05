try:
    from ConnectionServer import ConnectionServer
    from Connection import Connection
except Exception as err:
    from Connection.ConnectionServer import ConnectionServer
    from Connection.Connection import Connection
