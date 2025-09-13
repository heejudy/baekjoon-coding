import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int N = sc.nextInt();
        Integer[] array = new Integer[N];
        for (int i = 0; i < N; i++){
            int a = sc.nextInt();
            array[i] = a;
        }
        List<Integer> list = new ArrayList(Arrays.asList(array));
        int M = Collections.max(list);
        double sum = 0;
        for (int i = 0; i < N; i++){
            double A = array[i]*100;
            sum += (A)/M;
        }

        System.out.println(sum/N);
    }
}