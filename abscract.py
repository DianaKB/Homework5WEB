import json
from abc import ABCMeta, abstractmethod
import pickle

class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass

class Serialization_json(SerializationInterface):

    def serialize(self, data, file_name):
        with open(file_name, "w") as fh:
            json.dump(data, fh)

    def deserialize(self, data, file_name):
        return json.loads(*args)

class Serialization_bin(SerializationInterface):

    def serialize(self, data, file_name):
        with open(file_name, "wb") as fh:
            pickle.dump(data, fh)

    def deserialize(self, data, file_name):
        with open(file_name, "rb") as fh:
            pickle.load(fh)