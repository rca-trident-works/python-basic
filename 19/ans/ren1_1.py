import re


def extract_emails(input_file, output_file):
    '''メールアドレスを抽出し、ファイルへ出力する'''
    with open(input_file, 'r', encoding='utf8') as file:
        content = file.read()

    # より厳密なパターン(RFC準拠に近いパターン)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    emails = re.findall(email_pattern, content)

    # 重複を取り除く
    uniq_emails = set(emails)

    with open(output_file, 'w', encoding='utf8') as file:
        for email in uniq_emails:
            file.write(email + '\n')


# main
INPUT_FILE = 'aichi.html'
OUTPUT_FILE = 'aichi_mail.txt'
extract_emails(INPUT_FILE, OUTPUT_FILE)
