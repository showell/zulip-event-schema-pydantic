# hacked from Zulip

from typing import Any

from zerver.lib.types import GroupPermissionSetting


class SystemGroups:
    FULL_MEMBERS = "role:fullmembers"
    EVERYONE_ON_INTERNET = "role:internet"
    OWNERS = "role:owners"
    ADMINISTRATORS = "role:administrators"
    MODERATORS = "role:moderators"
    MEMBERS = "role:members"
    EVERYONE = "role:everyone"
    NOBODY = "role:nobody"


class Realm:
    property_types: dict[str, type | tuple[type, ...]] = dict(
        allow_edit_history=bool,
        allow_message_editing=bool,
        avatar_changes_disabled=bool,
        bot_creation_policy=int,
        default_code_block_language=str,
        default_language=str,
        description=str,
        digest_emails_enabled=bool,
        digest_weekday=int,
        disallow_disposable_email_addresses=bool,
        email_changes_disabled=bool,
        emails_restricted_to_domains=bool,
        enable_guest_user_indicator=bool,
        enable_read_receipts=bool,
        enable_spectator_access=bool,
        giphy_rating=int,
        inline_image_preview=bool,
        inline_url_embed_preview=bool,
        invite_required=bool,
        invite_to_stream_policy=int,
        jitsi_server_url=(str, type(None)),
        mandatory_topics=bool,
        message_content_allowed_in_email_notifications=bool,
        message_content_edit_limit_seconds=(int, type(None)),
        message_content_delete_limit_seconds=(int, type(None)),
        move_messages_between_streams_limit_seconds=(int, type(None)),
        move_messages_within_stream_limit_seconds=(int, type(None)),
        message_retention_days=(int, type(None)),
        name=str,
        name_changes_disabled=bool,
        push_notifications_enabled=bool,
        require_unique_names=bool,
        send_welcome_emails=bool,
        video_chat_provider=int,
        waiting_period_threshold=int,
        want_advertise_in_communities_directory=bool,
        wildcard_mention_policy=int,
    )

    REALM_PERMISSION_GROUP_SETTINGS: dict[str, GroupPermissionSetting] = dict(
        create_multiuse_invite_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.ADMINISTRATORS,
        ),
        can_access_all_users_group=GroupPermissionSetting(
            require_system_group=True,
            allow_internet_group=False,
            allow_nobody_group=False,
            allow_everyone_group=True,
            default_group_name=SystemGroups.EVERYONE,
            allowed_system_groups=[SystemGroups.EVERYONE, SystemGroups.MEMBERS],
        ),
        can_add_custom_emoji_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.MEMBERS,
        ),
        can_create_groups=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.MEMBERS,
        ),
        can_create_public_channel_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.MEMBERS,
        ),
        can_create_private_channel_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.MEMBERS,
        ),
        can_create_web_public_channel_group=GroupPermissionSetting(
            require_system_group=True,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.OWNERS,
            allowed_system_groups=[
                SystemGroups.MODERATORS,
                SystemGroups.ADMINISTRATORS,
                SystemGroups.OWNERS,
                SystemGroups.NOBODY,
            ],
        ),
        can_delete_any_message_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.ADMINISTRATORS,
        ),
        can_delete_own_message_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=True,
            default_group_name=SystemGroups.EVERYONE,
        ),
        can_invite_users_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.MEMBERS,
        ),
        can_manage_all_groups=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=False,
            allow_everyone_group=False,
            default_group_name=SystemGroups.OWNERS,
        ),
        can_move_messages_between_channels_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name=SystemGroups.MEMBERS,
        ),
        can_move_messages_between_topics_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=True,
            default_group_name=SystemGroups.EVERYONE,
        ),
        direct_message_initiator_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=True,
            default_group_name=SystemGroups.EVERYONE,
        ),
        direct_message_permission_group=GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=True,
            default_group_name=SystemGroups.EVERYONE,
        ),
    )


class Stream:
    STREAM_POST_POLICY_EVERYONE = 1
    STREAM_POST_POLICY_ADMINS = 2
    STREAM_POST_POLICY_RESTRICT_NEW_MEMBERS = 3
    STREAM_POST_POLICY_MODERATORS = 4

    STREAM_POST_POLICY_TYPES = [
        STREAM_POST_POLICY_EVERYONE,
        STREAM_POST_POLICY_ADMINS,
        STREAM_POST_POLICY_MODERATORS,
        STREAM_POST_POLICY_RESTRICT_NEW_MEMBERS,
    ]

    stream_permission_group_settings = {
        "can_administer_channel_group": GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=False,
            default_group_name="stream_creator_or_nobody",
        ),
        "can_remove_subscribers_group": GroupPermissionSetting(
            require_system_group=False,
            allow_internet_group=False,
            allow_nobody_group=True,
            allow_everyone_group=True,
            default_group_name=SystemGroups.ADMINISTRATORS,
        ),
    }


class UserProfile:
    display_settings_legacy = dict(
        # Don't add anything new to this legacy dict.
        # Instead, see `modern_settings` below.
        color_scheme=int,
        default_language=str,
        web_home_view=str,
        demote_inactive_streams=int,
        dense_mode=bool,
        emojiset=str,
        enable_drafts_synchronization=bool,
        enter_sends=bool,
        fluid_layout_width=bool,
        high_contrast_mode=bool,
        left_side_userlist=bool,
        starred_message_counts=bool,
        translate_emoticons=bool,
        twenty_four_hour_time=bool,
    )

    notification_settings_legacy = dict(
        # Don't add anything new to this legacy dict.
        # Instead, see `modern_notification_settings` below.
        desktop_icon_count_display=int,
        email_notifications_batching_period_seconds=int,
        enable_desktop_notifications=bool,
        enable_digest_emails=bool,
        enable_login_emails=bool,
        enable_marketing_emails=bool,
        enable_offline_email_notifications=bool,
        enable_offline_push_notifications=bool,
        enable_online_push_notifications=bool,
        enable_sounds=bool,
        enable_stream_audible_notifications=bool,
        enable_stream_desktop_notifications=bool,
        enable_stream_email_notifications=bool,
        enable_stream_push_notifications=bool,
        message_content_in_email_notifications=bool,
        notification_sound=str,
        pm_content_in_desktop_notifications=bool,
        presence_enabled=bool,
        realm_name_in_email_notifications_policy=int,
        wildcard_mentions_notify=bool,
    )

    modern_settings = dict(
        # Add new general settings here.
        display_emoji_reaction_users=bool,
        email_address_visibility=int,
        web_escape_navigates_to_home_view=bool,
        receives_typing_notifications=bool,
        send_private_typing_notifications=bool,
        send_read_receipts=bool,
        send_stream_typing_notifications=bool,
        allow_private_data_export=bool,
        web_mark_read_on_scroll_policy=int,
        web_channel_default_view=int,
        user_list_style=int,
        web_animate_image_previews=str,
        web_stream_unreads_count_display_policy=int,
        web_font_size_px=int,
        web_line_height_percent=int,
        web_navigate_to_sent_message=bool,
        web_suggest_update_timezone=bool,
    )

    modern_notification_settings: dict[str, Any] = dict(
        # Add new notification settings here.
        enable_followed_topic_desktop_notifications=bool,
        enable_followed_topic_email_notifications=bool,
        enable_followed_topic_push_notifications=bool,
        enable_followed_topic_audible_notifications=bool,
        enable_followed_topic_wildcard_mentions_notify=bool,
        automatically_follow_topics_policy=int,
        automatically_unmute_topics_in_muted_streams_policy=int,
        automatically_follow_topics_where_mentioned=bool,
    )

    notification_setting_types = {
        **notification_settings_legacy,
        **modern_notification_settings,
    }

    # Define the types of the various automatically managed properties
    property_types = {
        **display_settings_legacy,
        **notification_setting_types,
        **modern_settings,
    }

    USERNAME_FIELD = "email"
    MAX_NAME_LENGTH = 100
    MIN_NAME_LENGTH = 2
    API_KEY_LENGTH = 32
    NAME_INVALID_CHARS = ["*", "`", "\\", ">", '"', "@"]

    DEFAULT_BOT = 1
    """
    Incoming webhook bots are limited to only sending messages via webhooks.
    Thus, it is less of a security risk to expose their API keys to third-party services,
    since they can't be used to read messages.
    """
    INCOMING_WEBHOOK_BOT = 2
    # This value is also being used in web/src/settings_bots.js.
    # On updating it here, update it there as well.
    OUTGOING_WEBHOOK_BOT = 3
    """
    Embedded bots run within the Zulip server itself; events are added to the
    embedded_bots queue and then handled by a QueueProcessingWorker.
    """
    EMBEDDED_BOT = 4

    BOT_TYPES = {
        DEFAULT_BOT: "Generic bot",
        INCOMING_WEBHOOK_BOT: "Incoming webhook",
        OUTGOING_WEBHOOK_BOT: "Outgoing webhook",
        EMBEDDED_BOT: "Embedded bot",
    }

    SERVICE_BOT_TYPES = [
        OUTGOING_WEBHOOK_BOT,
        EMBEDDED_BOT,
    ]

    ROLE_REALM_OWNER = 100
    ROLE_REALM_ADMINISTRATOR = 200
    ROLE_MODERATOR = 300
    ROLE_MEMBER = 400
    ROLE_GUEST = 600

    ROLE_TYPES = [
        ROLE_REALM_OWNER,
        ROLE_REALM_ADMINISTRATOR,
        ROLE_MODERATOR,
        ROLE_MEMBER,
        ROLE_GUEST,
    ]


class RealmUserDefault(UserProfile):
    pass
