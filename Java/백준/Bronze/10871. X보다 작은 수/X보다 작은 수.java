import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner scanner = new Scanner(new InputStreamReader(System.in));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = scanner.nextInt();
        int X = scanner.nextInt();
        for (int i = 0; i < N; i++){
            int A = scanner.nextInt();
            if (A < X)
                System.out.print(A + " ");
        }

    }
}