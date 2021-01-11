import datetime
import uuid
import json
import model
import util

for i in range(10):
    transaction = model.Transaction(uuid.uuid4(), 1, 2, 3., datetime.datetime.now().isoformat())
    print("transaction={}".format(json.dumps(transaction.__dict__, cls=util.JsonEncoder)))
