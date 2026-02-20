import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        String s = sc.next();
        String[] alpha = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        List<String> list = new ArrayList<>(Arrays.asList(alpha));
        int sum = 0;
        for (int i = 0; i < s.length(); i++){
            String A = String.valueOf(s.charAt(i));
            for (String j:alpha){
                if (j.indexOf(A) != -1){
                    sum = sum + (list.indexOf(j)+3);
                }
            }
        }
        System.out.println(sum);
    }
}
