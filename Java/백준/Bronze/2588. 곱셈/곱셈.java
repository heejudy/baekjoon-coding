import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int intVal1 = scanner.nextInt();
        String str = scanner.next();

        String result1;
        for (int i = 1; i <= str.length(); i++) {
            result1 = str.substring(str.length()-i, str.length()-i+1);
            System.out.println(Integer.parseInt(result1)*intVal1);

        }

        System.out.println(intVal1*Integer.parseInt(str));

    }
}