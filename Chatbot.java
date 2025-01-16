import java.util.Scanner;
class Chatbot 
{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hello! I'm a chatbot. How can I help you today?");

        while (true) {
            String userInput = scanner.nextLine().toLowerCase();  

            if (userInput.contains("hi") || userInput.contains("hello")) {
                System.out.println("Chatbot: Hello there! How can I assist you?");
            } 
            else if (userInput.contains("how are you")) {
                System.out.println("Chatbot: I'm doing great! How about you?");
            } 
            else if (userInput.contains("name")) {
                System.out.println("Chatbot: I don't have a personal name. You can call me Chatbot.");
            } 
            else if (userInput.contains("What's your favorite color")) {
                System.out.println("Chatbot: I think blue is nice!");
            } 
            else if (userInput.contains("bye") || userInput.contains("exit") || userInput.contains("quit")) {
                System.out.println("Chatbot: Goodbye! Have a great day!");
                break;  
            } 
            else {
                System.out.println("Chatbot: I'm sorry, I didn't understand that. Could you please ask something else?");
            }
        }

        scanner.close();  
    }
}