from nextcloud_archiver.webdavclient import WebDavClient
from nextcloud_archiver.compression import archiveSubdirectory
from nextcloud_archiver.cacheallocator import CacheAllocator
import configuration.arguments as args
from webdav3.client import Client
import multiprocessing

def list_directories_by_depth(root_list: list, webdav: Client, depth: int = 0) -> list:
    """
    This method returns a list of all paths that need to be processed as an individual file group.
    Directories are determined by whether the file ends in a "/" character
    Note: the pass

    :param webdav: The webdav client object
    :param depth: Indicates the depth of file crawling
    """
    filelist = list()
    root_list.pop(0) # First item is always the name of the current directory
    print(root_list)
    while depth > 0:
        for file in root_list:
            print("\nFile in root: " + file)
            if file[-1] == "/": # All directories end in "/", while files don't
                sublist = map(lambda x: file + x, webdav.list(file)[1:])
                print(list(sublist))
                filelist += sublist
            else:
                filelist += file
        depth -= 1
    return filelist

<<<<<<< HEAD
=======
def 

>>>>>>> 8675129d88854406c77f81e6f2cab58959ac8411
def main():
    depth = -1
    end_archive = None
    threads = list()
    # client = Client(args.WEBDAV_OPTIONS)
    client = WebDavClient()
    root_directory = client.list()[1:]
    current_space_usage = 0 #in bytes
    max_space_usage = 1000000000 # 1000 Gb 
    print(root_directory[8] + "\n\n")
    print(client.list(root_directory[0], get_info=True))

    # print(client.get_size(client.list()[1]))
    # for directory in root_directory:
    #     if current_space_usage + max_space_usage 

        # TODO: change this to multiprocessing maybe, or just a vectorized loop 
        # if there is more than x amount of ram available
        # thread = threading.Thread(target=archiveSubdirectory, args=(directory))


    
    #   start thread with

    

if __name__ == "__main__":
    main()
# create temp folder for downloading
# for each file in nextcloud:
#   if archive with name nc.ARCHIVE_NAME doesn't exist:
#       create new archive and add file
#   else:
#       add file to archive