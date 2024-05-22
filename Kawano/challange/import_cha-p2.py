def print_charge(user_money,currency,from_currency_to_count):
    for i in from_currency_to_count.keys():
        while user_money >= int(i[:-1]):
            user_money -= currency
            from_currency_to_count[i] += 1
            
        
