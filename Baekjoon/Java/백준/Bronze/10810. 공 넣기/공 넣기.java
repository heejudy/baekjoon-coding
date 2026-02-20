import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String count = br.readLine();
        StringTokenizer st = new StringTokenizer(count);
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        for (int i = 0; i < M; i++){
            String ball = br.readLine();
            StringTokenizer str = new StringTokenizer(ball);
            int I = Integer.parseInt(str.nextToken());
            int J = Integer.parseInt(str.nextToken());
            int K = Integer.parseInt(str.nextToken());
            for (int j = I-1; j < J; j++){
                arr[j] = K;
            }
        }
        for (int i:arr){
            bw.write(i + " ");
        }
        bw.flush();
        bw.close();
    }
}