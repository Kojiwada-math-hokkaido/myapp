## Globally coupled map の時系列データを生成 & 確率分布を生成

### 仕様技術
<img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
### 使用時のインポート
~~~
import myapp
~~~
### コマンド一覧
| コマンド   | 引数     |処理               |
|------------|----------|--------------------|
|series      |alpha, e, initial, length trans_period|設定したパラメータに対応するGCMの時系列を生成|
|product_label|y_min, y_max, num_label|確率分布の最小・最大値をそれぞれy_min, y_maxとしてnum_label等分の確率分布のラベルを作成|
|save_csv_file|x_list, y_list|リストをcsvファイルに保存|

### 使用例
~~~
x_list, y_list = myapp.series(alpha, e, initial, length, trans_period)
~~~
~~~
dif_label = myapp.product_label(y_min, y_max, num_label)
~~~
~~~
myapp.save_csv_file(x_list, y_list)
~~~
