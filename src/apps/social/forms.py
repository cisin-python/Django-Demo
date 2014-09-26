from django import forms
from django.contrib.auth import get_user_model
from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Layout, HTML
from crispy_forms.bootstrap import FormActions
from social.models import Article, Comment, ARTICLE_TYPE
from parsley.decorators import parsleyfy


@parsleyfy
class ArticleForm(ModelForm):
    title = forms.CharField(max_length=255, required=True)
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(),
    )
    article_type = forms.ChoiceField(
        choices=ARTICLE_TYPE, required=True)
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                Div('title', css_class='span3'),
                css_class='span3'),
            Div(
                Div('description', css_class='span3'),
                css_class='span3'),
            Div(
                Div('article_type', css_class='span3'),
                css_class='span3'),
            css_class='row'),
    )
    helper.layout.append(
        FormActions(
            HTML(
                "<a href='{% url 'social_articles' %}' "
                "class='btn'>Cancel</a>"
            ),
            Submit('save', 'Save & Continue')
        )
    )

    class Meta:
        model = Article

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)


class CommentForm(ModelForm):

    helper = FormHelper()
    helper.form_id = 'comment-form'
    helper.form_tag = True
    helper.form_action = '.'
    helper.layout = Layout(
        Div(
            Div(
                Div('commenter', css_class='span3'),
                css_class='span3'),
            Div(
                Div('body', css_class='span3'),
                css_class='span3'),
            css_class='row'),
    )
    helper.layout.append(
        FormActions(
            HTML(
                "<a href='{% url 'social_articles' %}' "
                "class='btn'>Cancel</a>"
            ),
            Submit('save', 'Save & Continue')
        )
    )

    class Meta:
        model = Comment

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
