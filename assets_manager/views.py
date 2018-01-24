from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases() # noqa

# Packages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from requests.exceptions import RequestException
try:
    from urllib.parse import urljoin
except ImportError:
    from urllib.parse import urljoin
from django.contrib.auth.decorators import login_required

# Local
from .lib.http_helpers import files_from_request_form
from .mappers import AssetMapper


mapper = AssetMapper(
    server_url=urljoin(settings.SERVER_URL, 'v1/'),
    auth_token=settings.AUTH_TOKEN
)


def api_error(error):
    """
    Specific error message for when an API communication fails
    """

    return HttpResponse(
        (
            "The upstream API server is uncontactable "
            "or is not returning valid json. Details: {0}"
        ).format(error),
        status=502
    )


@login_required
def index(request):
    query = request.GET.get('q', '')
    asset_type = request.GET.get('type', '')

    try:
        assets = mapper.all(request.GET) if query else []
    except RequestException as error:
        return api_error(error)

    return render(
        request,
        'index.html',
        {
            'assets': assets,
            'query': query,
            'type': asset_type
        }
    )


@login_required
def create(request):
    template = "create.html"
    error = ""
    created_assets = []
    existing_assets = []
    tags = ''
    optimize = True

    # Process form post
    if request.method == "POST":
        # Get files from form data
        files = files_from_request_form(request, "assets")
        tags = request.POST.get('tags')
        optimize = request.POST.get('optimize')

        if files:

            # Create all files
            for asset_file in files:

                try:
                    response = mapper.create(
                        asset_file.read(), asset_file.name, tags, optimize
                    )

                    if 'code' in response and response['code'] != 200:
                        if response['code'] == 409 and 'file_path' in response:
                            asset = mapper.get(response['file_path'])
                            existing_assets.append(asset)
                        else:
                            # Error - pass on message
                            error = 'Error from server: {code}'.format(
                                code=response['code']
                            )
                    else:
                        # Success
                        created_assets.append(response)

                except RequestException as request_error:
                    error = api_error(request_error).content

            if not error:
                template = "created.html"

        else:
            error = "Please select files to upload"

    return render(
        request,
        template,
        {
            'error': error,
            'assets': created_assets,
            'existing': existing_assets,
            'tags': tags,
            'optimize': optimize
        }
    )


@login_required
def update(request):
    asset = mapper.get(request.GET.get('file-path'))
    template = "update.html"
    message = ""
    tags = asset['tags']

    # Process form post
    if request.method == "POST":
        # Get new tags
        tags = request.POST.get('tags')

        asset = mapper.update(asset['file_path'], tags)

        template = "updated.html"

    return render(
        request,
        template,
        {
            'asset': asset,
            'message': message
        }
    )


@login_required
def error_404(request):
    return HttpResponseNotFound(
        render(request, '404.html')
    )
