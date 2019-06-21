#!/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This was originally a sample for a translation fulfillment webhook for an Dialogflow agent. 
The original project by Google Inc. is available under https://github.com/dialogflow/fulfillment-translate-python

Benjamin Wüthrich (wuethrich.benjamin@gmail.com) amended the code and converted it into a 
prototype for an artificial assistance system (AAS) as part of his Master Thesis for the program 
MSc in Business Information Systems at University of Applied Sciences and Arts Northwestern Switzerland

Following Use Cases of the Master Thesis are part of the Prototye of the AAS: 
- Use Case 2: Propose planning
- Use Case 3: Manage list of pending items

"""

import json
import random
from http.client import HTTPException
from urllib.error import HTTPError, URLError

from flask import Flask, jsonify, make_response, request
from googleapiclient.discovery import build

from translate_response import (_PLANNING_HOUR, _QM_HOUR)


app = Flask(__name__)
log = app.logger


@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook

    This is meant to be used in conjunction with the translate Dialogflow agent
    """

    # Get request parameters
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    print("action is: " + action)
    
    # Check if the requested use case is implemented
    if action == 'UC2_ProposePlanning':
        # Get the parameters for the use case
        time = req['queryResult']['parameters'].get('time')
        task = req['queryResult']['parameters'].get('task')

        # Chose answer based on task
        if task == 'planning': 
             output = random.choice(_PLANNING_HOUR)
        elif task == 'quality management':
             output = random.choice(_QM_HOUR)
        # Compose the response to Dialogflow
        res = {'fulfillmentText': output}
    elif action == 'UC3_ManagePendingItems_tasks':
        # Get the parameters for the use case
        time = req['queryResult']['parameters'].get('time')
        task = req['queryResult']['parameters'].get('task')

        # Create answer based on task
        output = [
        u'Following two tasks are due this week:'
        u' (1) create project plan'
        u' (2) derive costs and fees'
        ]
        # Compose the response to Dialogflow
        res = {'fulfillmentText': output,
               'outputContexts': req['queryResult']['outputContexts']}
    elif action == 'UC3_ManagePendingItems_deadline':
        # Get the parameters for the use case
        time = req['queryResult']['parameters'].get('time')
        task = req['queryResult']['parameters'].get('task')

        # Create answer
        output = [
        u'The overall deadline is August 9th.'
        ]
        # Compose the response to Dialogflow
        res = {'fulfillmentText': output}
    else:
        # If the requested use case is not to implemented as an action throw an error
        log.error('Unexpected action requested: %s', json.dumps(req))
        res = {'speech': 'error', 'displayText': 'error'}

    return make_response(jsonify(res))



if __name__ == '__main__':
    PORT = 8080

    app.run(
        debug=True,
        port=PORT,
        host='0.0.0.0'
    )
