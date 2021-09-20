from webdav3.client import Client


class WebDavClient(Client):
    """
    A wrapper object that represents a connection to a WebDav server

    Attributes:
        - client: represents the client object

    Methods:
        - __init__: Initializes client object. Parameter is the configuration file
    """

    def __init__(self):
        Client.__init__(self, nc_config.WEBDAV_OPTIONS)
        self.donwload_settings = nc_config.WEBDAV_LOAD_KWARGS

    def list(self):
        self.client.list()

    def info(self, dir=None):
        self.client.info(dir)