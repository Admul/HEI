import FirstPackage.*;

class FirstClass {
    public static void main(String[] args) {
        SecondClass o = new SecondClass();
        int i, j;
        for(i=0;i<=8;i++) {
            for(j=0;j<=8;j++) {
                o.ChangeFirstNumber(i);
                o.ChangeSecondNumber(j);
                System.out.print(o.Sum());
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}