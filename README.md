The purpose of this code is to replace the use of `data_types.py` in Zulip
with pydantic types.

See the following new files:

* [event_schema.py](/zerver/lib/event_schema.py) (majorly modified from the current Zulip version)
* [event_types.py](/zerver/lib/event_types.py) (new code)

Run [test_checker.py](/test_checker.py)  to validate that this code is working.
