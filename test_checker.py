from zerver.lib.event_schema import (
    check_alert_words,
    check_attachment_add,
    check_attachment_remove,
    check_attachment_update,
    check_custom_profile_fields,
    check_default_stream_groups,
    check_default_streams,
    check_delete_message,
    check_direct_message,
    check_draft_add,
    check_draft_remove,
    check_draft_update,
    check_has_zoom_token,
    check_heartbeat,
    check_invites_changed,
    check_message,
    check_muted_topics,
    check_muted_users,
    check_onboarding_steps,
    check_presence,
    check_reaction_add,
    check_reaction_remove,
    check_realm_bot_add,
    check_realm_bot_delete,
    check_realm_bot_update,
    check_realm_deactivated,
    check_realm_default_update,
    check_realm_domains_add,
    check_realm_domains_change,
    check_realm_domains_remove,
    check_realm_emoji_update,
    check_realm_export,
    check_realm_export_consent,
    check_realm_linkifiers,
    check_realm_playgrounds,
    check_realm_update,
    check_realm_update_dict,
    check_realm_user_add,
    check_realm_user_remove,
    check_realm_user_update,
    check_saved_snippet_add,
    check_saved_snippet_remove,
    check_scheduled_message_add,
    check_scheduled_message_remove,
    check_scheduled_message_update,
    check_stream_create,
    check_stream_delete,
    check_stream_update,
    check_submessage,
    check_subscription_add,
    check_subscription_peer_add,
    check_subscription_peer_remove,
    check_subscription_remove,
    check_subscription_update,
    check_typing_start,
    check_typing_stop,
    check_update_display_settings,
    check_update_global_notifications,
    check_update_message,
    check_update_message_flags_add,
    check_update_message_flags_remove,
    check_user_group_add,
    check_user_group_add_members,
    check_user_group_add_subgroups,
    check_user_group_remove,
    check_user_group_remove_members,
    check_user_group_remove_subgroups,
    check_user_group_update,
    check_user_settings_update,
    check_user_status,
    check_user_topic,
)

from zerver.lib.types import AnonymousSettingGroupDict


class VisibilityPolicyType:
    def __init__(self):
        self.MUTED = 1
        self.UNMUTED = 2
        self.FOLLOWED = 3
        self.INHERIT = 0


VisiblityPolicy = VisibilityPolicyType()


class UserTopicType:
    def __init__(self):
        self.VisibilityPolicy = VisiblityPolicy


UserTopic = UserTopicType()

context = dict(
    AnonymousSettingGroupDict=AnonymousSettingGroupDict,
    UserTopic=UserTopic,
)

with open("real_world_checker_calls.txt", "r") as file:
    for i, line in enumerate(file):
        c = eval(line, context)
        f = globals()[c["name"]]
        print(i, c["name"])
        f(*c["args"], **c["kwargs"])
