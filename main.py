from nextcloud_archiver.webdavclient import WebDavClient
import nextcloud_archiver.archiveSubdirectory
import configuration.arguments as args
from webdav3.client import Client
import multiprocessing

def main():
    end_archive = None
    threads = list()
    client = Client(args.WEBDAV_OPTIONS)
    root_directory = client.list()
    for directory in root_directory:
        # TODO: change this to multiprocessing maybe, or just a vectorized loop 
        # if there is more than x amount of ram available
        thread = threading.Thread(target=archiveSubdirectory, args=(directory))

    """
    def archiveSubdirectory():
        calculate how large subdirectory will be 
        block until space opens up depending on conf
        reserve space
        async dl all files into temp folder
        add them to the archive 
    """
    
    #   start thread with

    

if __name__ == "__main__":
    main()
# create temp folder for downloading
# for each file in nextcloud:
#   if archive with name nc.ARCHIVE_NAME doesn't exist:
#       create new archive and add file
#   else:
#       add file to archive