import zerver.lib.event_schema_legacy
from zerver.lib.data_types import DictType, UnionType

print(
    """
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from zerver.lib.types import AnonymousSettingGroupDict
from pydantic import AfterValidator, BaseModel
from typing import Annotated, List, Literal, Tuple, Optional

def check_url(val: str) -> str:
    try:
        URLValidator()(val)
    except ValidationError:  # nocoverage
        raise AssertionError(f"{val} is not a URL")
    return val

Url = Annotated[str, AfterValidator(check_url)]
"""
)

module_dict = zerver.lib.event_schema_legacy.__dict__


def fix_name(k):
    if "topic_links" in k:
        k = "_topic_link"
    if k.startswith("_check_"):
        k = k.replace("_check_", "")
    if k.endswith("_type"):
        k = k.replace("_type", "")
    k = k.replace('_', ' ').strip().title().replace(' ', '')
    return k


for k in module_dict:
    if k == "realm_user_person_types":
        for flavor, data_type in module_dict[k].items():
            data_type._name = fix_name("person_" + flavor)
        continue

    v = module_dict[k]
    if type(v) is DictType:
        if not getattr(v, "__is_for_checker", False):
            v._name = fix_name(k)

for k in sorted(module_dict):
    if k.endswith("_event") and not k.startswith("check_"):
        schema = module_dict[k]
        orig_name = k
        k = k.strip("_")
        k = k.replace("_event", "")
        k = k.replace('_', ' ').strip().title().replace(' ', '')
        k = "Event" + k
        schema.print_full_pydantic(name=k)
