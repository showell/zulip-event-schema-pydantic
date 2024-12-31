"""This module sets up type classes like DictType and ListType that
define types for arbitrary objects.  The main use case is to specify
the types of Zulip events that come from send_event calls for
verification in test_events.py; in most other code paths we'll want to
use a TypedDict.

This module consists of workarounds for cases where we cannot express
the level of detail we desire or do comparison with OpenAPI types
easily with the native Python type system.
"""

from collections.abc import Callable, Sequence
from contextlib import suppress
from dataclasses import dataclass
from typing import Any

import random

"""
TODO: reincorporate
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
"""

PERSISTED_NAMES = set("AnonymousSettingGroupDict")

def get_flat_name(data_type):
    if hasattr(data_type, "_name"):
        if data_type._name not in PERSISTED_NAMES:
            data_type.print_full_pydantic(name=data_type._name)
            PERSISTED_NAMES.add(data_type._name)
        return data_type._name
    if data_type is dict:
        return "Dict"
    if data_type is int:
        return "int"
    if data_type is str:
        return "str"
    if data_type is bool:
        return "bool"
    return data_type.flat_name()

def get_sample_data(data_type):
    if hasattr(data_type, "sample_data"):
        return data_type.sample_data
    if data_type is int:
        return [42, 99]
    if data_type is str:
        return ["foo", "bar"]
    if data_type is bool:
        return [True, False]
    if data_type is dict:
        return [dict(anonymous="whatever")]
    print(data_type)
    print("unsupported")
    import sys

    sys.exit()


@dataclass
class DictType:
    """Dictionary is validated as having all required keys, all keys
    accounted for in required_keys and optional_keys, and recursive
    validation of types of fields.
    """

    def __init__(
        self,
        required_keys: Sequence[tuple[str, Any]],
        optional_keys: Sequence[tuple[str, Any]] = [],
    ) -> None:
        self.required_keys = required_keys
        self.optional_keys = optional_keys
        self.sample_data = [dict()]
        self.make_sample_data()

        # huge hack
        for key, data_type in self.required_keys:
            if key == "editable_by_user":
                self._name = "_detailed_custom_profile"
            if key == "direct_subgroups":
                self._name = "AnonymousSettingGroupDict"
            if key == "stream_weekly_traffic":
                self._name = "_basic_stream_fields"

        for key, data_type in self.optional_keys:
            if key == "unmuted_stream_msg":
                self._name = "_message_details"

    def make_sample_data(self):
        for key, data_type in self.required_keys:
            new_sample_data = []
            for new_val in get_sample_data(data_type):
                for old_sample in self.sample_data:
                    new_item = dict()
                    for k, v in old_sample.items():
                        new_item[k] = v
                    new_item[key] = new_val
                    new_sample_data.append(new_item)
            self.sample_data = new_sample_data
            if len(self.sample_data) > 40:
                self.sample_data = random.sample(self.sample_data, 40)

        for key, data_type in self.optional_keys:
            new_sample_data = []
            for new_val in get_sample_data(data_type):
                for old_sample in self.sample_data:
                    new_item = dict()
                    for k, v in old_sample.items():
                        new_item[k] = v
                    new_item[key] = new_val
                    new_sample_data.append(new_item)
                for old_sample in self.sample_data:
                    new_item = dict()
                    for k, v in old_sample.items():
                        new_item[k] = v
                    # LEAVE OUT KEY!
                    new_sample_data.append(new_item)
            self.sample_data = new_sample_data
            if len(self.sample_data) > 40:
                self.sample_data = random.sample(self.sample_data, 40)

    def flat_name(self):
        return "Any"

    def print_full_pydantic(self, *, name):
        if name == "AnonymousSettingGroupDict":
            return

        if self.optional_keys:
            superclass = name + "_core"
        else:
            superclass = name

        s = f"class {superclass}(BaseModel):\n"

        if not self.required_keys:
            s += "    pass \n"

        for key, data_type in self.required_keys:
            if type(data_type) is DictType and not hasattr(data_type, "_name"):
                data_type._name = "_" + name + "__" + key
            s += f"    {key}: {get_flat_name(data_type)}\n"
        s += "\n\n"

        print(s)

        if self.optional_keys:
            s = f"\n class {name}({superclass}):\n"
            s += "\n    # TODO: fix types to avoid optional fields\n"
            for key, data_type in self.optional_keys:
                s += f"    {key}: Optional[{get_flat_name(data_type)}] = None\n"
            s += "\n\n"
            print(s)


@dataclass
class EnumType:
    """An enum with the set of valid values declared."""

    valid_vals: Sequence[Any]

    def __init__(self, valid_vals):
        self.sample_data = valid_vals
        self.valid_vals = valid_vals

    def flat_name(self):
        return f"Literal{self.valid_vals}"


class Equals:
    """Type requiring a specific value."""

    def __init__(self, expected_value: Any) -> None:
        self.expected_value = expected_value

        # super hack for OpenAPI workaround
        if self.expected_value is None:
            self.equalsNone = True
        self.sample_data = [expected_value]

    def flat_name(self):
        return f"Literal[{self.expected_value!r}]"


class NumberType:
    """A Union[float, int]; needed to align with the `number` type in
    OpenAPI, because isinstance(4, float) == False"""

    def __init__(self):
        self.sample_data = [100, 3.14]

    def flat_name(self):
        return "Union[float, int]"

class ListType:
    """List with every object having the declared sub_type."""

    def __init__(self, sub_type: Any, length: int | None = None) -> None:
        self.sub_type = sub_type
        self.length = length
        self.sample_data = [[item, item, item] for item in get_sample_data(sub_type)]

    def flat_name(self):
        return f"List[{get_flat_name(self.sub_type)}]"


@dataclass
class StringDictType:
    """Type that validates an object is a Dict[str, str]"""

    value_type: Any

    def __init__(self, value_type):
        self.sample_data = [dict(some_key=val) for val in get_sample_data(value_type)]
        self.value_type = value_type

    def flat_name(self):
        return f"Dict[str, {get_flat_name(self.value_type)}]"


@dataclass
class OptionalType:
    sub_type: Any

    def __init__(self, sub_type):
        self.sample_data = [None] + get_sample_data(sub_type)
        self.sub_type = sub_type

    def flat_name(self):
        return f"Optional[{get_flat_name(self.sub_type)}]"


@dataclass
class TupleType:
    """Deprecated; we'd like to avoid using tuples in our API.  Validates
    the tuple has the sequence of sub_types."""

    sub_types: Sequence[Any]

    def __init__(self, sub_types):
        self.sub_types = sub_types
        self.sample_data = [list()]
        for data_type in sub_types:
            new_sample_data = []
            for new_val in get_sample_data(data_type):
                for old_sample in self.sample_data:
                    new_item = old_sample[:] + [new_val]
                    new_sample_data.append(new_item)
            self.sample_data = new_sample_data

        self.sample_data = [tuple(lst) for lst in new_sample_data]
        if len(self.sample_data) > 40:
            self.sample_data = random.sample(self.sample_data, 40)

    def flat_name(self):
        sub_names = [get_flat_name(t) for t in self.sub_types]
        return f"Tuple[{", ".join(sub_names)}]"

@dataclass
class UnionType:
    sub_types: Sequence[Any]

    def __init__(self, sub_types):
        self.sub_types = sub_types
        self.sample_data = []
        for sub_type in sub_types:
            self.sample_data += get_sample_data(sub_type)
        if len(self.sample_data) > 40:
            self.sample_data = random.sample(self.sample_data, 40)


    def flat_name(self):
        sub_names = [get_flat_name(t) for t in self.sub_types]
        return f"Union[{", ".join(sub_names)}]"

class UrlType:
    def __init__(self):
        self.sample_data = ["http://example.com"]

    def flat_name(self):
        return "UrlType"

def event_dict_type(
    required_keys: Sequence[tuple[str, Any]],
    optional_keys: Sequence[tuple[str, Any]] = [],
) -> DictType:
    """
    This is just a tiny wrapper on DictType, but it provides
    some minor benefits:

        - mark clearly that the schema is for a Zulip event
        - make sure there's a type field
        - add id field automatically
        - sanity check that we have no duplicate keys

    """
    rkeys = [key[0] for key in required_keys]
    okeys = [key[0] for key in optional_keys]
    keys = rkeys + okeys
    assert len(keys) == len(set(keys))
    assert "type" in rkeys
    assert "id" not in keys
    return DictType(
        required_keys=[*required_keys, ("id", int)],
        optional_keys=optional_keys,
    )


def make_checker(
    data_type: DictType,
) -> Callable[[str, dict[str, object]], None]:
    def f(var_name: str, event: dict[str, Any]) -> None:
        check_data(data_type, var_name, event)

    data_type.__is_for_checker = True
    return f

def check_data(
    data_type: Any,
    var_name: str,
    val: Any,
) -> None:
    """Check that val conforms to our data_type"""
    if hasattr(data_type, "check_data"):
        data_type.check_data(var_name, val)
        return
    if not isinstance(val, data_type):
        raise AssertionError(f"{var_name} is not type {data_type}")
