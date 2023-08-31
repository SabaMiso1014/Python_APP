# Hello World
print('Hello World')

# 演算子
print(10) # 数値はクォーテーションで囲む必要はありません。
print(10 + 5) # 足している
print(5 - 2)  # 引いている
print(10 / 2)   # 割っている
print(10 % 5)   # あまりを求めている
# 優先順位の変更
print((20 - 5) // 3)  # 通常は +と-よりも*や/の方が優先度が高いですが、()で囲むことで優先度を変えることができます。

# 変数
var = "var"
Var = "Var"
print(var) # varと出力される
print(Var) # Varと出力される
# Pythonで変数名をつける際に２単語続ける場合
lowercase_underscore = "lowercase_underscore" # 推奨
lowercaseunderscore = "lowercase_underscore"  # 非推奨
hello_world = "Hello, World" # 推奨
helloworld  = "Hello, World" # 非推奨

# 型変換
print("Hello" + "World") # +により文字列同士を連結
name = "Tom"
print("My name is " + name)
age = 24
# 以下は、データ型の異なる文字列型と数値型を連結してエラーになっているプログラムです。
print("My name is " + name + "My age is " + age) # この行はエラーになります
# TypeError: Can't convert 'int' object to str implicitly

# リスト
li = []
li.append("python")
print(li) # ['python']
li.append("php")
print(li) # ['python', 'php']

# 辞書型
profile = {"name": "tani", "email": "kazunori-t@cyberbra.in" }
print(profile["name"]) # tani
# 新しく要素を追加
profile["gender"] = "male"
# 新しく要素を追加した辞書型(profile)を出力
print(profile)

# IF文
score = 80
if score > 78: # 比較演算子 > を使っています。
    print("合格です。おめでとう！")
else:
    print("不合格。次回頑張りましょう。")

score = 100
if score == 100:
    print("満点")
elif score > 85:
    print("合格！")
else:
    print("不合格。次回頑張りましょう。")

# For文
for index, name in enumerate(["apple", "banana", "melon"]):
    print(index, name)

# While文
n = 0
while n < 10:
    print(n)
    n += 1 # +1するのを忘れずに。

# 関数
def hello():
    print("hello!")
