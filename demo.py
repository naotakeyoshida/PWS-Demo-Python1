import os
import uuid
import urlparse
import json
from flask import Flask

app = Flask(__name__)
port = int(os.getenv("PORT"))
myuuid = str(uuid.uuid1())
myinstance = str(os.getenv("CF_INSTANCE_INDEX", 0))

@app.route('/')
def main():
    return """
    <html>
    <head>
        <title> Pivotal Cloud Foundry Demo </title>
    </head>
    <body bgcolor="#CCCCCC" text="#000000" link="#0000ff" vlink="#800080" alink="#ff0000">
        <center><FONT size="6" color="black">====== Dell EMC ======</FONT>
    </body>
    </html>
    """.format(myinstance, myuuid, )
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
