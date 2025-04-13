[](dig.md)
# dig
`dig`（Domain Information Groper）は、DNSに問い合わせてドメインに関する情報（Aレコード、MXレコード、NSレコードなど）を取得するコマンド。トラブルシューティングやドメイン情報の確認に広く利用される。

  実行例 [](変更しない)

  ```
  dig example.com
  ```

  実行結果 [](変更しない)

  ```
  ; <<>> DiG 9.16.1-Ubuntu <<>> example.com
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

  ;; QUESTION SECTION:
  ;example.com.			IN	A

  ;; ANSWER SECTION:
  example.com.		1234	IN	A	93.184.216.34

  ;; Query time: 20 msec
  ;; SERVER: 8.8.8.8#53(8.8.8.8)
  ;; WHEN: Sat Apr 13 20:00:00 JST 2024
  ;; MSG SIZE  rcvd: 56
  ```

### オプション一覧

- **+short**

  出力を簡潔にしてIPアドレスなどの主要な情報だけを表示する。

  実行例 [](変更しない)

  ```
  dig +short example.com
  ```

  実行結果 [](変更しない)

  ```
  93.184.216.34
  ```

- **@DNSサーバ**

  特定のDNSサーバを指定して問い合わせる。

  実行例 [](変更しない)

  ```
  dig @8.8.8.8 example.com
  ```

  実行結果 [](変更しない)

  ```
  （GoogleのDNSサーバに問い合わせた結果が表示される）
  ```

- **-x [IPアドレス]**

  IPアドレスからドメイン名を逆引きする。

  実行例 [](変更しない)

  ```
  dig -x 8.8.8.8
  ```

  実行結果 [](変更しない)

  ```
  8.8.8.8.in-addr.arpa. 21599 IN PTR dns.google.
  ```

- **ANY**

  すべてのレコードタイプ（A, AAAA, MX, TXTなど）を一度に取得する。

  実行例 [](変更しない)

  ```
  dig example.com ANY
  ```

  実行結果 [](変更しない)

  ```
  （A, NS, MX, TXTなど多数のレコードが表示される）
  ```