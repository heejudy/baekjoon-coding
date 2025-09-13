import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        String A = sc.next(), B = sc.next();
        int sumA = 100 * Integer.parseInt(String.valueOf(A.charAt(2)))
                + 10 * Integer.parseInt(String.valueOf(A.charAt(1)))
                + 1 * Integer.parseInt(String.valueOf(A.charAt(0)));
        int sumB = 100 * Integer.parseInt(String.valueOf(B.charAt(2)))
                + 10 * Integer.parseInt(String.valueOf(B.charAt(1)))
                + 1 * Integer.parseInt(String.valueOf(B.charAt(0)));
        if (sumA > sumB){
            System.out.println(sumA);
        }
        else{
            System.out.println(sumB);
        }
    }
}