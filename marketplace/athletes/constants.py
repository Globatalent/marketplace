from django.utils.translation import ugettext_lazy as _


MALE = 'MALE'
FEMALE = 'FEMALE'
SEX_CHOICES = (
    (MALE, _('Male')),
    (FEMALE, _('Female'))
)

APPROVED = 'APPROVED'
REJECTED = 'REJECTED'
REVIEWING = 'REVIEWING'
PENDING_REVIEW = 'PENDING_REVIEW'
STATE_CHOICES = (
    (APPROVED, _('Approved')),
    (REJECTED, _('Rejected')),
    (REVIEWING, _('Reviewing')),
    (PENDING_REVIEW, _('Pending Review')),
)
