from ..compat import str

import re

ALEXA_MAPS = {
    'meta': {
        'generic': {
            'pattern': re.compile(r"^(description|keywords|title)", re.I),
            'map': {
                'description': 'description',
                'keywords': 'keywords',
                'title': 'title',
            },
            'image_key': '',
            'video_key': '',
            'key': 'name',
        },
    },
    'link': {
        'country': {
           'pattern': re.compile("/topsites/countries/"),
           'key': 'href',
           "another_key": "title",
           "another_pattern": re.compile(".+"),
        },
        'ranking': {
           'pattern': re.compile("/siteowners/certify\\?ax_atid"),
           'key': "href",
           # 'type': str('favicon'),
        },
    },
}