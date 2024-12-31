from pydantic import BaseModel
from typing import Any, Dict, List, Literal, Tuple, Optional, Union


class alert_words_event(BaseModel):
    type: Literal["alert_words"]
    alert_words: List[str]
    id: int


class attachment_add_event(BaseModel):
    type: Literal["attachment"]
    op: Literal["add"]
    attachment: Any
    upload_space_used: int
    id: int


class attachment_remove_event(BaseModel):
    type: Literal["attachment"]
    op: Literal["remove"]
    attachment: Any
    upload_space_used: int
    id: int


class attachment_update_event(BaseModel):
    type: Literal["attachment"]
    op: Literal["update"]
    attachment: Any
    upload_space_used: int
    id: int


class custom_profile_fields_event(BaseModel):
    type: Literal["custom_profile_fields"]
    fields: List[Any]
    id: int


class default_stream_groups_event(BaseModel):
    type: Literal["default_stream_groups"]
    default_stream_groups: List[Any]
    id: int


class default_streams_event(BaseModel):
    type: Literal["default_streams"]
    default_streams: List[int]
    id: int


class delete_message_event(BaseModel):
    type: Literal["delete_message"]
    message_type: Literal["private", "stream"]
    id: int
    message_id: Optional[int] = None
    message_ids: Optional[List[int]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class direct_message_event(BaseModel):
    type: Literal["message"]
    flags: List[str]
    message: Any
    id: int


class drafts_add_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["add"]
    drafts: List[Any]
    id: int


class drafts_remove_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["remove"]
    draft_id: int
    id: int


class drafts_update_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["update"]
    draft: Any
    id: int


class has_zoom_token_event(BaseModel):
    type: Literal["has_zoom_token"]
    value: bool
    id: int


class heartbeat_event(BaseModel):
    type: Literal["heartbeat"]
    id: int


class invites_changed_event(BaseModel):
    type: Literal["invites_changed"]
    id: int


class message_event(BaseModel):
    type: Literal["message"]
    flags: List[str]
    message: Any
    id: int


class muted_topics_event(BaseModel):
    type: Literal["muted_topics"]
    muted_topics: List[Tuple[str, str, int]]
    id: int


class muted_users_event(BaseModel):
    type: Literal["muted_users"]
    muted_users: List[Any]
    id: int


class onboarding_steps_event(BaseModel):
    type: Literal["onboarding_steps"]
    onboarding_steps: List[Any]
    id: int


class presence_event(BaseModel):
    type: Literal["presence"]
    user_id: int
    server_timestamp: Union[float, int]
    presence: Dict[str, Any]
    id: int
    email: Optional[str] = None


class reaction_add_event(BaseModel):
    type: Literal["reaction"]
    op: Literal["add"]
    message_id: int
    emoji_name: str
    emoji_code: str
    reaction_type: Literal["unicode_emoji", "realm_emoji", "zulip_extra_emoji"]
    user_id: int
    id: int


class reaction_remove_event(BaseModel):
    type: Literal["reaction"]
    op: Literal["remove"]
    message_id: int
    emoji_name: str
    emoji_code: str
    reaction_type: Literal["unicode_emoji", "realm_emoji", "zulip_extra_emoji"]
    user_id: int
    id: int


class realm_bot_add_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["add"]
    bot: Any
    id: int


class realm_bot_delete_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["delete"]
    bot: Any
    id: int


class realm_bot_update_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["update"]
    bot: Any
    id: int


class realm_deactivated_event(BaseModel):
    type: Literal["realm"]
    op: Literal["deactivated"]
    realm_id: int
    id: int


class realm_domains_add_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["add"]
    realm_domain: Any
    id: int


class realm_domains_change_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["change"]
    realm_domain: Any
    id: int


class realm_domains_remove_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["remove"]
    domain: str
    id: int


class realm_emoji_update_event(BaseModel):
    type: Literal["realm_emoji"]
    op: Literal["update"]
    realm_emoji: Dict[str, Any]
    id: int


class realm_export_consent_event(BaseModel):
    type: Literal["realm_export_consent"]
    user_id: int
    consented: bool
    id: int


class realm_export_event(BaseModel):
    type: Literal["realm_export"]
    exports: List[Any]
    id: int


class realm_linkifiers_event(BaseModel):
    type: Literal["realm_linkifiers"]
    realm_linkifiers: List[Any]
    id: int


class realm_playgrounds_event(BaseModel):
    type: Literal["realm_playgrounds"]
    realm_playgrounds: List[Any]
    id: int


class realm_update_dict_event(BaseModel):
    type: Literal["realm"]
    op: Literal["update_dict"]
    property: Literal["default", "icon", "logo", "night_logo"]
    data: Union[Any, Any, Any, Any, Any, Any, Any, Any]
    id: int


class realm_update_event(BaseModel):
    type: Literal["realm"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class realm_user_add_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["add"]
    person: Any
    id: int


class realm_user_remove_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["remove"]
    person: Any
    id: int


class realm_user_settings_defaults_update_event(BaseModel):
    type: Literal["realm_user_settings_defaults"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class realm_user_update_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["update"]
    person: Union[Any, Any, Any, Any, Any, Any, Any, Any, Any, Any]
    id: int


class restart_event(BaseModel):
    type: Literal["restart"]
    zulip_version: str
    zulip_merge_base: str
    zulip_feature_level: int
    server_generation: int
    id: int


class saved_snippet_add_event(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["add"]
    saved_snippet: Any
    id: int


class saved_snippet_remove_event(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["remove"]
    saved_snippet_id: int
    id: int


class scheduled_messages_add_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["add"]
    scheduled_messages: List[Any]
    id: int


class scheduled_messages_remove_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["remove"]
    scheduled_message_id: int
    id: int


class scheduled_messages_update_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["update"]
    scheduled_message: Any
    id: int


class stream_create_event(BaseModel):
    type: Literal["stream"]
    op: Literal["create"]
    streams: List[Any]
    id: int


class stream_delete_event(BaseModel):
    type: Literal["stream"]
    op: Literal["delete"]
    streams: List[Any]
    id: int


class stream_update_event(BaseModel):
    type: Literal["stream"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str, Any, Literal[None]]
    name: str
    stream_id: int
    id: int
    rendered_description: Optional[str] = None
    history_public_to_subscribers: Optional[bool] = None
    is_web_public: Optional[bool] = None


class submessage_event(BaseModel):
    type: Literal["submessage"]
    message_id: int
    submessage_id: int
    sender_id: int
    msg_type: str
    content: str
    id: int


class subscription_add_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["add"]
    subscriptions: List[Any]
    id: int


class subscription_peer_add_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["peer_add"]
    user_ids: List[int]
    stream_ids: List[int]
    id: int


class subscription_peer_remove_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["peer_remove"]
    user_ids: List[int]
    stream_ids: List[int]
    id: int


class subscription_remove_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["remove"]
    subscriptions: List[Any]
    id: int


class subscription_update_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["update"]
    property: str
    stream_id: int
    value: Union[bool, int, str]
    id: int


class typing_start_event(BaseModel):
    type: Literal["typing"]
    op: Literal["start"]
    message_type: Literal["direct", "stream"]
    sender: Any
    id: int
    recipients: Optional[List[Any]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class typing_stop_event(BaseModel):
    type: Literal["typing"]
    op: Literal["stop"]
    message_type: Literal["direct", "stream"]
    sender: Any
    id: int
    recipients: Optional[List[Any]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class update_display_settings_event(BaseModel):
    type: Literal["update_display_settings"]
    setting_name: str
    setting: Union[bool, int, str]
    user: str
    id: int
    language_name: Optional[str] = None


class update_global_notifications_event(BaseModel):
    type: Literal["update_global_notifications"]
    notification_name: str
    setting: Union[bool, int, str]
    user: str
    id: int


class update_message_event(BaseModel):
    type: Literal["update_message"]
    user_id: Optional[int]
    edit_timestamp: int
    message_id: int
    flags: List[str]
    message_ids: List[int]
    rendering_only: bool
    id: int
    stream_id: Optional[int] = None
    stream_name: Optional[str] = None
    is_me_message: Optional[bool] = None
    orig_content: Optional[str] = None
    orig_rendered_content: Optional[str] = None
    content: Optional[str] = None
    rendered_content: Optional[str] = None
    topic_links: Optional[List[Any]] = None
    subject: Optional[str] = None
    new_stream_id: Optional[int] = None
    propagate_mode: Optional[Literal["change_one", "change_later", "change_all"]] = None
    orig_subject: Optional[str] = None


class update_message_flags_add_event(BaseModel):
    type: Literal["update_message_flags"]
    op: Literal["add"]
    operation: Literal["add"]
    flag: str
    messages: List[int]
    all: bool
    id: int


class update_message_flags_remove_event(BaseModel):
    type: Literal["update_message_flags"]
    op: Literal["remove"]
    operation: Literal["remove"]
    flag: str
    messages: List[int]
    all: bool
    id: int
    message_details: Optional[Dict[str, Any]] = None


class user_group_add_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["add"]
    group: Any
    id: int


class user_group_add_members_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["add_members"]
    group_id: int
    user_ids: List[int]
    id: int


class user_group_add_subgroups_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["add_subgroups"]
    group_id: int
    direct_subgroup_ids: List[int]
    id: int


class user_group_remove_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["remove"]
    group_id: int
    id: int


class user_group_remove_members_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["remove_members"]
    group_id: int
    user_ids: List[int]
    id: int


class user_group_remove_subgroups_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["remove_subgroups"]
    group_id: int
    direct_subgroup_ids: List[int]
    id: int


class user_group_update_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["update"]
    group_id: int
    data: Any
    id: int


class user_settings_update_event(BaseModel):
    type: Literal["user_settings"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int
    language_name: Optional[str] = None


class user_status_event(BaseModel):
    type: Literal["user_status"]
    user_id: int
    id: int
    away: Optional[bool] = None
    status_text: Optional[str] = None
    emoji_name: Optional[str] = None
    emoji_code: Optional[str] = None
    reaction_type: Optional[Literal["unicode_emoji", "realm_emoji", "zulip_extra_emoji"]] = None


class user_topic_event(BaseModel):
    id: int
    type: Literal["user_topic"]
    stream_id: int
    topic_name: str
    last_updated: int
    visibility_policy: int


class web_reload_client_event(BaseModel):
    type: Literal["web_reload_client"]
    immediate: bool
    id: int
