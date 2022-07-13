# 誕生日を入力して、星座を判定するプログラムを作成してください。
# 基本的なプログラムができて3C(60点)平均点です。
# 提出方式はzipファイルのみです。
from datetime import date

import constell


def main():
    while True:
        print("星座を判定するプログラムです。")
        print("誕生日を入力してください。")
        month = int(input("月："))
        day = int(input("日："))
        try:
            birth_day = date(2004, month, day)
        except ValueError:
            print("正しい日付を入力してください")
            continue
        print("あなたの誕生日を" + str(birth_day.month) + "月" + str(birth_day.day) + "日として登録しました。")
        print("あなたの星座は" + get_constellation(birth_day) + "です。")
        break


def get_constellation(date: date):
    for constellation in constell.ConstellationType:
        if constellation.start_date <= date <= constellation.end_date:
            return constellation.jp_name


main()
