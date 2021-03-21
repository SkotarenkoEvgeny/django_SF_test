from django.views.generic import ListView

from .models import FeedItem, RegisteredUser


class FeedItemListView(ListView):
    model = FeedItem
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_user = self.request.user
        filter_parametr = self.request.GET.get('answer')
        if filter_parametr == 'my_posts' or filter_parametr == 'my_posts_subscribe':
            registered_user = RegisteredUser.objects.get(user=active_user)
            tracking_list = [active_user.id]
            if filter_parametr == 'my_posts_subscribe':
                tracking_list += [item.user.id for item in RegisteredUser.objects.get(user=active_user).tracking.all()]
            context['object_list'] = [item for item in FeedItem.objects.all() if item.user.id in tracking_list]

        return context
