Documentation:
https://github.com/ezhov-evgeny/webdav-client-python-3

NOTE: WEBDAV3's info function doesn't work, but if you do client.list(path, get_info=True) that gives you what you need

=== 
Progress
===
- Got python to talk to nextcloud
- Installed pypiserver on proxmox, need to port foward
- Half way through doing security for pypiserver. References: [1](https://www.jitsejan.com/setting-up-private-pypi-server) [2](https://github.com/pypiserver/pypiserver#quickstart-installation-and-usage) [3](https://medium.com/@christianhettlage/setting-up-a-pypi-server-679f1b55b96) [4](https://www.linode.com/docs/guides/how-to-create-a-private-python-package-repository/) [5](https://johnfraney.ca/posts/2019/05/28/create-publish-python-package-poetry/)


====
Todo
====
- CLI application with click
- Multiprocessing
- Comparison of cold storage options

====
Ideas
====
[Progress bar](https://stackoverflow.com/questions/32080382/using-click-progressbar-with-multiprocessing-in-python)

 # print(client.get_size(client.list()[1]))
    # for directory in root_directory:
    #     if current_space_usage + max_space_usage 

        # TODO: change this to multiprocessing maybe, or just a vectorized loop 
        # if there is more than x amount of ram available
        # thread = threading.Thread(target=archiveSubdirectory, args=(directory))

# create temp folder for downloading
# for each file in nextcloud:
#   if archive with name nc.ARCHIVE_NAME doesn't exist:
#       create new archive and add file
#   else:
#       add file to archive