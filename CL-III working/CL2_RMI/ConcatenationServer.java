import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
public class ConcatenationServer extends UnicastRemoteObject implements Concatenation {
 // ✅ Correct Constructor with 'throws RemoteException'
 public ConcatenationServer() throws RemoteException {
 super();
 }
 @Override
 public String concatenateStrings(String str1, String str2) throws RemoteException {
 return str1 + str2;
 }
 public static void main(String[] args) {
 try {
 // ✅ Start RMI registry in code instead of manually
 LocateRegistry.createRegistry(1099);
 System.out.println("RMI Registry started...");
 ConcatenationServer server = new ConcatenationServer();
 Naming.rebind("rmi://localhost/ConcatenationService", server);
 System.out.println("Concatenation Server is running...");
 } catch (Exception e) {
 e.printStackTrace(); // Print full error stack trace
 }
 }
}