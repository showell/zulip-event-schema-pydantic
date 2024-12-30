import zerver.lib.event_schema


foo = zerver.lib.event_schema.alert_words_event

print(foo.sample_data)
print(foo.schema("alert_words"))
