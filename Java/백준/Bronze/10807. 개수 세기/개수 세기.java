import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner scanner = new Scanner(new InputStreamReader(System.in));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sum = 0;
        int num = scanner.nextInt();
        Integer[] array = new Integer[num + 1];
        for (int i = 0; i < num; i++){
            int S = scanner.nextInt();
            array[i] = S;
        }
        int V = scanner.nextInt();

        List<Integer>list = new ArrayList<>(Arrays.asList(array));
        int cnt = Collections.frequency(list, V);

        System.out.println(cnt);
    }
}