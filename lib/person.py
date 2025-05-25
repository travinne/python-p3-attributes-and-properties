#!/usr/bin/env python3

class Person:
    approved_jobs = ["Software Engineer", "Data Scientist", "ITC", "Product Manager"]

    def __init__(self, name="Guido", job="Software Engineer"):
        self._name = None
        self._job = None

        self.name = name
        if self._name is not None: 
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None 

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, input):
        if input in self.approved_jobs:
            self._job = input
        else:
            print("Job must be in list of approved jobs.")
            self._job = None  