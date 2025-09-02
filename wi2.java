import java.util.*;
import java.io.*;
public class wi2 {
    static ArrayList<String> reminders = new ArrayList<String>();
    static final String FILE_NAME = "reminders.txt";
    public static void removeReminders(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Your reminders are:");  
        int number = 1;
        for (String reminder : reminders) {
            System.out.println(number + ". " + reminder);
            number++;
        }
        System.out.println("Enter the number of the reminder you want to remove:");
        int index = sc.nextInt();
        sc.nextLine();
   
        if (index > 0 && index <= reminders.size()) {
            System.out.println("Removing reminder: " + reminders.get(index - 1));
            reminders.remove(index - 1);
            saveReminders();
        } else {
            System.out.println("Invalid reminder number.");
        }
   
    }
    public static void loadReminders() {
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = reader.readLine()) != null) {
                reminders.add(line);
            }
        } catch (IOException e) {
            System.out.println("No previous reminders found.");
        }
    }

   
    public static void saveReminders() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME))) {
            for (String reminder : reminders) {
                writer.write(reminder);
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("Error saving reminders.");
        }
    }

    public static void addReminder() {
        System.out.println("Enter the title of reminder:");
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        reminders.add(a);
        saveReminders();
        System.out.println("You have added your reminder: " + a);
        System.out.println();
    }

    public static void viewReminders() {
        if (reminders.isEmpty()) {
            System.out.println("NO REMINDERS ARE SET");
        } else {
            System.out.println("Your reminders are:");
            for (String reminder : reminders) {
                System.out.println(" - " + reminder);
                System.out.println();
            }
        }
    }

    public static void main(String[] args) {
        loadReminders();

        Scanner sc = new Scanner(System.in);

        System.out.println("WELCOME TO REMINDER APP");
        boolean run = true;
        while (run) {
            System.out.println("SELECT AN OPTION:");
            System.out.println("1. ADD A REMINDER");
            System.out.println("2. VIEW THE REMINDERS");
            System.out.println("3.TASK COMPLETED....REMOVE REMINDER");
            System.out.println("4. EXIT");
            int entered_value = sc.nextInt();
            sc.nextLine();

            switch (entered_value) {
                case 1:
                    addReminder();
                    break;
                case 2:
                    viewReminders();
                    break;
                case 3:
                    removeReminders();
                case 4:
                    run = false;
                    System.out.println("Exited.");
                    break;
               
            }
        }
       
    }
}
