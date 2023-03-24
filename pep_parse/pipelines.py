import csv
from datetime import datetime

from pep_parse.settings import (DT_FORMAT, QTY, RESULTS, STATUS,
                                STATUS_SUMMARY, TOTAL)


class PepParsePipeline:
    def __init__(self):
        self.status_dict = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item[STATUS]
        if status in self.status_dict:
            self.status_dict[status] += 1
        else:
            self.status_dict[status] = 1
        return item

    def close_spider(self, spider):
        date_time_now = datetime.now().strftime(DT_FORMAT)
        filename = f'{STATUS_SUMMARY}_{date_time_now}.csv'
        with open(f'{RESULTS}/{filename}', 'w', newline='') as csvfile:
            fieldnames = [STATUS, QTY]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            total_qty = sum(self.status_dict.values())
            writer.writeheader()
            for status, qty in self.status_dict.items():
                writer.writerow({STATUS: status, QTY: qty})
            writer.writerow({STATUS: TOTAL, QTY: total_qty})
