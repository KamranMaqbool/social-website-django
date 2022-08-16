from django.contrib.contenttypes.models import ContentType
from .models import Action
import datetime
from django.utils import timezone


def create_action(user, verb, target=None):
    print('create_actionnnnnnnnn targettttttt', target)
    now = datetime.datetime.now()
    last_minute = now - timezone.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id, verb=verb, created_gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)
    
    if not similar_actions:
        # no existing actions found
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False