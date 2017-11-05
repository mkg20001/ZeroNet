try:
    from UiServer import UiServer
    from UiRequest import UiRequest
    from UiWebsocket import UiWebsocket
except Exception as err:
    from Ui.UiServer import UiServer
    from Ui.UiRequest import UiRequest
    from Ui.UiWebsocket import UiWebsocket
