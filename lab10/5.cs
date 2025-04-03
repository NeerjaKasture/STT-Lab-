class Calculator
{
    public int num1;
    public int num2;
    public Calculator(int num1, int num2)
    {
        this.num1 = num1;
        this.num2 = num2;
    }
    public void PerformOperations()
    {
        int sum = num1 + num2;
        int sub = num1 - num2;
        int mul = num1 * num2;
        Console.WriteLine("Sum: " + sum);
        Console.WriteLine("Difference: " + sub);
        Console.WriteLine("Product: " + mul);
        try
        {
            int div = num1 / num2;
            Console.WriteLine("Quotient: " + div);
        }
        catch (DivideByZeroException)
        { Console.WriteLine("Error: Division by Zero"); }

        if (sum % 2 == 0)
        { Console.WriteLine("The sum is even."); }
        else
        { Console.WriteLine("The sum is odd."); }
    }
}
class Program
{
    static void Main(string[] args)
    {
        try
        {
            Console.Write("Enter the first number: ");
            int num1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter the second number: ");
            int num2 = Convert.ToInt32(Console.ReadLine());
            Calculator calculator = new Calculator(num1, num2);
            calculator.PerformOperations();
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input! Please enter valid integers.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }
}
