import zerver.lib.event_schema

module_dict = zerver.lib.event_schema.__dict__
print("SAMPLE_DATA = [")
for k in sorted(module_dict):
    if k.endswith("_event") and not k.startswith("check_"):
        v = module_dict[k].sample_data
        print(f"    {k}={v},")
print("]")
