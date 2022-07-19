import datetime
import tkinter
from functools import partial
from tkinter import ttk

import constell


# メインウィンドウのOKボタンを押下した時呼び出されるメソッド
def accept_action(month: ttk.Combobox, day: ttk.Combobox):
    # 選択された値が正しいかどうかのチェック
    try:
        input_birth = datetime.date(2004, int(month.get()), int(day.get()))
    except ValueError:
        # 日付が不正な場合はエラーモーダルウィンドウとコンソールメッセージ表示
        print("ValueError: accept_action()")
        create_modal_dialog("エラー", "正しい値を入力してください")
        return
    # 取得した星座の情報を整形して表示
    result = constell.get_constellation(input_birth)
    formatted_date = (month.get() + "月" + day.get() + "日")
    create_modal_dialog("結果", (formatted_date + "の星座は" + result + "です"))


# メインウィンドウの作成メソッド
def create_main_window(title: str):
    # ウィンドウの初期化
    win = tkinter.Tk()
    win.title(title)
    win.geometry("300x120")
    win.resizable(width=False, height=False)
    win_frm = ttk.Frame(win)
    win_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=20, pady=20)

    # ウィンドウ上の要素を定義
    birth_label = ttk.Label(win_frm, text="誕生日を入力")
    year_range = list(range(1, 13))
    birth_month_set = ttk.Combobox(win_frm, values=year_range, width=5)
    birth_month_set.current(0)
    month_label = ttk.Label(win_frm, text="月")
    birth_day_set = ttk.Combobox(win_frm, values=list(range(1, 32)), width=5)
    day_label = ttk.Label(win_frm, text="日")
    accept_btn = ttk.Button(win_frm, text="OK", command=partial(accept_action, birth_month_set, birth_day_set))
    cancel_btn = ttk.Button(win_frm, text="キャンセル", command=win.quit)

    # 要素の配置
    birth_label.grid(column=0, row=0)
    birth_month_set.grid(column=1, row=0)
    month_label.grid(column=1, row=0)
    birth_day_set.grid(column=2, row=0)
    day_label.grid(column=2, row=0)

    accept_btn.grid(column=1, row=3)
    cancel_btn.grid(column=2, row=3)

    # ウィンドウの表示
    win.mainloop()


# モーダルウィンドウの作成メソッド
def create_modal_dialog(title: str, text: str):
    # ウィンドウの初期化
    modal = tkinter.Toplevel()
    modal.resizable(width=False, height=False)
    modal.title(title)
    modal.geometry("300x50")
    # ウィンドウをモーダル化
    modal.grab_set()
    modal.focus_set()

    # ウィンドウ上の要素を定義
    text_label = ttk.Label(modal, text=text)
    close_button = ttk.Button(modal, text="閉じる", command=modal.destroy)

    # 要素の配置
    text_label.pack(anchor='center', expand=1)
    close_button.pack(side='bottom', expand=1)
