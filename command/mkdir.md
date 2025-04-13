[](mkdir.md)
# mkdir
新しいディレクトリを作成するコマンド。指定した名前で空のディレクトリを作成し、既に同名のファイルやディレクトリが存在する場合はエラーとなる。複数のディレクトリを一度に作成したり、親ディレクトリを再帰的に作成するオプションも存在する。

  実行例 [](変更しない)

  ```
  mkdir myfolder
  ```

  実行結果 [](変更しない)

  ```
  user@localhost:~$ ls
  myfolder
  ```

### オプション一覧

- **-p**

  存在しない親ディレクトリも含めて再帰的にディレクトリを作成する。

  実行例 [](変更しない)

  ```
  mkdir -p parent/child/grandchild
  ```

  実行結果 [](変更しない)

  ```
  user@localhost:~$ tree
  .
  └── parent
      └── child
          └── grandchild
  ```

- **-v**

  作成したディレクトリ名を出力する。作成の進行状況を確認するのに便利。

  実行例 [](変更しない)

  ```
  mkdir -v newdir
  ```

  実行結果 [](変更しない)

  ```
  mkdir: ディレクトリ 'newdir' を作成しました
  ```

- **--mode=MODE**

  作成するディレクトリのパーミッションを指定する。MODEは `chmod` と同じ形式で指定可能。

  実行例 [](変更しない)

  ```
  mkdir --mode=700 secret_folder
  ```

  実行結果 [](変更しない)

  ```
  user@localhost:~$ ls -ld secret_folder
  drwx------ 2 user user 4096 Apr 13 14:33 secret_folder
  ```