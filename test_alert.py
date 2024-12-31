from sample_data import SAMPLE_DATA

from pydantic_schema import alert_words_event


for event in SAMPLE_DATA["alert_words_event"]:
    print(event)
    alert_words_event(**event)
