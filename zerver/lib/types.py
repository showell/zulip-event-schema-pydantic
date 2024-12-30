# hacked version from zulip

from dataclasses import dataclass


@dataclass
class AnonymousSettingGroupDict:
    direct_members: list[int]
    direct_subgroups: list[int]
