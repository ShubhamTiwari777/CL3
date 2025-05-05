import java.rmi.Naming;
public class ConcatenationClient {
 public static void main(String[] args) {
 try {
 Concatenation obj = (Concatenation)
Naming.lookup("rmi://localhost/ConcatenationService");
 // Example Input
 String str1 = "Hello, ";
 String str2 = "World!";

 // Remote Method Call
 String result = obj.concatenateStrings(str1, str2);

 System.out.println("Concatenated Result: " + result);
 } catch (Exception e) {
 System.err.println("Client Error: " + e.getMessage());
 }
 }
}
