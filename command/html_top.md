# HTML
HTML（HyperText Markup Language）は、ウェブページを作成するための標準的なマークアップ言語である。HTMLは、テキストベースの文書を構造化し、コンテンツを表示するための<b>タグ</b>を使用する。
タグは< hoge >から< /hoge >までを一つのブロックと見なす。
<b>そのため大文字/小文字の区別や空白や改行も無視される</b>。

(2024/05/13 追記：授業内で小文字推奨と案内されたため、こちらの方でも小文字表記に統一した。)

記述例 [](変更しない)

```
<!-- saved from url=(0035)http://api.fml.org/dist/lsform.html -->
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head>
  <body>
  <p>SHOPPING CART</p>
    <form method="POST" action="http://api.fml.org/api/lsform/v1">
      <p>item-01<input name="item-01" type="text"></p>
      <p>item-02<input name="item-02" type="text"></p>
      <p>item-03<input name="item-03" type="text"></p>
      <p><input type="submit" value="buy"></p>
    </form>
  </body>
</html>
```

表示結果　[](変更しない)

![](../goto/html_top.png)

### タグ一覧

<font size="5">
  <a href="b"><B>b</B></a>
</font>太文字
<font size="5">
  <a href="body"><B>body</B></a>
</font>メインコンテンツ
<font size="5">
  <a href="form"><B>form</B></a>
</font>情報を送ることができる
<font size="5">
  <a href="h"><B>h</B></a>
</font>見出し
<font size="5">
  <a href="head"><B>head</B></a>
</font>ヘッダー情報
<font size="5">
  <a href="html"><B>html</B></a>
</font>HTML文と指定する
<font size="5">
  <a href="p"><B>p</B></a>
</font>一つの段落、文章
