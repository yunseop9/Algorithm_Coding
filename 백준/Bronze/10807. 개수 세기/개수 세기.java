import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws Exception{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      int N = Integer.parseInt(br.readLine()); // 정수의 개수
      
      int[] arr = new int[N]; // N개의 정수가 있는 배열열
      
      StringTokenizer st = new StringTokenizer(br.readLine()," ");
      
      for(int i = 0; i<N; i++){
          arr[i] = Integer.parseInt(st.nextToken());
      }
      
      int v = Integer.parseInt(br.readLine()); // 찾으려는 수수
      
      int count = 0;
      for(int x : arr){
          if(x == v){
              count++;
          }
      }
      
      System.out.println(count);
      
      
  }
}