from django.conf.urls import patterns, include, url


urlpatterns = patterns('social.views',

                       url(r'^$', "articles",
                           name='social_articles'),
                       url(r'^article/create/$', "article_create_update",
                           name='social_article_create'),
                       url(r'^articles/(?P<article_id>\w+)/edit/$',
                           "article_create_update",
                           name='social_article_edit'),
                       url(r'^articles/(?P<article_id>\w+)/delete/$',
                           "article_delete",
                           name='social_article_update'),
                       url(r'^articles/(?P<article_id>\w+)$',
                           "article_comments",
                           name='social_article_comments'),

                       url(r'^articles/(?P<article_id>\w+)/comment/create/$',
                           "comment_create_update",
                           name='social_comment_create'),
                       url(r'^articles/(?P<article_id>\w+)/comments/(?P<comment_id>\w+)/edit/$',
                           "comment_create_update",
                           name='social_comment_edit'),
                       )
