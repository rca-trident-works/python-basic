import os

env_var_name = input("取得する環境変数の名前を入力してください: ")
env_var_value = os.getenv(env_var_name)
if env_var_value is not None:
    print(f"{env_var_name} = {env_var_value}")
else:
    print(f"環境変数 '{env_var_name}' は存在しません。")
