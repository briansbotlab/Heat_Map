# Heat_Map
在進行資料的分析時，利用Heat Map可以快速了解每個資料特徵兩兩之間的關係。<br/>

### 使用前請先確認環境有安裝好相關套件。

  
## 使用方法:
1. 修改下列程式碼，將<code>'file_path'</code>更改成你想要進行Heat Map的資料的路徑。
<pre>
<code>
 #讀取資料
 raw_csv = pd.read_csv('file_path')
</code>
</pre>
2. 執行hmap.py，會得到Heat Map以及output.csv，以便在資料特徵過多，導致無法清晰顯示圖像之際，能夠利用csv來一覽資料間的關係。<br/>
