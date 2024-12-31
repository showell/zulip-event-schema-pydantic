import zerver.lib.event_schema_legacy

import random

random.seed(42)

module_dict = zerver.lib.event_schema_legacy.__dict__
print("SAMPLE_DATA = dict(")
for k in sorted(module_dict):
    if k.endswith("_event") and not k.startswith("check_"):
        print(f"    {k}=[")
        for sample in module_dict[k].sample_data:
            print(f"        {sample},")
        print(f"    ],")
print(")")
