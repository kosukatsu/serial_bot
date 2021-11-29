# serial_bot
シリアル通信で受信した内容をslackに投稿するボット
## 使い方
1. Incoming Webhook URLを取得する．
[（Slack での Incoming Webhook の利用）](https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-%E3%81%A7%E3%81%AE-Incoming-Webhook-%E3%81%AE%E5%88%A9%E7%94%A8)
2. シリアル通信のポートを確認する．
3. `defaults.yml`内の`web_hook_url`と`serial_port`を変更する．
4. `python serial_bot.py defaults.yml`
