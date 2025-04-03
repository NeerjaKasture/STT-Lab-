using System;
class Student
{
    public string Name;
    public string ID;
    public int Marks;

    public Student(string name, string id, int marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    public string GetGrade()
    {
        if (Marks >= 90)
            return "A";
        else if (Marks >= 75)
            return "B";
        else if (Marks >= 60)
            return "C";
        else if (Marks >= 45)
            return "D";
        else
            return "F";
    }

    public static void Main()
    {
        Student student1 = new Student("John Doe", "S12345", 85);
        Console.WriteLine("Student Details:");
        Console.WriteLine($"Student Name: {student1.Name}");
        Console.WriteLine($"Student ID: {student1.ID}");
        Console.WriteLine($"Marks: {student1.Marks}");
        Console.WriteLine($"Grade: {student1.GetGrade()}");
        Console.WriteLine();  
    }
}

class StudentIITGN : Student
{

    public string Hostel_Name_IITGN;

    public StudentIITGN(string name, string id, int marks, string hostelName)
        : base(name, id, marks)  
    {
        Hostel_Name_IITGN = hostelName;
    }

    public static void Main()
    {
        StudentIITGN studentIITGN = new StudentIITGN("Jane Smith", "S54321", 92, "Hostel A");
        Console.WriteLine("Student Details:");
        Console.WriteLine($"Student Name: {studentIITGN.Name}");
        Console.WriteLine($"Student ID: {studentIITGN.ID}");
        Console.WriteLine($"Marks: {studentIITGN.Marks}");
        Console.WriteLine($"Grade: {studentIITGN.GetGrade()}");
        Console.WriteLine($"Hostel Name (IITGN): {studentIITGN.Hostel_Name_IITGN}");
    }


}
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Calling Student class Main method:");
        Student.Main();

        Console.WriteLine("Calling StudentIITGN class Main method:");
        StudentIITGN.Main();
    }
}
