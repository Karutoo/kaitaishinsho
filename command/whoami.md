[](whoami.md)
# whoami
現在ログイン中のユーザー名を表示するコマンド。スクリプトや複数ユーザーが関わるシステムで、「今の操作主体が誰か」を確認する際に用いられる。

  実行例 [](変更しない)

  ```
  whoami
  ```

  実行結果 [](変更しない)

  ```
  admin
  ```

  上記のように、現在ログイン中のユーザー名（Linuxでのアカウント名など）が表示される。

---

### オプション一覧

`whoami` コマンド自体はシンプルで、ほとんどの環境でオプションを必要としない。ただし、以下のような関連コマンドや組み合わせで使うことも多い。

---

- **sudoと組み合わせて使用**

  `sudo`で管理者権限になった際、自分が誰として認識されているかを確認するために使える。

  実行例 [](変更しない)

  ```
  sudo whoami
  ```

  実行結果 [](変更しない)

  ```
  root
  ```

  通常ユーザーが`sudo`で実行することで、現在の権限が「root」であることを確認できる。

---

- **ログイン名との違い（`logname`との比較）**

  `whoami`は「現在の実効ユーザー名」、`logname`は「ログイン時のユーザー名」。

  実行例 [](変更しない)

  ```
  logname
  ```

  実行結果 [](変更しない)

  ```
  user123
  ```

  `sudo`などで切り替えていても、`logname`は元のユーザー、`whoami`は現在のユーザーを示す。

---

このコマンドはトラブルシューティングや権限の検証、スクリプト中での条件分岐などにも使われる。