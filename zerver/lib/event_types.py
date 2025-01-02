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


class EventAlertWords(BaseModel):
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


class EventAttachmentAdd(BaseModel):
    type: Literal["attachment"]
    op: Literal["add"]
    attachment: Attachment
    upload_space_used: int
    id: int


class _EventAttachmentRemove__attachment(BaseModel):
    id: int


class EventAttachmentRemove(BaseModel):
    type: Literal["attachment"]
    op: Literal["remove"]
    attachment: _EventAttachmentRemove__attachment
    upload_space_used: int
    id: int


class EventAttachmentUpdate(BaseModel):
    type: Literal["attachment"]
    op: Literal["update"]
    attachment: Attachment
    upload_space_used: int
    id: int


class DetailedCustomProfileCore(BaseModel):
    id: int
    type: int
    name: str
    hint: str
    field_data: str
    order: int
    required: bool
    editable_by_user: bool


class DetailedCustomProfile(DetailedCustomProfileCore):
    # TODO: fix types to avoid optional fields
    display_in_profile_summary: Optional[bool] = None


class EventCustomProfileFields(BaseModel):
    type: Literal["custom_profile_fields"]
    fields: List[DetailedCustomProfile]
    id: int


class StreamGroup(BaseModel):
    name: str
    id: int
    description: str
    streams: List[int]


class EventDefaultStreamGroups(BaseModel):
    type: Literal["default_stream_groups"]
    default_stream_groups: List[StreamGroup]
    id: int


class EventDefaultStreams(BaseModel):
    type: Literal["default_streams"]
    default_streams: List[int]
    id: int


class EventDeleteMessageCore(BaseModel):
    type: Literal["delete_message"]
    message_type: Literal["private", "stream"]
    id: int


class EventDeleteMessage(EventDeleteMessageCore):
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


class _EventDirectMessage__message(BaseModel):
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


class EventDirectMessage(BaseModel):
    type: Literal["message"]
    flags: List[str]
    message: _EventDirectMessage__message
    id: int


class DraftFieldsCore(BaseModel):
    id: int
    type: Literal["", "private", "stream"]
    to: List[int]
    topic: str
    content: str


class DraftFields(DraftFieldsCore):
    # TODO: fix types to avoid optional fields
    timestamp: Optional[int] = None


class EventDraftsAdd(BaseModel):
    type: Literal["drafts"]
    op: Literal["add"]
    drafts: List[DraftFields]
    id: int


class EventDraftsRemove(BaseModel):
    type: Literal["drafts"]
    op: Literal["remove"]
    draft_id: int
    id: int


class EventDraftsUpdate(BaseModel):
    type: Literal["drafts"]
    op: Literal["update"]
    draft: DraftFields
    id: int


class EventHasZoomToken(BaseModel):
    type: Literal["has_zoom_token"]
    value: bool
    id: int


class EventHeartbeat(BaseModel):
    type: Literal["heartbeat"]
    id: int


class EventInvitesChanged(BaseModel):
    type: Literal["invites_changed"]
    id: int


class _EventMessage__message(BaseModel):
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


class EventMessage(BaseModel):
    type: Literal["message"]
    flags: List[str]
    message: _EventMessage__message
    id: int


class EventMutedTopics(BaseModel):
    type: Literal["muted_topics"]
    muted_topics: List[Tuple[str, str, int]]
    id: int


class MutedUser(BaseModel):
    id: int
    timestamp: int


class EventMutedUsers(BaseModel):
    type: Literal["muted_users"]
    muted_users: List[MutedUser]
    id: int


class OnboardingSteps(BaseModel):
    type: str
    name: str


class EventOnboardingSteps(BaseModel):
    type: Literal["onboarding_steps"]
    onboarding_steps: List[OnboardingSteps]
    id: int


class Presence(BaseModel):
    status: Literal["active", "idle"]
    timestamp: int
    client: str
    pushable: bool


class EventPresenceCore(BaseModel):
    type: Literal["presence"]
    user_id: int
    server_timestamp: Union[float, int]
    presence: dict[str, Presence]
    id: int


class EventPresence(EventPresenceCore):
    # TODO: fix types to avoid optional fields
    email: Optional[str] = None


class EventReactionAdd(BaseModel):
    type: Literal["reaction"]
    op: Literal["add"]
    message_id: int
    emoji_name: str
    emoji_code: str
    reaction_type: Literal["realm_emoji", "unicode_emoji", "zulip_extra_emoji"]
    user_id: int
    id: int


class EventReactionRemove(BaseModel):
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


class EventRealmBotAdd(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["add"]
    bot: Bot
    id: int


class BotTypeForDelete(BaseModel):
    user_id: int


class EventRealmBotDelete(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["delete"]
    bot: BotTypeForDelete
    id: int


class BotTypeForUpdateCore(BaseModel):
    user_id: int


class BotTypeForUpdate(BotTypeForUpdateCore):
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


class EventRealmBotUpdate(BaseModel):
    type: Literal["realm_bot"]
    op: Literal["update"]
    bot: BotTypeForUpdate
    id: int


class EventRealmDeactivated(BaseModel):
    type: Literal["realm"]
    op: Literal["deactivated"]
    realm_id: int
    id: int


class RealmDomain(BaseModel):
    domain: str
    allow_subdomains: bool


class EventRealmDomainsAdd(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["add"]
    realm_domain: RealmDomain
    id: int


class EventRealmDomainsChange(BaseModel):
    type: Literal["realm_domains"]
    op: Literal["change"]
    realm_domain: RealmDomain
    id: int


class EventRealmDomainsRemove(BaseModel):
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


class EventRealmEmojiUpdate(BaseModel):
    type: Literal["realm_emoji"]
    op: Literal["update"]
    realm_emoji: dict[str, RealmEmoji]
    id: int


class EventRealmExportConsent(BaseModel):
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


class EventRealmExport(BaseModel):
    type: Literal["realm_export"]
    exports: List[Export]
    id: int


class RealmLinkifier(BaseModel):
    pattern: str
    url_template: str
    id: int


class EventRealmLinkifiers(BaseModel):
    type: Literal["realm_linkifiers"]
    realm_linkifiers: List[RealmLinkifier]
    id: int


class RealmPlayground(BaseModel):
    id: int
    name: str
    pygments_language: str
    url_template: str


class EventRealmPlaygrounds(BaseModel):
    type: Literal["realm_playgrounds"]
    realm_playgrounds: List[RealmPlayground]
    id: int


class AllowMessageEditingData(BaseModel):
    allow_message_editing: bool


class AuthenticationMethodDictCore(BaseModel):
    enabled: bool
    available: bool


class AuthenticationMethodDict(AuthenticationMethodDictCore):
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


class GroupSettingUpdateDataCore(BaseModel):
    pass


class GroupSettingUpdateData(GroupSettingUpdateDataCore):
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


class EventRealmUpdateDict(BaseModel):
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


class EventRealmUpdate(BaseModel):
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


class EventRealmUserAdd(BaseModel):
    type: Literal["realm_user"]
    op: Literal["add"]
    person: RealmUser
    id: int


class RemovedUser(BaseModel):
    user_id: int
    full_name: str


class EventRealmUserRemove(BaseModel):
    type: Literal["realm_user"]
    op: Literal["remove"]
    person: RemovedUser
    id: int


class EventRealmUserSettingsDefaultsUpdate(BaseModel):
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


class CustomProfileFieldCore(BaseModel):
    id: int
    value: Optional[str]


class CustomProfileField(CustomProfileFieldCore):
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


class EventRealmUserUpdate(BaseModel):
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


class EventRestart(BaseModel):
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


class EventSavedSnippetAdd(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["add"]
    saved_snippet: SavedSnippetFields
    id: int


class EventSavedSnippetRemove(BaseModel):
    type: Literal["saved_snippets"]
    op: Literal["remove"]
    saved_snippet_id: int
    id: int


class ScheduledMessageFieldsCore(BaseModel):
    scheduled_message_id: int
    type: Literal["private", "stream"]
    to: Union[List[int], int]
    content: str
    rendered_content: str
    scheduled_delivery_timestamp: int
    failed: bool


class ScheduledMessageFields(ScheduledMessageFieldsCore):
    # TODO: fix types to avoid optional fields
    topic: Optional[str] = None


class EventScheduledMessagesAdd(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["add"]
    scheduled_messages: List[ScheduledMessageFields]
    id: int


class EventScheduledMessagesRemove(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["remove"]
    scheduled_message_id: int
    id: int


class EventScheduledMessagesUpdate(BaseModel):
    type: Literal["scheduled_messages"]
    op: Literal["update"]
    scheduled_message: ScheduledMessageFields
    id: int


class BasicStreamFields(BaseModel):
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


class EventStreamCreate(BaseModel):
    type: Literal["stream"]
    op: Literal["create"]
    streams: List[BasicStreamFields]
    id: int


class EventStreamDelete(BaseModel):
    type: Literal["stream"]
    op: Literal["delete"]
    streams: List[BasicStreamFields]
    id: int


class EventStreamUpdateCore(BaseModel):
    type: Literal["stream"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str, AnonymousSettingGroupDict, Literal[None]]
    name: str
    stream_id: int
    id: int


class EventStreamUpdate(EventStreamUpdateCore):
    # TODO: fix types to avoid optional fields
    rendered_description: Optional[str] = None
    history_public_to_subscribers: Optional[bool] = None
    is_web_public: Optional[bool] = None


class EventSubmessage(BaseModel):
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


class EventSubscriptionAdd(BaseModel):
    type: Literal["subscription"]
    op: Literal["add"]
    subscriptions: List[SingleSubscription]
    id: int


class EventSubscriptionPeerAdd(BaseModel):
    type: Literal["subscription"]
    op: Literal["peer_add"]
    user_ids: List[int]
    stream_ids: List[int]
    id: int


class EventSubscriptionPeerRemove(BaseModel):
    type: Literal["subscription"]
    op: Literal["peer_remove"]
    user_ids: List[int]
    stream_ids: List[int]
    id: int


class RemoveSub(BaseModel):
    name: str
    stream_id: int


class EventSubscriptionRemove(BaseModel):
    type: Literal["subscription"]
    op: Literal["remove"]
    subscriptions: List[RemoveSub]
    id: int


class EventSubscriptionUpdate(BaseModel):
    type: Literal["subscription"]
    op: Literal["update"]
    property: str
    stream_id: int
    value: Union[bool, int, str]
    id: int


class TypingPerson(BaseModel):
    email: str
    user_id: int


class EventTypingStartCore(BaseModel):
    type: Literal["typing"]
    op: Literal["start"]
    message_type: Literal["direct", "stream"]
    sender: TypingPerson
    id: int


class EventTypingStart(EventTypingStartCore):
    # TODO: fix types to avoid optional fields
    recipients: Optional[List[TypingPerson]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class EventTypingStopCore(BaseModel):
    type: Literal["typing"]
    op: Literal["stop"]
    message_type: Literal["direct", "stream"]
    sender: TypingPerson
    id: int


class EventTypingStop(EventTypingStopCore):
    # TODO: fix types to avoid optional fields
    recipients: Optional[List[TypingPerson]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None


class EventUpdateDisplaySettingsCore(BaseModel):
    type: Literal["update_display_settings"]
    setting_name: str
    setting: Union[bool, int, str]
    user: str
    id: int


class EventUpdateDisplaySettings(EventUpdateDisplaySettingsCore):
    # TODO: fix types to avoid optional fields
    language_name: Optional[str] = None


class EventUpdateGlobalNotifications(BaseModel):
    type: Literal["update_global_notifications"]
    notification_name: str
    setting: Union[bool, int, str]
    user: str
    id: int


class EventUpdateMessageCore(BaseModel):
    type: Literal["update_message"]
    user_id: Optional[int]
    edit_timestamp: int
    message_id: int
    flags: List[str]
    message_ids: List[int]
    rendering_only: bool
    id: int


class EventUpdateMessage(EventUpdateMessageCore):
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


class EventUpdateMessageFlagsAdd(BaseModel):
    type: Literal["update_message_flags"]
    op: Literal["add"]
    operation: Literal["add"]
    flag: str
    messages: List[int]
    all: bool
    id: int


class MessageDetailsCore(BaseModel):
    type: Literal["private", "stream"]


class MessageDetails(MessageDetailsCore):
    # TODO: fix types to avoid optional fields
    mentioned: Optional[bool] = None
    user_ids: Optional[List[int]] = None
    stream_id: Optional[int] = None
    topic: Optional[str] = None
    unmuted_stream_msg: Optional[bool] = None


class EventUpdateMessageFlagsRemoveCore(BaseModel):
    type: Literal["update_message_flags"]
    op: Literal["remove"]
    operation: Literal["remove"]
    flag: str
    messages: List[int]
    all: bool
    id: int


class EventUpdateMessageFlagsRemove(EventUpdateMessageFlagsRemoveCore):
    # TODO: fix types to avoid optional fields
    message_details: Optional[dict[str, MessageDetails]] = None


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


class EventUserGroupAdd(BaseModel):
    type: Literal["user_group"]
    op: Literal["add"]
    group: Group
    id: int


class EventUserGroupAddMembers(BaseModel):
    type: Literal["user_group"]
    op: Literal["add_members"]
    group_id: int
    user_ids: List[int]
    id: int


class EventUserGroupAddSubgroups(BaseModel):
    type: Literal["user_group"]
    op: Literal["add_subgroups"]
    group_id: int
    direct_subgroup_ids: List[int]
    id: int


class EventUserGroupRemove(BaseModel):
    type: Literal["user_group"]
    op: Literal["remove"]
    group_id: int
    id: int


class EventUserGroupRemoveMembers(BaseModel):
    type: Literal["user_group"]
    op: Literal["remove_members"]
    group_id: int
    user_ids: List[int]
    id: int


class EventUserGroupRemoveSubgroups(BaseModel):
    type: Literal["user_group"]
    op: Literal["remove_subgroups"]
    group_id: int
    direct_subgroup_ids: List[int]
    id: int


class UserGroupDataCore(BaseModel):
    pass


class UserGroupData(UserGroupDataCore):
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


class EventUserGroupUpdate(BaseModel):
    type: Literal["user_group"]
    op: Literal["update"]
    group_id: int
    data: UserGroupData
    id: int


class EventUserSettingsUpdateCore(BaseModel):
    type: Literal["user_settings"]
    op: Literal["update"]
    property: str
    value: Union[bool, int, str]
    id: int


class EventUserSettingsUpdate(EventUserSettingsUpdateCore):
    # TODO: fix types to avoid optional fields
    language_name: Optional[str] = None


class EventUserStatusCore(BaseModel):
    type: Literal["user_status"]
    user_id: int
    id: int


class EventUserStatus(EventUserStatusCore):
    # TODO: fix types to avoid optional fields
    away: Optional[bool] = None
    status_text: Optional[str] = None
    emoji_name: Optional[str] = None
    emoji_code: Optional[str] = None
    reaction_type: Optional[Literal["realm_emoji", "unicode_emoji", "zulip_extra_emoji"]] = None


class EventUserTopic(BaseModel):
    id: int
    type: Literal["user_topic"]
    stream_id: int
    topic_name: str
    last_updated: int
    visibility_policy: int


class EventWebReloadClient(BaseModel):
    type: Literal["web_reload_client"]
    immediate: bool
    id: int
