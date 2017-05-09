"""
Author:     Connor Perill
Program:    Hello - Testing that Flask is working correctly
Usage:      For parsing what the user wants
                Functions:
                    parsetext


"""

import json
import requests


def begin(message):
    """
    Beginning method, will return a message to send to the user
    :param message: 
    :return: 
    """

    # First step, we must parse the users message to get the Named Entitys (Named Entity Recognition - NER) and to get
    # the users sentiment (the reason why they are contacting the bot)

    parsetext(message)

    return "Work in progress"


def parsetext(m):
    """
     We will contact Luis.ai to parse the users sentiment, we will then use the json response to form a reply
     Eventually I will implement NLTK (http://www.nltk.org/book/) to form my own NLP algorithim
    :param m: 
    :return: 
    """



