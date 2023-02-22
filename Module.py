from pymongo import MongoClient
from bson.objectid import ObjectId
import json


class AnimalShelter(object):
    
    def __init__(self, me, a):
        self.client = MongoClient('mongodb://%s:%s@localhost:55061' % (me, a))
        self.database = self.client['ACC'] 
    def create(self,data):
            if data is not None:
                print("true")
                self.database.animals.insert(data)  #Use this if I want to see the data for that dataset
            else:
                print("false")
                raise Exception("Nothing to save, parameter empty")    
        
    def read(self, data):
        if data is not None:
            result = self.database.animals.find_one(data,{"_id":False})
            return result
        else:
            print("no document to read")
    
    def readAll(self,data):
        if data is not None:
            allResult = self.database.animals.find(data,{"_id":False})
            return allResult
        else:
            print("no documents read")
            
    def update(self, query, data):
        if data is not None:
            updateResultes =  self.database.animals.update(query, data)
            return updateResultes
        else: 
            print("update failed")
    def delete(self, query, data):
        if data is not None:
            deleted = self.database.animals.remove(query, data)
            return print(deleted)
        else:
            return print("document does not exist or has been delete")

    