import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String T = br.readLine();
        int num = Integer.parseInt(T);

        for (int i = 0; i < num; i++){
            String A = br.readLine();
            StringTokenizer st = new StringTokenizer(A);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int sum = a + b;
            bw.write(sum+"\n");
        }
        bw.flush();
        bw.close();
    }
}