import zerver.lib.event_schema

print(
    """
from pydantic import BaseModel
from typing import Any, Dict, List, Literal, Tuple, Optional, Union
"""
)

module_dict = zerver.lib.event_schema.__dict__
for k in sorted(module_dict):
    if k.endswith("_event") and not k.startswith("check_"):
        schema = module_dict[k]
        schema.print_full_pydantic(name=k)
