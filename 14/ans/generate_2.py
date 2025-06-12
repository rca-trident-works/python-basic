def gen_pi4():
    lst = [1, 4, 1, 5]
    for i in lst:
        yield i


def gen_pi6():
    ans = 355/113 - 3
    for _ in range(6):
        yield int(ans * 10)
        ans = ans*10 - int(ans*10)


def gen_pi15():
    ans = 1019514486099146 / 324521540032945 - 3
    for _ in range(15):
        yield int(ans * 10)
        ans = ans*10 - int(ans*10)


def gen_pi1000():
    try:
        with open('pi.txt', 'r') as f:
            lst = f.readline()
        for i in lst:
            yield i
    except FileNotFoundError:
        print("ファイルが見つかりません")
        return
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return

# main
print("\npi4()")
for n in gen_pi4():
    print(n,end='')

print("\npi6()")
for n in gen_pi6():
    print(n,end='')

print("\npi15()")
for n in gen_pi15():
    print(n,end='')

print("\npi1000()")
for n in gen_pi1000():
    print(n,end='')
