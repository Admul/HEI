package FirstPackage;

public class SecondClass {
    private int firstNumber;
    private int secondNumber;

    public SecondClass() {
        this(0, 0);
    }

    public SecondClass(int firstNumber) {
        this(firstNumber, 0);
    }

    public SecondClass(int firstNumber, int secondNumber) {
        this.firstNumber = firstNumber;
        this.secondNumber = secondNumber;
    }

    public int GetFirstNumber() { return this.firstNumber; }
    public int GetSecondNumber() { return this.secondNumber; }
    public int ChangeFirstNumber(int newNum) { return this.firstNumber = newNum; }
    public int ChangeSecondNumber(int newNum) { return this.secondNumber = newNum; }
    public int Sum() { return this.firstNumber+this.secondNumber; }

}
