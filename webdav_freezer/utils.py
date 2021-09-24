from .webdavclient import WebDavClient

def list_directories_by_depth(root_list: list, webdav: WebDavClient, depth: int = 0) -> list:
    """
    This method returns a list of all paths that need to be processed as an individual file group.
    Directories are determined by whether the file ends in a "/" character
    Note: the pass

    :param webdav: The webdav client object
    :param depth: Indicates the depth of file crawling
    """
    filelist = list()
    root_list.pop(0)  # First item is always the name of the current directory
    print(root_list)
    while depth > 0:
        for file in root_list:
            print("\nFile in root: " + file)
            if file[-1] == "/":  # All directories end in "/", while files don't
                sublist = map(lambda x: file + x, webdav.list(file)[1:])
                print(list(sublist))
                filelist += sublist
            else:
                filelist += file
        depth -= 1
    return filelist

def partition_files(root_list: list, webdav: WebDavClient, depth: int = 0) -> list:
    full_list = list_directories_by_depth(root_list, webdav, depth)

