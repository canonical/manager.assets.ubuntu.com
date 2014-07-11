import requests
import mimetypes
from urlparse import urljoin
from base64 import b64encode


class AssetMapper:
    """
    Map data from the Assets API into model objects
    """

    server_url = ""
    image_types = ["image/png", "image/jpeg", "image/svg+xml", "image/gif"]

    def __init__(self, server_url):
        self.server_url = server_url

    def get(self, filename):
        asset_data_url = urljoin(self.server_url, '{0}.json'.format(filename))

        return self.format_asset(
            requests.get(asset_data_url).json()
        )

    def all(self, search=''):
        url = self.server_url

        # Search, if requested
        if search:
            url += '?q={0}'.format(search)

        return self.format_assets(requests.get(url).json())

    def create(self, asset_content, filename, tags):
        api_response = requests.post(
            self.server_url,
            data={
                'asset': b64encode(asset_content),
                'filename': filename,
                'tags': tags,
                'type': 'base64'
            }
        )

        response = api_response.json()

        if api_response.status_code < 300:
            response = self.format_asset(response)

        return response

    def update(self, filename, tags):
        asset_url = urljoin(self.server_url, filename)

        api_response = requests.put(
            asset_url,
            data={
                'tags': tags
            }
        )

        return self.format_asset(api_response.json())

    def format_assets(self, data):
        formatted_data = []

        for datum in data:
            formatted_data.append(self.format_asset(datum))

        return formatted_data

    def format_asset(self, datum):
        mimetype = mimetypes.guess_type(datum["filename"])[0]

        return {
            "filename": datum["filename"],
            "tags": datum["tags"],
            "url": urljoin(self.server_url, datum["filename"]),
            "image": mimetype in self.image_types,
            "created": datum["created"]
        }
