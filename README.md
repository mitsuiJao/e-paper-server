## 説明
waveshare, e-paper7.5inch Bの描画をするREST APIサーバです。

クライアントはAPIを叩き送られてくるバイナリデータを描画します。
いわゆるシンクライアントってやつです。

クライアントのリポジトリ
https://github.com/mitsuiJao/e-paper-client


## 使い方
python仮想環境を適当に立ててください。

次のコマンドを実行
```shell
uvicorn main:app --reload
```

--portオプションでポート番号を指定できます。デフォルトは8000です。

あとはuvicornの説明でも参照してください。