using System;
using System.Drawing;
using System.Windows.Forms;

namespace Form1
{
    public partial class Form1 : Form
    {
        private TimeSpan targetTime;
        private Timer timer;
        private Random random;

        public Form1()
        {
            InitializeComponent();
            random = new Random();
            timer = new Timer();
            timer.Interval = 1000;
            timer.Tick += Timer_Tick;

           
            button1.Text = "Start Alarm";

           
            button1.Click += Button1_Click;

           
            textBox1.TextChanged -= textBox1_TextChanged;
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            if (TimeSpan.TryParse(textBox1.Text, out targetTime))
            {
                timer.Start();
            }
            else
            {
                MessageBox.Show("Please enter a valid time in HH:MM:SS format.");
            }
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
           
            this.BackColor = Color.FromArgb(
                random.Next(256),
                random.Next(256),
                random.Next(256)
            );

            TimeSpan currentTime = DateTime.Now.TimeOfDay;

            if (currentTime.Hours == targetTime.Hours &&
                currentTime.Minutes == targetTime.Minutes &&
                currentTime.Seconds == targetTime.Seconds)
            {
                timer.Stop();
                MessageBox.Show("Alarm ringing!");
            }
        }

        
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            // You can leave this empty or remove it
        }
    }
}
