public class Programa {
    public static int operaciones(
int a, int b, int c) {
        int resultado = a + b * c;
        return resultado;
    }
    public static void main(String[] args) {
        System.out.println(operaciones(1, 9, 10));
    }
}