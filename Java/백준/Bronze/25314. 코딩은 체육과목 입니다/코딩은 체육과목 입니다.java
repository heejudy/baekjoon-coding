import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        if (N % 4 == 0){
            for (int i = 0; i < N/4; i++){
                System.out.print("long ");
            }
            System.out.println("int");
        }
        else{
            for (int i = 0; i <= N/4; i++){
                System.out.print("long ");
            }
            System.out.println("int");
        }

    }
}