# coding: utf-8

from django.forms import widgets
from django.forms.util import flatatt
from django.utils.encoding import smart_str
from django.utils.safestring import mark_safe

from accounts.geo.models import City


class CityChoiceWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        self.choices = [("1", "Not Selected")] if self.form_instance.instance.country.id != 1 else []

        # if value is None:
        if value == 1:
            # if no city has been previously selected,
            # render either an empty list or, if a country has
            # been selected, render its cities
            value = ''
            model_obj = self.form_instance.instance
            if model_obj and model_obj.country:
                for m in model_obj.country.city_set.all():
                    self.choices.append((m.id, smart_str(m)))
        else:
            # if a city X has been selected,
            # render only these cities, that belong
            # to X's country
            obj = City.objects.get(id=value)
            for m in City.objects.filter(country=obj.country):
                self.choices.append((m.id, smart_str(m)))

        # copy-paste from widgets.Select.render
        final_attrs = self.build_attrs(attrs, name=name)
        output = ['<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe(u'\n'.join(output))