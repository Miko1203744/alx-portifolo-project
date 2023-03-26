using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace giraffe
{
    class program
    {
        static void Main(string[] args)
        {
          Book book1=new Book();
          book1.title="harry potter";
          book1.author="jk rowling";
          book1.page=400;
          Console.WriteLine(book1.title);
        }

    }
}