class Calculadora {
int sumar(int a, int b) {
return a + b;
}
}


class CalculadoraCientifica extends Calculadora {
@override
int sumar(int a, int b) {
int resultado = super.sumar(a, b);
return resultado + 10;
}
}

void main() {
Calculadora calculadora = Calculadora();
print(calculadora.sumar(5, 3));

CalculadoraCientifica calculadoraCientifica = CalculadoraCientifica();
print(calculadoraCientifica.sumar(5, 3));
}