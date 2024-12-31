# hacked version from zulip

from dataclasses import dataclass, field


@dataclass
class AnonymousSettingGroupDict:
    direct_members: list[int]
    direct_subgroups: list[int]

@dataclass
class GroupPermissionSetting:
    require_system_group: bool
    allow_internet_group: bool
    allow_nobody_group: bool
    allow_everyone_group: bool
    default_group_name: str
    default_for_system_groups: str | None = None
    allowed_system_groups: list[str] = field(default_factory=list)
