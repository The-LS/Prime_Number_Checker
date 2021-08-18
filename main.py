num = int(input("소수인지 확인할 숫자:"))     #체크할 숫자 받아옴
wh = 2 #반복하는 동안 나눌 숫자
ch = 0 # 반복하는동안 소수인지 판별
casd = " " #소수인지 판별해주는

if num == 1:
    print("1은 소수가 아닙니다.")
    num = int(input("확인할 숫자를 다시 적어주세요"))
while wh < num:
    aw = num / wh
    gsd, sdg = str(aw).split(".")
    wa = float(gsd) - aw
    if wa == 0:
        ch = ch + 1
        casd = "약수      "
    else:
        casd = "약수가 아님"
    print(f"{wh} = {num}의 {casd}  <==  {wh}/{num}")
    wh = wh + 1




if ch == 0:
    print(f"{num}는 소수입니다")
else:
    print(f"{num}은 합성수입니다")

