def validator(tckn: str) -> (bool, str):
    odd_sum, even_sum, total_sum = 0, 0, 0
    if len(tckn) == 11 and tckn.isdigit():
        if tckn[0] == '0':
            print('first digit cannot be zero')
            return False, tckn
        else:
            for i, num in enumerate(tckn):
                if (i + 1) < 11:  # sum of 1.2.3.4.5.6.7.8.9.10 digits
                    total_sum += int(num)
                if (i + 1) % 2 == 1:  # sum of 1.3.5.7.9. digits
                    if (i + 1) == 11:
                        pass
                    else:
                        odd_sum += int(num)
                else:
                    if (i + 1) == 10:
                        pass
                    else:  # sum of 2.4.6.8. digits
                        even_sum += int(num)
        # Logic control of given tckn is valid or not.
        if (odd_sum * 7 - even_sum) % 10 == int(tckn[9]) and (total_sum % 10) == int(tckn[10]):
            return True, tckn
        else:
            return False, tckn
