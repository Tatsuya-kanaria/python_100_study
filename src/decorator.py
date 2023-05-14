import datetime
import functools


def my_logger(f):
    @functools.wraps(f)
    def _wrapper(*args, **keywords):
        # 前処理
        print(f'{f.__name__}の実行')
        print(f'開始: {datetime.datetime.now()}')

        # デコレート対象の関数の実行
        v = f(*args, **keywords)

        # 後処理
        print(f'終了: {datetime.datetime.now()}')
        print(f'実行結果: {v}')

        return v
    return _wrapper


@my_logger
def return_one():
    return 1


print(dir(return_one))
print(return_one.__name__)
return_one()


def tag(tag_name):
    def _tag(f):
        def _wrapper(*args, **keywords):
            v = f(*args, **keywords)
            return f'<{tag_name}>{v}</{tag_name}>'
        return _wrapper
    return _tag


@tag('h1')
def greet():
    return 'hello decorator'


print(greet())
