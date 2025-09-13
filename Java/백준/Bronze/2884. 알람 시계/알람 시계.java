import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        if (b >= 45) {
            System.out.print(a);
            System.out.print(" ");
            System.out.print(b - 45);
        }
        else{
            if (a == 0){
                System.out.print(23);
                System.out.print(" ");
                System.out.print(b + 15);
            }
            else {
                System.out.print(a-1);
                System.out.print(" ");
                System.out.print(b+15);
            }
        }
    }
}