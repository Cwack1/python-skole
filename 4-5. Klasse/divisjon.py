#Hva kan et "tall" deles på? (For å få et heltall)

tall = 20
#Starter på tallet "tall", -1 for hver gang helt ned til 1
for n in range(tall, 1, -1):
    if tall % n == 0:
        print(f'{tall} / {n} = {int(tall / n)}')