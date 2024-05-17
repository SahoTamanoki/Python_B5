import syaku

s2cm = syaku.syaku_to_cm
print("10尺", s2cm(10), "cm")

# モジュールを使わない方法
def syaku_to_cm(syaku):
    return round(syaku * 303.03, 3)
print(syaku(10))
