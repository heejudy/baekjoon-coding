import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int N = sc.nextInt();
        for (int i = 0; i < N; i++){
            String s = sc.next();
            System.out.print(s.charAt(0));
            System.out.println(s.charAt(s.length()-1));
        }
    }
}