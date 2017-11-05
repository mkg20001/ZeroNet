try:
    from Event import Event
    from Noparallel import Noparallel
    from Pooled import Pooled
except Exception as err:
    from util.Event import Event
    from util.Noparallel import Noparallel
    from util.Pooled import Pooled
