import os

class CacheAllocator():
    def __init__(self, path, max_storage = -1) -> None:
        self.directory = path 
        try:
            os.mkdir(path)
        except:
            print("Path is invalid, exit") 
        self.storage_used = 0
        self.max_storage = max_storage

<<<<<<< HEAD
    def get_storage(self) -> int:
=======
    def get_storage(self):
>>>>>>> 8675129d88854406c77f81e6f2cab58959ac8411
        return(self.storage_used)

    def allocate(self, filesize: int) -> bool:
        if (self.storage_used + filesize) < self.max_storage:
            self.storage_used += filesize 
            return True
        else:
            return False

    def deallocate(self, filesize: int) -> bool:
        if (self.storage_used - filesize) < 0:
            print("Cache deallocation error")
        else:
           self.storage_used -= filesize
           return True