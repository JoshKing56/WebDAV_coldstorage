EXISTS = True  # Only for unit testing purposes

"""
Webdav connection parameters
"""
WEBDAV_OPTIONS = {
    # """
    # Required arguments
    #     When a proxy server you need to specify settings to connect through it.
    # """
    'webdav_hostname': "https://nextcloud.asuka.rocks/remote.php/dav/files/josh/",
    'webdav_login': "josh",
    'webdav_password': "KIB2don9kooc_ruw"

    # """
    # Optional arguments
    #     When a proxy server you need to specify settings to connect through it.
    # """
    # "webdav_proxy_hostname": "http://127.0.0.1:8080",
    # "webdav_proxy_login": "p_login",
    # "webdav_proxy_password": "p_password",
    # "webdav_override_methods": {"check": "GET"},
    # "webdav_timeout": 30,
    # "webdav_cert_path": "",
    # "webdav_key_path": "",
}

"""
Webdav upload/download keywords
"""
WEBDAV_LOAD_KWARGS = {
        'local_path': "Temp",
        'callback': lambda: print("Thread complete")
    }
