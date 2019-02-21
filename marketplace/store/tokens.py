from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, invited, timestamp):
        return (
            six.text_type(invited.pk) + six.text_type(timestamp) +
            six.text_type(invited.is_used)
        )
account_activation_token = TokenGenerator()