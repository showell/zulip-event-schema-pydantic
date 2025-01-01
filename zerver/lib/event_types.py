from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from zerver.lib.types import AnonymousSettingGroupDict
from pydantic import AfterValidator, BaseModel
from typing import Annotated, List, Literal, Tuple, Optional, Union


def check_url(val: str) -> str:
    try:
        URLValidator()(val)
    except ValidationError:  # nocoverage
        raise AssertionError(f"{val} is not a URL")
    return val


Url = Annotated[str, AfterValidator(check_url)]


class alert_words_event(BaseModel):
    type: Literal["alert_words"]
    alert_words: List[str]
    id: int


class AttachmentMessage(BaseModel):
    id: int
    date_sent: int


class Attachment(BaseModel):
    id: int
    name: str
    size: int
    path_id: str
    create_time: int
    messages: List[AttachmentMessage]


class attachment_add_event(BaseModel):
    type: Literal["attachment"]
    op: Literal["add"]
    attachment: Attachment
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
    attachment: Attachment
    upload_space_used: int
    id: int


class _detailed_custom_profile_core(BaseModel):
    id: int
    type: int
    name: str
    hint: str
    field_data: str
    order: int
    required: bool
    editable_by_user: bool


class _detailed_custom_profile(_detailed_custom_profile_core):
    # TODO: fix types to avoid optional fields
    display_in_profile_summary: Optional[bool] = None


class custom_profile_fields_event(BaseModel):
    type: Literal["custom_profile_fields"]
    fields: List[_detailed_custom_profile]
    id: int


class StreamGroup(BaseModel):
    name: str
    id: int
    description: str
    streams: List[int]


class default_stream_groups_event(BaseModel):
    type: Literal["default_stream_groups"]
    default_stream_groups: List[StreamGroup]
    id: int


class default_streams_event(BaseModel):
    type: Literal["default_streams"]
    default_streams: List[int]
    id: int


class _delete_message_event_core(BaseModel):
    type: Literal["delete_message"]
    message_type: Literal["private", "stream"]
    id: int


class delete_message_event(_delete_message_event_core):
    # TODO: fix types to avoid optional fields
    message_id: Optional[int] = None
    message_ids: Optional[List[int]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class TopicLink(BaseModel):
    text: str
    url: str


class DirectMessageDisplayRecipient(BaseModel):
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
    reactions: List[dict[str, object]]
    recipient_id: int
    sender_realm_str: str
    sender_email: str
    sender_full_name: str
    sender_id: int
    subject: str
    topic_links: List[TopicLink]
    submessages: List[dict[str, object]]
    timestamp: int
    type: str
    display_recipient: List[DirectMessageDisplayRecipient]


class direct_message_event(BaseModel):
    type: Literal["message"]
    flags: List[str]
    message: _direct_message_event__message
    id: int


class _DraftFields_core(BaseModel):
    id: int
    type: Literal["", "private", "stream"]
    to: List[int]
    topic: str
    content: str


class DraftFields(_DraftFields_core):
    # TODO: fix types to avoid optional fields
    timestamp: Optional[int] = None


class drafts_add_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["add"]
    drafts: List[DraftFields]
    id: int


class drafts_remove_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["remove"]
    draft_id: int
    id: int


class drafts_update_event(BaseModel):
    type: Literal["drafts"]
    op: Literal["update"]
    draft: DraftFields
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
    reactions: List[dict[str, object]]
    recipient_id: int
    sender_realm_str: str
    sender_email: str
    sender_full_name: str
    sender_id: int
    subject: str
    topic_links: List[TopicLink]
    submessages: List[dict[str, object]]
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


class MutedUser(BaseModel):
    id: int
    timestamp: int


class muted_users_event(BaseModel):
    type: Literal["muted_users"]
    muted_users: List[MutedUser]
    id: int


class OnboardingSteps(BaseModel):
    type: str
    name: str


class onboarding_steps_event(BaseModel):
    type: Literal["onboarding_steps"]
    onboarding_steps: List[OnboardingSteps]
    id: int


class Presence(BaseModel):
    status: Literal["active", "idle"]
    timestamp: int
    client: str
    pushable: bool


class _presence_event_core(BaseModel):
    type: Literal["presence"]
    user_id: int
    server_timestamp: Union[float, int]
    presence: dict[str, Presence]
    id: int


class presence_event(_presence_event_core):
    # TODO: fix types to avoid optional fields
    email: Optional[str] = None


class reaction_add_event(BaseModel):
    type: Literal["reaction"]
    op: Literal["add"]
    message_id: int
    emoji_name: str
    emoji_code: str
    reaction_type: Literal["realm_emoji", "unicode_emoji", "zulip_extra_emoji"]
    user_id: int
    id: int


class reaction_remove_event(BaseModel):
    type: Literal["reaction"]
    op: Literal["remove"]
    message_id: int
    emoji_name: str
    emoji_code: str
    reaction_type: Literal["realm_emoji", "unicode_emoji", "zulip_extra_emoji"]
    user_id: int
    id: int


class BotServicesOutgoing(BaseModel):
    base_url: Url
    interface: int
    token: str


class BotServicesEmbedded(BaseModel):
    service_name: str
    config_data: dict[str, str]


class Bot(BaseModel):
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
    services: List[Union[BotServicesOutgoing, BotServicesEmbedded]]


class realm_bot_add_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["add"]
    bot: Bot
    id: int


class BotTypeForDelete(BaseModel):
    user_id: int


class realm_bot_delete_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["delete"]
    bot: BotTypeForDelete
    id: int


class _BotTypeForUpdate_core(BaseModel):
    user_id: int


class BotTypeForUpdate(_BotTypeForUpdate_core):
    # TODO: fix types to avoid optional fields
    api_key: Optional[str] = None
    avatar_url: Optional[str] = None
    default_all_public_streams: Optional[bool] = None
    default_events_register_stream: Optional[Optional[str]] = None
    default_sending_stream: Optional[Optional[str]] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    owner_id: Optional[int] = None
    services: Optional[List[Union[BotServicesOutgoing, BotServicesEmbedded]]] = None


class realm_bot_update_event(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["update"]
    bot: BotTypeForUpdate
    id: int


class realm_deactivated_event(BaseModel):
    type: Literal["realm"]
    op: Literal["deactivated"]
    realm_id: int
    id: int


class RealmDomain(BaseModel):
    domain: str
    allow_subdomains: bool


class realm_domains_add_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["add"]
    realm_domain: RealmDomain
    id: int


class realm_domains_change_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["change"]
    realm_domain: RealmDomain
    id: int


class realm_domains_remove_event(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["remove"]
    domain: str
    id: int


class RealmEmoji(BaseModel):
    id: str
    name: str
    source_url: str
    deactivated: bool
    author_id: int
    still_url: Optional[str]


class realm_emoji_update_event(BaseModel):
    type: Literal["realm_emoji"]
    op: Literal["update"]
    realm_emoji: dict[str, RealmEmoji]
    id: int


class realm_export_consent_event(BaseModel):
    type: Literal["realm_export_consent"]
    user_id: int
    consented: bool
    id: int


class Export(BaseModel):
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
    exports: List[Export]
    id: int


class RealmLinkifier(BaseModel):
    pattern: str
    url_template: str
    id: int


class realm_linkifiers_event(BaseModel):
    type: Literal["realm_linkifiers"]
    realm_linkifiers: List[RealmLinkifier]
    id: int


class RealmPlayground(BaseModel):
    id: int
    name: str
    pygments_language: str
    url_template: str


class realm_playgrounds_event(BaseModel):
    type: Literal["realm_playgrounds"]
    realm_playgrounds: List[RealmPlayground]
    id: int


class AllowMessageEditingData(BaseModel):
    allow_message_editing: bool


class _AuthenticationMethodDict_core(BaseModel):
    enabled: bool
    available: bool


class AuthenticationMethodDict(_AuthenticationMethodDict_core):
    # TODO: fix types to avoid optional fields
    unavailable_reason: Optional[str] = None


class AuthenticationDict(BaseModel):
    Google: AuthenticationMethodDict
    Dev: AuthenticationMethodDict
    LDAP: AuthenticationMethodDict
    GitHub: AuthenticationMethodDict
    Email: AuthenticationMethodDict


class AuthenticationData(BaseModel):
    authentication_methods: AuthenticationDict


class IconData(BaseModel):
    icon_url: str
    icon_source: str


class LogoData(BaseModel):
    logo_url: str
    logo_source: str


class MessageContentEditLimitSecondsData(BaseModel):
    message_content_edit_limit_seconds: Optional[int]


class NightLogoData(BaseModel):
    night_logo_url: str
    night_logo_source: str


class _GroupSettingUpdateData_core(BaseModel):
    pass


class GroupSettingUpdateData(_GroupSettingUpdateData_core):
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


class PlanTypeData(BaseModel):
    plan_type: int
    upload_quota_mib: Optional[int]
    max_file_upload_size_mib: int


class realm_update_dict_event(BaseModel):
    type: Literal["realm"]
    op: Literal["update_dict"]
    property: Literal["default", "icon", "logo", "night_logo"]
    data: Union[
        AllowMessageEditingData,
        AuthenticationData,
        IconData,
        LogoData,
        MessageContentEditLimitSecondsData,
        NightLogoData,
        GroupSettingUpdateData,
        PlanTypeData,
    ]
    id: int


class realm_update_event(BaseModel):
    type: Literal["realm"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class RealmUser(BaseModel):
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
    profile_data: dict[str, dict[str, object]]
    timezone: str
    date_joined: str
    delivery_email: Optional[str]


class realm_user_add_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["add"]
    person: RealmUser
    id: int


class RemovedUser(BaseModel):
    user_id: int
    full_name: str


class realm_user_remove_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["remove"]
    person: RemovedUser
    id: int


class realm_user_settings_defaults_update_event(BaseModel):
    type: Literal["realm_user_settings_defaults"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class PersonAvatarFields(BaseModel):
    user_id: int
    avatar_source: str
    avatar_url: Optional[str]
    avatar_url_medium: Optional[str]
    avatar_version: int


class PersonBotOwnerId(BaseModel):
    user_id: int
    bot_owner_id: int


class _CustomProfileField_core(BaseModel):
    id: int
    value: Optional[str]


class CustomProfileField(_CustomProfileField_core):
    # TODO: fix types to avoid optional fields
    rendered_value: Optional[str] = None


class PersonCustomProfileField(BaseModel):
    user_id: int
    custom_profile_field: CustomProfileField


class PersonDeliveryEmail(BaseModel):
    user_id: int
    delivery_email: Optional[str]


class PersonEmail(BaseModel):
    user_id: int
    new_email: str


class PersonFullName(BaseModel):
    user_id: int
    full_name: str


class PersonIsBillingAdmin(BaseModel):
    user_id: int
    is_billing_admin: bool


class PersonRole(BaseModel):
    user_id: int
    role: Literal[100, 200, 300, 400, 600]


class PersonTimezone(BaseModel):
    user_id: int
    email: str
    timezone: str


class PersonIsActive(BaseModel):
    user_id: int
    is_active: bool


class realm_user_update_event(BaseModel):
    type: Literal["realm_user"]
    op: Literal["update"]
    person: Union[
        PersonAvatarFields,
        PersonBotOwnerId,
        PersonCustomProfileField,
        PersonDeliveryEmail,
        PersonEmail,
        PersonFullName,
        PersonIsBillingAdmin,
        PersonRole,
        PersonTimezone,
        PersonIsActive,
    ]
    id: int


class restart_event(BaseModel):
    type: Literal["restart"]
    zulip_version: str
    zulip_merge_base: str
    zulip_feature_level: int
    server_generation: int
    id: int


class SavedSnippetFields(BaseModel):
    id: int
    title: str
    content: str
    date_created: int


class saved_snippet_add_event(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["add"]
    saved_snippet: SavedSnippetFields
    id: int


class saved_snippet_remove_event(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["remove"]
    saved_snippet_id: int
    id: int


class _ScheduledMessageFields_core(BaseModel):
    scheduled_message_id: int
    type: Literal["private", "stream"]
    to: Union[List[int], int]
    content: str
    rendered_content: str
    scheduled_delivery_timestamp: int
    failed: bool


class ScheduledMessageFields(_ScheduledMessageFields_core):
    # TODO: fix types to avoid optional fields
    topic: Optional[str] = None


class scheduled_messages_add_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["add"]
    scheduled_messages: List[ScheduledMessageFields]
    id: int


class scheduled_messages_remove_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["remove"]
    scheduled_message_id: int
    id: int


class scheduled_messages_update_event(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["update"]
    scheduled_message: ScheduledMessageFields
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


class _stream_update_event_core(BaseModel):
    type: Literal["stream"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str, AnonymousSettingGroupDict, Literal[None]]
    name: str
    stream_id: int
    id: int


class stream_update_event(_stream_update_event_core):
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


class SingleSubscription(BaseModel):
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
    subscriptions: List[SingleSubscription]
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


class RemoveSub(BaseModel):
    name: str
    stream_id: int


class subscription_remove_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["remove"]
    subscriptions: List[RemoveSub]
    id: int


class subscription_update_event(BaseModel):
    type: Literal["subscription"]
    op: Literal["update"]
    property: str
    stream_id: int
    value: Union[bool, int, str]
    id: int


class TypingPerson(BaseModel):
    email: str
    user_id: int


class _typing_start_event_core(BaseModel):
    type: Literal["typing"]
    op: Literal["start"]
    message_type: Literal["direct", "stream"]
    sender: TypingPerson
    id: int


class typing_start_event(_typing_start_event_core):
    # TODO: fix types to avoid optional fields
    recipients: Optional[List[TypingPerson]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class _typing_stop_event_core(BaseModel):
    type: Literal["typing"]
    op: Literal["stop"]
    message_type: Literal["direct", "stream"]
    sender: TypingPerson
    id: int


class typing_stop_event(_typing_stop_event_core):
    # TODO: fix types to avoid optional fields
    recipients: Optional[List[TypingPerson]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class _update_display_settings_event_core(BaseModel):
    type: Literal["update_display_settings"]
    setting_name: str
    setting: Union[bool, int, str]
    user: str
    id: int


class update_display_settings_event(_update_display_settings_event_core):
    # TODO: fix types to avoid optional fields
    language_name: Optional[str] = None


class update_global_notifications_event(BaseModel):
    type: Literal["update_global_notifications"]
    notification_name: str
    setting: Union[bool, int, str]
    user: str
    id: int


class _update_message_event_core(BaseModel):
    type: Literal["update_message"]
    user_id: Optional[int]
    edit_timestamp: int
    message_id: int
    flags: List[str]
    message_ids: List[int]
    rendering_only: bool
    id: int


class update_message_event(_update_message_event_core):
    # TODO: fix types to avoid optional fields
    stream_id: Optional[int] = None
    stream_name: Optional[str] = None
    is_me_message: Optional[bool] = None
    orig_content: Optional[str] = None
    orig_rendered_content: Optional[str] = None
    content: Optional[str] = None
    rendered_content: Optional[str] = None
    topic_links: Optional[List[TopicLink]] = None
    subject: Optional[str] = None
    new_stream_id: Optional[int] = None
    propagate_mode: Optional[Literal["change_all", "change_later", "change_one"]] = None
    orig_subject: Optional[str] = None


class update_message_flags_add_event(BaseModel):
    type: Literal["update_message_flags"]
    op: Literal["add"]
    operation: Literal["add"]
    flag: str
    messages: List[int]
    all: bool
    id: int


class _message_details_core(BaseModel):
    type: Literal["private", "stream"]


class _message_details(_message_details_core):
    # TODO: fix types to avoid optional fields
    mentioned: Optional[bool] = None
    user_ids: Optional[List[int]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None
    unmuted_stream_msg: Optional[bool] = None


class _update_message_flags_remove_event_core(BaseModel):
    type: Literal["update_message_flags"]
    op: Literal["remove"]
    operation: Literal["remove"]
    flag: str
    messages: List[int]
    all: bool
    id: int


class update_message_flags_remove_event(_update_message_flags_remove_event_core):
    # TODO: fix types to avoid optional fields
    message_details: Optional[dict[str, _message_details]] = None


class Group(BaseModel):
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
    group: Group
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


class _UserGroupData_core(BaseModel):
    pass


class UserGroupData(_UserGroupData_core):
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
    data: UserGroupData
    id: int


class _user_settings_update_event_core(BaseModel):
    type: Literal["user_settings"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class user_settings_update_event(_user_settings_update_event_core):
    # TODO: fix types to avoid optional fields
    language_name: Optional[str] = None


class _user_status_event_core(BaseModel):
    type: Literal["user_status"]
    user_id: int
    id: int


class user_status_event(_user_status_event_core):
    # TODO: fix types to avoid optional fields
    away: Optional[bool] = None
    status_text: Optional[str] = None
    emoji_name: Optional[str] = None
    emoji_code: Optional[str] = None
    reaction_type: Optional[Literal["realm_emoji", "unicode_emoji", "zulip_extra_emoji"]] = None


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
