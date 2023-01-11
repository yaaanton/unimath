wood = [52,94,252,1311,1416]
gas = [106,318,530,636,1377]
mazut = [318,477,530,636,742]
coal = [318,953,530,265,106]

'''wood = [0,100,250,1200,1300]
gas = [100,300,500,600,1300]
mazut = [300,450,500,600,700]
coal = [300,900,500,250,100]'''

# npv, PI, IRR, срок окупаемости
NPVwood = 0
NPVgas = 0
NPVmazut = 0
NPVcoal = 0

def NPV(I, rate): #сумма дисконтированных значений потока платежей
    counter = 1 #с итепень по годам
    NPV = 0 #начальное
    for i in I:
        NPV += i / ((1+rate) ** counter)# слогаемое нпв
        counter += 1#увеличение на единицу после сложения за год
    NPV -= 1200 # вычетание инвестиций
    return NPV


def IRR(I, baseRate, negativeRate): #Внутренняя норма доходности
    # I - возвраты по годам
    # baseRate - базовая ставка инфляции (12% или сколько-то)
    # negativeRate - ставка при которой не выгодно производить (ставка при которой NPV отрицательный)
    IRR= baseRate + (NPV(I, baseRate) / (NPV(I, baseRate) - NPV(I, negativeRate))) * (negativeRate - baseRate) # рассчёт IRR
    return IRR


def PI (I, rate): #Чистая приведённая стоимость
    counter = 1 #степень по годам
    PI = 0 #начальное
    for i in I:
        PI += i / ((1+rate) ** counter)# слогаемое PI где в числителе возврат по годам, а в знаменателе произведение ставок в год
        counter += 1
    PI /= 1200 # делим на сумму инвестиций
    return PI


def remainsByYears (I, baserate):
    invest = -1200
    counter = 1
    yearlyRemains = [-1200]
    yearlyReturns = []
    for i in I:
        yearReturn = i / ((1 + baserate) ** counter)
        invest += yearReturn
        yearlyRemains.append(invest)
        yearlyReturns.append(yearReturn)
        print(f'Возврат в {yearlyRemains.index(invest)} году составит {yearReturn}')
        counter += 1
    print(f'Остатки по годам начиная с 0:\n{yearlyRemains}\n')
    return {'YearlyRemains': yearlyRemains, 'YearlyReturn': yearlyReturns}


print('1) расчёт базового NPV')
NPVwood= NPV(wood, 0.12)
NPVgas = NPV(gas, 0.12)
NPVmazut = NPV(mazut, 0.12)
NPVcoal = NPV(coal, 0.12)
print(NPVwood)
print(NPVgas)
print(NPVmazut)
print(NPVcoal)



print('\n2) расчёт наименьшего отрицательного NPV для всех вариантов одновременно:')
NPVwood= NPV(wood, 0.3)
NPVgas = NPV(gas, 0.3)
NPVmazut = NPV(mazut, 0.3)
NPVcoal = NPV(coal, 0.3)

print(NPVwood)
print(NPVgas)
print(NPVmazut)
print(NPVcoal)
'''
первый расчёт IRR
'''

print('\n3) расчёт IRR при базовой ставке 12% и ставке с наименьшим отрицательным NPV для всех одновременно:')
IRRwood = IRR(wood, 0.12, 0.3)
IRRgas = IRR(gas, 0.12, 0.3)
IRRmazut = IRR(mazut, 0.12, 0.3)
IRRcoal = IRR(coal, 0.12, 0.3)
print(IRRwood*100)
print(IRRgas*100)
print(IRRmazut*100)
print(IRRcoal*100)
print('')
'''
для каждого ирр ищем наибольшее ближайшее положительное нпв
'''
print('4) Рассчёт минимально положительного NPV при максимально высокой ставке - тут подбираем')
print(NPV(wood, 0.25))
print(NPV(gas,0.27))
print(NPV(mazut,0.29))
print(NPV(coal,0.28))

'''
пересчитать irr для разницы между ближайшей положительной и ближайшей отрицательной
'''
print('\n5) Расчёт IRR для разницы ближайшей положительной для каждого NPV и ближайшей отрицательной для NPV ставки (значения 3 действие и 4 действия) %:')
IRRwood = IRR(wood, IRRwood, 0.25)
IRRgas = IRR(gas, IRRgas, 0.27)
IRRmazut = IRR(mazut, IRRmazut, 0.29)
IRRcoal = IRR(coal, IRRcoal, 0.28)
print(IRRwood*100)
print(IRRgas*100)
print(IRRmazut*100)
print(IRRcoal*100)

'''
Рассчитываем PI
'''
print('\n6)Рассчёт PI чистой приведённой стоимости с базовой ставкой: ')
print(PI(wood, 0.12))
print(PI(gas, 0.12))
print(PI(mazut, 0.12))
print(PI(coal, 0.12))

'''
период окупаемости
'''
print('\nдерево')
twod=remainsByYears(wood, 0.12)
print('газ')
tgas=remainsByYears(gas, 0.12)
print('мазут')
tmazut=remainsByYears(mazut, 0.12)
print('уголь')
tcoal=remainsByYears(coal, 0.12)

'''
Период окупаемости по ресурсам
'''
print(f'''
7) сроки окупаемости
Срок окупаемости дерева     {4+ abs(tcoal['YearlyRemains'][4])/(abs(tcoal['YearlyRemains'][4])+tcoal['YearlyRemains'][5])}
Срок окупаемости газа       {4+abs(tgas['YearlyRemains'][4])/(abs(tcoal['YearlyRemains'][4])+tcoal['YearlyRemains'][5])}
Срок окупаемости мазута     {3+abs(tcoal['YearlyRemains'][3])/(abs(tcoal['YearlyRemains'][3])+tcoal['YearlyRemains'][4])}
Срок окупаемости угля       {2+abs(tcoal['YearlyRemains'][2])/(abs(tcoal['YearlyRemains'][2])+tcoal['YearlyRemains'][3])}
''')



