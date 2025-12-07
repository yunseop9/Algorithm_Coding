using System;

class Program{
    static void Main(){
        int B = int.Parse(Console.ReadLine());
        B -= B / 11;
        Console.WriteLine(B);
    }
}