#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>
#include <conio.h>

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

struct TrieNode
{
    struct TrieNode *child[128]; //pointer to children indicating next letter
    int isEnd;                   //1 indicates end of word
    char rate[4];                //to store the rating of the movie
    char *desc;                  //to store the movie description
};

struct TrieNode *r; //root of trie

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

struct TrieNode *getnode() //funtion to get a default trie node initialised
{
    struct TrieNode *t = (struct TrieNode *)malloc(sizeof(struct TrieNode));
    t->isEnd = 0;
    for (int i = 0; i < 128; i++)
        t->child[i] = NULL;

    return t;
}

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

void mainmenu() //function to print mainmenu
{
    printf("S.Search\nQ.quit\n");
}

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

void searchmenu() //function to print searchmenu
{
    printf("Enter name of Movie (end it with *) : ");
}

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

void Trieinsert(struct TrieNode *root, char *name, char *rating, char *description) //funtion to insert in trie
{

    struct TrieNode *t = root;

    for (int i = 0; i < strlen(name); i++)
    {
        int ind = name[i]; //get the index from the character

        if (t->child[ind] == NULL)
        {

            t->child[ind] = getnode();
            //t->child[ind]->rate = rating;
        }
        t = t->child[ind];
    }
    //t will now point to the last character of name
    t->isEnd = 1; //indicates it is end of the word

    //inserting rating
    strcpy(t->rate, rating);

    //inserting desc
    t->desc = (char *)malloc(sizeof(char) * (strlen(description) + 1));
    strcpy(t->desc, description);
    return;

    //DEBUGGING
    // t = root;
    // int i = 0;
    // while (1)
    // {

    //     int ind = name[i];
    //     i++;
    //     if (t->child[ind] != NULL)
    //         printf("%c", ind);
    //     if (t->isEnd == 1)
    //         break;
    //     t = t->child[ind];
    // }
    // printf(" %s", t->mov->rating);
    // printf("\n");
}

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

char s1[100], s2[100], s3[100]; //top 3 searches
char *r1, *r2, *r3;             //pointer to top 3 movies' Ratings
char *d1, *d2, *d3;             //pointer to top 3 movies' descriptions

int leng;                               //length of queried string
int count;                              //too keep count of number of movies found
void top3(struct TrieNode *root, int i) //function to get top3 movies matching with the query
{
    if (count == 3)
        return;
    if (root->isEnd == 1)
    { //if reached end of word, store its rating and details
        if (count == 0)
        {
            s1[i] = '\0';
            r1 = root->rate;
            d1 = root->desc;
            count++;
        }
        else if (count == 1)
        {
            s2[i] = '\0';
            r2 = root->rate;
            d2 = root->desc;
            count++;
        }
        else if (count == 2)
        {
            s3[i] = '\0';
            r3 = root->rate;
            d3 = root->desc;
            count++;
        }
    }
    if (count == 3)
        return;
    for (int j = 0; j < 128; j++) //to further find and store the names of the movies alphabetically
    {
        if (root->child[j] != NULL)
        {
            if (count == 0)
            {
                s1[i] = j;
                s2[i] = j;
                s3[i] = j;
            }
            else if (count == 1)
            {
                s2[i] = j;
                s3[i] = j;
            }
            else if (count == 2)
            {
                s3[i] = j;
            }
            top3(root->child[j], i + 1);
        }
    }
    return;
}

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

int Triesearch(struct TrieNode *root, char *name) //function to search in trie
{
    struct TrieNode *t = root;
    for (int i = 0; i < strlen(name); i++) //iterates over each character to progress in the trie
    {
        int ind = name[i];
        if (t->child[ind] == NULL)
        {
            return 0;
        }
        t = t->child[ind];
    }

    strcpy(s1, name);
    strcpy(s2, name);
    strcpy(s3, name); //stores the names in s1, s2, s3;
    leng = strlen(name);
    count = 0;
    top3(t, strlen(name)); //find top 3

    if (count >= 1)
        printf("1.%s\n", s1);
    if (count >= 2)
        printf("2.%s\n", s2);
    if (count == 3)
        printf("3.%s\n", s3);

    return 1;
}

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

int main()
{

    //reading and storing data from file into trie
    r = getnode(); //initialises root of trie
    FILE *data;
    data = fopen("data.txt", "r"); //open data file

    char ch;
    char name[100];  //stores movie name
    char rate[100];  //stores rating
    char desc[1000]; //stores description
    int i = 0;       //index of name;
    int stat = 1;    //variable to check if to store in trie or not, 1 if storing, 0 if not storing
    while ((ch = fgetc(data)) != EOF)
    {

        if (stat == 1)
        {
            if (ch == '#')
            {
                stat = 2;       //dont store further
                name[i] = '\0'; //marks end of string
                i = 0;          //resets index
            }
            else
            {
                name[i] = ch; //continue storing the name
                i++;
            }
        }
        else if (stat == 2)
        {
            if (ch == '#')
            {

                stat = 3; //start storing details
                rate[i] = '\0';
                i = 0;
            }
            else
            {
                rate[i] = ch;
                i++;
            }
        }
        else if (stat == 3)
        {
            if (ch == '#')
            {

                stat = 4; //stop storing
                desc[i] = '\0';
                i = 0;

                Trieinsert(r, name, rate, desc);
            }
            else
            {
                desc[i] = ch;
                i++;
            }
        }
        else if (stat == 4)
        {
            if (ch == '\n')
            {
                stat = 1; //start storing;
            }
        }
    }

    ///////////////////////////////
    //The actual program begins here
    ///////////////////////////////
    i = 0;
    int init_launch = 1;
    char inp = 'a';
    while (inp != 'Q')
    {

        system("cls");
        //FOR INTRO MESSAGE
        if (init_launch == 1)
        {
            printf("Welcome to our movie search engine!\nYou can search for any movie using the first few letters of its title. The search is case sensitive\n\n");
            init_launch = 0;
        }
        ///////////
        mainmenu();
        scanf(" %c", &inp);
        system("cls");
        switch (inp)
        {
        case 'S':
        {

            searchmenu();
            i = 0;
            scanf(" %c", &ch);
            while (ch != '*')
            {
                name[i] = ch;
                i++;
                scanf("%c", &ch);
            }

            name[i] = '\0';
            printf("\n");
            system("cls");
            int ans = Triesearch(r, name);
            if (ans == 0)
                printf("Not found\n");
            else
            {
                printf("Enter desired option, 0 to go back : ");
                char opt;
                scanf(" %c", &opt);
                system("cls");
                switch (opt)
                {
                case '1':
                {
                    printf("\nName : %s\nRating : %s\n\n%s\n", s1, r1, d1);
                    break;
                }
                case '2':
                {
                    if (count < 2)
                        printf("Invalid input\n");
                    else
                    {
                        printf("\nName : %s\nRating : %s\n\n%s\n", s2, r2, d2);
                    }
                    break;
                }
                case '3':
                {
                    if (count < 3)
                        printf("Invalid input\n");
                    else
                    {
                        printf("\nName : %s\nRating : %s\n\n%s\n", s3, r3, d3);
                    }
                    break;
                }
                case '0':
                    break;
                default:
                    printf("INVALID INPUT\n");
                }
            }
            printf("\n\n");
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
