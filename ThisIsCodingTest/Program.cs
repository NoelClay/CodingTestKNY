// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World! \n This is CodingTest Book Program \n Please, Input Chapter Index \n 03 : Greedy");

while (true)
{
    int answer = ConvertToChapterIndex(ConsoleReadLineCheckNull());

    if (answer == 0)
    {

    }
}




string ? ConsoleReadLineCheckNull()
{
    string? input;
    int cnt = 0;
    while (true)
    {
        if (cnt >= 100) return "일부러 틀리네..아 그냥 꺼요";
        input = Console.ReadLine();
        if (input == null) Console.WriteLine("EOF가 감지되었습니다. 다시 입력해 주세요.");
        else return input;
        cnt++;
    }
}

int ConvertToChapterIndex(string? input)
{
    int answer = 0;
    for (int i = 0;i<100;i++)   

}

