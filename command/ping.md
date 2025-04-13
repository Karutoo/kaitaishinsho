[](ping.md)  
# ping  
指定したホスト（IPアドレスやドメイン）とのネットワーク接続状況を確認するコマンド。  
ICMPパケットを送信し、その応答時間（レイテンシ）やパケットの損失率などを表示することで、通信可否や回線状態を調査するのに利用される。

  実行例 [](変更しない)

  ```
  ping www.google.com
  ```

  実行結果 [](変更しない)

  ```
  PING www.google.com (142.250.199.36) 56(84) bytes of data.
  64 bytes from nrt12s42-in-f4.1e100.net (142.250.199.36): icmp_seq=1 ttl=115 time=10.6 ms
  64 bytes from nrt12s42-in-f4.1e100.net (142.250.199.36): icmp_seq=2 ttl=115 time=10.3 ms
  64 bytes from nrt12s42-in-f4.1e100.net (142.250.199.36): icmp_seq=3 ttl=115 time=10.1 ms
  64 bytes from nrt12s42-in-f4.1e100.net (142.250.199.36): icmp_seq=4 ttl=115 time=10.2 ms

  --- www.google.com ping statistics ---
  4 packets transmitted, 4 received, 0% packet loss, time 3005ms
  rtt min/avg/max/mdev = 10.144/10.323/10.636/0.190 ms
  ```

### オプション一覧

- **-c [回数]**

  指定した回数だけICMPリクエストを送信する。

  実行例 [](変更しない)

  ```
  ping -c 3 www.google.com
  ```

  実行結果 [](変更しない)

  ```
  PING www.google.com (142.250.199.36) 56(84) bytes of data.
  64 bytes from 142.250.199.36: icmp_seq=1 ttl=115 time=10.3 ms
  64 bytes from 142.250.199.36: icmp_seq=2 ttl=115 time=10.2 ms
  64 bytes from 142.250.199.36: icmp_seq=3 ttl=115 time=10.1 ms

  --- www.google.com ping statistics ---
  3 packets transmitted, 3 received, 0% packet loss, time 2004ms
  rtt min/avg/max/mdev = 10.123/10.233/10.325/0.081 ms
  ```

- **-i [秒]**

  各ICMPパケットを送る間隔を秒単位で指定する。

  実行例 [](変更しない)

  ```
  ping -i 2 www.google.com
  ```

  実行結果 [](変更しない)

  ```
  PING www.google.com (142.250.199.36) 56(84) bytes of data.
  64 bytes from 142.250.199.36: icmp_seq=1 ttl=115 time=10.3 ms
  64 bytes from 142.250.199.36: icmp_seq=2 ttl=115 time=10.2 ms
  ...
  ```

- **-t [TTL値]**

  パケットの生存時間（TTL: Time to Live）を指定する。中継できるルーターの最大数。

  実行例 [](変更しない)

  ```
  ping -t 5 www.google.com
  ```

  実行結果 [](変更しない)

  ```
  PING www.google.com (142.250.199.36) 56(84) bytes of data.
  64 bytes from 142.250.199.36: icmp_seq=1 ttl=5 time=10.3 ms
  ...
  ```

- **-q**

  サマリ情報だけを表示（静かに実行し、統計結果のみ出力）。

  実行例 [](変更しない)

  ```
  ping -c 3 -q www.google.com
  ```

  実行結果 [](変更しない)

  ```
  --- www.google.com ping statistics ---
  3 packets transmitted, 3 received, 0% packet loss, time 2001ms
  rtt min/avg/max/mdev = 10.123/10.233/10.325/0.081 ms
  ```

- **-s [バイト数]**

  ICMPパケットのデータ部分のサイズを指定。

  実行例 [](変更しない)

  ```
  ping -s 128 www.google.com
  ```

  実行結果 [](変更しない)

  ```
  PING www.google.com (142.250.199.36) 128(156) bytes of data.
  136 bytes from 142.250.199.36: icmp_seq=1 ttl=115 time=10.4 ms
  ...
  ```