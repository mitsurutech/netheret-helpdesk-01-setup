# Netheretヘルプデスク ステップ01：セットアップ

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

授業のための作例です。16のステップで、小さな会社のITを支える架空の会社Netheretのために、ヘルプデスクのWebアプリを作っていきます。 このステップでは、プロジェクトを始めます。Flaskアプリ、仮想環境、Git、フォルダ構成を用意します。

## このステップで加わるもの

- `requirements.txt`：アプリが使う2つのライブラリです。全員が同じものを入れられるよう、
  バージョンを固定しています。
- `helpdesk/__init__.py`：アプリを組み立てる関数 `create_app()`。
- `helpdesk/main.py`：ブループリントの中に、ページが1つだけ（トップページ）あります。
- `.gitignore`：Gitで追跡しないファイル（仮想環境、Pythonのキャッシュ、
  のちにはデータベース）。

## 動かしてみる

Python 3.10以降が必要です。

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

http://127.0.0.1:5000 を開くと、「The app is running.」と表示されるはずです。
`--debug` を付けると、ファイルを保存したときにアプリが再読み込みされます。本番のサーバーでは決して使わないでください。

## フォルダ構成

```
requirements.txt     the libraries to install
helpdesk/            the app itself (a Python package)
  __init__.py        create_app()
  main.py            general pages
```

このあとのステップで、HTML用の `helpdesk/templates/`、CSSとJavaScript用の `helpdesk/static/`、
そして機能ごとに1つのPythonファイルを加えていきます。

## 注目するところ

- `create_app()` がどのようにアプリを作り、`main` ブループリントを登録しているか。
- `@bp.route("/")` がどのようにアドレスとPythonの関数を結び付けているか。

## このステップを学ぶ

これは **Task 2. Developing the solution** の16ステップ中のステップ1です。T Level Digital Software Developmentの無料レッスン（英語）のシリーズで、PythonとFlaskを使い、アジャイルのスプリントでNetheretのヘルプデスクを作ります。このステップのレッスンはこちらです：
[Flaskプロジェクトの準備](https://mitsurutech.co.uk/resources/t-level/dsd-t2-01-setup)。

- 次のステップ：[ステップ02「JinjaテンプレートとCSSによるページレイアウト」](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- [T Level Digitalの無料レッスン一覧](https://mitsurutech.co.uk/resources/t-level)
- [これらのレッスンをMitsuruTechでクラスに教える](https://mitsurutech.co.uk/ja/learning)、[料金を見る](https://mitsurutech.co.uk/ja/pricing)、
  [学校で無料の1年を始める](https://mitsurutech.co.uk/ja/signup)

## この作例について

T Level Digital Software Developmentの授業のための作例として、[Mitsuru Technologies](https://mitsurutech.co.uk/ja)（MitsuruTech）が書きました。
Netheret IT Support Solutionsの課題文はPearsonのサンプル評価資料によるものです。このコードと解説は私たち自身のもので、
PearsonやDepartment for Educationが公開、推奨、承認したものではありません。
「T Level」はDepartment for Educationの登録商標です。
