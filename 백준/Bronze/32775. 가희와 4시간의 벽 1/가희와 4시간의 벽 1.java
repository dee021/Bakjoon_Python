import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int s = Integer.parseInt(br.readLine());
		int f = Integer.parseInt(br.readLine());
		
		if (f < s) System.out.println("flight");		
		else System.out.println("high speed rail");

		br.close();
	}	
}