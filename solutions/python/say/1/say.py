def say(number):
    if not 0 <= number <= 999_999_999_999:
        raise ValueError('input out of range')
    
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if number < 10:
        return ones[number]
    if number < 20:
        return teens[number - 10]
    if number < 100:
        return tens[(number // 10)] + ('-'+ ones[number % 10] if number % 10 != 0 else '')
    if number < 1000:
        return ones[number // 100] + ' hundred'+ (' '+ say(number % 100) if number % 100 != 0 else '')
    
    chunk = [
        (1_000_000_000, 'billion'),
        (1_000_000, 'million'),
        (1_000, 'thousand')
    ]

    for value, name in chunk:
        if number >= value:
            return say(number // value) + f' {name}' + (' ' + say(number % value) if number % value != 0 else '')