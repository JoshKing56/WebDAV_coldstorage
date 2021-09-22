from webdav3.client import Client
import configuration.arguments as args


class WebDavClient(Client):
    """
    A wrapper object that represents a connection to a WebDav server

    Attributes:
        - client: represents the client object

    Methods:
        - __init__: Initializes client object. Parameter is the configuration file
    """

    def __init__(self):
        Client.__init__(self, args.WEBDAV_OPTIONS)
        self.donwload_settings = args.WEBDAV_LOAD_KWARGS

    #TODO: Rewrite this with self()
    def get_size(self, dir=None):
        self.info(dir)
