additions = [
    # start above 200k for pynab regex
    {
        'id': 200000,
        'group_name': '.*',
        'regex': '/^trtk\d{4,8} - \[\d{1,5}\/\d{1,5}\] - "(?P<name>.+?)\.(?:nzb|vol\d+(?:\+\d+){1,}?\.par2|part\d+\.rar|par2|r\d{1,})" yEnc/i',
        'ordinal': 1,
        'status': True,
        'description': 'music releases'
    }
]

replacements = {
    '677': {
        'id': 677,
        'regex': '/^.*?\"(?P<name>.*?)\.(pdb|htm|prc|lit|epub|lrf|txt|pdf|rtf|doc|chf|chn|mobi|chm|doc|par|rar|sfv|nfo|nzb|srt|ass|txt|zip|ssa|r\d{1,3}|7z|tar|idx|t\d{1,2}|u\d{1,3})/i',
        'status': True,
        'ordinal': 9,
        'group_name': 'alt.binaries.e-book.flood'
    },
    '678': {
        'id': 678,
        'regex': '/^.*?\"(?P<name>.*?)\.(pdb|htm|prc|lit|epub|lrf|txt|pdf|rtf|doc|chf|chn|mobi|chm|doc|par|rar|sfv|nfo|nzb|srt|ass|txt|zip|ssa|r\d{1,3}|7z|tar|idx|t\d{1,2}|u\d{1,3})/i',
        'status': True,
        'ordinal': 9,
        'group_name': 'alt.binaries.e-book'
    },
    '679': {
        'id': 679,
        'regex': '/^.*?\"(?P<name>.*?)\.(pdb|htm|prc|lit|epub|lrf|txt|pdf|rtf|doc|chf|chn|mobi|chm|doc|par|rar|sfv|nfo|nzb|srt|ass|txt|zip|ssa|r\d{1,3}|7z|tar|idx|t\d{1,2}|u\d{1,3})/i',
        'status': True,
        'ordinal': 9,
        'group_name': 'alt.binaries.ebook'
    },
    '680': {
        'id': 680,
        'regex': '/^.*?\"(?P<name>.*?)\.(pdb|htm|prc|lit|epub|lrf|txt|pdf|rtf|doc|chf|chn|mobi|chm|doc|par|rar|sfv|nfo|nzb|srt|ass|txt|zip|ssa|r\d{1,3}|7z|tar|idx|t\d{1,2}|u\d{1,3})/i',
        'status': True,
        'ordinal': 9,
        'group_name': 'alt.binaries.e-book.technical'
    },
    '682': {
        'id': 682,
        'regex': '/^.*?\"(?P<name>.*?)\.(pdb|htm|prc|lit|epub|lrf|txt|pdf|rtf|doc|chf|chn|mobi|chm|doc|par|rar|sfv|nfo|nzb|srt|ass|txt|zip|ssa|r\d{1,3}|7z|tar|idx|t\d{1,2}|u\d{1,3})/i',
        'status': False,
        'ordinal': 9,
        'group_name': 'alt.binaries.ebook.flood'
    },
}