import graphene
import json
import pprint

from flask import Flask, request
from structure import query

SCHEMA = graphene.Schema(query=query.Queries)
print(SCHEMA)

app = Flask(__name__)

@app.route("/api/v1", methods=['GET'])
def v1():
    rq_json = request.get_json()
    result = SCHEMA.execute(rq_json['query'], variables=rq_json['variables'])
    return json.dumps(result.data), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

