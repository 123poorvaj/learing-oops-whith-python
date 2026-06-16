s=' 3445 '

s=s.strip() #strip use to remove the extra space in string and ending of the string
is_digit=s.isdigit() #isdigit is use to check the the given string is digit or not if it's digit print Ture else False
is_4_digit=(len(s)==4)
is_valid=is_digit and is_4_digit
print(is_valid)