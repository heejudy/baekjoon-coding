import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int T = sc.nextInt();
        for (int i = 0; i < T; i++){
            int R = sc.nextInt();
            String s = sc.next();
            String A = "";
            for (int j = 0; j < s.length(); j++){
                String a = String.valueOf(s.charAt(j));
                A += a.repeat(R);
            }
            System.out.println(A);
        }
    }
}