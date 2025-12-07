using System;
					
public class Program
{
	public static void Main()
	{
		int T = int.Parse(Console.ReadLine());
		
		for(int i = 0; i < T; i++){
			string[] input = Console.ReadLine().Split(' ');
			
			int X = int.Parse(input[0]);
			string op = input[1];
			int Y = int.Parse(input[2]);
			string eq = input[3];
			int Z = int.Parse(input[4]);
				
			int cal = 0;
			
			if(op == "+"){
				cal = X + Y;
			}
			else if(op == "-"){
				cal = X - Y;
			}
			
			if(cal == Z){
				Console.WriteLine("Case " + (i + 1) + ": YES");
			}
			else{
				Console.WriteLine("Case " + (i + 1) + ": NO");
			}
				
		}
		
	}
}