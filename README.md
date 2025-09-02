## License
This project includes content from [Dhole/weather-pixel-icons](https://github.com/Dhole/weather-pixel-icons), which is licensed under CC BY-SA 4.0.

## 説明
waveshare, e-paper7.5inch Bの描画をするREST APIサーバです。

クライアントはAPIを叩き送られてくるバイナリデータを描画します。
いわゆるシンクライアントってやつです。

もともとpicoで作っていてメモリが足りなくなったのでシンクライアントにしたのですが、シンクライアントでもメモリが足りなくなりました。

今はラズパイ3のモデルBを使ってます。現状シンクライアントにする必要はないのですが、とりあえずこれで作ってます。

クライアントのリポジトリ
https://github.com/mitsuiJao/e-paper-client


## 使い方
### 事前に
GoogleカレンダーAPIからイベントを取得しているので、GCPからその有効化。また、サービスアカウントを作成し、認証情報がかかれたJSONを同じディレクトリに配置します。

またそのJSONのファイル名を`secret.py`に記述します。詳しくは[google_calendar.py](https://github.com/mitsuiJao/e-paper-server/blob/main/google_calendar.py)のソースコードを直接見てみてください。

### サーバは
python仮想環境を適当に立ててください。

次のコマンドを実行
```shell
uvicorn main:app
```

--portオプションでポート番号を指定できます。デフォルトは8000です。

あとはuvicornの説明でも参照してください。

### あとは
systemdに登録して起動時に自動実行してもらえばいいと思います！

世界一わかりにくいREADME終わり