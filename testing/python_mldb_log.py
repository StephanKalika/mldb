# This file is part of MLDB. Copyright 2015 mldb.ai inc. All rights reserved.


###
#   test that mldb.log correnctly handles all types
###

import json
from mldb import mldb

conf = {
    "source": """
from mldb import mldb
mldb.log("patate")
mldb.log({"patate":2.44})
mldb.log(["patate", "pwel"])
mldb.log(25)
mldb.log("a", "b", 2)
mldb.log()
"""
}
rtn = mldb.perform("POST", "/v1/types/plugins/python/routes/run", [], conf)

jsRtn = json.loads(rtn["response"])
mldb.log(jsRtn)

assert jsRtn["logs"][0]["c"] == "patate"
assert jsRtn["logs"][1]["c"] == "{\n    \"patate\": 2.44\n}"
assert jsRtn["logs"][2]["c"] == "[\n    \"patate\",\n    \"pwel\"\n]"
assert jsRtn["logs"][3]["c"] == "25"
assert jsRtn["logs"][4]["c"] == "a b 2"
#assert jsRtn["logs"][5]["c"] == ""

request.set_return("success")

