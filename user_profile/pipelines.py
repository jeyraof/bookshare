# -*- coding: utf-8 -*-
from user_profile.models import Profile


def create_profile_when_join(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        if not hasattr(user, 'profile'):
            profile = Profile(user_id=user.id,
                              photo='http://graph.facebook.com/{0}/picture?type=large'.format(response.get('id')),
                              level=10)
            profile.save()
            user.profile = profile

    return {'profile': user.profile}
