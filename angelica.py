import graphene
import json
import pickle
import signal
import sys

from flask import Flask, Response, request
from structure import query
from utils import logchan as log #pylint: disable=import-error

pickle.HIGHEST_PROTOCOL = 4 # Force to use Protocol 4 to support modern Python systems
import rq_dashboard
from redis import Redis

# Signal handler
def sig_handler(sig, frame):
    log.critical("SIG command {} detected, exiting...".format(sig), color=log.LoggingColors.LRED)
    sys.exit()
# Add in SIGKILL handler
signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

SCHEMA = graphene.Schema(query=query.Queries)
print(SCHEMA)
app = Flask(__name__)

@app.route("/api/v1", methods=['GET'])
def v1():
    rq_json = request.get_json()
    result = SCHEMA.execute(rq_json['query'], variables=rq_json['variables'])
    return Response(json.dumps(result.data), mimetype='application/json')
    #return json.dumps(result.data), 200

if __name__ == "__main__":
    log.info("Starting Angelica API server.", color=log.LoggingColors.GREEN)
    app.run(host='0.0.0.0', port=8080)

