# -*- coding: utf-8 -*-
import pickle, pandas


class Review:

    def __init__(self, text, bookie, rating):
        self.text = text
        self.bookie = bookie
        self.ratings = rating


def unpack_reviews(filename):
    with open(filename, 'rb') as csvfile:
        data = pickle.load(csvfile)
        all_bookmakers = data.bookmaker.unique()
        return data

unpack_reviews('df.dump')