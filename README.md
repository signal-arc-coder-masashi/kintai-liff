# kintai-liff

LINE打刻用の静的LIFFページ（GitHub Pagesで配信）。

- これは**フロント（HTML1枚）**のみ。バックエンド（本人確認・記録・集計）は別のGAS Web Appが担う。
- **秘密情報は含めない**（チャネルシークレット／アクセストークン等はバックエンド側のスクリプトプロパティにのみ保持）。
- ここに載るのは公開前提の値だけ：LIFF ID（元々クライアントに埋め込まれる公開値）と、バックエンドの受け口URL。
- 守りはこのページの秘匿ではなく、バックエンドでの**id_token検証＋登録済みユーザー許可リスト**で担保する。

## 構成
- `index.html` … 打刻ページ。LIFF初期化 → 位置情報取得 → バックエンドへPOST。下部に「📅 当月の打刻状況を見る」リンク。
- `view.html` … 閲覧/申請ページ（`?view=board/mymonth/shinsei/fix/yukyu/contact`）。LIFF本人確認（idToken）でバックエンドのPOST APIを呼ぶ。

## デプロイ
`main` ブランチ直下を GitHub Pages で配信。

## 変更履歴

### 2026-11-05 当月の打刻状況ビュー＋打刻修正の取消/時刻変更
- **変更ファイル**: `view.html`, `index.html`
- **内容**: `?view=mymonth`（`renderMyMonth`＝本人の当月20日〆の日別 出退勤・実働・時間外・合計）を追加。導線＝`index.html` 打刻ボタン下の「📅 当月の打刻状況を見る」（相対 `./view.html?view=mymonth`・LIFF内遷移で idToken 継続）＋各種申請→照会。あわせて `?view=fix` を「対象日→本人の打刻一覧（各行に取消/時刻を直す）＋打ち忘れ追加」に再構成（`op=add/cancel/edit` を `source:fix-request` で送信）。
- **理由**: 職員が自分の当月勤務を確認でき、押し間違い（1日1回ガード下）を取消/修正で直せるようにするため。

### 2026-11-03（セキュリティ）view.html を LIFF 本人確認対応に刷新
- **変更ファイル**: `view.html`
- **内容**: 閲覧ページ（出勤簿/連絡/有給）を LIFF 対応に。`liff.init`→`getIDToken` を取得し、バックエンドへは **idToken を POST ボディで送付**（URLクエリにトークンを残さない）。未連携・無効トークンは `needAuth` 通知を表示。打刻修正は GAS フォームへの外部リンクをやめ、**氏名欄なしの LIFF 内フォーム**（申請者は idToken で自動特定）に置換。
- **理由**: バックエンドが全閲覧API/申請を「連携済職員のみ（idToken検証）」に限定したため、フロントも本人確認トークンを送る必要がある。他人名義の申請・無認証の個人情報閲覧を防ぐ。
- **前提**: LINEコンソールの LIFF Endpoint URL を Pages ルートに設定（リッチメニューは `liff.line.me/<id>/view.html?view=…` で開く）。
