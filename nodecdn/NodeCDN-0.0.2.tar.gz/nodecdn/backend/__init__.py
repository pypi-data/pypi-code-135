import os, time, sys, re, random, requests

allow = []
deny = ["/"]

def init(app):
    if app.config['NODECDN_COMMUNICATION_PATH'] == None:
        print("Starting NODECDN without communication sync...")
    elif app.config['NODECDN_COMMUNICATION_PATH'] != None:
        print("Starting NODECDN with communication sync...")

    print("Started NODECDN.")

    @app.route('nodecdn/dist', methods=['GET', 'POST'])
    def nodecdndistrobution():
        codedistro = requests.get('https://hostereric.herokuapp.com/NodeCDN/index.min.js')
        return codedistro.text()