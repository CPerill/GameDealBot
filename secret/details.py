"""
Author:     Connor Perill
Program:    for sending client connection secrets - not to be included in GitHub
Usage:      Sends connection strings (until I set up config file)
                pat
                    Page Access Token for Facebook
                reddit
                    client_id and client_secret for Reddit application

Lesson: n/a
"""

def pat():
    return 'EAACAFmJHCnYBALaqWcQC5bTtCkld5rQPhHeEveG6ytZBJh5UPydcyxTpEitVTNCqbPztvm5xkxWmBVkgk0NYRGcLHEgRpVGpwqvtj' \
      'EFLbSgLhBAXNH42f5ozx3ZAOnu7VIZCJ1kZBxSP5MqaPSVaiv9WT4my2LXpnV2SzxRz9gZDZD'


def reddit():
    return account()

class account:
    def __init__(self):
        self.client_id = 'taGkw_H9ngsFzQ',
        self.client_secret = 'jvuzMogt35XJTxrmf3E1hX9ZH-M',
        self.user_agent = 'my_user_agent'