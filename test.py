from sample_data import SAMPLE_DATA

import pydantic_schema

SCHEMA_DICT = pydantic_schema.__dict__


for k, events in SAMPLE_DATA.items():
    for event in events:
        print(event)
        checker = SCHEMA_DICT[k]
        checker(**event)
