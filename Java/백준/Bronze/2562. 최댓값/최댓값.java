import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[9];
        int[] array = new int[9];
        for (int i = 0; i < 9; i++){
            String s = br.readLine();
            arr[i] = Integer.parseInt(s);
            array[i] = Integer.parseInt(s);
        }

        int maxn = arr[0];
        int ind = 1;

        for (int i = 0; i < arr.length; i++){
            if(maxn < arr[i]){
                maxn = arr[i];
            }
        }
        for (int i = 0; i< arr.length; i++){
            if (array[0] == maxn){
                break;
            }
            if(array[i] != maxn){
                ind++;
            }
            else{
                break;
            }
        }

        bw.write(maxn + "\n" + ind);
        bw.flush();
        bw.close();
    }
}