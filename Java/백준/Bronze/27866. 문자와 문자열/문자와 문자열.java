import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        String s = sc.next();
        int N = sc.nextInt();
        System.out.println(s.charAt(N-1));
    }
}