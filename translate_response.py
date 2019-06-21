#!/usr/bin/env python
# Copyright 2017 Google Inc.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
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


_PLANNING_HOUR = [
    u'I suggest scheduling three labour days for project planning.'
    u' Based on comperable prior proposals.',
    u'Based on my experience, '
    u'I suggest scheduling three labour days for project planning.'
]

_QM_HOUR = [
    u'I suggest scheduling one labour day for quality management.'
    u' If I compere to similar projects.',
    u'Let me compare this project to similar projects. '
    u'One labour day for quality management is enough.'
]
