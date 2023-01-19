from Data import values, tree


class ConverterExeption(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(qba:list):
        if len(qba) != 3:
            raise ConverterExeption('Неверное количество параметров')
        quote, base, amount = qba
        quote, base, amount = quote.capitalize(), base.capitalize(), amount.capitalize()
        if base == quote:
            raise ConverterExeption(f'Одинаковая валюта {quote}')
        if (quote not in values.keys()) or (base not in values.keys()):
            raise ConverterExeption(f'Неизвестная валюта quote:{quote}, base:{base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConverterExeption(f'Неудалось обработать количество {amount}')
        if base == "Рубль":
            value_b = 1
            value_q = tree[values[str(quote)]]["Value"]
        elif quote == "Рубль":
            value_q = 1
            value_b = tree[values[str(base)]]["Value"]
        else:
            value_q = tree[values[str(quote)]]["Value"]*tree[values[str(quote)]]["Nominal"]
            value_b = tree[values[str(base)]]["Value"]*tree[values[str(base)]]["Nominal"]
        result = float(amount)*value_q / value_b
        result = round(result, 2)
        return amount, values[str(quote)], result, values[str(base)]