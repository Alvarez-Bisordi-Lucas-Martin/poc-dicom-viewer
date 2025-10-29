import base64

from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import TemplateView


def home(_):
    return redirect('viewer_v2')


class ViewerV1TemplateView(TemplateView):
    template_name = 'viewer_v1.html'


class ViewerV2TemplateView(TemplateView):
    template_name = 'viewer_v2.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        dicom_path = settings.BASE_DIR.parent / 'inputs' / 'dicom_v1.dcm'

        with open(dicom_path, 'rb') as file:
            ctx['dicom_base64'] = base64.b64encode(file.read()).decode('utf-8')

        return ctx
