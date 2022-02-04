import java.util.Scanner;

public class Bathwater
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner input = new Scanner(System.in);
		String firstLine = input.nextLine();
		int testCases = Integer.parseInt(firstLine);
		
		for (int i = 0; i < testCases; i++)
		{
			String nextLine = input.nextLine();
			String[] arrayNextLine = nextLine.split(" ");
			
			int v1 = Integer.parseInt(arrayNextLine[0]);
			int t1 = Integer.parseInt(arrayNextLine[1]);
			int v2 = Integer.parseInt(arrayNextLine[2]);
			int t2 = Integer.parseInt(arrayNextLine[3]);
			int v3 = Integer.parseInt(arrayNextLine[4]);
			int t3 = Integer.parseInt(arrayNextLine[5]);
			
			if (t2 > t3)
			{
				System.out.println("NO");
			}
			else if (v1 + v2 < v3)
			{
				System.out.println("NO");
			}
			else if (t2 < t3)
			{
				System.out.println("NO");
			}
			else if (v1 + v2 >= v3)
			{
				boolean possible = false;
				if (t3 >= t1 && t3 <= t2)
				{
					possible = true;
				}
				if (v1 + v2 >= v3)
				{
					for (int j = 0; j < v1; j++)
					{
						for (int k = 0; k < v2; k++)
						{
							if ((j * t1 + k * t2) / (j + k) == t3)
							{
								possible = true;
							}
						}
					}
				}
				if (possible)
				{
					System.out.println("YES");
				}
				else
				{
					System.out.println("NO");
				}
			}
			else if (v1 >= v3 && v2 >= v3 && t3 <= t2 && t3 >= t1)
			{
				System.out.println("YES");
			}
			else if (v1 >= v3 && t1 == t3)
			{
				System.out.println("YES");
			}
			else if (v2 >= v3 && t2 == t3)
			{
				System.out.println("YES");
			}
			else if (t2 != t3)
			{
				int neededHotWater = ((v1 * t1) - (v1 * t3)) / (t3 - t2);
				
				if (v1 + neededHotWater != 0 &&
						((v1 * t1 + neededHotWater * t2) / (v1 + neededHotWater) == t3))
				{
					System.out.println("YES");
				}
				else
				{
					System.out.println("NO");
				}
			}
			else if (t1 != t3)
			{
				int neededHotWater = ((v2 * t2) - (v2 * t3)) / (t3 - t1);
				
				if (v2 + neededHotWater != 0 &&
						((v2 * t2 + neededHotWater * t1) / (v2 + neededHotWater) == t3))
				{
					System.out.println("YES");
				}
				else
				{
					System.out.println("NO");
				}
			}
			else
			{
				System.out.println("NO");
			}
		}
	}
}
