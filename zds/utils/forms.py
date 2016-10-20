# coding: utf-8
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout, ButtonHolder, Field, Div, HTML

from zds.utils.misc import contains_utf8mb4
from zds.utils.models import Tag


class CommonLayoutEditor(Layout):

    def __init__(self, *args, **kwargs):
        super(CommonLayoutEditor, self).__init__(
            Field('text', css_class='md-editor'),
            HTML("<div class='message-bottom'>"),
            HTML("<div class='message-submit'>"),
            StrictButton(
                _(u'Envoyer'),
                type='submit',
                name='answer'),
            StrictButton(
                _(u'Aperçu'),
                type='submit',
                name='preview',
                css_class='btn-grey',
                data_ajax_input='preview-message'),
            HTML("</div>"),
            HTML("</div>"),
            *args, **kwargs
        )


class CommonLayoutVersionEditor(Layout):

    def __init__(self, *args, **kwargs):
        super(CommonLayoutVersionEditor, self).__init__(
            Div(
                Field('text', css_class='md-editor'),
                Field('msg_commit'),
                ButtonHolder(
                    StrictButton(
                        _(u'Envoyer'),
                        type='submit',
                        name='answer'),
                    StrictButton(
                        _(u'Aperçu'),
                        type='submit',
                        name='preview',
                        css_class='btn-grey'),
                ),
            ),
            *args, **kwargs
        )


class CommonLayoutModalText(Layout):

    def __init__(self, *args, **kwargs):
        super(CommonLayoutModalText, self).__init__(
            Field('text'),
            *args, **kwargs
        )


class TagValidator(object):
    """
    validate tags
    """

    @staticmethod
    def validate_raw_string(raw_string):
        tags_list = raw_string.split(',')
        length_error = TagValidator.validate_length(tags_list)
        if not length_error:
            return length_error

        content_error = TagValidator.validate_content(tags_list)
        if not content_error:
            return content_error

        return True

    @staticmethod
    def validate_content(tags_list):
        with_utf8mb4_tags = filter(lambda tag: contains_utf8mb4(tag), tags_list)
        if with_utf8mb4_tags:
            if len(with_utf8mb4_tags) == 1:
                return _(u'Vous avez entré un tag utf8mb4 : "{}"'.format(with_utf8mb4_tags[0]))
            else:
                return _(u'Certains tags sont utf8mb4 : "{}"'.format(with_utf8mb4_tags.join('", "')))
        return True

    @staticmethod
    def validate_length(tags_list):
        msg = ''
        too_long = [tag for tag in tags_list if len(tag) > Tag._meta.get_field("title").max_length]
        if too_long:
            if len(too_long) == 1:
                msg = _(u'Vous avez entré un tag trop long : "{}"'.format(too_long[0]))
            else:
                msg = _(u'Certains tags sont trop longs : "{}"'.format(too_long.join('", "')))
        if msg:
            return msg
        return True
