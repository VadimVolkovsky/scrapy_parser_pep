import csv
from datetime import datetime
from collections import defaultdict

from pep_parse.settings import (BASE_DIR, DT_FORMAT, QTY, RESULTS, STATUS,
                                STATUS_SUMMARY, TOTAL)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """При запуске паука создается словарь со статусами PEP"""
        self.pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        """В процессе переборки item добавляем статусы pep в словарь,
          и считаем их количество"""
        self.pep_statuses[item.get(STATUS)] += 1
        return item

    def close_spider(self, spider):
        """При закрытии паука задаем формат вывод данных,
        и сохраняем результаты в CSV файл"""
        date_time_now = datetime.now().strftime(DT_FORMAT)
        filename = f'{STATUS_SUMMARY}_{date_time_now}.csv'
        with open(
            f'{self.results_dir}/{filename}', 'w', newline=''
        ) as csvfile:
            fieldnames = [STATUS, QTY]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            total_qty = sum(self.pep_statuses.values())
            writer.writeheader()
            for status, qty in self.pep_statuses.items():
                writer.writerow({STATUS: status, QTY: qty})
            writer.writerow({STATUS: TOTAL, QTY: total_qty})
