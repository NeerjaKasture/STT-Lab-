class Functions
{    public void Loop10()
    {   Console.WriteLine("Numbers from 1 to 10:");
        for (int i = 1; i <= 10; i++)
        {   Console.WriteLine(i);}
    }
    public void WhileLoop()
    {   string userInput;
        do
        {   Console.WriteLine("Enter exit to quit the loop");
            userInput = Console.ReadLine();
        } while (userInput != "exit");
    }
    public long Factorial(int number)
    {   long factorial = 1;
        for (int i = 1; i <= number; i++)
        {   factorial *= i;}
        return factorial;
    }}
class Program
{   static void Main(string[] args)
    {
        Functions functions = new Functions();
        Console.Write("Running for loop to print 1 to 10");
        functions.Loop10();
        Console.WriteLine("Running while loop until you type exit");
        functions.WhileLoop();
        Console.Write("Calculating factorial. Enter a number: ");
        int num = Convert.ToInt32(Console.ReadLine());
        Console.Write("The factorial is "+functions.Factorial(num)); 
    }}
