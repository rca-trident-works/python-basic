import os

def main():
    input_env_key = input("取得する環境変数の名前を入力してください: ")
    if not input_env_key:
        print("環境変数の名前は空にできません。")
        return
    env_value = os.getenv(input_env_key)
    if env_value is None:
        print(f"環境変数 '{input_env_key}' は存在しません.")
    else:
        print(f"{input_env_key} = {env_value}")

if __name__ == "__main__":
    main()
