print("Hej, välkommen till den Koola kiosken!")
print("Här kan du köpa Glass för 20kr styck, Varmkrov för 15kr styck, bröd kostar extra. Läsk för 15kr och sist en enstaka godis för 10kr")
print("Så vad får det lov att vara?")
item = input()
Glass = 20

if item == "Glass":
    print("Och hur mycket glass vill du ha?")
    amount = input()
    amount = int(amount)
elif item == "Korv":
    print("Och hur många korvar vill du ha?")
    amount = input()
    amount = int(amount)
elif item == "Läsk":
    print("Och hur mycket läsk vill du ha?")
    amount = input()
    amount = int(amount)
elif item == "Godis":
    print("Och hur mycket läsk vill du ha?")
    amount = input()
    amount = int(amount)