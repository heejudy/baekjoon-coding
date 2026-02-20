import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] array = new int[N];

        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        for (int i = 0; i < N; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        int maxn = array[0];
        int minn = array[0];

        for (int i = 0; i < array.length; i++){
            if (array[i] > maxn)
                maxn = array[i];
            if (array[i] < minn)
                minn = array[i];
        }
        bw.write(minn + " " + maxn);
        bw.flush();
        bw.close();
    }
}