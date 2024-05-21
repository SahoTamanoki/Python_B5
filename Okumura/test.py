# int/str、指定してる？
# end、書いてる？
#import sys
#args = sys.argv

from datetime import datetime

date = "20220501"
if date.weekday(date) < 5:
    # return "平日"
    print("平日")