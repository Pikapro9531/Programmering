print("Hej, välkommen till den Koola kiosken!")
print("Här kan du köpa Glass för 20kr styck, Varmkrov för 15kr styck, bröd kostar extra. Läsk för 15kr och sist en enstaka godis för 10kr")
print("Så vad får det lov att vara?")
item = input()
icecream_price = 20
Hotdog_price = 15
Soda_price = 15
Candy_price= 10

if item == "Glass":
    print("Och hur mycket glass vill du ha?")
    amount = input()
    amount = int(amount)

    print(icecream_price * amount, "kronor det att kosta")

elif item == "Korv":
    print("Och hur många korvar vill du ha?")
    amount = input()
    amount = int(amount)

    print(Hotdog_price * amount, "kronor kommer det att kosta")

elif item == "Läsk":
    print("Och hur mycket läsk vill du ha?")
    amount = input()
    amount = int(amount)
    
    print(Soda_price * amount, "kronor kommer det att kosta")

elif item == "Godis":
    print("Och hur många Godisar vill du ha?")
    amount = input()
    amount = int(amount)
    
    print(Candy_price * amount, "kronor kommer det att kosta")