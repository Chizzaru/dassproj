from django import forms
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode

class SelectWithTitles(forms.Select):
    def __init__(self, *args, **kwargs):
        super(SelectWithTitles, self).__init__(*args, **kwargs)
        # Ensure the titles dict exists
        self.titles = {}

    def render_option(self, selected_choices, option_value, option_label):
        title_html = (option_label in self.titles) and \
            u' title="%s" ' % escape(force_unicode(self.titles[option_label])) or ''
        option_value = force_unicode(option_value)
        selected_html = (option_value in selected_choices) and u' selected="selected"' or ''
        return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), title_html, selected_html,
            conditional_escape(force_unicode(option_label)))

class ChoiceFieldWithTitles(forms.ChoiceField):
    widget = SelectWithTitles

    def __init__(self, choices=(), *args, **kwargs):
        choice_pairs = [(c[0], c[1]) for c in choices]
        super(ChoiceFieldWithTitles, self).__init__(choices=choice_pairs, *args, **kwargs)
        self.widget.titles = dict([(c[1], c[2]) for c in choices])