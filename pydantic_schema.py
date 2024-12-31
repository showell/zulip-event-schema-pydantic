from pydantic import BaseModel
from typing import Dict, List, Literal, Tuple, Optional, Union

# TODO: Make this check for valid urls using URLValidator from django
UrlType = str

from zerver.lib.types import AnonymousSettingGroupDict


class alert_words_event(BaseModel):
    type: Literal["alert_words"]
    alert_words: List[str]
    id: int


class _attachment_message_type(BaseModel):
    id: int
    date_sent: int


class _attachment_type(BaseModel):
    id: int
    name: str
    size: int
    path_id: str
    create_time: int
    messages: List[_attachment_message_type]


class attachment_add_event(BaseModel):
    type: Literal["attachment"]
    op: Literal["add"]
    attachment: _attachment_type
    upload_space_used: int
    id: int


class _attachment_remove_event__attachment(BaseModel):
    id: int


class attachment_remove_event(BaseModel):
    type: Literal["attachment"]
    op: Literal["remove"]
    attachment: _attachment_remove_event__attachment
    upload_space_used: int
    id: int


class attachment_update_event(BaseModel):
    type: Literal["attachment"]
    op: Literal["update"]
    attachment: _attachment_type
    upload_space_used: int
    id: int


class _detailed_custom_profile(BaseModel):
    id: int
    type: int
    name: str
    hint: str
    field_data: str
    order: int
    required: bool
    editable_by_user: bool

    # TODO: fix types to avoid optional fields
    display_in_profile_summary: Optional[bool] = None


class custom_profile_fields_event(BaseModel):
    type: Literal["custom_profile_fields"]
    fields: List[_detailed_custom_profile]
    id: int


class _stream_group(BaseModel):
    name: str
    id: int
    description: str
    streams: List[int]


class default_stream_groups_event(BaseModel):
    type: Literal["default_stream_groups"]
    default_stream_groups: List[_stream_group]
    id: int


class default_streams_event(BaseModel):
    type: Literal["default_streams"]
    default_streams: List[int]
    id: int


class delete_message_event(BaseModel):
    type: Literal["delete_message"]
    message_type: Literal["private", "stream"]
    id: int

    # TODO: fix types to avoid optional fields
    message_id: Optional[int] = None
    message_ids: Optional[List[int]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class _topic_link(BaseModel):
    text: str
    url: str


class _direct_message_display_recipient(BaseModel):
    id: int
    is_mirror_dummy: bool
    email: str
    full_name: str


class _direct_message_event__message(BaseModel):
    avatar_url: Optional[str]
    client: str
    content: str
    content_type: Literal["text/html"]
    id: int
    is_me_message: bool
    reactions: List[Dict]
    recipient_id: int
    sender_realm_str: str
    sender_email: str
    sender_full_name: str
    sender_id: int
    subject: str
    topic_links: List[_topic_link]
    submessages: List[Dict]
    timestamp: int
    type: str
    display_recipient: List[_direct_message_display_recipient]


class direct_message_event(BaseModel):
    type: Literal["message"]
    flags: List[str]
    message: _direct_message_event__message
    id: int


class _draft_fields(BaseModel):
    id: int
    type: Literal["", "stream", "private"]
    to: List[int]
    topic: str
    content: str

    # TODO: fix types to avoid optional fields
    timestamp: Optional[int] = None


class drafts_add_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["add"]
    drafts: List[_draft_fields]
    id: int


class drafts_remove_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["remove"]
    draft_id: int
    id: int


class drafts_update_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["update"]
    draft: _draft_fields
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


class _message_event__message(BaseModel):
    avatar_url: Optional[str]
    client: str
    content: str
    content_type: Literal["text/html"]
    id: int
    is_me_message: bool
    reactions: List[Dict]
    recipient_id: int
    sender_realm_str: str
    sender_email: str
    sender_full_name: str
    sender_id: int
    subject: str
    topic_links: List[_topic_link]
    submessages: List[Dict]
    timestamp: int
    type: str
    display_recipient: str
    stream_id: int


class message_event(BaseModel):
    type: Literal["message"]
    flags: List[str]
    message: _message_event__message
    id: int


class muted_topics_event(BaseModel):
    type: Literal["muted_topics"]
    muted_topics: List[Tuple[str, str, int]]
    id: int


class _muted_user_type(BaseModel):
    id: int
    timestamp: int


class muted_users_event(BaseModel):
    type: Literal["muted_users"]
    muted_users: List[_muted_user_type]
    id: int


class _onboarding_steps(BaseModel):
    type: str
    name: str


class onboarding_steps_event(BaseModel):
    type: Literal["onboarding_steps"]
    onboarding_steps: List[_onboarding_steps]
    id: int


class _presence_type(BaseModel):
    status: Literal["active", "idle"]
    timestamp: int
    client: str
    pushable: bool


class presence_event(BaseModel):
    type: Literal["presence"]
    user_id: int
    server_timestamp: Union[float, int]
    presence: Dict[str, _presence_type]
    id: int

    # TODO: fix types to avoid optional fields
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


class _bot_services_outgoing_type(BaseModel):
    base_url: UrlType
    interface: int
    token: str


class _bot_services_embedded_type(BaseModel):
    service_name: str
    config_data: Dict[str, str]


class _bot_type(BaseModel):
    user_id: int
    api_key: str
    avatar_url: str
    bot_type: int
    default_all_public_streams: bool
    default_events_register_stream: Optional[str]
    default_sending_stream: Optional[str]
    email: str
    full_name: str
    is_active: bool
    owner_id: int
    services: List[Union[_bot_services_outgoing_type, _bot_services_embedded_type]]


class realm_bot_add_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["add"]
    bot: _bot_type
    id: int


class _bot_type_for_delete(BaseModel):
    user_id: int


class realm_bot_delete_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["delete"]
    bot: _bot_type_for_delete
    id: int


class _bot_type_for_update(BaseModel):
    user_id: int

    # TODO: fix types to avoid optional fields
    api_key: Optional[str] = None
    avatar_url: Optional[str] = None
    default_all_public_streams: Optional[bool] = None
    default_events_register_stream: Optional[Optional[str]] = None
    default_sending_stream: Optional[Optional[str]] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    owner_id: Optional[int] = None
    services: Optional[List[Union[_bot_services_outgoing_type, _bot_services_embedded_type]]] = None


class realm_bot_update_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["update"]
    bot: _bot_type_for_update
    id: int


class realm_deactivated_event(BaseModel):
    type: Literal["realm"]
    op: Literal["deactivated"]
    realm_id: int
    id: int


class _realm_domain_type(BaseModel):
    domain: str
    allow_subdomains: bool


class realm_domains_add_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["add"]
    realm_domain: _realm_domain_type
    id: int


class realm_domains_change_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["change"]
    realm_domain: _realm_domain_type
    id: int


class realm_domains_remove_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["remove"]
    domain: str
    id: int


class _realm_emoji_type(BaseModel):
    id: str
    name: str
    source_url: str
    deactivated: bool
    author_id: int
    still_url: Optional[str]


class realm_emoji_update_event(BaseModel):
    type: Literal["realm_emoji"]
    op: Literal["update"]
    realm_emoji: Dict[str, _realm_emoji_type]
    id: int


class realm_export_consent_event(BaseModel):
    type: Literal["realm_export_consent"]
    user_id: int
    consented: bool
    id: int


class _export_type(BaseModel):
    id: int
    export_time: Union[float, int]
    acting_user_id: int
    export_url: Optional[str]
    deleted_timestamp: Optional[Union[float, int]]
    failed_timestamp: Optional[Union[float, int]]
    pending: bool
    export_type: int


class realm_export_event(BaseModel):
    type: Literal["realm_export"]
    exports: List[_export_type]
    id: int


class _realm_linkifier_type(BaseModel):
    pattern: str
    url_template: str
    id: int


class realm_linkifiers_event(BaseModel):
    type: Literal["realm_linkifiers"]
    realm_linkifiers: List[_realm_linkifier_type]
    id: int


class _realm_playground_type(BaseModel):
    id: int
    name: str
    pygments_language: str
    url_template: str


class realm_playgrounds_event(BaseModel):
    type: Literal["realm_playgrounds"]
    realm_playgrounds: List[_realm_playground_type]
    id: int


class _allow_message_editing_data(BaseModel):
    allow_message_editing: bool


class _authentication_method_dict(BaseModel):
    enabled: bool
    available: bool

    # TODO: fix types to avoid optional fields
    unavailable_reason: Optional[str] = None


class _authentication_dict(BaseModel):
    Google: _authentication_method_dict
    Dev: _authentication_method_dict
    LDAP: _authentication_method_dict
    GitHub: _authentication_method_dict
    Email: _authentication_method_dict


class _authentication_data(BaseModel):
    authentication_methods: _authentication_dict


class _icon_data(BaseModel):
    icon_url: str
    icon_source: str


class _logo_data(BaseModel):
    logo_url: str
    logo_source: str


class _message_content_edit_limit_seconds_data(BaseModel):
    message_content_edit_limit_seconds: Optional[int]


class _night_logo_data(BaseModel):
    night_logo_url: str
    night_logo_source: str


class _group_setting_update_data_type(BaseModel):
    # TODO: fix types to avoid optional fields
    create_multiuse_invite_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_access_all_users_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_add_custom_emoji_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_create_groups: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_create_public_channel_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_create_private_channel_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_create_web_public_channel_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_delete_any_message_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_delete_own_message_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_invite_users_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_manage_all_groups: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_move_messages_between_channels_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_move_messages_between_topics_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    direct_message_initiator_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    direct_message_permission_group: Optional[Union[int, AnonymousSettingGroupDict]] = None


class _plan_type_data(BaseModel):
    plan_type: int
    upload_quota_mib: Optional[int]
    max_file_upload_size_mib: int


class realm_update_dict_event(BaseModel):
    type: Literal["realm"]
    op: Literal["update_dict"]
    property: Literal["default", "icon", "logo", "night_logo"]
    data: Union[
        _allow_message_editing_data,
        _authentication_data,
        _icon_data,
        _logo_data,
        _message_content_edit_limit_seconds_data,
        _night_logo_data,
        _group_setting_update_data_type,
        _plan_type_data,
    ]
    id: int


class realm_update_event(BaseModel):
    type: Literal["realm"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class _realm_user_type(BaseModel):
    user_id: int
    email: str
    avatar_url: Optional[str]
    avatar_version: int
    full_name: str
    is_admin: bool
    is_billing_admin: bool
    is_owner: bool
    is_bot: bool
    is_guest: bool
    role: Literal[100, 200, 300, 400, 600]
    is_active: bool
    profile_data: Dict[str, Dict]
    timezone: str
    date_joined: str
    delivery_email: Optional[str]


class realm_user_add_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["add"]
    person: _realm_user_type
    id: int


class _removed_user_type(BaseModel):
    user_id: int
    full_name: str


class realm_user_remove_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["remove"]
    person: _removed_user_type
    id: int


class realm_user_settings_defaults_update_event(BaseModel):
    type: Literal["realm_user_settings_defaults"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class _person_avatar_fields(BaseModel):
    user_id: int
    avatar_source: str
    avatar_url: Optional[str]
    avatar_url_medium: Optional[str]
    avatar_version: int


class _person_bot_owner_id(BaseModel):
    user_id: int
    bot_owner_id: int


class _custom_profile_field_type(BaseModel):
    id: int
    value: Optional[str]

    # TODO: fix types to avoid optional fields
    rendered_value: Optional[str] = None


class _person_custom_profile_field(BaseModel):
    user_id: int
    custom_profile_field: _custom_profile_field_type


class _person_delivery_email(BaseModel):
    user_id: int
    delivery_email: Optional[str]


class _person_email(BaseModel):
    user_id: int
    new_email: str


class _person_full_name(BaseModel):
    user_id: int
    full_name: str


class _person_is_billing_admin(BaseModel):
    user_id: int
    is_billing_admin: bool


class _person_role(BaseModel):
    user_id: int
    role: Literal[100, 200, 300, 400, 600]


class _person_timezone(BaseModel):
    user_id: int
    email: str
    timezone: str


class _person_is_active(BaseModel):
    user_id: int
    is_active: bool


class realm_user_update_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["update"]
    person: Union[
        _person_avatar_fields,
        _person_bot_owner_id,
        _person_custom_profile_field,
        _person_delivery_email,
        _person_email,
        _person_full_name,
        _person_is_billing_admin,
        _person_role,
        _person_timezone,
        _person_is_active,
    ]
    id: int


class restart_event(BaseModel):
    type: Literal["restart"]
    zulip_version: str
    zulip_merge_base: str
    zulip_feature_level: int
    server_generation: int
    id: int


class _saved_snippet_fields(BaseModel):
    id: int
    title: str
    content: str
    date_created: int


class saved_snippet_add_event(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["add"]
    saved_snippet: _saved_snippet_fields
    id: int


class saved_snippet_remove_event(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["remove"]
    saved_snippet_id: int
    id: int


class _scheduled_message_fields(BaseModel):
    scheduled_message_id: int
    type: Literal["stream", "private"]
    to: Union[List[int], int]
    content: str
    rendered_content: str
    scheduled_delivery_timestamp: int
    failed: bool

    # TODO: fix types to avoid optional fields
    topic: Optional[str] = None


class scheduled_messages_add_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["add"]
    scheduled_messages: List[_scheduled_message_fields]
    id: int


class scheduled_messages_remove_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["remove"]
    scheduled_message_id: int
    id: int


class scheduled_messages_update_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["update"]
    scheduled_message: _scheduled_message_fields
    id: int


class _basic_stream_fields(BaseModel):
    is_archived: bool
    can_administer_channel_group: Union[int, AnonymousSettingGroupDict]
    can_remove_subscribers_group: Union[int, AnonymousSettingGroupDict]
    creator_id: Optional[int]
    date_created: int
    description: str
    first_message_id: Optional[int]
    is_recently_active: bool
    history_public_to_subscribers: bool
    invite_only: bool
    is_announcement_only: bool
    is_web_public: bool
    message_retention_days: Optional[int]
    name: str
    rendered_description: str
    stream_id: int
    stream_post_policy: int
    stream_weekly_traffic: Optional[int]


class stream_create_event(BaseModel):
    type: Literal["stream"]
    op: Literal["create"]
    streams: List[_basic_stream_fields]
    id: int


class stream_delete_event(BaseModel):
    type: Literal["stream"]
    op: Literal["delete"]
    streams: List[_basic_stream_fields]
    id: int


class stream_update_event(BaseModel):
    type: Literal["stream"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str, AnonymousSettingGroupDict, Literal[None]]
    name: str
    stream_id: int
    id: int

    # TODO: fix types to avoid optional fields
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


class _single_subscription_type(BaseModel):
    is_archived: bool
    can_administer_channel_group: Union[int, AnonymousSettingGroupDict]
    can_remove_subscribers_group: Union[int, AnonymousSettingGroupDict]
    creator_id: Optional[int]
    date_created: int
    description: str
    first_message_id: Optional[int]
    is_recently_active: bool
    history_public_to_subscribers: bool
    invite_only: bool
    is_announcement_only: bool
    is_web_public: bool
    message_retention_days: Optional[int]
    name: str
    rendered_description: str
    stream_id: int
    stream_post_policy: int
    stream_weekly_traffic: Optional[int]
    audible_notifications: Optional[bool]
    color: str
    desktop_notifications: Optional[bool]
    email_notifications: Optional[bool]
    in_home_view: bool
    is_muted: bool
    pin_to_top: bool
    push_notifications: Optional[bool]
    subscribers: List[int]
    wildcard_mentions_notify: Optional[bool]


class subscription_add_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["add"]
    subscriptions: List[_single_subscription_type]
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


class _remove_sub_type(BaseModel):
    name: str
    stream_id: int


class subscription_remove_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["remove"]
    subscriptions: List[_remove_sub_type]
    id: int


class subscription_update_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["update"]
    property: str
    stream_id: int
    value: Union[bool, int, str]
    id: int


class _typing_person_type(BaseModel):
    email: str
    user_id: int


class typing_start_event(BaseModel):
    type: Literal["typing"]
    op: Literal["start"]
    message_type: Literal["direct", "stream"]
    sender: _typing_person_type
    id: int

    # TODO: fix types to avoid optional fields
    recipients: Optional[List[_typing_person_type]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class typing_stop_event(BaseModel):
    type: Literal["typing"]
    op: Literal["stop"]
    message_type: Literal["direct", "stream"]
    sender: _typing_person_type
    id: int

    # TODO: fix types to avoid optional fields
    recipients: Optional[List[_typing_person_type]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class update_display_settings_event(BaseModel):
    type: Literal["update_display_settings"]
    setting_name: str
    setting: Union[bool, int, str]
    user: str
    id: int

    # TODO: fix types to avoid optional fields
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

    # TODO: fix types to avoid optional fields
    stream_id: Optional[int] = None
    stream_name: Optional[str] = None
    is_me_message: Optional[bool] = None
    orig_content: Optional[str] = None
    orig_rendered_content: Optional[str] = None
    content: Optional[str] = None
    rendered_content: Optional[str] = None
    topic_links: Optional[List[_topic_link]] = None
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


class _message_details(BaseModel):
    type: Literal["private", "stream"]

    # TODO: fix types to avoid optional fields
    mentioned: Optional[bool] = None
    user_ids: Optional[List[int]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None
    unmuted_stream_msg: Optional[bool] = None


class update_message_flags_remove_event(BaseModel):
    type: Literal["update_message_flags"]
    op: Literal["remove"]
    operation: Literal["remove"]
    flag: str
    messages: List[int]
    all: bool
    id: int

    # TODO: fix types to avoid optional fields
    message_details: Optional[Dict[str, _message_details]] = None


class _group_type(BaseModel):
    id: int
    name: str
    creator_id: Optional[int]
    date_created: Optional[int]
    members: List[int]
    direct_subgroup_ids: List[int]
    description: str
    is_system_group: bool
    can_add_members_group: Union[int, AnonymousSettingGroupDict]
    can_join_group: Union[int, AnonymousSettingGroupDict]
    can_leave_group: Union[int, AnonymousSettingGroupDict]
    can_manage_group: Union[int, AnonymousSettingGroupDict]
    can_mention_group: Union[int, AnonymousSettingGroupDict]
    can_remove_members_group: Union[int, AnonymousSettingGroupDict]
    deactivated: bool


class user_group_add_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["add"]
    group: _group_type
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


class _user_group_data_type(BaseModel):
    # TODO: fix types to avoid optional fields
    name: Optional[str] = None
    description: Optional[str] = None
    can_add_members_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_join_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_leave_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_manage_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_mention_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    can_remove_members_group: Optional[Union[int, AnonymousSettingGroupDict]] = None
    deactivated: Optional[bool] = None


class user_group_update_event(BaseModel):
    type: Literal["user_group"]
    op: Literal["update"]
    group_id: int
    data: _user_group_data_type
    id: int


class user_settings_update_event(BaseModel):
    type: Literal["user_settings"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int

    # TODO: fix types to avoid optional fields
    language_name: Optional[str] = None


class user_status_event(BaseModel):
    type: Literal["user_status"]
    user_id: int
    id: int

    # TODO: fix types to avoid optional fields
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
