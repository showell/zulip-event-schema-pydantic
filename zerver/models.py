# hacked from Zulip

class Realm:
    pass

class RealmUserDefault:
    pass

class Stream:
    pass

class UserProfile:
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
