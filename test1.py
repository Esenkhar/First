import decimal

try:
    with decimal.localcontext() as ctx:
        ctx.prec = 2;
        print(decimal.Decimal(1.00) / decimal.Decimal('3.00'))
        print(1/0)
except Exception as e:
    print(e)
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
