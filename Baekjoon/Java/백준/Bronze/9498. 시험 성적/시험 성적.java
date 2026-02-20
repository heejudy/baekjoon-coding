import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        String grade = "";

        if(a >= 90)
            grade = "A";
        else if(a >= 80)
            grade = "B";
        else if(a >= 70)
            grade = "C";
        else if(a >= 60)
            grade = "D";       
        else
            grade = "F";
        
        System.out.println(grade);
    }
}