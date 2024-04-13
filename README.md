## Globally coupled map の時系列データを生成 & csvファイルとして保存

### 仕様技術
<img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">

### コマンド一覧
| コマンド   | 引数     |処理               |
|------------|----------|--------------------|
|series      |alpha, e, initial, length trans_period|設定したパラメータに対応するGCMの時系列を生成|
|save_csv_file|x_list, y_list|リストをcsvファイルに保存|

### 使用例
~~~
x_list, y_list = myapp.series(alpha, e, initial, length, trans_period)
~~~

~~~
myapp.save_csv_file(x_list, y_list)
~~~
