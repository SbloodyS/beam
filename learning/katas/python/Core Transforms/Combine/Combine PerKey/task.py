#   Licensed to the Apache Software Foundation (ASF) under one
#   or more contributor license agreements.  See the NOTICE file
#   distributed with this work for additional information
#   regarding copyright ownership.  The ASF licenses this file
#   to you under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in compliance
#   with the License.  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# beam-playground:
#   name: CombinePerKey
#   description: Task from katas to implement the summation of scores per player.
#   multifile: false
#   categories:
#     - Combiners

import apache_beam as beam

from log_elements import LogElements

PLAYER_1 = 'Player 1'
PLAYER_2 = 'Player 2'
PLAYER_3 = 'Player 3'

with beam.Pipeline() as p:

  (p | beam.Create([(PLAYER_1, 15), (PLAYER_2, 10), (PLAYER_1, 100),
                    (PLAYER_3, 25), (PLAYER_2, 75)])
     | beam.CombinePerKey(sum)
     | LogElements())

