"""
Author:     Connor Perill
Program:    Fetches links from Reddit
Usage:      For getting links from Reddit
                Functions:
                    fetch


"""
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import praw
import secret
import requests
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']

db = SQLAlchemy(app)


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def fetch(session, users, name, subreddit_name):
    """
    
    :param session: 
    :param users: 
    :param name: 
    :return: 
    """

    myUser = get_or_create(db.session, Users, name=recipient)

    reddit = secret.details.reddit()

    for submission in reddit.subreddit(subreddit_name).hot(limit=None):
        if (submission.is_self == True):
            query_result = Posts.query.filter(Posts.name == submission.id).first()
            if query_result is None:
                myPost = Posts(submission.id, submission.title)
                myUser


    return True


relationship_table=db.Table('relationship_table',
    db.Column('user_id', db.Integer,db.ForeignKey('users.id'), nullable=False),
    db.Column('post_id',db.Integer,db.ForeignKey('posts.id'),nullable=False),
    db.PrimaryKeyConstraint('user_id', 'post_id') )


class Posts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, unique=True, nullable=False)
    url=db.Column(db.String, nullable=False)

    def __init__(self, name=None, url=None):
        self.name = name
        self.url = url


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    posts=db.relationship('Posts', secondary=relationship_table, backref='users' )

    def __init__(self, name=None):
        self.name = name