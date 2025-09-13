import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int A, B;
        String[] arrays;
        int T = Integer.parseInt(bf.readLine());
        for (int i = 0; i < T; i++){
            arrays = bf.readLine().split(" ");
            A = Integer.parseInt(arrays[0]);
            B = Integer.parseInt(arrays[1]);
            System.out.println(A + B);
        }
    }
}