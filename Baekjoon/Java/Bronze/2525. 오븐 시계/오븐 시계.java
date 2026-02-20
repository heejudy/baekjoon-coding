import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int hour = scanner.nextInt();
        int min = scanner.nextInt();
        int addMin = scanner.nextInt();
        int sum = min + addMin;

        if (sum >= 60){
            if(hour + (sum / 60) > 23){
                System.out.print(hour + (sum / 60)-24);
                System.out.print(" ");
                System.out.print(sum % 60);
            }
            else{
                System.out.print(hour + (sum / 60));
                System.out.print(" ");
                System.out.print(sum % 60);
            }
        }
        else{
            System.out.print(hour);
            System.out.print(" ");
            System.out.print(sum);
        }
    }
}