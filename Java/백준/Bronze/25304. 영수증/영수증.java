import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int total = scanner.nextInt();
        int N = scanner.nextInt();
        int sum = 0;

        for (int i = 0; i < N; i++){
            int price = scanner.nextInt();
            int num = scanner.nextInt();
            sum += price * num;
        }
        if (total == sum){
            System.out.println("Yes");
        }
        else
            System.out.println("No");
    }
}