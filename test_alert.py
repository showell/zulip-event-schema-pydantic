from sample_data import SAMPLE_DATA
from pydantic import BaseModel
from typing import List, Literal

class alert_words_event(BaseModel):
    type: str = Literal["alert_words"]
    alert_words: List[str]
    id: int

for event in SAMPLE_DATA["alert_words_event"]:
    print(event)
    alert_words_event(**event)


