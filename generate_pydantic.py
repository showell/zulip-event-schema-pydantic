import zerver.lib.event_schema

module_dict = zerver.lib.event_schema.__dict__
for k in sorted(module_dict):
    if k.endswith("_event") and not k.startswith("check_"):
        schema = module_dict[k]
        print(schema.full_pydantic(name=k))
        print()
        print()
