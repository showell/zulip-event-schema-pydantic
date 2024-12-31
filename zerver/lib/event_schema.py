# This module is a collection of testing helpers for validating the
# schema of "events" sent by Zulip's server-to-client push system.
#
# By policy, every event generated by Zulip's API should be validated
# by a test in test_events.py with a schema checker here.
#
# See https://zulip.readthedocs.io/en/latest/subsystems/events-system.html
from zerver.lib.topic import ORIG_TOPIC, TOPIC_NAME
from zerver.lib.types import AnonymousSettingGroupDict
from zerver.models import Realm, RealmUserDefault, Stream, UserProfile


from pydantic_schema import (
    _allow_message_editing_data,
    _authentication_data,
    _bot_services_embedded_type,
    _bot_services_outgoing_type,
    _group_setting_update_data_type,
    _icon_data,
    _logo_data,
    _message_content_edit_limit_seconds_data,
    _night_logo_data,
    _person_avatar_fields,
    _person_bot_owner_id,
    _person_custom_profile_field,
    _person_delivery_email,
    _person_email,
    _person_full_name,
    _person_is_active,
    _person_is_billing_admin,
    _person_role,
    _person_timezone,
    _plan_type_data,
    alert_words_event,
    attachment_add_event,
    attachment_remove_event,
    attachment_update_event,
    custom_profile_fields_event,
    default_stream_groups_event,
    default_streams_event,
    delete_message_event,
    direct_message_event,
    drafts_add_event,
    drafts_remove_event,
    drafts_update_event,
    has_zoom_token_event,
    heartbeat_event,
    invites_changed_event,
    message_event,
    muted_topics_event,
    muted_users_event,
    onboarding_steps_event,
    presence_event,
    reaction_add_event,
    reaction_remove_event,
    realm_bot_add_event,
    realm_bot_delete_event,
    realm_bot_update_event,
    realm_deactivated_event,
    realm_domains_add_event,
    realm_domains_change_event,
    realm_domains_remove_event,
    realm_emoji_update_event,
    realm_export_consent_event,
    realm_export_event,
    realm_linkifiers_event,
    realm_playgrounds_event,
    realm_update_dict_event,
    realm_update_event,
    realm_user_add_event,
    realm_user_remove_event,
    realm_user_settings_defaults_update_event,
    realm_user_update_event,
    restart_event,
    saved_snippet_add_event,
    saved_snippet_add_event,
    saved_snippet_remove_event,
    saved_snippet_remove_event,
    scheduled_messages_add_event,
    scheduled_messages_remove_event,
    scheduled_messages_update_event,
    stream_create_event,
    stream_delete_event,
    stream_update_event,
    submessage_event,
    subscription_add_event,
    subscription_peer_add_event,
    subscription_peer_remove_event,
    subscription_remove_event,
    subscription_update_event,
    typing_start_event,
    typing_stop_event,
    update_display_settings_event,
    update_global_notifications_event,
    update_message_event,
    update_message_flags_add_event,
    update_message_flags_remove_event,
    user_group_add_event,
    user_group_add_members_event,
    user_group_add_subgroups_event,
    user_group_remove_event,
    user_group_remove_members_event,
    user_group_remove_subgroups_event,
    user_group_update_event,
    user_settings_update_event,
    user_status_event,
    user_topic_event,
    web_reload_client_event,
)

PERSON_TYPES = dict(
    avatar_fields=_person_avatar_fields,
    bot_owner_id=_person_bot_owner_id,
    custom_profile_field=_person_custom_profile_field,
    delivery_email=_person_delivery_email,
    email=_person_email,
    full_name=_person_full_name,
    is_billing_admin=_person_is_billing_admin,
    role=_person_role,
    timezone=_person_timezone,
    is_active=_person_is_active,
)


def make_checker(base_model):
    def f(name, event):
        print("name", name)
        print("event", event)
        print("base_model", base_model)
        base_model(**event)

    return f


_check_delete_message = make_checker(delete_message_event)
_check_has_zoom_token = make_checker(has_zoom_token_event)
_check_presence = make_checker(presence_event)
_check_realm_bot_add = make_checker(realm_bot_add_event)
_check_realm_bot_update = make_checker(realm_bot_update_event)
_check_realm_default_update = make_checker(realm_user_settings_defaults_update_event)
_check_realm_emoji_update = make_checker(realm_emoji_update_event)
_check_realm_export = make_checker(realm_export_event)
_check_realm_update = make_checker(realm_update_event)
_check_realm_update_dict = make_checker(realm_update_dict_event)
_check_realm_user_update = make_checker(realm_user_update_event)
_check_stream_update = make_checker(stream_update_event)
_check_subscription_update = make_checker(subscription_update_event)
_check_update_display_settings = make_checker(update_display_settings_event)
_check_update_global_notifications = make_checker(update_global_notifications_event)
_check_update_message = make_checker(update_message_event)
_check_user_group_update = make_checker(user_group_update_event)
_check_user_settings_update = make_checker(user_settings_update_event)
_check_user_status = make_checker(user_status_event)


def check_delete_message(
    var_name: str,
    event: dict[str, object],
    message_type: str,
    num_message_ids: int,
    is_legacy: bool,
) -> None:
    _check_delete_message(var_name, event)

    keys = {"id", "type", "message_type"}

    assert event["message_type"] == message_type

    if message_type == "stream":
        keys |= {"stream_id", "topic"}
    elif message_type == "private":
        pass
    else:
        raise AssertionError("unexpected message_type")

    if is_legacy:
        assert num_message_ids == 1
        keys.add("message_id")
    else:
        assert isinstance(event["message_ids"], list)
        assert num_message_ids == len(event["message_ids"])
        keys.add("message_ids")

    assert set(event.keys()) == keys


def check_has_zoom_token(
    var_name: str,
    event: dict[str, object],
    value: bool,
) -> None:
    _check_has_zoom_token(var_name, event)
    assert event["value"] == value


def check_presence(
    var_name: str,
    event: dict[str, object],
    has_email: bool,
    presence_key: str,
    status: str,
) -> None:
    _check_presence(var_name, event)

    assert ("email" in event) == has_email

    assert isinstance(event["presence"], dict)

    # Our tests only have one presence value.
    [(event_presence_key, event_presence_value)] = event["presence"].items()
    assert event_presence_key == presence_key
    assert event_presence_value["status"] == status


def check_realm_bot_add(
    var_name: str,
    event: dict[str, object],
) -> None:
    _check_realm_bot_add(var_name, event)

    assert isinstance(event["bot"], dict)
    bot_type = event["bot"]["bot_type"]

    services_field = f"{var_name}['bot']['services']"
    services = event["bot"]["services"]

    if bot_type == UserProfile.DEFAULT_BOT:
        assert services == []
    elif bot_type == UserProfile.OUTGOING_WEBHOOK_BOT:
        assert len(services) == 1
        _bot_services_outgoing_type(**services[0])
    elif bot_type == UserProfile.EMBEDDED_BOT:
        assert len(services) == 1
        _bot_services_embedded_type(**services[0])
    else:
        raise AssertionError(f"Unknown bot_type: {bot_type}")


def check_realm_bot_update(
    # Check schema plus the field.
    var_name: str,
    event: dict[str, object],
    field: str,
) -> None:
    # Check the overall schema first.
    _check_realm_bot_update(var_name, event)

    assert isinstance(event["bot"], dict)
    assert {"user_id", field} == set(event["bot"].keys())


def check_realm_emoji_update(var_name: str, event: dict[str, object]) -> None:
    """
    The way we send realm emojis is kinda clumsy--we
    send a dict mapping the emoji id to a sub_dict with
    the fields (including the id).  Ideally we can streamline
    this and just send a list of dicts.  The clients can make
    a Map as needed.
    """
    _check_realm_emoji_update(var_name, event)

    assert isinstance(event["realm_emoji"], dict)
    for k, v in event["realm_emoji"].items():
        assert v["id"] == k


def check_realm_export(
    var_name: str,
    event: dict[str, object],
    has_export_url: bool,
    has_deleted_timestamp: bool,
    has_failed_timestamp: bool,
) -> None:
    # Check the overall event first, knowing it has some
    # optional types.
    _check_realm_export(var_name, event)

    # It's possible to have multiple data exports, but the events tests do not
    # exercise that case, so we do strict validation for a single export here.
    assert isinstance(event["exports"], list)
    assert len(event["exports"]) == 1
    export = event["exports"][0]

    # Now verify which fields have non-None values.
    assert has_export_url == (export["export_url"] is not None)
    assert has_deleted_timestamp == (export["deleted_timestamp"] is not None)
    assert has_failed_timestamp == (export["failed_timestamp"] is not None)


def check_realm_update(
    var_name: str,
    event: dict[str, object],
    prop: str,
) -> None:
    """
    Realm updates have these two fields:

        property
        value

    We check not only the basic schema, but also that
    the value people actually matches the type from
    Realm.property_types that we have configured
    for the property.
    """
    _check_realm_update(var_name, event)

    assert prop == event["property"]
    value = event["value"]

    if prop in [
        "moderation_request_channel_id",
        "new_stream_announcements_stream_id",
        "signup_announcements_stream_id",
        "zulip_update_announcements_stream_id",
        "org_type",
    ]:
        assert isinstance(value, int)
        return

    property_type = Realm.property_types[prop]

    if property_type in (bool, int, str):
        assert isinstance(value, property_type)
    elif property_type == (int, type(None)):
        assert isinstance(value, int)
    elif property_type == (str, type(None)):
        assert isinstance(value, str)
    else:
        raise AssertionError(f"Unexpected property type {property_type}")


def check_realm_default_update(
    var_name: str,
    event: dict[str, object],
    prop: str,
) -> None:
    _check_realm_default_update(var_name, event)

    assert prop == event["property"]
    assert prop != "default_language"
    assert prop in RealmUserDefault.property_types

    prop_type = RealmUserDefault.property_types[prop]
    assert isinstance(event["value"], prop_type)


def check_realm_update_dict(
    # handle union types
    var_name: str,
    event: dict[str, object],
) -> None:
    _check_realm_update_dict(var_name, event)

    if event["property"] == "default":
        assert isinstance(event["data"], dict)

        if "allow_message_editing" in event["data"]:
            sub_type = _allow_message_editing_data
        elif "message_content_edit_limit_seconds" in event["data"]:
            sub_type = _message_content_edit_limit_seconds_data
        elif "authentication_methods" in event["data"]:
            sub_type = _authentication_data
        elif any(
            setting_name in event["data"] for setting_name in Realm.REALM_PERMISSION_GROUP_SETTINGS
        ):
            sub_type = _group_setting_update_data_type
        elif "plan_type" in event["data"]:
            sub_type = _plan_type_data
        else:
            raise AssertionError("unhandled fields in data")

    elif event["property"] == "icon":
        sub_type = _icon_data
    elif event["property"] == "logo":
        sub_type = _logo_data
    elif event["property"] == "night_logo":
        sub_type = _night_logo_data
    else:
        raise AssertionError("unhandled property: {event['property']}")

    sub_type(**event["data"])


def check_realm_user_update(
    # person_flavor tells us which extra fields we need
    var_name: str,
    event: dict[str, object],
    person_flavor: str,
) -> None:
    _check_realm_user_update(var_name, event)

    sub_type = PERSON_TYPES[person_flavor]
    sub_type(**event["person"])


def check_stream_update(
    var_name: str,
    event: dict[str, object],
) -> None:
    _check_stream_update(var_name, event)
    prop = event["property"]
    value = event["value"]

    extra_keys = set(event.keys()) - {
        "id",
        "type",
        "op",
        "property",
        "value",
        "name",
        "stream_id",
        "first_message_id",
    }

    if prop == "description":
        assert extra_keys == {"rendered_description"}
        assert isinstance(value, str)
    elif prop == "invite_only":
        assert extra_keys == {"history_public_to_subscribers", "is_web_public"}
        assert isinstance(value, bool)
    elif prop == "message_retention_days":
        assert extra_keys == set()
        if value is not None:
            assert isinstance(value, int)
    elif prop == "name":
        assert extra_keys == set()
        assert isinstance(value, str)
    elif prop == "stream_post_policy":
        assert extra_keys == set()
        assert value in Stream.STREAM_POST_POLICY_TYPES
    elif prop in Stream.stream_permission_group_settings:
        assert extra_keys == set()
        assert isinstance(value, int | AnonymousSettingGroupDict)
    elif prop == "first_message_id":
        assert extra_keys == set()
        assert isinstance(value, int)
    elif prop == "is_recently_active":
        assert extra_keys == set()
        assert isinstance(value, bool)
    else:
        raise AssertionError(f"Unknown property: {prop}")


def check_subscription_update(
    var_name: str, event: dict[str, object], property: str, value: bool
) -> None:
    _check_subscription_update(var_name, event)
    assert event["property"] == property
    assert event["value"] == value


def check_update_display_settings(
    var_name: str,
    event: dict[str, object],
) -> None:
    """
    Display setting events have a "setting" field that
    is more specifically typed according to the
    UserProfile.property_types dictionary.
    """
    _check_update_display_settings(var_name, event)
    setting_name = event["setting_name"]
    setting = event["setting"]

    assert isinstance(setting_name, str)
    if setting_name == "timezone":
        assert isinstance(setting, str)
    else:
        setting_type = UserProfile.property_types[setting_name]
        assert isinstance(setting, setting_type)

    if setting_name == "default_language":
        assert "language_name" in event
    else:
        assert "language_name" not in event


def check_user_settings_update(
    var_name: str,
    event: dict[str, object],
) -> None:
    _check_user_settings_update(var_name, event)
    setting_name = event["property"]
    value = event["value"]

    assert isinstance(setting_name, str)
    if setting_name == "timezone":
        assert isinstance(value, str)
    else:
        setting_type = UserProfile.property_types[setting_name]
        assert isinstance(value, setting_type)

    if setting_name == "default_language":
        assert "language_name" in event
    else:
        assert "language_name" not in event


def check_update_global_notifications(
    var_name: str,
    event: dict[str, object],
    desired_val: bool | int | str,
) -> None:
    """
    See UserProfile.notification_settings_legacy for
    more details.
    """
    _check_update_global_notifications(var_name, event)
    setting_name = event["notification_name"]
    setting = event["setting"]
    assert setting == desired_val

    assert isinstance(setting_name, str)
    setting_type = UserProfile.notification_settings_legacy[setting_name]
    assert isinstance(setting, setting_type)


def check_update_message(
    var_name: str,
    event: dict[str, object],
    is_stream_message: bool,
    has_content: bool,
    has_topic: bool,
    has_new_stream_id: bool,
    is_embedded_update_only: bool,
) -> None:
    # Always check the basic schema first.
    _check_update_message(var_name, event)

    actual_keys = set(event.keys())
    expected_keys = {
        "id",
        "type",
        "user_id",
        "edit_timestamp",
        "message_id",
        "flags",
        "message_ids",
        "rendering_only",
    }

    if is_stream_message:
        expected_keys |= {
            "stream_id",
            "stream_name",
        }

    if has_content:
        expected_keys |= {
            "is_me_message",
            "orig_content",
            "orig_rendered_content",
            "content",
            "rendered_content",
        }

    if has_topic:
        expected_keys |= {
            "topic_links",
            ORIG_TOPIC,
            TOPIC_NAME,
            "propagate_mode",
        }

    if has_new_stream_id:
        expected_keys |= {
            "new_stream_id",
            ORIG_TOPIC,
            "propagate_mode",
        }

    if is_embedded_update_only:
        expected_keys |= {
            "content",
            "rendered_content",
        }
        assert event["user_id"] is None
    else:
        assert isinstance(event["user_id"], int)

    assert event["rendering_only"] == is_embedded_update_only
    print(expected_keys)
    print(actual_keys)
    print(actual_keys - expected_keys)
    print(expected_keys - actual_keys)
    assert expected_keys == actual_keys


def check_user_group_update(var_name: str, event: dict[str, object], field: str) -> None:
    _check_user_group_update(var_name, event)

    assert isinstance(event["data"], dict)

    assert set(event["data"].keys()) == {field}


def check_user_status(var_name: str, event: dict[str, object], fields: set[str]) -> None:
    _check_user_status(var_name, event)

    assert set(event.keys()) == {"id", "type", "user_id"} | fields


check_alert_words = make_checker(alert_words_event)
check_attachment_add = make_checker(attachment_add_event)
check_attachment_remove = make_checker(attachment_remove_event)
check_attachment_update = make_checker(attachment_update_event)
check_custom_profile_fields = make_checker(custom_profile_fields_event)
check_default_stream_groups = make_checker(default_stream_groups_event)
check_default_streams = make_checker(default_streams_event)
check_direct_message = make_checker(direct_message_event)
check_draft_add = make_checker(drafts_add_event)
check_draft_remove = make_checker(drafts_remove_event)
check_draft_update = make_checker(drafts_update_event)
check_heartbeat = make_checker(heartbeat_event)
check_invites_changed = make_checker(invites_changed_event)
check_message = make_checker(message_event)
check_muted_topics = make_checker(muted_topics_event)
check_muted_users = make_checker(muted_users_event)
check_onboarding_steps = make_checker(onboarding_steps_event)
check_reaction_add = make_checker(reaction_add_event)
check_reaction_remove = make_checker(reaction_remove_event)
check_realm_bot_delete = make_checker(realm_bot_delete_event)
check_realm_deactivated = make_checker(realm_deactivated_event)
check_realm_domains_add = make_checker(realm_domains_add_event)
check_realm_domains_change = make_checker(realm_domains_change_event)
check_realm_domains_remove = make_checker(realm_domains_remove_event)
check_realm_export_consent = make_checker(realm_export_consent_event)
check_realm_linkifiers = make_checker(realm_linkifiers_event)
check_realm_playgrounds = make_checker(realm_playgrounds_event)
check_realm_user_add = make_checker(realm_user_add_event)
check_realm_user_remove = make_checker(realm_user_remove_event)
check_restart_event = make_checker(restart_event)
check_saved_snippet_add = make_checker(saved_snippet_add_event)
check_saved_snippet_add = make_checker(saved_snippet_add_event)
check_saved_snippet_remove = make_checker(saved_snippet_remove_event)
check_saved_snippet_remove = make_checker(saved_snippet_remove_event)
check_scheduled_message_add = make_checker(scheduled_messages_add_event)
check_scheduled_message_remove = make_checker(scheduled_messages_remove_event)
check_scheduled_message_update = make_checker(scheduled_messages_update_event)
check_stream_create = make_checker(stream_create_event)
check_stream_delete = make_checker(stream_delete_event)
check_submessage = make_checker(submessage_event)
check_subscription_add = make_checker(subscription_add_event)
check_subscription_peer_add = make_checker(subscription_peer_add_event)
check_subscription_peer_remove = make_checker(subscription_peer_remove_event)
check_subscription_remove = make_checker(subscription_remove_event)
check_typing_start = make_checker(typing_start_event)
check_typing_stop = make_checker(typing_stop_event)
check_update_message_flags_add = make_checker(update_message_flags_add_event)
check_update_message_flags_remove = make_checker(update_message_flags_remove_event)
check_user_group_add = make_checker(user_group_add_event)
check_user_group_add_members = make_checker(user_group_add_members_event)
check_user_group_add_subgroups = make_checker(user_group_add_subgroups_event)
check_user_group_remove = make_checker(user_group_remove_event)
check_user_group_remove_members = make_checker(user_group_remove_members_event)
check_user_group_remove_subgroups = make_checker(user_group_remove_subgroups_event)
check_user_topic = make_checker(user_topic_event)
check_web_reload_client_event = make_checker(web_reload_client_event)
