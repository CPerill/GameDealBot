"""
Author:     Connor Perill
Program:    Hello - Testing that Flask is working correctly
Usage:      For parsing what the user wants
                Functions:
                    parsetext


"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
SQLALCHEMY_DATABASE_URI = 'postgres://hvqpcqkgwkpiqx:2e3aed129d0eaf139c38873eacc22c0463c4df9fa0defe4bb1022672c239e023@ec' \
                          '2-54-247-120-169.eu-west-1.compute.amazonaws.com:5432/d4o8ehme8ggjmv'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repositry')