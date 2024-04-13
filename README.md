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
|product_whole_label_list|dif_label, num | dif_labelに格納されている状態をnum個の時系列に対応するようにシステムすべての状態を作成する|
|product_whole_prob_matrix| dif_list, dif_label |dif_list の時系列からdif_labelをラベルとしたシステム全体の確率分布を作成 |
|cal_entropy | whole_dist | 確率分布whole_distからエントロピーを計算|
|product_sub_prob_matrix| dif_list, dif_label| dif_list の時系列からdif_labelをラベルとした部分ごとの確率分布を作成 |

### 使用例
~~~
x_list, y_list = myapp.series(alpha, e, initial, length, trans_period)
~~~
~~~
dif_label = myapp.product_label(y_min, y_max, num_label)
~~~
~~~
whole_label = myapp.product_whole_label_list(dif_label, len(dif_list[0]))
~~~
~~~
whole_dist = myapp.product_whole_prob_matrix(dif_list, dif_label)
~~~
~~~
entropy = myapp.cal_entropy(whole_dist)
~~~
~~~
sub_dist = myapp.product_sub_prob_matrix(dif_list, dif_label)
~~~
