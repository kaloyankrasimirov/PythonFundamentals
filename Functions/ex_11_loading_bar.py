def load_bar(some_number:int) -> str:
    if some_number == 100:
        return "100% Complete!\n [%%%%%%%%%%]"
    loaded_percents = some_number // 10
    not_loaded_percents = 10 - loaded_percents
    return f"{some_number}% [{'%' * loaded_percents}\{'.' * not_loaded_percents}]\nStill loading..."

number = int(input())
print(load_bar(number))