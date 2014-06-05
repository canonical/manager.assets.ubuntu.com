# System
import os

# Installed
from django.shortcuts import render
from django.http import HttpResponse
from requests.exceptions import RequestException

# Local
from lib.http_helpers import files_from_request_form
from lib.mappers import AssetMapper

assets_server_hostname = os.environ.get(
    'HTTP_SERVER_HOSTNAME',
    'localhost:8001'
)
mapper = AssetMapper(server_url="http://{0}/v1/".format(assets_server_hostname))


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


def index(request):
    query = request.GET.get('q', '')

    try:
        assets = mapper.all(query) if query else []
    except RequestException as error:
        return api_error(error)

    return render(
        request,
        'index.html',
        {
            'assets': assets,
            'query': query
        }
    )


def create(request):
    template = "create.html"
    error = ""
    message = ""
    created_assets = []
    existing_asset = {}
    tags = ''

    # Process form post
    if request.method == "POST":
        # Get files from form data
        files = files_from_request_form(request, "assets")
        tags = request.POST.get('tags')

        if files:

            # Create all files
            for asset_file in files:
                try:
                    response = mapper.create(
                        asset_file.read(), asset_file.name, tags
                    )

                    if 'code' in response and response['code'] != 200:
                        if response['code'] == 409 and 'filename' in response:
                            message = 'Asset already exists:'
                            existing_asset = mapper.get(response['filename'])
                        else:
                            # Error - pass on message
                            error = 'Error: {message}'.format(
                                message=response['message']
                            )
                    else:
                        # Success
                        created_assets.append(response)
                        template = "created.html"

                except RequestException as error:
                    api_error(error)

        else:
            error = "Please select files to upload"

    return render(
        request,
        template,
        {
            'error': error,
            'message': message,
            'assets': created_assets,
            'asset': existing_asset,
            'tags': tags
        }
    )


def update(request):
    asset = mapper.get(request.GET.get('filename'))
    template = "update.html"
    message = ""
    tags = asset['tags']

    # Process form post
    if request.method == "POST":
        # Get new tags
        tags = request.POST.get('tags')

        asset = mapper.update(asset['filename'], tags)

        template = "updated.html"

    return render(
        request,
        template,
        {
            'asset': asset,
            'message': message
        }
    )
