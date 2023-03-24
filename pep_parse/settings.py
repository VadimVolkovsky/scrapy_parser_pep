
from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


ROBOTSTXT_OBEY = True
BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS
NUMBER = 'number'
NAME = 'name'
STATUS = 'status'
QTY = 'qty'
STATUS_SUMMARY = 'status_summary'
TOTAL = 'Total'
DT_FORMAT = "%Y-%m-%d_%H-%M-%S"

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': [NUMBER, NAME, STATUS],
        'overwrite': True,
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
