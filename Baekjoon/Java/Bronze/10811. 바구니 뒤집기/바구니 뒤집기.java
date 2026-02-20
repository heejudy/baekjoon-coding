import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int N = sc.nextInt(), M = sc.nextInt();
        int[] arr = new int[N];
        for (int b = 0; b < N; b++){
            arr[b] = b + 1;
        }
        for (int a = 0; a < M; a++){
            int i = sc.nextInt(), j = sc.nextInt();
            int cnt = (j-i)/2 + 1;
            for (int c = 0; c < cnt; c++){
                int temp = arr[i-1];
                arr[i-1] = arr[j-1];
                arr[j-1] = temp;
                i++;
                j--;
            }
        }
        for (int i: arr){
            System.out.print(i + " ");
        }
    }
}