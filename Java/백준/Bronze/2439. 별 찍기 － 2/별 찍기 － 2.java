import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(new InputStreamReader(System.in));

        int N = scanner.nextInt();

        for (int i = 1; i <= N; i++){
            System.out.print(" ".repeat(N-i));
            System.out.println("*".repeat(i));
        }
    }
}