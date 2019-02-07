from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()  # noqa


def files_from_request_form(request, key):
    """
    Given a request containing files submitted
    through an HTML5 form containing multiple files
    (with name "<key>" - e.g.: <input type="file" name="key" multiple>)
    extract said files and return them as a list
    """

    selected_files = []

    if request.FILES:
        file_lists = request.FILES.lists()

        selected_list = [
            file_list
            for file_list in file_lists
            if file_list[0] == key and len(file_list[1]) and file_list[1][0]
        ]

        if len(selected_list):
            selected_files = selected_list[0][1]

    return selected_files
