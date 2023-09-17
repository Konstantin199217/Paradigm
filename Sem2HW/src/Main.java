import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
   //Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n

        Scanner sc = new Scanner(System.in);
        System.out.println("Введите число");
        int num = sc.nextInt();
        for(int i = 1; i <= num; i++){
            for(int k = 1; k <= num; k++){
                System.out.printf("%4d", (k*i));
            }
            System.out.println();
        }
    }
}