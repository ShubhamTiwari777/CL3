import java.rmi.Remote;
import java.rmi.RemoteException;
public interface Concatenation extends Remote {
 String concatenateStrings(String str1, String str2) throws RemoteException;
}
