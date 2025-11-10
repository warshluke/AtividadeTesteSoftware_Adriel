from eficiencia_motor import *
def test_calcular_Eficiencia():
    assert calcular_eficiencia(900,1000) == 90.0
    resultado = calcular_eficiencia(855,1000)
    assert f"{resultado:.1f}" == "85.5"
    assert calcular_eficiencia(900,0) == ('Potência de entrada deve ser maior que zero.')
def test_classificar_Eficiencia():
    assert classificar_eficiencia(75.0) == ("IE1 - Baixa eficiência")
    assert classificar_eficiencia(85.0) == ("IE2 - Eficiência média")
    assert classificar_eficiencia(92.0) == ("IE3 - Alta eficiência")
def test_integracao():
    motor= calcular_eficiencia(880,1000)
    assert motor == 88.0
    assert classificar_eficiencia(motor) == ("IE2 - Eficiência média")
