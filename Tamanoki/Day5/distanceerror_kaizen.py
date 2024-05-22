import sys
args = sys.argv

#引数を変数に代入
station_from = args[1]
station_to = args[2]

#駅名と東京駅からの距離を辞書型にする
from_station_to_distance = { "東京":0.00, "品川":6.78, "新横浜":25.54,
             "名古屋":342.02, "京都":476.31, "新大阪":515.35 }

#のぞみ停車駅以外を入力した場合の例外処理

#行いたい処理内容
try:
    #引数で指定した駅の東京からの距離を取得し、駅と駅の距離の差を計算
    distance = from_station_to_distance[station_from]
    - from_station_to_distance[station_to]

    #絶対値で計算する
    distance = abs(distance)

    #小数点2位まで出力する
    print(round(distance,2))

#エラーが起きた場合の処理
except:
    print("のぞみの停車駅を引数に設定してください")