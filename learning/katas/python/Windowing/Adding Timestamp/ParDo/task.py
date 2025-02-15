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
#   name: WindowingParDo
#   description: Task from katas to assign each element a timestamp based on the the `Event.timestamp`.
#   multifile: false
#   categories:
#     - Streaming

import datetime
import pytz

import apache_beam as beam
from apache_beam.transforms import window

from log_elements import LogElements


class Event:
    def __init__(self, id, event, timestamp):
        self.id = id
        self.event = event
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f'Event({self.id}, {self.event}, {self.timestamp})'


class AddTimestampDoFn(beam.DoFn):

    def process(self, element, **kwargs):
        unix_timestamp = element.timestamp.timestamp()
        yield window.TimestampedValue(element, unix_timestamp)


with beam.Pipeline() as p:

  (p | beam.Create([
          Event('1', 'book-order', datetime.datetime(2020, 3, 4, 0, 0, 0, 0, tzinfo=pytz.UTC)),
          Event('2', 'pencil-order', datetime.datetime(2020, 3, 5, 0, 0, 0, 0, tzinfo=pytz.UTC)),
          Event('3', 'paper-order', datetime.datetime(2020, 3, 6, 0, 0, 0, 0, tzinfo=pytz.UTC)),
          Event('4', 'pencil-order', datetime.datetime(2020, 3, 7, 0, 0, 0, 0, tzinfo=pytz.UTC)),
          Event('5', 'book-order', datetime.datetime(2020, 3, 8, 0, 0, 0, 0, tzinfo=pytz.UTC)),
       ])
     | beam.ParDo(AddTimestampDoFn())
     | LogElements(with_timestamp=True))

