#원하는 범위에서 소수를 찾아주는 코드.

num = int(input("시작할 숫자를 입력해주세요."))
asf = int(input("마지막 숫자를 입력해주세요."))
pnlist = list([])
ond = 0 # 소수개수
while num < asf + 1:
    wh = 2  # 반복하는 동안 나눌 숫자
    ch = 0  # 반복하는동안 소수인지 판별
    awd = 0  # 조기종료 판별
    if num == 1:
        print("1은 소수가 아닙니다.")
        num = int(input("확인할 숫자를 다시 적어주세요"))
    while wh < num:
        aw = num / wh
        gsd, sdg = str(aw).split(".")
        wa = float(gsd) - aw
        if wa == 0:
            ch = ch + 1

        wh = wh + 1
        if ch >= 1:
            awd = 1
            break

    if awd == 0:
        if ch == 0:
            print(f"{num}는 소수입니다")
            pnlist.append(num)
            ond = ond + 1
    num = num + 1

print(f"""[{num}~{asf}]까지의 소수 개수:{len(pnlist)}
{pnlist}""")

