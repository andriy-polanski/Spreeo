from django.forms.widgets import FileInput, DateTimeInput
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.encoding import force_text
from django.template import Context
from django.template.loader import render_to_string
from django.forms.util import flatatt

class ImageInput(FileInput):
    template_name = 'dashboard/partials/image_input_widget.html'
    attrs = {'accept': 'image/*'}

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if not value or isinstance(value, InMemoryUploadedFile):
            # can't display images that aren't stored
            image_url = ''
        else:
            image_url = final_attrs['value'] = force_text(
                self._format_value(value))

        return render_to_string(self.template_name, Context({
            'input_attrs': flatatt(final_attrs),
            'image_url': image_url,
            'image_id': "%s-image" % final_attrs['id'],
        }))
