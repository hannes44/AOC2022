// https://adventofcode.com/2022/day/1
string input = File.ReadAllText("../input.txt");
// parsing input
string[] elvesCalories = input.Split(new string[] { "\r\n\r\n" },
                               StringSplitOptions.RemoveEmptyEntries);
List <int> totalCaloriesPerElf = new List<int>();
foreach (string s in elvesCalories)
{
    int totalCalories = 0;
    string[] totalCaloriesElf = s.Split(new string[] { "\n" },
                               StringSplitOptions.RemoveEmptyEntries);
    foreach (string calorieEntry in totalCaloriesElf)
    {
        totalCalories += int.Parse(calorieEntry);
    }
    totalCaloriesPerElf.Add(totalCalories);
}

// part 1
Console.WriteLine(totalCaloriesPerElf.Max());

totalCaloriesPerElf.Sort(((a, b) => b.CompareTo(a)));
// part 2
int threeHighestCaloriesCount = totalCaloriesPerElf[0] + totalCaloriesPerElf[1] + totalCaloriesPerElf[2];
Console.WriteLine(threeHighestCaloriesCount);