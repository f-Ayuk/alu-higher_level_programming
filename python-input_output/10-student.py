#!/usr/bin/python3
'''Defines class student
'''


class Student:
    '''Represents user data of a student
    '''
    def __init__(self, first_name, last_name, age):
        '''Initializes a new student inatsnce
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns a dictionary representation of the student instance
        '''
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
