from datetime import date
from holiday import insert_holiday
from tables import Holiday

HOLDAYS = {
    date(2024, 1, 1): "元日",
    date(2024, 1, 8): "成人の日",
    date(2024, 2, 11): "建国記念日",
    date(2024, 2, 12): "休日",
    date(2024, 2, 23): "天皇誕生日",
    date(2024, 3, 20): "春分の日",
    date(2024, 4, 29): "昭和の日",
    date(2024, 5, 3): "憲法記念日",
    date(2024, 5, 4): "みどりの日",
    date(2024, 5, 5): "こどもの日",
    date(2024, 5, 6): "休日",
    date(2024, 7, 15): "海の日",
    date(2024, 8, 11): "山の日",
    date(2024, 8, 12): "休日",
    date(2024, 9, 16): "敬老の日",
    date(2024, 9, 22): "秋分の日",
    date(2024, 9, 23): "休日",
    date(2024, 10, 14): "スポーツの日",
    date(2024, 11, 3): "文化の日",
    date(2024, 11, 4): "休日",
    date(2024, 11, 23): "勤労感謝の日",
}

for k, v in HOLDAYS.items():
    insert_holiday(Holiday(holi_date=k, holi_text=v))
