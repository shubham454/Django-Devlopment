import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)


class IvalidLoginAttempltsCache:
    @staticmethod
    def _key(email):
        return 'invalid_login_attempt_{}'.format(email)

    @staticmethod
    def _value(lockout_timestamp, timebucket):
        return {'lockout_start': lockout_timestamp,
                'invalid_attempt_tomestamp': timebucket
                }

    @staticmethod
    def delete(email):
        try:
            cache.delete(IvalidLoginAttempltsCache._key(email))
        except Exception as e:
            logger.exception(e.message)

    @staticmethod
    def get(email):
        try:
            key=IvalidLoginAttempltsCache._key(email)
            return cache.get(key)
        except Exception as e:
            logger.exception(e.message)