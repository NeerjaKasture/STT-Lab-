using System;
using System.Threading;

class Alarm
{
    public event Action AlarmTriggered;

    private TimeSpan targetTime;

    public Alarm(string inputTime)
    {
        targetTime = TimeSpan.Parse(inputTime);
    }

    public void Start()
    {
        Console.WriteLine("Waiting for the alarm time...");

        while (true)
        {
            TimeSpan currentTime = DateTime.Now.TimeOfDay;

            if (currentTime.Hours == targetTime.Hours &&
                currentTime.Minutes == targetTime.Minutes &&
                currentTime.Seconds == targetTime.Seconds)
            {
                AlarmTriggered?.Invoke();
                break;
            }

            Thread.Sleep(1000);
        }
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter alarm time (HH:MM:SS):");
        string input = Console.ReadLine();

        try
        {
            Alarm alarm = new Alarm(input);
            alarm.AlarmTriggered += RingAlarm;
            alarm.Start();
        }
        catch
        {
            Console.WriteLine("Invalid time format. Please use HH:MM:SS.");
        }

        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }

    static void RingAlarm()
    {
        Console.WriteLine(" Alarm ringing!");
    }
}
