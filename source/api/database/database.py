import ZODB, ZODB.FileStorage
import BTrees
import transaction

class ProfileIndex:
    def __init__(self, root):
        if 'profiles' not in root:
            root['profiles'] = BTrees.OOBTree.BTree()
        transaction.commit()
        self.profiles = root['profiles']
    
    def getUserByProfileName(profileName : str):
        return self.root['profiles'].get(profileName)
        
class Database:
    def __init__(self):
        self.storage = ZODB.FileStorage.FileStorage('databse.fs')
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        if 'users' not in self.root:
            self.root['users'] = BTrees.OOBTree.BTree()

        self.profileIndex = ProfileIndex(self.root)
    
    def ProfileIndex():
        return self.profileIndex
Database()