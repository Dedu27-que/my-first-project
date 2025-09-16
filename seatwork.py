def convert_usd(amount):
    inr = amount * 83.5
    gbp = amount * 0.76
    cny = amount * 7.30
    return inr, gbp, cny

def main():
    while True:
        doll = input("Enter dollar ($) (* to exit): ")
        if doll == '*':
            print("Bye")
            break

        parts = doll.split('@')

        print("Dollar($)\tIndian Rupee(R)\tBritish(Pound)\tChina Yuan(Y)")

        for part in parts:
            if part.isdigit():
                usd = int(part)
                inr, gbp, cny = convert_usd(usd)
                print(usd, "\t\t", round(inr, 2), "\t\t", round(gbp, 2), "\t\t", round(cny, 2))
            else:
                print(part, "is not a valid number, skipped.")

main()
