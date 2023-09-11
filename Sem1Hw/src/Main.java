import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] array = {4,3,2,1,4,2,3};
        bubbleSort(array);
        System.out.println(" Императивный стиль ");
        sort(array);
        System.out.println(" Декларативный стиль ");
    }

    public static void bubbleSort(int[] sortArr){
        for (int i = 0; i < sortArr.length - 1; i++) {
            for(int j = 0; j < sortArr.length - i - 1; j++) {
                if(sortArr[j + 1] < sortArr[j]) {
                    int swap = sortArr[j];
                    sortArr[j] = sortArr[j + 1];
                    sortArr[j + 1] = swap;
                }
            }
        }
        for (int i = 0; i < sortArr.length ; i++) {
            System.out.print(sortArr[i]);
        }

    }
    public static void sort(int[] sortArr){
        Arrays.sort(sortArr);
        for (int i = 0; i < sortArr.length ; i++) {
            System.out.print(sortArr[i]);
        }
    }
}