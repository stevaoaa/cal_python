# -*- coding: utf-8 -*-

import pytest

import cal


def test_cal():
    """

        Casos de teste:	
        - n = 19
        - 0 < dds <= 6 e 28 <= n <= 31
        (casos invalidos sao descartados pelo main, pois ambos os parametros
        sao gerados pelos metodos firstOfMonth e numberOfDays, que ja estao sendo testados)
    """
    expected_result_1 = "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"
    expected_result_2 = "          1  2  3  4\n 5  6  7  8  9 10 11\n12 13 14 15 16 17 18\n19 20 21 22 23 24 25\n26 27 28 29 30 "

    assert cal.cal(2, 19) == expected_result_1
    assert cal.cal(3, 30) == expected_result_2


@pytest.mark.parametrize('input, expected_result', [
    (4, True),     #Ano menor que 1752 e multiplo de 4
    (1501, False), #Ano menor que 1752 e não-multiplo de 4
    (1900, False), #Ano maior que 1752 e multiplo de 100
    (1903, False), #Ano maior que 1752 e não multiplo de 4    
    (1904, True),  #Ano maior que 1752 e multiplo de 4
    (2000, True),  #Ano maior que 1752 e multiplo de 400
])
def test_is_leap(input, expected_result):
    
    actual = cal.is_leap(input) 
    assert  actual == expected_result


@pytest.mark.skipif(True, reason = 'simply ignoring for now')
def test_mutation_is_leap():

    assert cal.is_leap(1752) == True



@pytest.mark.parametrize('input, expected_result', [
    ((1, 1), 6),      #Ano não-bissexto
    ((1, 4), 2),      #Ano bissexto, mês <= 2
    ((5, 4), 4),      #Ano bissexto, mês > 2
    ((9, 1752), 2),   #Ano 1752, mês <= 9    
    ((11, 1752), 3),  #Ano 1752, mês > 9
])
def test_first_of_month(input, expected_result):
    
    month, year = input
    actual = cal.first_of_month(month, year) 
    assert  actual == expected_result



@pytest.mark.parametrize('input, expected_result', [
    (1801, 4), #Ano maior que 1800 (esperado: quinta-feira, 4)
    (1780, 6), #Ano menor que 1800 e maior que 1752 (esperado: sabado, 6)
    (1500, 3), #Ano menor que 1752 (esperado: quarta-feira, 3)
])
def test_jan1(input, expected_result):
    
    actual = cal.jan1(input) 
    assert  actual == expected_result



@pytest.mark.parametrize('input, expected_result', [
    ((3, 2001), 31),   #Ano não-bissexto
    ((2, 2000), 29),   #Ano bissexto, mês <= 2
    ((3, 2000), 31),   #Ano bissexto, mês > 2
    ((9, 1752), 19),   #Ano 1752, mês <= 9    
    ((12, 1752), 31),  #Ano 1752, mês > 9
])
def test_number_of_days(input, expected_result):
    
    month, year = input
    actual = cal.number_of_days(month, year) 
    assert  actual == expected_result
