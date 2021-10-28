#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>

#ifdef _WIN32
#include <conio.h> //for clrscr()
#else
#include <stdio.h>
#define clrscr() printf("\e[1;1H\e[2J")
#endif

int indx(char c)
{
    if (c >= 32 && c <= 58) //0-27 have ASCII 32-58
    {
        return c - 32;
    }
    else if (c >= 65 && c <= 90) //capital letters from 27-52
    {
        return c - 38;
    }
    else if (c >= 97 && c <= 122) //small letters from
    {
        return c - 48;
    }

    return 0;
}

struct Trienode
{

    struct Trienode *next[96]; //pointer to possible characters
    int isEnd;                 //indicates if end of word
};

struct Trienode *root;

struct Trienode *triegetnode()
{
    struct Trienode *t = (struct Trienode *)malloc(sizeof(struct Trienode));
    t->isEnd = 0;
    for (int i = 0; i < 53; i++)
        t->next[i] = NULL;
    return t;
}

void Trieinsert(struct Trienode *r, char *name) //r is root of trie; name is pointer to string of entire name;
{
    struct Trienode *t = r;
    for (int i = 0; i < strlen(name); i++)
    {
        int ind = indx(name[i]);
        if (t->next[ind] == NULL)
        {
            t->next[ind] = triegetnode(); //if next pointer of that character points to NULL
            t = t->next[ind];
        }
    }
    t->isEnd = 1;
}

void Triesearch(struct Trienode *r, char *name) //display upto 3 names
{
    struct Trienode *t = r;
    for (int i = 0; i < strlen(name); i++)
    {
        int ind = indx(name[i]);
        printf("%c \n", name[i]);
        if (t->next[ind] == NULL)
        {
            for (int i = 0; i < 96; i++)
            {
                printf("%d no next \n", i);
            }
            printf("No movies with this exist\n");
            return;
        }

        t = t->next[ind];
    }

    //t will now point to letter at end of typed name
    //now need to print first 3 suggestion by iterating till first 3 end of words
}

void mainmenu()
{
    //clrscr();
    printf("1.Search\nQ.quit\n");
}

void searchmenu()
{
    //clrscr();
    printf("Enter name of Movie (press * when done) : ");
}

int main()
{
    root = triegetnode();
    FILE *data;
    data = fopen("data.txt", "r");
    char ch;
    int stat = 0; //0 indicates reading from file, 1 indicates dont store the string
    char s[100];
    int i = 0;                        //index of s;
    while ((ch = fgetc(data)) != EOF) //reading from file and storing name in trie
    {
        if (stat == 0 && ch == '#')
        {
            s[i] = '\0';
            Trieinsert(root, s);
            printf("%s", s);
            stat = 1;
            i = 0;
        }
        else if (stat == 0)
        {
            s[i] = ch;
            i++;
        }
        else if (stat == 1 && ch == '\n')
            stat = 0;
    }

    i = 0;

    char inp = 'a';
    while (inp != 'Q')
    {
        // clrscr();
        mainmenu();
        scanf("%c", &inp);
        switch (inp)
        {
        case '1':
        {

            searchmenu();
            i = 0;
            scanf(" %c", &ch);
            while (ch != '*')
            {
                //printf("%c", &ch);

                s[i] = ch;
                i++;
                scanf("%c", &ch);
            }

            s[i] = '\0';
            printf("Done taking input\n");

            Triesearch(root, s);
            getch();
            break;
        }
        case 'Q':
        {
            break;
        }
        default:
            printf("Invalid input \n");
        }
    }
}
