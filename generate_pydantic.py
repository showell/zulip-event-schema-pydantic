import zerver.lib.event_schema
from zerver.lib.data_types import DictType, UnionType

print(
    """
from pydantic import BaseModel
from typing import Any, Dict, List, Literal, Tuple, Optional, Union

UrlType = str
"""
)

module_dict = zerver.lib.event_schema.__dict__


def fix_name(k):
    if k.startswith("_check_"):
        k = k.replace("_check_", "")
    if not k.startswith("_"):
        k = "_" + k
    return k


for k in module_dict:
    v = module_dict[k]
    if type(v) is DictType:
        if not getattr(v, "__is_for_checker", False):
            v._name = fix_name(k)

for k in sorted(module_dict):
    if k.endswith("_event") and not k.startswith("check_"):
        schema = module_dict[k]
        schema.print_full_pydantic(name=k)
