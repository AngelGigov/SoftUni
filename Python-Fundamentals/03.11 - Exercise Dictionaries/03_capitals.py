country = input().split(", ")
capital = input().split(", ")

country_and_capital = {country: capital for country, capital in zip(country, capital)}

for key, value in country_and_capital.items():
    print(f"{key} -> {value}")