import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer str;

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++){
            arr[i] = i+1;
        }

        for (int i = 0; i < M; i++){
            str = new StringTokenizer(br.readLine());
            int I = Integer.parseInt(str.nextToken()), J = Integer.parseInt(str.nextToken());
            int temp = arr[I-1];
            arr[I-1] = arr[J-1];
            arr[J-1] = temp;
        }

        for (int i:arr){
            bw.write(i +" ");
        }
        bw.flush();
        bw.close();
    }
}