WARNING: You are using pip version 21.2.3; however, version 21.3.1 is available.
You should consider upgrading via the '/Users/HOME/diary_django/venv/bin/python -m pip install --upgrade pip' command.

/Users/HOME/venv/bin/python -m pip install --upgrade pip

仮想環境を構築
python3 -m venv ven

仮想環境をアクティベート
source venv/bin/activate

Django をインストール
pip install Django

インストール済みのパッケージを「requirements.txt」というファイルへ書き込む
pip freeze > requirements.txt

クローン先のリポジトリ

#1. git clone
$ git clone fuga

#2. virtualenv 構築
$ virtualenv .

#3. requirement.txt から pip でパッケージを入れる
$ pip install -r requirements.txt

#4. 同期完了
$ pip list
