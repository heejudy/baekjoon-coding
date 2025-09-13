import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        String sen = sc.nextLine();
        sen = sen.trim();
        int sum = 0;
        if (sen.length() == 0){
            System.out.println(sen.length());
        }
        else{
            for (int i = 0; i < sen.length(); i++){
                if(sen.charAt(i) == ' '){
                    sum += 1;
                }
            }
            System.out.println(sum+1);
        }

    }
}