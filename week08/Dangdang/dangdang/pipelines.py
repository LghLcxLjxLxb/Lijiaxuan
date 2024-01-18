import csv
from itemadapter import ItemAdapter


class DangdangPipeline:
    def process_item(self, item, spider):
        with open('dangdang.csv', 'a', newline="") as csvfile:
            fieldnames = ['author', 'now_price',
                          'title', 'short_title', 'pre_price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # 如果文件是空的，写入header
            if csvfile.tell() == 0:
                writer.writeheader()

            # print('hibegin')
            # print(item)
            # print('hiend')
            writer.writerow(item)
        return item