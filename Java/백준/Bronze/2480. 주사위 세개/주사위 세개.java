import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int fst = scanner.nextInt();
        int snd = scanner.nextInt();
        int trd = scanner.nextInt();
        int[] array = {fst, snd, trd};

        if (fst == snd && snd == trd){
            System.out.print(10000 + 1000*fst);
        }
        else if(fst != snd && snd != trd && fst != trd){
            System.out.print(100*Arrays.stream(array).max().getAsInt());
        }
        else{
            if (fst == snd){
                System.out.print(1000+100*fst);
            }
            else if(fst == trd)
                System.out.print(1000+100*fst);
            else
                System.out.print(1000+100*snd);
        }
    }
}