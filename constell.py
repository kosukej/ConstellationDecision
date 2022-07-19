import enum
from datetime import date

# 閏年に対応させるため閏年を指定
default_year = 2004


# 星座の列挙
class ConstellationType(enum.Enum):
    CAPRICORN2 = ("♑山羊座", date(default_year, 1, 1), date(default_year, 1, 19))
    AQUARIUS = ("♒水瓶座", date(default_year, 1, 20), date(default_year, 2, 18))
    PISCES = ("♓魚座", date(default_year, 2, 19), date(default_year, 3, 20))
    ARIES = ("♈牡羊座", date(default_year, 3, 21), date(default_year, 4, 19))
    TAURUS = ("♉牡牛座", date(default_year, 4, 20), date(default_year, 5, 20))
    GEMINI = ("♊双子座", date(default_year, 5, 21), date(default_year, 6, 21))
    CANCER = ("♋蟹座", date(default_year, 6, 22), date(default_year, 7, 22))
    LEO = ("♌獅子座", date(default_year, 7, 23), date(default_year, 8, 22))
    VIRGO = ("♍乙女座", date(default_year, 8, 23), date(default_year, 9, 22))
    LIBRA = ("♎天秤座", date(default_year, 9, 23), date(default_year, 10, 22))
    SCORPIO = ("♏蠍座", date(default_year, 10, 23), date(default_year, 11, 21))
    SAGITTARIUS = ("♐射手座", date(default_year, 11, 22), date(default_year, 12, 21))
    CAPRICORN = ("♑山羊座", date(default_year, 12, 22), date(default_year, 12, 31))

    # 星座の列挙型のコンストラクタ(要素の変数化)
    def __init__(self, jp_name: str, start_date: date, end_date: date):
        self.jp_name = jp_name
        self.start_date = start_date
        self.end_date = end_date


# 引数で指定された日付がどの星座に属するかの日本語名を返答する関数
def get_constellation(day: date):
    # 星座の列挙型の要素を取得
    for constellation in ConstellationType:
        # 星座の列挙型の要素のstart_dateとend_dateの間にdayがあるか確認
        if constellation.start_date <= day <= constellation.end_date:
            # 星座の列挙型の要素のjp_nameを返答
            return constellation.jp_name
