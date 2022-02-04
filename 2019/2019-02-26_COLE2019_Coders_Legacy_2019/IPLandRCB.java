import java.util.Scanner;

public class IPLandRCB
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		String firstLine = input.nextLine();
		@SuppressWarnings("unused")
		int testCases = Integer.parseInt(firstLine);
		
		for (int i = 0; i < testCases; i++)
		{
			String nextLine = input.nextLine();
			String[] arrayNextLine = nextLine.split(" ");
			
			int points = Integer.parseInt(arrayNextLine[0]);
			int matches = Integer.parseInt(arrayNextLine[1]);
			
			if (points > matches)
			{
				System.out.println((points - matches));
			}
			else
			{
				System.out.println(0);
			}
		}
	}
}
