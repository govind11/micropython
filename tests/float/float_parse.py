# test parsing of floats

inf = float('inf')

# it shouldn't matter where the decimal point is if the exponent balances the value
print(float('1234') - float('0.1234e4'))
print(float('1.015625') - float('1015625e-6'))

# very large integer part with a very negative exponent should cancel out
print('%.4e' % float('9' * 60 + 'e-60'))
print('%.4e' % float('9' * 60 + 'e-40'))

# many fractional digits
print(float('.' + '9' * 70))
print(float('.' + '9' * 70 + 'e20'))
print(float('.' + '9' * 70 + 'e-50') == float('1e-50'))

# tiny fraction with large exponent
print(float('.' + '0' * 60 + '1e10') == float('1e-51'))
print(float('.' + '0' * 60 + '9e25'))
print(float('.' + '0' * 60 + '9e40'))

# ensure that accuracy is retained when value is close to a subnormal
print(float('1.00000000000000000000e-37'))
print(float('10.0000000000000000000e-38'))
print(float('100.000000000000000000e-39'))
