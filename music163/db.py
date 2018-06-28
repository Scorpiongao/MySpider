import pymongo
from config import *


class MongoDB():
    def __init__(self,table):
        self.table=table
        self.client=pymongo .MongoClient (MONGO_URL ,connect= False )
        self.db=self.client [MONGO_DB ]
        # self.filter(self.db,result )
        # self .save_to_mongo(self.db,result )

    def save_to_mongo(self,result):
        if self.db[self .table].update({'id':result ['id']},{'$set':result },True ):
            print('Saved to MongoDB successful', result['id'],result['name'])
        else:
            print('Saved to MongoDB Failed', result['id'])

    def filter(self,id):
        if self.db[self.table ].find_one({'id':id}):
            print('%s already in mongodb '%id)
            return True
