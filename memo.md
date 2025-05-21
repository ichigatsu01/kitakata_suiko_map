# 各ファイルの内容
手書きでjsonファイルを埋めていくので、各項目にどういう内容を入れていくかをここで決める。    
主にwebで調べていくが、もし見つからなさそうなら英語表記や中華サイトを探しに行く方法もある。 
追加順序は基本的に、作品で舞台になった順番とする。

## prefecture.json
- name_Song  
宋代の州名。    
- name_modern   
現代中国でどのあたりに位置しているか。  
- lat   
緯度(Latitude)。地図でいう上下。なお緯度・経度は当時の州都がどこに設置されていたかで判断する。    
- lon   
経度(Longitude)。地図でいう左右。   
- description   
その州について補足があれば入力。

## foliumの設定
- 州名、または官軍の拠点：青
- 拠点名：赤

## その他メモ
二竜山、桃花山、清風山の位置は現実と小説でズレてる可能性が高い。
一旦ブラウジングで確認できたものを記載しつつ、最終的には北方水滸伝ベースに直す必要がありそう。

## 作成経緯
マーカーを強調するためにleaflet.jsの導入を検討した。    
ただ、強調するだけならselectbox&if文でマップを再レンダリングすることで対処可能と分かったため、  
Streamlitのみでの対処とした。


# foliumの使い方について ... sandbox.ipynbでまとめたものを転記
## icon(https://python-visualization.github.io/folium/latest/reference.html)：
### 要約
デフォルトでは[glyphicon for bootstrap 3](https://getbootstrap.com/docs/3.3/components/)が適用されており、これらの中からicon名を設定する。   
ただし使えないものもあるようで、使えるかどうかは実際に試さないとわからなさそう。    
prefixで'fa'を指定するとfont-awesomeを使えるようになる。

### 使える色
[‘red’, ‘blue’, ‘green’, ‘purple’, ‘orange’, ‘darkred’,     
’lightred’, ‘beige’, ‘darkblue’, ‘darkgreen’, ‘cadetblue’, ‘darkpurple’,    
‘white’, ‘pink’, ‘lightblue’, ‘lightgreen’, ‘gray’, ‘black’, ‘lightgray’]

### 原文(抜粋)
- icon (str, default 'info-sign')
The name of the marker sign. See Font-Awesome website to choose yours. Warning : depending on the icon you choose you may need to adapt the prefix as well.

- prefix (str, default 'glyphicon')
The prefix states the source of the icon. ‘fa’ for font-awesome or ‘glyphicon’ for bootstrap 3.