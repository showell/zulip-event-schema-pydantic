import zerver.lib.event_schema

module_dict = zerver.lib.event_schema.__dict__
print("SAMPLE_DATA = dict(")
for k in sorted(module_dict):
    if k.endswith("_event") and not k.startswith("check_"):
        print(f"    {k}=[")
        for sample in module_dict[k].sample_data:
            print(f"        {sample},")
        print(f"    ],")
print(")")
