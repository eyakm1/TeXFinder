import TeXFile
import pickle
import os
import sys


class DS:
    __slots__ = ['list_of_files', 'trigram_to_files', 'files_to_trigrams']
    def __init__(self, list_of_files=None, trigram_to_files=None, files_to_trigrams=None):
        if list_of_files is None:
            list_of_files = []
        if trigram_to_files is None:
            trigram_to_files = {}
        if files_to_trigrams is None:
            files_to_trigrams = []
        self.list_of_files, self.trigram_to_files, self.files_to_trigrams = list_of_files, trigram_to_files, files_to_trigrams  
    
    def load(self):
        with open('data.pickle', 'rb') as f:
            (self.list_of_files, self.trigram_to_files, self.files_to_trigrams) = pickle.load(f)
        return self
            
    def dump(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump((self.list_of_files, self.trigram_to_files, self.files_to_trigrams), f)
    
    def __repr__(self):
        return '{}(list_of_files={}, trigram_to_files={}, files_to_trigrams={})'.format(
            self.__class__.__name__,
            repr(self.list_of_files),
            repr(self.trigram_to_files),
            repr(self.files_to_trigrams),
        )



ds = DS().load()
print(ds)