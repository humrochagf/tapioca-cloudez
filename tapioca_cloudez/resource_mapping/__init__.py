# -*- coding: utf-8 -*-

from .database import DATABASE_MAPPING
from .domain import DOMAIN_MAPPING
from .email import EMAIL_MAPPING
from .email_account import EMAIL_ACCOUNT_MAPPING
from .email_account_autoreply import EMAIL_ACCOUNT_AUTOREPLY_MAPPING
from .email_group import EMAIL_GROUP_MAPPING
from .migration import MIGRATION_MAPPING
from .website import WEBSITE_MAPPING

RESOURCE_MAPPING = {}
RESOURCE_MAPPING.update(DATABASE_MAPPING)
RESOURCE_MAPPING.update(DOMAIN_MAPPING)
RESOURCE_MAPPING.update(EMAIL_MAPPING)
RESOURCE_MAPPING.update(EMAIL_ACCOUNT_MAPPING)
RESOURCE_MAPPING.update(EMAIL_ACCOUNT_AUTOREPLY_MAPPING)
RESOURCE_MAPPING.update(EMAIL_GROUP_MAPPING)
RESOURCE_MAPPING.update(MIGRATION_MAPPING)
RESOURCE_MAPPING.update(WEBSITE_MAPPING)
