import click
from webdavclient import WebDavClient
from compression import archiveSubdirectory
from cacheallocator import CacheAllocator
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
